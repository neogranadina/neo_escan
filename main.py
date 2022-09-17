# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.4
# 2022-04-11
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import glob
from pathlib import Path
import json
import shutil
import gc
import psutil

from locale import getdefaultlocale
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QPixmap, QImage, QMovie

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel, QGridLayout, QPushButton
from PySide2.QtCore import QSize, QTranslator, QLibraryInfo, Qt

from ui_main import Ui_MainWindow
from db.db_handler import connectToDatabase, createElement, getElementIdByMetadata, insertInfo, editInfo, getElementInfo, getLastElementID, listofIDs, getElementMetadatabyID, erase_element, getImagesInfo, kill_connection, getLastImgs, getDocumentTypeByID
from camcontrol import Cam
from filecontrol import UpdateFiles
import configparser
import ctypes
import time
from utils.logcontrol import LogControl as log
import filemanager.b2 as b2
from utils.monitor import promedio_captura

# config

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'setup/config.cfg')
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

version = config['DEFAULT']['version']

# Check compatibility and return images directory

if sys.platform == 'linux':
    IMGDIR = config['DEFAULT']['img_dir']
    os.makedirs(IMGDIR, exist_ok=True)
elif sys.platform == 'win32':
    IMGDIR = config['DEFAULT']['images_dir_windows']
    os.makedirs(IMGDIR, exist_ok=True)
else:
    ctypes.windll.user32.MessageBoxW(
        0, "Sistema operativo no soportado", "Error", 0)
    sys.exit(0)

