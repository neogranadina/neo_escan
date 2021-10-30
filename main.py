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
from PySide2.QtGui import QSessionManager

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import QTranslator, QLibraryInfo

from ui_main import Ui_MainWindow
from db import connectToDatabase, createElement, getLastId, insertInfo
#from camcontrol import Cam


# logs

logging.basicConfig(filename="neo_escan.log",
                    level=logging.DEBUG)
logger = logging.getLogger("logger")

# Entorno de la aplicación


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
    # print(status)


def inicio_proyecto():
    pass
    #devs = Cam().devs()
    # return devs


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
        '''
        global cams
        cams = inicio_proyecto()
        if len(cams) <= 1:
            QMessageBox().warning(self, "Error",
                                  "No se encontró ninguna cámara.\nEncienda las cámaras para evitar errores al escanear.", QMessageBox.Discard)
        '''

        # Conectar a la base de datos
        connectToDatabase()

        # Botones, menú
        widgets.inicioButton.clicked.connect(self.buttonClick)
        widgets.coleccionesButton.clicked.connect(self.buttonClick)
        widgets.escanerButton.clicked.connect(self.buttonClick)
        widgets.imagenesButton.clicked.connect(self.buttonClick)
        widgets.exportarButton.clicked.connect(self.buttonClick)

        # Seleccionar página de inicio
        widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)

        # Botón nuevo proyecto
        widgets.nuevoProyectoButton.clicked.connect(self.buttonClick)

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
        

        # tomar fotografía
        widgets.capturaButton.clicked.connect(self.getCaptura)

    # navigation functions

    # Navegar por las páginas desde el menú principal

    def buttonClick(self):
        # nombre del botón
        btn = self.sender()
        btnName = btn.objectName()

        # navega por cada una de las páginas
        if btnName == "inicioButton":
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
        elif btnName == "backtoInicioButton":
            # warning message box
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
            widgets.stackedWidget.setCurrentWidget(widgets.escanerPage)
            try:
                pass
                # Cam().cam(cams)
            except IndexError:
                QMessageBox().warning(self, "Error",
                                            "Compruebe que ambas cámaras estén encendidas. Se reiniciará la aplicación", QMessageBox.Reset)
                restart()

        elif btnName == "imagenesButton":
            widgets.stackedWidget.setCurrentWidget(widgets.imgsPage)
        elif btnName == "exportarButton":
            widgets.stackedWidget.setCurrentWidget(widgets.exportarPage)

    # navegar por la página de metadatos

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

            # set current widget to escanerPage
            widgets.tipoColeccion.setCurrentWidget(widgets.escanerPage)

    # Funciones de control de la cámara

    def getCaptura(self):
        try:
            pass
            # Cam().captura(cams)
        except:
            msg = QMessageBox().warning(self, "Cámaras no disponibles",
                                        "Una o ambas cámaras están apagadas. Encienda las cámaras y se reiniciará la aplicación.", QMessageBox.Reset)
            restart()

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
