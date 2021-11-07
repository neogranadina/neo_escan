# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.0-alpha
#
# ///////////////////////////////////////////////////////////////

import sys
import logging
import os
from pathlib import Path
from locale import getdefaultlocale
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QPixmap, QRegExpValidator

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel, QGridLayout, QPushButton
from PySide2.QtCore import QSize, QTranslator, QLibraryInfo, QRegExp, Qt

from ui_main import Ui_MainWindow
from db import connectToDatabase, createElement, getElementsDataFrame, getLastId, insertInfo, getElementInfo, getLastElementID, getElementsDataFrame
from camcontrol import Cam
import configparser
import ctypes

# logs

logging.basicConfig(filename="neo_escan.log",
                    level=logging.DEBUG)
logger = logging.getLogger("logger")

# config

config = configparser.ConfigParser()
config.read('config.cfg')

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


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
    # print(status)


def inicio_proyecto():
    devs = Cam().devs()
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
        if len(cams) <= 1:
            QMessageBox().warning(self, "Error",
                                  "No se encontró ninguna cámara.\nEncienda las cámaras para evitar errores al escanear.", QMessageBox.Discard)

        # Conectar a la base de datos
        connectToDatabase()

        # set version

        widgets.versionLabel.setText(f'v{version}')

        # Botones, menú
        widgets.inicioButton.clicked.connect(self.buttonClick)
        widgets.coleccionesButton.clicked.connect(self.buttonClick)
        widgets.escanerButton.clicked.connect(self.buttonClick)
        widgets.imagenesButton.clicked.connect(self.buttonClick)
        widgets.exportarButton.clicked.connect(self.buttonClick)

        # Seleccionar página de inicio
        widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)

        # set home page
        widgets.nuevoProyectoButton.clicked.connect(self.buttonClick)
        self.display_elements()

        # Botón regresar al inicio
        widgets.backtoInicioButton.clicked.connect(self.buttonClick)

        # Página de metadatos
        widgets.tipodocComboBox.currentIndexChanged.connect(self.indexChange)
        widgets.enviarFormLegajoButton.clicked.connect(self.enviarForm)
        widgets.enviarFormDocumentoButton.clicked.connect(
            self.enviarForm)
        widgets.enviarFormImageButton.clicked.connect(self.enviarForm)
        widgets.enviarFormSeriadaButton.clicked.connect(self.enviarForm)
        widgets.enviarFormLibroButton.clicked.connect(self.enviarForm)
        widgets.enviarFormSimpleButton.clicked.connect(self.enviarForm)
        widgets.browserDirButton.clicked.connect(self.getDirName)

        # abrir directorio
        widgets.openFolderButton.clicked.connect(self.openimagesDir)

        # tomar fotografía
        widgets.capturaButton.clicked.connect(self.getCaptura)
        # validar fotografía
        widgets.validateButton.clicked.connect(self.validateCaptura)
        widgets.resetButton.clicked.connect(self.resetCaptura)

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
        elif btnName == "escanerButton":
            self.set_scanner_page()
        elif btnName == "imagenesButton":
            widgets.stackedWidget.setCurrentWidget(widgets.imgsPage)
        elif btnName == "exportarButton":
            widgets.stackedWidget.setCurrentWidget(widgets.exportarPage)

    # Funciones para la página de elementos

    def display_elements(self):
        elementos = getElementsDataFrame()
        print(elementos)
        print(elementos.shape)
        print(elementos.columns)

        widgets.elementslayout = QGridLayout()
        widgets.elementslayout.setVerticalSpacing(10)
        widgets.elementslayout.setHorizontalSpacing(10)
        widgets.elementslayout.setContentsMargins(0, 0, 0, 0)
        widgets.elementslayout.setObjectName("elementslayout")

        cantidad_elementos = len(elementos)

        if cantidad_elementos > 0:
            widgets.proyectos_actuales_label.setText(
                f"Proyectos actuales [{cantidad_elementos}]")
        else:
            widgets.proyectos_actuales_label.setText(
                "No se han creado proyectos.")

        for i in range(cantidad_elementos):

            elemento = elementos.iloc[i]
            element_id = elemento['element_id']
            element_name = elemento['titulo']
            element_description = elemento['descripcion']

            image_path = Path(IMGDIR + f'{element_id}')
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
            widgets.elementslayout.addWidget(label, i, 0)

            # Display element name in the grid
            label = QLabel()
            label.setText(
                f'<h3>{element_name}</h3> [{num_imagenes} imágenes]\n{element_description}')
            label.setObjectName(f"element_name_{element_id}")
            label.setMinimumSize(QSize(400, 70))
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignLeft)
            widgets.elementslayout.addWidget(label, i, 1)

            # Set three buttons in the grid
            button = QPushButton()
            # button.setText("Editar")
            button.setObjectName(f"edit_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon1 = QIcon()
            icon1.addFile(u":/imgs/imgs/icons/pencil-on-a-square-outline.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon1)
            button.setIconSize(QSize(20, 20))
            button.clicked.connect(self.edit_element)
            widgets.elementslayout.addWidget(button, i, 2)

            button = QPushButton()
            # button.setText("Exportar")
            button.setObjectName(f"export_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon2 = QIcon()
            icon2.addFile(u":/imgs/imgs/icons/download-symbol.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon2)
            button.setIconSize(QSize(20, 20))
            button.clicked.connect(self.export_element)
            widgets.elementslayout.addWidget(button, i, 3)

            button = QPushButton()
            # button.setText("Eliminar")
            button.setObjectName(f"delete_element_{element_id}")
            button.setMinimumSize(QSize(42, 42))
            button.setMaximumSize(QSize(42, 42))
            icon3 = QIcon()
            icon3.addFile(u":/imgs/imgs/icons/trash-can-with-cover-from-side-view.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon3)
            button.setIconSize(QSize(20, 20))
            button.clicked.connect(self.delete_element)
            widgets.elementslayout.addWidget(button, i, 4)

        widgets.verticalLayout_20.addLayout(widgets.elementslayout)

    def edit_element(self):
        print("add :)")
    # navegar por la página de metadatos

    def export_element(self):
        print("export :)")

    def delete_element(self):
        print("delete :)")

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
                self.set_scanner_page()

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

    def lenImagenesDir(self, folder_path):
        '''
        return the number of images in the directory
        and set the label with the number
        '''
        num_imagenes = len(os.listdir(folder_path))
        widgets.cantidadimgsLabel.setText(str(num_imagenes))

    def set_scanner_page(self):
        # set current page to escanerPage
        widgets.stackedWidget.setCurrentWidget(widgets.escanerPage)

        # obtener datos para la barra izquierda
        id_elemento = getLastElementID()
        datos_elemento = getElementInfo(id_elemento)

        # show data in labels
        widgets.elementoIDLabel.setText(str(id_elemento))
        widgets.elementoTituloLabel.setText(datos_elemento[1])

        # create directory to save images
        folder_path = IMGDIR + str(id_elemento)

        try:
            os.makedirs(folder_path, exist_ok=True)
        except OSError as e:
            print(e)
            raise

        # set folder_path to label
        widgets.directorio_elementos.setText(os.path.abspath(folder_path))

        self.lenImagenesDir(folder_path)

        try:
            Cam().cam(cams)
        except IndexError:
            QMessageBox().warning(self, "Error",
                                        "Compruebe que ambas cámaras estén encendidas. Se reiniciará la aplicación", QMessageBox.Reset)
            restart()

    # Funciones de control de la cámara

    def getCaptura(self):
        try:
            self.lenImagenesDir(widgets.directorio_elementos.text())
            Cam().captura(cams)
            # get the last images from the directory
            # and show it in the label

            # set validator for the lineEdit
            rx = QRegExp("^[a-zA-Z0-9-_]+$")
            validator = QRegExpValidator(rx, self)

            widgets.folioizqLineEdit.setValidator(validator)
            widgets.folioderLineEdit.setValidator(validator)

            # validate if text in folioizqLineEdit match regular expression
            if widgets.folioizqLineEdit.hasAcceptableInput() and widgets.folioderLineEdit.hasAcceptableInput():
                if widgets.folioizqLineEdit.text() != widgets.folioderLineEdit.text():
                    left_img_name = widgets.folioizqLineEdit.text() + '.jpg'
                    right_img_name = widgets.folioderLineEdit.text() + '.jpg'

                    left_img_path = widgets.directorio_elementos.text() + '/' + left_img_name
                    right_img_path = widgets.directorio_elementos.text() + '/' + right_img_name

                    widgets.imagenizqLabel.setPixmap(QPixmap(left_img_path))
                    widgets.imagederLabel.setPixmap(QPixmap(right_img_path))

                    # display validation buttons
                    widgets.controlesCamstackedWidget.setCurrentWidget(
                        widgets.validar)
                else:
                    QMessageBox().warning(self, "Error",
                                                "Los número de los folios deben ser diferentes", QMessageBox.Ok)
            else:
                QMessageBox().warning(self, "Error",
                                            "El número de los folios solamente puede contener letras, números y guiones", QMessageBox.Ok)

        except:
            msg = QMessageBox().warning(self, "Cámaras no disponibles",
                                        "Una o ambas cámaras están apagadas. Encienda las cámaras y se reiniciará la aplicación.", QMessageBox.Reset)
            restart()

    def validateCaptura(self):
        # erase the folio labels
        widgets.folioizqLineEdit.setText('')
        widgets.folioderLineEdit.setText('')
        # erase the images
        widgets.imagenizqLabel.setPixmap(QPixmap())
        widgets.imagederLabel.setPixmap(QPixmap())
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
    window.show()
    # correr el loop principal Qt
    sys.exit(app.exec_())