# Entorno de la aplicación


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
    log.log(f"Reinicio de la aplicación. Status: {status}")


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Establecer el título
        title = "NeoEscan"

        self.setWindowTitle(title)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Establece los widgets de la ui como globales
        global widgets
        widgets = self.ui
        # crea las cámaras
        global Cams
        Cams = Cam()
        # Conectar a la base de datos
        try:
            connectToDatabase()
        except Exception as e:
            print("Error en la conexión con la base de datos")
            log.log(
                f"ERROR FATAL: Falló conexión con la base de datos. Error {e} en {__file__} linea {e.__traceback__.tb_lineno}")
            raise

        # Comprobación inicial
        self.check_dir()

        # set version
        widgets.versionLabel.setText(f'v{version}')

        # close button
        widgets.closeButton.clicked.connect(self.gentle_close)

        # Botones, menú
        widgets.inicioButton.clicked.connect(self.buttonClick)
        widgets.coleccionesButton.clicked.connect(self.buttonClick)
        widgets.escanerButton.clicked.connect(self.buttonClick)
        widgets.configButton.clicked.connect(self.buttonClick)
        widgets.b2Send.clicked.connect(self.buttonClick)

        # Seleccionar página de inicio
        if not config['camaras']['exposicion_predeterminada'] == '' or not config['camaras']['zoom_predeterminado'] == '':
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
        else:
            widgets.stackedWidget.setCurrentWidget(widgets.configurationPage)
            self.set_config_page()

        # set home page
        widgets.nuevoProyectoButton.clicked.connect(self.buttonClick)
        self.display_elements()

        # Botón regresar al inicio
        widgets.backtoInicioButton.clicked.connect(self.buttonClick)

        # Página de metadatos
        widgets.tipodocComboBox.currentIndexChanged.connect(self.indexChange)
        widgets.enviarFormButton.clicked.connect(self.enviarForm)
        widgets.browserDirButton.clicked.connect(self.getDirName)
        widgets.zoom_dial.valueChanged.connect(lambda: self.zoom_dial())
        widgets.exposicionDial.valueChanged.connect(lambda: self.exposicion())

        # abrir directorio
        widgets.openFolderButton.clicked.connect(self.openimagesDir)

        # tomar fotografía
        widgets.capturaButton.clicked.connect(self.capturar)
        # validar fotografía
        # TODO: depurar función validateCaptura
        # widgets.validateButton.clicked.connect(self.validateCaptura)
        widgets.resetButton.clicked.connect(self.resetCaptura)
        # cerrar escaner
        widgets.finalizarButton.clicked.connect(self.finalizarCaptura)

        # config page
        widgets.zoom_dial_2.valueChanged.connect(lambda: self.zoom_dial_2())
        widgets.exposicionDial_2.valueChanged.connect(
            lambda: self.exposicion_2())
        widgets.selectCamIzq.currentIndexChanged.connect(
            lambda: self.selectCam(widgets.selectCamIzq.currentIndex()))
        widgets.selectCamDer.currentIndexChanged.connect(
            lambda: self.selectCam(widgets.selectCamDer.currentIndex()))
        # botones config
        widgets.testconfig.clicked.connect(self.test_config)
        widgets.saveconfig.clicked.connect(self.save_config)
        # b2 config
        widgets.b2config.clicked.connect(self.b2_config)
        widgets.b2configSet.clicked.connect(self.b2_config_set)

        # sincronización con B2
        widgets.send2B2.clicked.connect(self.send2B2)

    # comprobación inicial
    def check_dir(self):
        '''
        En caso de que la base de datos esté vacía pero existan capturas en el directorio
        se hace un backup de las capturas y se prepara la carpeta para reiniciar las capturas
        '''
        r = getLastElementID()
        if r is '':
            dir = os.listdir(IMGDIR)
            if len(dir) != 0:
                for files in dir:
                    if files != 'old_backup':
                        shutil.move(os.path.join(IMGDIR, files),
                                    os.path.join(IMGDIR, 'old_backup', files))
                log.log(f"Se hizo un backup de las capturas")

    # navigation functions

    # Navegar por las páginas desde el menú principal

    def buttonClick(self):
        # nombre del botón
        btn = self.sender()
        btnName = btn.objectName()

        # navega por cada una de las páginas
        if btnName == "inicioButton":
            # assert cams to play mode
            try:
                Cams.pause_devs()
            except Exception as e:
                log.log(
                    f'WARNING: No se pudieron detener las cámaras. {e} en {__file__} linea {e.__traceback__.tb_lineno}')
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            self.display_elements()
        elif btnName == "backtoInicioButton":
            # assert cams to play mode
            try:
                Cams.pause_devs()
            except Exception as e:
                log.log(
                    f'WARNING: No se pudieron detener las cámaras. {e} en {__file__} linea {e.__traceback__.tb_lineno}')
            msgBox = QMessageBox
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("¿Está seguro que desea salir del formulario?")
            msgBox.setWindowTitle("Volver al inicio")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            if msgBox.exec_() == QMessageBox.Yes:
                index = widgets.tipodocComboBox.currentIndex() + 1
                self.cleanForm(index)
                widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            else:
                pass
        elif btnName == "coleccionesButton" or btnName == "nuevoProyectoButton":
            # assert cams to play mode
            try:
                Cams.pause_devs()
            except Exception as e:
                log.log(
                    f'WARNING: No se pudieron detener las cámaras. {e} en {__file__} linea {e.__traceback__.tb_lineno}')
            widgets.stackedWidget.setCurrentWidget(widgets.metadataPage)
            widgets.tipoColeccion.setCurrentWidget(widgets.formLegajo)
            widgets.botones_metadata.setCurrentWidget(widgets.enviar)
        elif btnName == "escanerButton":
            self.set_scanner_page()
            widgets.controlesCamstackedWidget.setCurrentWidget(widgets.captura)
        elif btnName == "configButton":
            widgets.stackedWidget.setCurrentWidget(widgets.configurationPage)
            widgets.b2conf.setCurrentWidget(widgets.b2ini)
            self.set_config_page()
        elif btnName == "b2Send":
            widgets.stackedWidget.setCurrentWidget(widgets.b2SendPage)

    # Funciones para la página de elementos

    def display_elements(self):

        try:
            widgets.verticalLayout_20.removeItem(widgets.elementslayout)
            # delete all elements
            for i in reversed(range(widgets.elementslayout.count())):
                widgets.elementslayout.itemAt(i).widget().setParent(None)
        except AttributeError:
            pass


        widgets.elementslayout = QGridLayout()
        widgets.elementslayout.setVerticalSpacing(10)
        widgets.elementslayout.setHorizontalSpacing(10)
        widgets.elementslayout.setContentsMargins(0, 0, 0, 0)
        widgets.elementslayout.setObjectName("elementslayout")

        element_ids = listofIDs()

        if len(element_ids) > 0:
            widgets.proyectos_actuales_label.setText(
                f"Proyectos actuales [{len(element_ids)}]")
        else:
            widgets.proyectos_actuales_label.setText(
                "No se han creado proyectos.")

        for id in reversed(element_ids[-10:]):

            elemento = getElementMetadatabyID(id)
            element_id = id
            element_name = elemento[1]
            element_description = elemento[2]
            element_identifier = elemento[9]

            # TODO: arreglar la ruta a la imagen para thumbnail
            image_path = Path(IMGDIR, f'{element_identifier}', 'data', 'JPG')
            image_not_found = "imgs/No-Photo-Available.png"

            # Display image in the grid
            try:
                num_imagenes = len(os.listdir(image_path))
                img_path = os.listdir(image_path)[0]
                img_path = os.path.join(image_path, img_path)
            except FileNotFoundError:
                num_imagenes = 0
                img_path = image_not_found
            except IndexError:
                num_imagenes = 0
                img_path = image_not_found

            img = QPixmap(img_path)
            img = img.scaled(80, 80, Qt.KeepAspectRatio)
            label = QLabel()
            label.setPixmap(img)
            label.setObjectName(f"element_{element_id}")
            label.setMaximumSize(100, 100)
            label.setAlignment(Qt.AlignLeft)
            widgets.elementslayout.addWidget(label, id, 0)

            # Display element name in the grid
            label1 = QLabel()
            label1.setText(
                f'<h3>{element_name}</h3> [{num_imagenes} imágenes]\n{element_description}')
            label1.setObjectName(f"element_name_{element_id}")
            label1.setMinimumSize(QSize(400, 70))
            label1.setWordWrap(True)
            label1.setAlignment(Qt.AlignLeft)
            widgets.elementslayout.addWidget(label1, id, 1)

            button1 = QPushButton()
            # button.setText("Añadir imágenes")
            button1.setObjectName(f"add_more_{element_id}")
            button1.setMinimumSize(QSize(42, 42))
            button1.setMaximumSize(QSize(42, 42))
            icon1 = QIcon()
            icon1.addFile("imgs/icons/camera-to-take-photos.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button1.setIcon(icon1)
            button1.setIconSize(QSize(20, 20))
            button1.clicked[bool].connect(
                lambda _, element_id=element_id: self.set_scanner_page(element_id))
            widgets.elementslayout.addWidget(button1, id, 2)

            # Set four buttons in the grid
            button = QPushButton()
            # button.setText("Editar")
            button.setObjectName(f"edit_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon1 = QIcon()
            icon1.addFile("imgs/icons/pencil-on-a-square-outline.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon1)
            button.setIconSize(QSize(20, 20))
            button.clicked[bool].connect(
                lambda _, element_id=element_id: self.edit_element(element_id))
            widgets.elementslayout.addWidget(button, id, 3)

            button2 = QPushButton()
            # button.setText("Exportar")
            button2.setObjectName(f"export_element_{element_id}")
            button2.setMinimumSize(QSize(42, 42))
            button2.setMaximumSize(QSize(42, 42))
            icon2 = QIcon()
            icon2.addFile("imgs/icons/download-symbol.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button2.setIcon(icon2)
            button2.setIconSize(QSize(20, 20))
            button2.clicked[bool].connect(
                lambda _, element_id=element_id, image_path=image_path: self.export_element(element_id))
            widgets.elementslayout.addWidget(button2, id, 4)

            button3 = QPushButton()
            # button.setText("Eliminar")
            button3.setObjectName(f"delete_element_{element_id}")
            button3.setMinimumSize(QSize(42, 42))
            button3.setMaximumSize(QSize(42, 42))
            icon3 = QIcon()
            icon3.addFile("imgs/icons/trash-can-with-cover-from-side-view.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button3.setIcon(icon3)
            button3.setIconSize(QSize(20, 20))
            widgets_list = [button3, button2, button1, button, label1, label]
            button3.clicked[bool].connect(
                lambda _, element_id=element_id, widgets_list=widgets_list, element_identifier=element_identifier: self.delete_element(element_id, widgets_list, element_identifier))
            widgets.elementslayout.addWidget(button3, id, 5)

        widgets.verticalLayout_20.addLayout(widgets.elementslayout)

    def edit_element(self, element_id):
        '''
        edit element from element_id
        '''
        # go to metadata page
        widgets.stackedWidget.setCurrentWidget(widgets.metadataPage)
        dtype = getDocumentTypeByID(element_id)

        widgets.tipodocComboBox.setCurrentIndex(dtype)

        # write element_id in the form
        self.write_fields_info(element_id)

    def export_element(self, element_id, image_path):
        '''
        exportar datos e imágenes de un elemento
        '''
        EXPORTDIR = QFileDialog.getExistingDirectory(
            self,
            caption="Seleccionar el directorio para guardar los archivos"
        )

        element_info = getElementInfo(element_id)
        if element_info:
            self.write_json(EXPORTDIR, element_info, element_id, "info")
        else:
            print("error al obtener datos del elemento")
            log.log(f"ERROR al obtener datos del elemento {element_info}")

        metadata_info = getElementMetadatabyID(element_id)
        if metadata_info:
            self.write_json(EXPORTDIR, metadata_info, element_id, "metadata")

        # get images from element_id
        images = getImagesInfo(element_id)
        if images:
            self.write_json(EXPORTDIR, images, element_id, "images")

        # copy files from image_path to EXPORTDIR
        if os.path.exists(image_path):
            try:
                shutil.copytree(image_path, os.path.join(EXPORTDIR, "images"))
            except FileNotFoundError:
                print("error al copiar imágenes")
                log.log(f"ERROR al copiar imágenes {image_path}")

        QMessageBox.information(
            widgets.stackedWidget, "Exportar", "Se ha exportado el elemento correctamente.")

    def delete_element(self, element_id, widgets_list, element_identifier):
        '''
        borra datos y archivos de un elemento
        '''
        folder_path = os.path.join(IMGDIR, element_identifier)

        if QMessageBox.question(
                widgets.stackedWidget, "Eliminar", "¿Está seguro de eliminar el elemento?") == QMessageBox.Yes:
            # delete files from image_path
            # for file in os.listdir(folder_path):
            #    os.remove(f"{folder_path}/{file}")
            try:
                shutil.rmtree(folder_path)
            except FileNotFoundError as e:
                print("error al borrar carpeta")
                log.log(
                    f"WARNING: EL directorio {folder_path} ya no existe o fue borrado manualmente. {e}")
            # elimina el elemento de la base de datos
            erase_element(element_id)
            # elimina el elemento de la interfaz
            for w in widgets_list:
                widgets.elementslayout.removeWidget(w)
                w.deleteLater()
            QMessageBox.information(
                widgets.stackedWidget, "Eliminar", "Se ha eliminado el elemento correctamente.")

        # return to home
        widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
        self.display_elements()

    def indexChange(self):
        '''
        recupera el índice del ComboBox del tipo de documento
        navega por el QStackedWidget
        '''
        index = widgets.tipodocComboBox.currentIndex()

        if index == 0:
            widgets.tipoColeccion.setCurrentWidget(widgets.formLegajo)
        elif index == 1:
            widgets.tipoColeccion.setCurrentWidget(widgets.formDocumento)
        elif index == 2:
            widgets.tipoColeccion.setCurrentWidget(widgets.formImagen)
        elif index == 3:
            widgets.tipoColeccion.setCurrentWidget(widgets.formSeriada)
        elif index == 4:
            widgets.tipoColeccion.setCurrentWidget(widgets.formLibro)
        elif index == 5:
            widgets.tipoColeccion.setCurrentWidget(widgets.formSimple)

        # assesst enviar button
        widgets.botones_metadata.setCurrentWidget(widgets.enviar)

    # Obtener la dirección del directorio de proyectos

    def getDirName(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption="Seleccionar el directorio"
        )
        widgets.folderlineEdit.setText(response)

    # Forms de metadatos

    def requiredFields(self, tipo_documento):
        '''
        check if fields are empty and return error
        '''
        if tipo_documento == 1:
            if widgets.titulolineEdit.text() == "" and widgets.identificadoreslineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formLegajo)
                return False
            else:
                return True
        elif tipo_documento == 2:
            if widgets.titulodoclineEdit.text() == "" and widgets.identificadoresdoclineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formDocumento)
                return False
            else:
                return True
        elif tipo_documento == 3:
            if widgets.tituloimagenlineEdit.text() == "" and widgets.identificadoresimagenlineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formImagen)
                return False
            else:
                return True
        elif tipo_documento == 4:
            if widgets.nombreserlineEdit.text() == "" and widgets.identificadoreserlineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Nombre no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formSeriada)
                return False
            else:
                return True
        elif tipo_documento == 5:
            if widgets.titulolibrolineEdit.text() == "" and widgets.identificadoresLibrolineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formLibro)
                return False
            else:
                return True
        elif tipo_documento == 6:
            if widgets.nombrearchivolineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Nombre no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formSimple)
                return False
            elif widgets.folderlineEdit.text() == "":
                QMessageBox.warning(self, "Error",
                                    "El campo Directorio no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formSimple)
                return False
            else:
                return True

    def get_fields_info(self, tipo_de_documento):
        '''
        get the info for a specific form fields and return a dictionary
        '''

        if tipo_de_documento == 1:
            return {
                'título': widgets.titulolineEdit.text(),
                'descripción': widgets.descripcionlineEdit.toPlainText(),
                'creador': widgets.creadorlineEdit.text(),
                'fecha': widgets.fechaIlineEdit.text(),
                'fecha_final': widgets.fechaFlineEdit.text(),
                'espacio': widgets.coberturalineEdit.text(),
                'idioma': widgets.idiomalineEdit.text(),
                'folios': widgets.numfollineEdit.text(),
                'identificadores': widgets.identificadoreslineEdit.text(),
            }
        elif tipo_de_documento == 2:
            return {
                'título': widgets.titulodoclineEdit.text(),
                'descripción': widgets.descripciondoclineEdit.toPlainText(),
                'creador': widgets.creadordoclineEdit.text(),
                'fecha': widgets.fechaIdoclineEdit.text(),
                'fecha_final': widgets.fechaFdoclineEdit.text(),
                'espacio': widgets.coberturadoclineEdit.text(),
                'idioma': widgets.idiomadoclineEdit.text(),
                'folios': widgets.numfoliodoclineEdit.text(),
                'identificadores': widgets.identificadoresdoclineEdit.text(),
            }
        elif tipo_de_documento == 3:
            return {
                'título': widgets.tituloimagenlineEdit.text(),
                'descripción': widgets.descripcionimagenlineEdit.toPlainText(),
                'creador': widgets.creadorimagenlineEdit.text(),
                'fecha': widgets.fechaimagenlineEdit.text(),
                'espacio': widgets.coberturaespacialimagenlineEdit.text(),
                'descripción_física': widgets.descripcionfisicaimagenlineEdit.text(),
                'tipo_imagen': widgets.tipoimagenlineEdit.text(),
                'identificadores': widgets.identificadoresimagenlineEdit.text(),
            }
        elif tipo_de_documento == 4:
            return {
                'título': widgets.nombreserlineEdit.text(),
                'volumen': widgets.volumenserlineEdit.text(),
                'ejemplar': widgets.ejemplarserlineEdit.text(),
                'fecha': widgets.fechaserlineEdit.text(),
                'páginas': widgets.paginaserlineEdit.text(),
                'descripción': widgets.descripcionserlineEdit.toPlainText(),
                'idioma': widgets.idiomaserlineEdit.text(),
                'issn': widgets.issnserlineEdit.text(),
                'identificadores': widgets.identificadoreserlineEdit.text(),
            }
        elif tipo_de_documento == 5:
            return {
                'identificadores': widgets.identificadoresLibrolineEdit.text(),
                'título': widgets.titulolibrolineEdit.text(),
                'descripción': widgets.descripcionLibrolineEdit.toPlainText(),
                'creador': widgets.autorlibrolineEdit.text(),
                'volumen': widgets.volumelibrolineEdit.text(),
                'serie': widgets.serieLibrolineEdit.text(),
                'edición': widgets.edicionLibrolineEdit.text(),
                'espacio': widgets.lugarLibrolineEdit.text(),
                'editorial': widgets.editorialLibrolineEdit.text(),
                'fecha': widgets.fechaLibrolineEdit.text(),
                'páginas': widgets.paginasLibrolineEdit.text(),
                'idioma': widgets.idiomaLibrolineEdit.text(),
                'isbn': widgets.isbnLibrolineEdit.text(),
            }
        elif tipo_de_documento == 6:
            return {
                'nombre_archivo': widgets.nombrearchivolineEdit.text(),
                'folder': widgets.folderlineEdit.text(),
            }
        else:
            return None

    def write_fields_info(self, element_id):
        '''
        display the form from an element according with its type
        and write in its fields the information retrieved from the db
        '''

        tipo_documento = getDocumentTypeByID(element_id)
        data = getElementMetadatabyID(element_id)

        if tipo_documento == 1:
            widgets.tipodocComboBox.setCurrentIndex(0)
            widgets.titulolineEdit.setText(data[1])
            widgets.descripcionlineEdit.setPlainText(data[2])
            widgets.creadorlineEdit.setText(data[3])
            widgets.fechaIlineEdit.setText(data[4])
            widgets.fechaFlineEdit.setText(data[19])
            widgets.coberturalineEdit.setText(data[5])
            widgets.idiomalineEdit.setText(data[6])
            widgets.numfollineEdit.setText(data[7])
            widgets.identificadoreslineEdit.setText(data[9])
        elif tipo_documento == 2:
            widgets.tipodocComboBox.setCurrentIndex(1)
            widgets.titulodoclineEdit.setText(data[1])
            widgets.descripciondoclineEdit.setPlainText(data[2])
            widgets.creadordoclineEdit.setText(data[3])
            widgets.fechaIdoclineEdit.setText(data[4])
            widgets.fechaFdoclineEdit.setText(data[19])
            widgets.coberturadoclineEdit.setText(data[5])
            widgets.idiomadoclineEdit.setText(data[6])
            widgets.numfoliodoclineEdit.setText(data[7])
            widgets.identificadoresdoclineEdit.setText(data[9])
        elif tipo_documento == 3:
            widgets.tipodocComboBox.setCurrentIndex(2)
            widgets.tituloimagenlineEdit.setText(data[1])
            widgets.descripcionimagenlineEdit.setPlainText(data[2])
            widgets.creadorimagenlineEdit.setText(data[3])
            widgets.fechaimagenlineEdit.setText(data[4])
            widgets.coberturaespacialimagenlineEdit.setText(data[5])
            widgets.descripcionfisicaimagenlineEdit.setText(data[10])
            widgets.tipoimagenlineEdit.setText(data[11])
            widgets.identificadoresimagenlineEdit.setText(data[9])
        elif tipo_documento == 4:
            widgets.tipodocComboBox.setCurrentIndex(3)
            widgets.nombreserlineEdit.setText(data[1])
            widgets.volumenserlineEdit.setText(data[12])
            widgets.ejemplarserlineEdit.setText(data[13])
            widgets.fechaserlineEdit.setText(data[4])
            widgets.paginaserlineEdit.setText(data[8])
            widgets.descripcionserlineEdit.setPlainText(data[2])
            widgets.idiomaserlineEdit.setText(data[6])
            widgets.issnserlineEdit.setText(data[15])
            widgets.identificadoreserlineEdit.setText(data[9])
        elif tipo_documento == 5:
            widgets.tipodocComboBox.setCurrentIndex(4)
            widgets.titulolibrolineEdit.setText(data[1])
            widgets.autorlibrolineEdit.setText(data[3])
            widgets.volumelibrolineEdit.setText(data[12])
            widgets.serieLibrolineEdit.setText(data[16])
            widgets.edicionLibrolineEdit.setText(data[17])
            widgets.lugarLibrolineEdit.setText(data[5])
            widgets.editorialLibrolineEdit.setText(data[18])
            widgets.fechaLibrolineEdit.setText(data[4])
            widgets.paginasLibrolineEdit.setText(data[8])
            widgets.descripcionLibrolineEdit.setPlainText(data[2])
            widgets.idiomaLibrolineEdit.setText(data[6])
            widgets.isbnLibrolineEdit.setText(data[14])
            widgets.identificadoresLibrolineEdit.setText(data[9])
        elif tipo_documento == 6:
            QMessageBox.information(
                self, 'Error', 'No se puede editar un escaneo sencillo')

        # assesst editar button
        # get current widget
        widgets.botones_metadata.setCurrentWidget(widgets.editar)
        widgets.enviarFormEditButton.clicked[bool].connect(
            lambda _, element_id=element_id: self.editarForm(element_id))


    def cleanForm(self, tipo_de_documento):
        '''
        set all Text to blank
        '''
        if tipo_de_documento == 1:
            widgets.titulolineEdit.setText('')
            widgets.descripcionlineEdit.setPlainText('')
            widgets.creadorlineEdit.setText('')
            widgets.fechaIlineEdit.setText('')
            widgets.fechaFlineEdit.setText('')
            widgets.coberturalineEdit.setText('')
            widgets.idiomalineEdit.setText('')
            widgets.numfollineEdit.setText('')
            widgets.identificadoreslineEdit.setText('')
        elif tipo_de_documento == 2:
            widgets.titulodoclineEdit.setText('')
            widgets.descripciondoclineEdit.setPlainText('')
            widgets.creadordoclineEdit.setText('')
            widgets.fechaIdoclineEdit.setText('')
            widgets.fechaFdoclineEdit.setText('')
            widgets.coberturadoclineEdit.setText('')
            widgets.idiomadoclineEdit.setText('')
            widgets.numfoliodoclineEdit.setText('')
            widgets.identificadoresdoclineEdit.setText('')
        elif tipo_de_documento == 3:
            widgets.tituloimagenlineEdit.setText('')
            widgets.descripcionimagenlineEdit.setPlainText('')
            widgets.creadorimagenlineEdit.setText('')
            widgets.fechaimagenlineEdit.setText('')
            widgets.coberturaespacialimagenlineEdit.setText('')
            widgets.descripcionfisicaimagenlineEdit.setText('')
            widgets.tipoimagenlineEdit.setText('')
            widgets.identificadoresimagenlineEdit.setText('')
        elif tipo_de_documento == 4:
            widgets.nombreserlineEdit.setText('')
            widgets.volumenserlineEdit.setText('')
            widgets.ejemplarserlineEdit.setText('')
            widgets.fechaserlineEdit.setText('')
            widgets.paginaserlineEdit.setText('')
            widgets.descripcionserlineEdit.setPlainText('')
            widgets.idiomaserlineEdit.setText('')
            widgets.issnserlineEdit.setText('')
            widgets.identificadoreserlineEdit.setText('')
        elif tipo_de_documento == 5:
            widgets.titulolibrolineEdit.setText('')
            widgets.autorlibrolineEdit.setText('')
            widgets.volumelibrolineEdit.setText('')
            widgets.serieLibrolineEdit.setText('')
            widgets.edicionLibrolineEdit.setText('')
            widgets.lugarLibrolineEdit.setText('')
            widgets.editorialLibrolineEdit.setText('')
            widgets.fechaLibrolineEdit.setText('')
            widgets.paginasLibrolineEdit.setText('')
            widgets.descripcionLibrolineEdit.setPlainText('')
            widgets.idiomaLibrolineEdit.setText('')
            widgets.isbnLibrolineEdit.setText('')
            widgets.identificadoresLibrolineEdit.setText('')
        elif tipo_de_documento == 6:
            widgets.nombrearchivolineEdit.setText('')
            widgets.folderlineEdit.setText('')
        else:
            return None

    def write_json(self, export_dir, element_info, element_id, tipo):
        # dict to json
        element_info_json = json.dumps(element_info)
        # write json to file
        with open(f'{export_dir}/{element_id}_{tipo}.json', 'w') as f:
            f.write(element_info_json)

    def zoom_dial(self):
        value = widgets.zoom_dial.value()
        widgets.zoom_valuedit.setText(str(value))

    def exposicion(self):
        value = widgets.exposicionDial.value()
        widgets.exposicionValue.setText(str(value))

    def zoom_dial_2(self):
        value = widgets.zoom_dial_2.value()
        widgets.zoom_valuedit_2.setText(str(value))

    def exposicion_2(self):
        value = widgets.exposicionDial_2.value()
        widgets.exposicionValue_2.setText(str(value))

    def selectCam(self, index_value):
        widgets.selectCamIzq.setCurrentIndex(index_value)
        widgets.selectCamDer.setCurrentIndex(index_value)

    def save_project_config(self, path, zoom, shutter, orientacion, dng, info):
        '''
        save config
        '''
        config = {
            'zoom': zoom,
            'shutter': shutter,
            'orientacion': orientacion,
            'dng': dng,
        }
        # merge config dict with info dict
        config.update(info)
        # save config
        with open(os.path.join(path, "config_project.json"), 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)

    def enviarForm(self):
        '''
        envia el formulario a la base de datos
        '''
        tipo_de_documento = widgets.tipodocComboBox.currentIndex() + 1

        #zoom_value = widgets.zoom_dial.value()
        zoom_value = widgets.zoom_valuedit.text()
        shutter_value = widgets.exposicionValue.text()
        orientacion_value = [
            "vertical" if widgets.orientacionValue.currentIndex() == 0 else "horizontal"][0]

        # dng_checkbox value
        if widgets.dng_check.isChecked():
            dng = 'True'
        else:
            dng = 'False'

        # validate required items
        if self.requiredFields(tipo_de_documento):
            # create element
            if not tipo_de_documento == 6:
                createElement(tipo_de_documento, 0, 1)

                # get the identifier of last element created
                id_element = getLastElementID()

                # get the info for the form fields
                info = self.get_fields_info(tipo_de_documento)

                # insert the info into the database
                insertInfo(id_element, info)

                datos_elemento = getElementMetadatabyID(id_element)

                # create project directory
                folder_path = os.path.join(IMGDIR, str(datos_elemento[9]))
                try:
                    os.makedirs(folder_path, exist_ok=True)
                except OSError as e:
                    print(e)
                    log.log(
                        f'ERROR: Al crear {folder_path} se encontró un OSError {e} en {__file__} linea {e.__traceback__.tb_lineno}')
                    raise

                # save project_config.json file
                self.save_project_config(folder_path, zoom_value,
                                         shutter_value, orientacion_value, dng, info)

                # clean form fields
                self.cleanForm(tipo_de_documento)

                # set and config Scanner Page
                self.set_scanner_page(id_element)


    def editarForm(self, element_id_editar):
        '''
        edita el elemento en la base de datos
        '''
        tipo_de_documento = widgets.tipodocComboBox.currentIndex() + 1

        #zoom_value = widgets.zoom_dial.value()
        zoom_value = widgets.zoom_valuedit.text()
        shutter_value = widgets.exposicionValue.text()
        orientacion_value = "vertical" if widgets.orientacionValue.currentIndex() == 0 else "horizontal"
        dng = "True" if widgets.dng_check.isChecked() else "False"

        # validate required items
        if self.requiredFields(tipo_de_documento):

            # get the info for the form fields
            info = self.get_fields_info(tipo_de_documento)

            # insert the info into the database
            editInfo(element_id_editar, info)

            datos_elemento = getElementMetadatabyID(element_id_editar)

            # create project directory
            folder_path = os.path.join(IMGDIR, str(datos_elemento[9]))

            # save project_config.json file
            self.save_project_config(folder_path, zoom_value,
                                     shutter_value, orientacion_value, dng, info)

            # clean form fields
            self.cleanForm(tipo_de_documento)

            # back to home
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            
            # close button signal
            widgets.enviarFormEditButton.clicked.disconnect()

            log.log(f'INFO: Se editó el elemento {element_id_editar} con los datos {info}')

            self.display_elements()

        else:
            log.log(f"ERROR: No se pudo editar el elemento {element_id_editar} en {__file__} linea {sys._getframe().f_lineno}")


    def openimagesDir(self):
        '''
        open images directory from label path
        '''
        ruta = widgets.directorio_elementos.text()
        if sys.platform == 'linux':
            # works on raspberry pi OS
            os.system('xdg-open ' + ruta)
        elif sys.platform == 'win32':
            # this option is just for development
            os.startfile(ruta)
        else:
            print('No se puede abrir la carpeta')
            log.log(f'ERROR: No se puede abrir la carpeta {ruta}')
            log.log(f'ERROR: {sys.platform}')

    def lenImagenesDir(self, folder_path):
        '''
        return the number of images in the directory
        and set the label with the number
        '''
        try:
            num_imagenes = len(os.listdir(folder_path))
        except FileNotFoundError:
            num_imagenes = 0

        widgets.cantidadimgsLabel.setText(str(num_imagenes))

    def open_cameras(self):
        '''
        Intenta saber si hay cámaras conectadas y establece
        una conexión con una o dos cámaras
        return: single or dual camera mode
        '''

        try:
            # avoid error if no cameras are connected
            cam_response = Cams.cam()
            intentos = 0
            while cam_response is False:
                respuesta = QMessageBox.question(self, 'Error', 'No es posible iniciar \
                 porque no se encontró ninguna cámara conectada.\n \
                     Por favor, conecte al menos una cámara y vuelva a intentarlo.',
                                                 QMessageBox.Ok | QMessageBox.Discard)
                if respuesta == QMessageBox.Ok:
                    time.sleep(2)
                    cam_response = Cams.cam()
                    intentos += 1
                    if intentos == 3:
                        QMessageBox.critical(
                            self, 'Error', 'No fue posible iniciar la cámara.')
                        log.log(f'ERROR: No fue posible iniciar la cámara después de tres intentos. \n \
                            cam_response = {cam_response}')
                        return False
                else:
                    cam_response = True
                    # back to home
                    widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
                    self.display_elements()
            return "dual_camera_mode"

        except IndexError as e:
            log.log(
                f"ERROR: {e} en {__file__} linea {e.__traceback__.tb_lineno}")
            # single camera QMessageBox, accept retry cancel
            respuesta = QMessageBox.question(self, "Una cámara conectada",
                                             "Solamente una cámara está conectada.\n \
                                        ¿Desea intentar escanear con ella?",
                                             QMessageBox.Ok | QMessageBox.Retry | QMessageBox.Cancel)

            if respuesta == QMessageBox.Ok:
                return "single_camera_mode"
            elif respuesta == QMessageBox.Retry:
                respuesta = QMessageBox.question(self, "Reintentar",
                                                 "Asegúrese de que la cámara esté conectada y vuelva a intentarlo.",
                                                 QMessageBox.Ok | QMessageBox.Cancel)
                if respuesta == QMessageBox.Ok:
                    cam_response = Cams.cam()
                    return "dual_camera_mode"
                else:
                    # back to home
                    widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
                    self.display_elements()

    def set_scanner_page(self, id_element=None):
        # set current page to escanerPage
        widgets.stackedWidget.setCurrentWidget(widgets.escanerPage)

        # obtener datos para la barra izquierda
        if id_element is None:
            id_element = getLastElementID()

        datos_elemento = getElementMetadatabyID(id_element)

        # show data in labels
        widgets.elementoIDLabel.setText(datos_elemento[9])
        widgets.elementoTituloLabel.setText(datos_elemento[1])

        # get config file
        config_file = os.path.join(IMGDIR, str(
            datos_elemento[9]), 'config_project.json')

        cfg_text = open(config_file, 'r')
        cfg_data = json.load(cfg_text)
        widgets.configLabel.setText(f"""
        <b>Zoom:</b> {cfg_data['zoom']}. <br \>
        <b>Velocidad obturación:</b> {cfg_data['shutter']}. <br \>
        <b>Orientación:</b> {cfg_data['orientacion']}. <br \>
        <b>DNG:</b> {str(cfg_data['dng'])}.
        """)

        # path to images directory
        folder_path = os.path.join(IMGDIR, str(datos_elemento[9]))

        # set folder_path to label
        widgets.directorio_elementos.setText(os.path.abspath(folder_path))

        self.lenImagenesDir(Path(folder_path, 'data', 'JPG'))

        return self.open_cameras()

    # Funciones de control de la cámara

    def capturar(self):
        # asegurar el botón correcto
        widgets.controlesCamstackedWidget.setCurrentWidget(
            widgets.captura)

        # save the images
        element_ident = widgets.elementoIDLabel.text()
        element_id = getElementIdByMetadata(element_ident)

        # get last image number pair
        last_img_group = getLastImgs(element_id)
        try:
            numbers = [li.replace('.jpg', '').replace('.dng', '')
                       for li in last_img_group]
            numbers = list(dict.fromkeys(numbers))
            # esto evita que se presenten errores si se desconecta una cámara y se sigue capturando
            # con una de ellas.
            # TODO: Con una sola cámara ¿cómo evitar que se creen ids para pares o impares?
            numbers = numbers[:2]
            last_img_left = [int(i) for i in numbers if int(i) % 2 != 0]
            last_img_right = [int(i) for i in numbers if int(i) % 2 == 0]
            # En caso de haberse tomado repetidas fotografías con una sola cámara, este método
            # retoma la serie par e impar.
            # TODO: corrección hecha con premura por deadline. Requiere una solución más elegante.
            if len(last_img_left) == 0:
                try:
                    last_img_left = last_img_right - 1
                except TypeError:
                    last_img_left = last_img_right[0] - 1
                log.log(f'WARNING: Se ha restablecido la secuencia en la cámara izquierda. \
                    last_img_left = {last_img_left}')
            elif len(last_img_right) == 0:
                try:
                    last_img_right = last_img_left - 1
                except TypeError:
                    last_img_right = last_img_left[0] - 1
                log.log(f'WARNING: Se ha restablecido la secuencia en la cámara derecha. \
                    last_img_right = {last_img_right}')
            else:
                # cachar algún error desconocido
                log.log(
                    f'INFO: secuencia de imágenes sin issues. last_img_left = {last_img_left} y last_img_right = {last_img_right}')
                pass
            try:
                last_img_left = [last_img_left[0] +
                                 2 if last_img_left is not 0 else 1][0]
            except TypeError:
                last_img_left = [last_img_left +
                                 2 if last_img_left is not 0 else 1][0]
            last_img_left = f'{last_img_left:04d}'
            try:
                last_img_right = last_img_right[0] + 2
            except TypeError:
                last_img_right = last_img_right + 2
            last_img_right = f'{last_img_right:04d}'
        except AttributeError:
            last_img_left = '0001'
            last_img_right = '0002'

        widgets.statusLabel.setText("capturando imágenes...")

        left_img_path = Path(
            widgets.directorio_elementos.text(), 'data', 'JPG', f'{last_img_left}.jpg')
        right_img_path = Path(
            widgets.directorio_elementos.text(), 'data', 'JPG', f'{last_img_right}.jpg')

        config_project = open(os.path.join(IMGDIR, widgets.directorio_elementos.text(
        ), 'config_project.json'), 'r', encoding='utf-8')
        config_project = json.load(config_project)

        zoom = int(config_project['zoom'])
        shutter = config_project['shutter']
        orientacion = config_project['orientacion']

        try:
            # TODO: ¡Hacer que esto funcione!
            dng_status = config_project['dng']
            Cams.captura(element_ident, last_img_left,
                         last_img_right, zoom, shutter, orientacion, dng_status)
        except TypeError as e:
            QMessageBox.warning(self, "Error",
                                "No se encontraron cámaras", QMessageBox.Ok)
            log.log(
                f'ERROR: No se encontraron cámaras en {__file__} linea {e.__traceback__.tb_lineno}')

        # insert overlay to avoid unwanted clicks on capture button
        # display validation buttons
        movie = QMovie("imgs/ajax-loader.gif")
        # scale gif to 30 * 30 pixels
        movie.setScaledSize(QSize(30, 30))
        widgets.capturando.setMovie(movie)
        movie.start()
        widgets.controlesCamstackedWidget.setCurrentWidget(
            widgets.validar)
        app.processEvents()

        # Este loop permite que haya una espera de 10 segundos hasta que se permita una nueva toma
        if Cams.len_devs() > 1:
            tolerancia = 0
            while not os.path.exists(left_img_path) or not os.path.exists(right_img_path):
                time.sleep(2)
                tolerancia += 1
                if tolerancia > 5:
                    break
        else:
            time.sleep(5)

        # erase image labels
        widgets.imagenizqLabel.setPixmap(QPixmap())
        widgets.imagederLabel.setPixmap(QPixmap())

        # for some reason QPixmap is not working with PosixPath
        # raise TypeError. As a temporary solution transform PosixPath to str
        left_img_path = left_img_path.absolute().as_posix()
        right_img_path = right_img_path.absolute().as_posix()

        left_img = QImage(left_img_path)
        right_img = QImage(right_img_path)

        left_img = left_img.scaled(
            200, 266, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        right_img = right_img.scaled(
            200, 266, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)

        widgets.imagenizqLabel.setPixmap(QPixmap.fromImage(left_img))
        widgets.imagederLabel.setPixmap(QPixmap.fromImage(right_img))

        self.lenImagenesDir(
            Path(widgets.directorio_elementos.text(), 'data', 'JPG'))  # Fix images count

        widgets.statusLabel.setText(
            f"Capturadas {last_img_left} y {last_img_right}.\nTiempo promedio de captura {promedio_captura()}")
        log.log(
            f'INFO: Imágenes {last_img_left} y {last_img_right} capturadas')

        # display validation buttons
        widgets.controlesCamstackedWidget.setCurrentWidget(
            widgets.captura)

        mem = psutil.virtual_memory()
        log.log(f'INFO: Memoria libre: {mem.free / 1024 ** 2} MB')
        if mem.available < 500 * 1024 * 1024:
            log.log('INFO: Se ha liberado memoria')
            gc.collect()

    def validateCaptura(self):
        """
        Función obsoleta. Se mantiene por compatibilidad con versiones anteriores.
        """

        # actualiza la cantidad de imagenes en la carpeta
        self.lenImagenesDir(
            Path(widgets.directorio_elementos.text(), 'data', 'JPG'))
        widgets.statusLabel.setText("Iniciar nueva captura")
        # back to captura widget
        widgets.controlesCamstackedWidget.setCurrentWidget(widgets.captura)

    def resetCaptura(self):
        # delete most recent images from directory
        folder_path = widgets.directorio_elementos.text()

        tipos = ['JPG', 'DNG']
        for t in tipos:
            last_imagenes = glob.glob(f'{folder_path}/data/{t}/*.{t.lower()}')
            last_imagenes.sort(key=os.path.getctime, reverse=True)
            last_imagenes = last_imagenes[:2]
            for f in last_imagenes:
                try:
                    os.remove(f)
                except OSError as e:
                    log.log(
                        f'ERROR: Al eliminar {f} se encontró un OSError {e} en {__file__} linea {e.__traceback__.tb_lineno}')
                    raise

        # erase image labels
        widgets.imagenizqLabel.setPixmap(QPixmap())
        widgets.imagederLabel.setPixmap(QPixmap())

        # back to capture widget
        widgets.controlesCamstackedWidget.setCurrentWidget(widgets.captura)
        self.lenImagenesDir(Path(folder_path, 'data', 'JPG'))

    def finalizarCaptura(self):
        '''
        gentle close escanerPage and back to home
        '''
        if QMessageBox.question(self, "Cerrar el proyecto",
                                "¿Está seguro que desea cerrar el proyecto?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:

            widgets.imagederLabel.setPixmap(QPixmap())
            widgets.imagenizqLabel.setPixmap(QPixmap())
            nombre_proyecto = widgets.elementoIDLabel.text()
            widgets.elementoIDLabel.setText('')
            titulo_proyecto = widgets.elementoTituloLabel.text()
            widgets.elementoTituloLabel.setText('')
            widgets.directorio_elementos.setText('')
            widgets.cantidadimgsLabel.setText('')
            widgets.configLabel.setText('')
            # back to home
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            self.display_elements()
            # add label to verticallayout
            warning_label = QLabel(
                f"El paquete del proyecto \"{titulo_proyecto}\" se está creando... Puede tomar unos minutos.")
            warning_label.setStyleSheet("color: red")
            widgets.verticalLayout_20.addWidget(warning_label)

            try:
                Cams.pause_devs()
            except Exception as e:
                log.log(
                    f'WARNING: No se pudieron detener las cámaras. {e} en {__file__} linea {e.__traceback__.tb_lineno}')

            app.processEvents()
            UpdateFiles(nombre_proyecto).finish_and_update()
            widgets.verticalLayout_20.removeWidget(warning_label)
            warning_label.deleteLater()
            app.processEvents()
            self.display_elements()
    # Configuration page

    def set_config_page(self):
        '''
        set config page
        '''
        expo_pred = config['camaras']['exposicion_predeterminada']
        zoom_pred = config['camaras']['zoom_predeterminado']

        valor_dial_expo = [int(expo_pred) if expo_pred != '' else 25][0]
        valor_dial_zoom = [int(zoom_pred) if zoom_pred != '' else 27][0]
        # set dial value
        widgets.exposicionDial_2.setValue(valor_dial_expo)
        widgets.zoom_dial_2.setValue(valor_dial_zoom)
        # set label value
        widgets.exposicionValue_2.setText(str(valor_dial_expo))
        widgets.zoom_valuedit_2.setText(str(valor_dial_zoom))

        return self.open_cameras()

    def test_config(self):
        '''
        replica el comportamiento de la funcion capturar() de manera más sintética.
        Las imágenes en el test siempre se sobreescriben.
        '''
        # delete test_config folder
        try:
            shutil.rmtree(Path(IMGDIR, 'test_config', 'data', 'JPG'))
        except Exception as e:
            log.log(
                f'No se elimina la carpeta test_config porque no se ha creado. {e} en {__file__} linea {e.__traceback__.tb_lineno}')
            pass

        # get values from selectores
        expo = widgets.exposicionValue_2.text()
        zoom = widgets.zoom_valuedit_2.text()
        dng = False

        # test captura
        Cams.captura("test_config", "0000", "0001",
                     zoom, expo, "vertical", dng)

        left_image_path = Path(IMGDIR, 'test_config',
                               'data', 'JPG', '0000.jpg')
        right_image_path = Path(IMGDIR, 'test_config',
                                'data', 'JPG', '0001.jpg')

        tolerancia = 0
        while not os.path.exists(left_image_path) or not os.path.exists(right_image_path):
            time.sleep(2)
            tolerancia += 1
            if tolerancia > 5:
                break

        # set Pixmap to empty
        widgets.imagenizqLabel_2.setPixmap(QPixmap())
        widgets.imagederLabel_2.setPixmap(QPixmap())

        left_image_path = left_image_path.absolute().as_posix()
        right_image_path = right_image_path.absolute().as_posix()

        left_img = QImage(left_image_path)
        right_img = QImage(right_image_path)

        left_img = left_img.scaled(
            250, 250, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        right_img = right_img.scaled(
            250, 250, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)

        widgets.imagenizqLabel_2.setPixmap(QPixmap.fromImage(left_img))
        widgets.imagederLabel_2.setPixmap(QPixmap.fromImage(right_img))

    def save_config(self):
        '''
        Guardar la configuración deseada en el archivo config.cfg
        '''
        # reload config.cfg
        config.read(CONFIG_PATH)
        # get values from selectores
        expo = widgets.exposicionValue_2.text()
        zoom = widgets.zoom_valuedit_2.text()
        dng = "False"
        if not widgets.selectCamIzq.currentIndex != 0:
            cam_izq = config['camaras']['serial_der']
            cam_der = config['camaras']['serial_izq']
        else:
            cam_izq = config['camaras']['serial_izq']
            cam_der = config['camaras']['serial_der']

        print(
            f'Exposicion: {expo} Zoom: {zoom} DNG: {dng} Cam Izq: {cam_izq} Cam Der: {cam_der}')

        # save config
        config['camaras']['serial_izq'] = cam_izq
        config['camaras']['serial_der'] = cam_der
        config['camaras']['exposicion_predeterminada'] = expo
        config['camaras']['zoom_predeterminado'] = zoom
        config['camaras']['dng'] = dng
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)

        # delete test_config folder
        try:
            shutil.rmtree(Path(IMGDIR, 'test_config'))
        except Exception as e:
            log.log(
                f'WARNING: No se pudo borrar la carpeta test_config. {e} en {__file__} linea {e.__traceback__.tb_lineno}')

        # back to inicio
        widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
        Cams.close_dev()

    def b2_config(self):
        """
        solamente pasa al formulario de configuración
        """
        widgets.b2conf.setCurrentWidget(widgets.b2confForm)

    def b2_config_set(self):
        """
        Recupera la información del formulario y 
        crea con ella un archivo .env
        """

        # get values from selectores
        endpoint = widgets.endpointInput.text()
        keyID = widgets.keyIDInput.text()
        keyName = widgets.keyNameInput.text()  # nombre del bucket
        appKey = widgets.appKeyInput.text()

        config['PROJECT']['project_name'] = keyName
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)

        # assert endpoint starts with https://
        if not endpoint.startswith('https://'):
            endpoint = f'https://{endpoint}'

        # save config
        with open("setup/.env", "w") as f:
            f.write(f"ENDPOINT={endpoint}\n")
            f.write(f"KEY_ID={keyID}\n")
            f.write(f"KEY_NAME={keyName}\n")
            f.write(f"APPLICATION_KEY={appKey}\n")

        widgets.b2conf.setCurrentWidget(widgets.b2ini)

    def send2B2(self):
        """
        Sincroniza los archivos con el bucket en B2
        Requiere previa configuración del archivo .env desde
        el formulario en la página de configuración.
        """

        # crea objeto Sync
        widgets.promtText.setText("\nIniciando sincronización...")
        app.processEvents()
        try:
            sync = b2.Sync()
            widgets.promtText.setText(
                f"{widgets.promtText.text()}\nSincronizando... (no cierre esta ventana hasta finalizar la transferencia)")
            app.processEvents()
            sync.sync_dir()
            widgets.promtText.setText(
                f"{widgets.promtText.text()}\nSincronización finalizada.\n{sync}")
            app.processEvents()
        except Exception as e:
            log.log(
                f'ERROR: No se pudo sincronizar. {e} en {__file__} linea {e.__traceback__.tb_lineno}')
            widgets.promtText.setText(
                f"ERROR: No se pudo sincronizar. {e}")

    def gentle_close(self):
        '''
        close cams session, close db connection and close application
        '''
        Cams.close_dev()
        kill_connection()
        window.close()

# Fin de las funciones de la aplicación


if __name__ == '__main__':
    # crear una aplicación Qt
    app = QApplication(sys.argv)
    locale = getdefaultlocale()

    # Aplicar el traductor para español
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)

    # Crear y mostrar la ventana principal
    window = MainWindow()
    window.showMaximized()
    # correr el loop principal Qt
    sys.exit(app.exec_())
