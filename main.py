# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.4
# 2022-03-18
#
# ///////////////////////////////////////////////////////////////

import sys
import os
from pathlib import Path
import json
import shutil
from locale import getdefaultlocale
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QPixmap, QRegExpValidator

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel, QGridLayout, QPushButton
from PySide2.QtCore import QSize, QTranslator, QLibraryInfo, QRegExp, Qt

from ui_main import Ui_MainWindow
from db_handler import connectToDatabase, createElement, getLastId, insertInfo, editInfo, getElementInfo, getLastElementID, listofIDs, getElementMetadatabyID, erase_element, getImagesInfo, kill_connection, getLastImgs
from camcontrol import Cam
import configparser
import ctypes
import time

# config

config = configparser.ConfigParser()
config.read(Path('config.cfg'))

version = config['DEFAULT']['version']

# Check compatibility and return images directory

if sys.platform == 'linux':
    IMGDIR = config['DEFAULT']['img_dir']
elif sys.platform == 'win32':
    IMGDIR = config['DEFAULT']['images_dir_windows']
else:
    ctypes.windll.user32.MessageBoxW(
        0, "Sistema operativo no soportado", "Error", 0)
    sys.exit(0)

# Entorno de la aplicación

# logs
try:
    os.makedirs("logs", exist_ok=True)
except OSError:
    raise


def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    error = open("logs/neoscan_log.log", "a")
    error.write(ts + ": " + msg + "\n")
    error.close()


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
    log(f"Reinicio de la aplicación. Status: {status}")


def inicio_proyecto():
    devs = Cam().devs
    return devs


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
        global cams
        cams = inicio_proyecto()
        """if len(cams) <= 1:
            QMessageBox().warning(self, "Error",
                                  "No se encontró ninguna cámara.\nEncienda las cámaras para evitar errores al escanear.", QMessageBox.Discard)
        """
        # Conectar a la base de datos
        try:
            connectToDatabase()
        except Exception as e:
            print("Error en la conexión con la base de datos")
            log(
                f"ERROR Falló conexión con la base de datos. Error {e} en {__file__} linea {e.__traceback__.tb_lineno}")
            raise

        # set version
        widgets.versionLabel.setText(f'v{version}')

        # close button
        widgets.closeButton.clicked.connect(self.gentle_close)

        # Botones, menú
        widgets.inicioButton.clicked.connect(self.buttonClick)
        widgets.coleccionesButton.clicked.connect(self.buttonClick)
        widgets.escanerButton.clicked.connect(self.buttonClick)

        # Seleccionar página de inicio
        widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)

        # set home page
        widgets.nuevoProyectoButton.clicked.connect(self.buttonClick)
        self.display_elements()

        # Botón regresar al inicio
        widgets.backtoInicioButton.clicked.connect(self.buttonClick)

        # Página de metadatos
        widgets.tipodocComboBox.currentIndexChanged.connect(self.indexChange)
        widgets.enviarFormButton.clicked.connect(self.enviarForm)
        widgets.enviarFormEditButton.clicked.connect(
            self.editarForm)
        widgets.browserDirButton.clicked.connect(self.getDirName)

        # abrir directorio
        widgets.openFolderButton.clicked.connect(self.openimagesDir)

        # tomar fotografía
        widgets.capturaButton.clicked.connect(self.capturar)
        # validar fotografía
        widgets.validateButton.clicked.connect(self.validateCaptura)
        widgets.resetButton.clicked.connect(self.resetCaptura)
        # cerrar escaner
        widgets.finalizarButton.clicked.connect(self.finalizarCaptura)

    # navigation functions

    # Navegar por las páginas desde el menú principal

    def buttonClick(self):
        # nombre del botón
        btn = self.sender()
        btnName = btn.objectName()

        # navega por cada una de las páginas
        if btnName == "inicioButton":
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            self.display_elements()
        elif btnName == "backtoInicioButton":
            msgBox = QMessageBox()
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
            widgets.stackedWidget.setCurrentWidget(widgets.metadataPage)
            widgets.tipoColeccion.setCurrentWidget(widgets.formLegajo)
            widgets.botones_metadata.setCurrentWidget(widgets.enviar)
        elif btnName == "escanerButton":
            self.set_scanner_page()
            widgets.controlesCamstackedWidget.setCurrentWidget(widgets.captura)

    # Funciones para la página de elementos

    def display_elements(self):

        try:
            widgets.verticalLayout_20.removeItem(widgets.elementslayout)
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

            image_path = Path(IMGDIR + f'/{element_id}/' + 'JPG')
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
            label = QLabel()
            label.setText(
                f'<h3>{element_name}</h3> [{num_imagenes} imágenes]\n{element_description}')
            label.setObjectName(f"element_name_{element_id}")
            label.setMinimumSize(QSize(400, 70))
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignLeft)
            widgets.elementslayout.addWidget(label, id, 1)

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
            button.clicked.connect(self.edit_element)
            widgets.elementslayout.addWidget(button, id, 2)

            button = QPushButton()
            # button.setText("Añadir imágenes")
            button.setObjectName(f"edit_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon1 = QIcon()
            icon1.addFile("imgs/icons/camera-to-take-photos.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon1)
            button.setIconSize(QSize(20, 20))
            button.clicked.connect(lambda: self.set_scanner_page(element_id))
            widgets.elementslayout.addWidget(button, id, 2)

            button = QPushButton()
            # button.setText("Exportar")
            button.setObjectName(f"export_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon2 = QIcon()
            icon2.addFile("imgs/icons/download-symbol.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon2)
            button.setIconSize(QSize(20, 20))
            button.clicked.connect(
                lambda: self.export_element(element_id, image_path))
            widgets.elementslayout.addWidget(button, id, 3)

            button = QPushButton()
            # button.setText("Eliminar")
            button.setObjectName(f"delete_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon3 = QIcon()
            icon3.addFile("imgs/icons/trash-can-with-cover-from-side-view.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon3)
            button.setIconSize(QSize(20, 20))
            button.clicked.connect(
                lambda: self.delete_element(element_id, image_path))
            widgets.elementslayout.addWidget(button, id, 4)

        widgets.verticalLayout_20.addLayout(widgets.elementslayout)

    def edit_element(self, element_id):
        '''
        edit element from element_id
        '''
        # go to metadata page
        widgets.stackedWidget.setCurrentWidget(widgets.metadataPage)
        widgets.botones_metadata.setCurrentWidget(widgets.editar)

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
            log(f"ERROR al obtener datos del elemento {element_info}")

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
                log(f"ERROR al copiar imágenes {image_path}")

        QMessageBox.information(
            widgets.stackedWidget, "Exportar", "Se ha exportado el elemento correctamente.")

    def write_json(self, export_dir, element_info, element_id, tipo):
        # dict to json
        element_info_json = json.dumps(element_info)
        # write json to file
        with open(f'{export_dir}/{element_id}_{tipo}.json', 'w') as f:
            f.write(element_info_json)

    def delete_element(self, element_id, image_path):
        '''
        borra datos y archivos de un elemento
        '''
        if QMessageBox.question(
                widgets.stackedWidget, "Eliminar", "¿Está seguro de eliminar el elemento?") == QMessageBox.Yes:
            erase_element(element_id)
            # delete files from image_path
            for file in os.listdir(image_path):
                os.remove(f"{image_path}/{file}")
            QMessageBox.information(
                widgets.stackedWidget, "Eliminar", "Se ha eliminado el elemento correctamente.")

        # return to home
        widgets.stackedWidget.setCurrentWidget(widgets.homePage)
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
            if widgets.titulolineEdit.text() == "":
                QMessageBox().warning(self, "Error",
                                      "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formLegajo)
                return False
            else:
                return True
        elif tipo_documento == 2:
            if widgets.titulodoclineEdit.text() == "":
                QMessageBox().warning(self, "Error",
                                      "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formDocumento)
                return False
            else:
                return True
        elif tipo_documento == 3:
            if widgets.tituloimagenlineEdit.text() == "":
                QMessageBox().warning(self, "Error",
                                      "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formImagen)
                return False
            else:
                return True
        elif tipo_documento == 4:
            if widgets.nombreserlineEdit.text() == "":
                QMessageBox().warning(self, "Error",
                                      "El campo Nombre no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formSeriada)
                return False
            else:
                return True
        elif tipo_documento == 5:
            if widgets.titulolibrolineEdit.text() == "":
                QMessageBox().warning(self, "Error",
                                      "El campo Título no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formLibro)
                return False
            else:
                return True
        elif tipo_documento == 6:
            if widgets.nombrearchivolineEdit.text() == "":
                QMessageBox().warning(self, "Error",
                                      "El campo Nombre no puede estar vacío.", QMessageBox.Discard)
                widgets.tipoColeccion.setCurrentWidget(widgets.formSimple)
                return False
            elif widgets.folderlineEdit.text() == "":
                QMessageBox().warning(self, "Error",
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
                'nombre': widgets.nombreserlineEdit.text(),
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
                'título': widgets.titulolibrolineEdit.text(),
                'creador': widgets.autorlibrolineEdit.text(),
                'volumen': widgets.volumelibrolineEdit.text(),
                'serie': widgets.serieLibrolineEdit.text(),
                'edición': widgets.edicionLibrolineEdit.text(),
                'lugar': widgets.lugarLibrolineEdit.text(),
                'editorial': widgets.editorialLibrolineEdit.text(),
                'fecha': widgets.fechaLibrolineEdit.text(),
                'páginas': widgets.paginasLibrolineEdit.text(),
                'descripción': widgets.descripcionLibrolineEdit.toPlainText(),
                'idioma': widgets.idiomaLibrolineEdit.text(),
                'isbn': widgets.isbnLibrolineEdit.text(),
                'identificadores': widgets.identificadoresLibrolineEdit.text(),
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

        tipo_documento = getElementInfo(element_id)['tipo_documento']
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

    def enviarForm(self):
        '''
        envia el formulario a la base de datos
        '''
        tipo_de_documento = widgets.tipodocComboBox.currentIndex() + 1

        # validate required items
        if self.requiredFields(tipo_de_documento):
            # create element
            if not tipo_de_documento == 6:
                createElement(tipo_de_documento, 0, 1)

                # get the id of last element created
                id_element = getLastId()

                # get the info for the form fields
                info = self.get_fields_info(tipo_de_documento)

                # insert the info into the database
                insertInfo(id_element, info)

                # clean form fields
                self.cleanForm(tipo_de_documento)

                # set and config Scanner Page
                self.set_scanner_page(id_element)

    def editarForm(self, element_id):
        '''
        edita el elemento en la base de datos
        '''
        tipo_de_documento = widgets.tipodocComboBox.currentIndex() + 1

        # validate required items
        if self.requiredFields(tipo_de_documento):

            # get the info for the form fields
            info = self.get_fields_info(tipo_de_documento)

            # insert the info into the database
            editInfo(element_id, info)

            # clean form fields
            self.cleanForm(tipo_de_documento)

            # back to home
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            self.display_elements()

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
            log(f'ERROR: No se puede abrir la carpeta {ruta}')
            log(f'ERROR: {sys.platform}')

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
            cam_response = Cam().cam()
            intentos = 0
            while cam_response is None:
                respuesta = QMessageBox.question(self, 'Error', 'No es posible iniciar \
                 porque no se encontró ninguna cámara conectada.\n \
                     Por favor, conecte al menos una cámara y vuelva a intentarlo.',
                                                 QMessageBox.Ok | QMessageBox.Discard)
                if respuesta == QMessageBox.Ok:
                    time.sleep(2)
                    cam_response = Cam().cam()
                    intentos += 1
                    if intentos == 3:
                        QMessageBox.critical(
                            self, 'Error', 'No fue posible iniciar la cámara.')
                        log(f'ERROR: No fue posible iniciar la cámara después de tres intentos. \n \
                            cam_response = {cam_response}')
                        return None
                else:
                    cam_response = True
                    # back to home
                    widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
                    self.display_elements()
            return "dual_camera_mode"

        except IndexError as e:
            log(f"ERROR: {e} en {__file__} linea {e.__traceback__.tb_lineno}")
            # single camera QMessageBox, accept retry cancel
            respuesta = QMessageBox().question(self, "Una cámara conectada",
                                               "Solamente una cámara está conectada.\n \
                                        ¿Desea intentar escanear con ella?",
                                               QMessageBox.Ok | QMessageBox.Retry | QMessageBox.Cancel)

            if respuesta == QMessageBox.Ok:
                return "single_camera_mode"
            elif respuesta == QMessageBox.Retry:
                respuesta = QMessageBox().question(self, "Reintentar",
                                                   "Asegúrese de que la cámara esté conectada y vuelva a intentarlo.",
                                                   QMessageBox.Ok | QMessageBox.Cancel)
                if respuesta == QMessageBox.Ok:
                    cam_response = Cam().cam()
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
        widgets.elementoIDLabel.setText(str(id_element))
        widgets.elementoTituloLabel.setText(datos_elemento[1])

        # create directory to save images
        folder_path = Path(IMGDIR, str(id_element))

        try:
            os.makedirs(folder_path, exist_ok=True)
        except OSError as e:
            print(e)
            log(f'ERROR: Al crear {folder_path} se encontró un OSError {e} en {__file__} linea {e.__traceback__.tb_lineno}')
            raise

        # set folder_path to label
        widgets.directorio_elementos.setText(os.path.abspath(folder_path))

        self.lenImagenesDir(Path(folder_path, 'JPG'))

        return self.open_cameras()

    # Funciones de control de la cámara

    def capturar(self):
        # save the images
        element_id = widgets.elementoIDLabel.text()

        # get last image number pair
        last_img_pair = getLastImgs(element_id)
        last_img_left = f'{last_img_pair[0]:04d}'
        last_img_right = f'{last_img_pair[1]:04d}'

        widgets.statusLabel.setText("capturando imágenes...")

        left_img_path = Path(
            widgets.directorio_elementos.text(), 'JPG', f'{last_img_left}.jpg')
        right_img_path = Path(
            widgets.directorio_elementos.text(), 'JPG', f'{last_img_right}.jpg')

        try:
            Cam().captura(element_id, last_img_left, last_img_right)
        except TypeError:
            QMessageBox().warning(self, "Error",
                                        "No se encontraron cámaras", QMessageBox.Ok)

        while not os.path.exists(left_img_path) or not os.path.exists(right_img_path):
            time.sleep(0.1)

        widgets.statusLabel.setText(
            f"Capturadas {last_img_left} y {last_img_right}")

        widgets.imagenizqLabel.setPixmap(
            QPixmap(left_img_path))
        widgets.imagederLabel.setPixmap(
            QPixmap(right_img_path))

        # display validation buttons
        widgets.controlesCamstackedWidget.setCurrentWidget(
            widgets.validar)

    def validateCaptura(self):
        widgets.statusLabel.setText(
            f"últimos folios capturados {widgets.folioizqLineEdit.text()} y {widgets.folioderLineEdit.text()}")
        # erase the folio labels
        widgets.folioizqLineEdit.setText('')
        widgets.folioderLineEdit.setText('')
        # erase the images
        widgets.imagenizqLabel.setPixmap(QPixmap())
        widgets.imagederLabel.setPixmap(QPixmap())
        # actualiza la cantidad de imagenes en la carpeta
        self.lenImagenesDir(Path(widgets.directorio_elementos.text(), 'JPG'))

        # back to captura widget
        widgets.controlesCamstackedWidget.setCurrentWidget(widgets.captura)

    def resetCaptura(self):
        # delete images from directory
        folder_path = widgets.directorio_elementos.text()
        leftimage = folder_path + '/' + widgets.folioizqLineEdit.text() + '.png'
        rightimage = folder_path + '/' + widgets.folioderLineEdit.text() + '.png'
        try:
            os.remove(leftimage)
            os.remove(rightimage)
        except:
            pass

        # erase image labels
        widgets.imagenizqLabel.setPixmap(QPixmap())
        widgets.imagederLabel.setPixmap(QPixmap())

        # back to capture widget
        widgets.controlesCamstackedWidget.setCurrentWidget(widgets.captura)
        self.lenImagenesDir(folder_path)

    def finalizarCaptura(self):
        '''
        gentle close escanerPage and back to home
        '''
        if QMessageBox().question(self, "Cerrar el proyecto",
                                  "¿Está seguro que desea cerrar el proyecto?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            widgets.imagederLabel.setPixmap(QPixmap())
            widgets.imagenizqLabel.setPixmap(QPixmap())
            widgets.elementoIDLabel.setText('')
            widgets.elementoTituloLabel.setText('')
            widgets.directorio_elementos.setText('')
            widgets.cantidadimgsLabel.setText('')
            widgets.folioizqLineEdit.setText('')
            widgets.folioderLineEdit.setText('')
            # back to home
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
            self.display_elements()

    def gentle_close(self):
        '''
        close cams session, close db connection and close application
        '''
        Cam().close_dev()
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
