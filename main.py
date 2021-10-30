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
from db import connectToDatabase, insertInfo, testProyDuplicados, regresa_info_proyecto, checkDirectorio
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

        # Página de colecciones
        widgets.tipodocComboBox.currentIndexChanged.connect(self.indexChange)

        # get directorio
        widgets.browserDirButton.clicked.connect(getDirName)

        # tomar fotografía
        widgets.capturaButton.clicked.connect(self.getCaptura)

    # Navegar por las páginas desde el menú principal

    def buttonClick(self):
        # nombre del botón
        btn = self.sender()
        btnName = btn.objectName()

        # navega por cada una de las páginas
        if btnName == "inicioButton":
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
        elif btnName == "coleccionesButton":
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

    # navegar por los widgets de las colecciones

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
        widgets.rutaLine.setText(response)

    # guarda información en las tabla y fija la ventana en "Escáner"

    def guardarInfo(self):
        '''
        save info from metadata page
        '''
        # Recupera los datos de la página de metadatos
        titulo = widgets.tituloLine.text()
        autor = widgets.autorLine.text()
        fecha = widgets.fechaLine.text()
        tipo = widgets.tipodocComboBox.currentText()
        # Guarda los datos en la base de datos
        insertInfo(titulo, autor, fecha, tipo)
        # Limpia los campos
        widgets.tituloLine.clear()
        widgets.autorLine.clear()
        widgets.fechaLine.clear()
        # Pone la ventana en "Escáner"
        widgets.stackedWidget.setCurrentWidget(widgets.escanerPage)

    # Funciones de control de la cámara

    def getCaptura(self):
        try:
            pass
            # Cam().captura(cams)
        except:
            msg = QMessageBox().warning(self, "Cámaras no disponibles",
                                        "Una o ambas cámaras están apagadas. Encienda las cámaras y se reiniciará la aplicación.", QMessageBox.Reset)
            restart()

    def getDirName(self):
        '''
        get the directory name
        '''
        response = QFileDialog.getExistingDirectory(
            None, 'Seleccione una carpeta', './')
        widgets.rutaLine.setText(response)

    def get_fields_info(self, tipo_de_documento):
        '''
        get the info for a specific form fields and return a dictionary
        '''
        if tipo_de_documento == "Legajo":
            return {
                'titulo': widgets.titulolineEdit.text(),
                'descripción': widgets.descripcionlineEdit.text(),
                'creador': widgets.creadorlineEdit.text(),
                'fecha_inicial': widgets.fechaIlineEdit.text(),
                'fecha_final': widgets.fechaFlineEdit.text(),
                'cobertura_espacial': widgets.coberturalineEdit.text(),
                'idioma': widgets.idiomalineEdit.text(),
                'num_folios': widgets.numfollineEdit.text(),
                'identificadores': widgets.identificadoreslineEdit.text(),
            }
        elif tipo_de_documento == "Documento":
            return {
                'titulo': widgets.titulodoclineEdit.text(),
                'descripción': widgets.descripciondoclineEdit.text(),
                'creador': widgets.creadordoclineEdit.text(),
                'fecha_inicial': widgets.fechaIdoclineEdit.text(),
                'fecha_final': widgets.fechaFdoclineEdit.text(),
                'cobertura_espacial': widgets.coberturadoclineEdit.text(),
                'idioma': widgets.idiomadoclineEdit.text(),
                'num_folios': widgets.numfoliodoclineEdit.text(),
                'identificadores': widgets.identificadoresdoclineEdit.text(),
            }
        elif tipo_de_documento == "Imagen":
            return {
                'titulo': widgets.tituloimagenlineEdit.text(),
                'descripción': widgets.descripcionimagenlineEdit.text(),
                'creador': widgets.creadorimagenlineEdit.text(),
                'fecha': widgets.fechaimagenlineEdit.text(),
                'cobertura_espacial': widgets.coberturaespacialimagenlineEdit.text(),
                'descripción_física': widgets.descripcionfisicaimagenlineEdit.text(),
                'tipo': widgets.tipoimagenlineEdit.text(),
                'identificadores': widgets.identificadoresimagenlineEdit.text(),
            }
        elif tipo_de_documento == "Seriada":
            return {
                'nombre': widgets.nombreserlineEdit.text(),
                'volumen': widgets.volumenserlineEdit.text(),
                'ejemplar': widgets.ejemplarserlineEdit.text(),
                'fecha': widgets.fechaserlineEdit.text(),
                'páginas': widgets.paginaserlineEdit.text(),
                'descripción': widgets.descripcionserlineEdit.text(),
                'idioma': widgets.idiomaserlineEdit.text(),
                'issn': widgets.issnserlineEdit.text(),
                'identificadores': widgets.identificadoreserlineEdit.text(),
            }
        elif tipo_de_documento == "Libro":
            return {
                'título': widgets.titulolibrolineEdit.text(),
                'autor': widgets.autorlibrolineEdit.text(),
                'volumen': widgets.volumelibrolineEdit.text(),
                'serie': widgets.serieLibrolineEdit.text(),
                'edición': widgets.edicionLibrolineEdit.text(),
                'lugar': widgets.lugarLibrolineEdit.text(),
                'editorial': widgets.editorialLibrolineEdit.text(),
                'fecha': widgets.fechaLibrolineEdit.text(),
                'páginas': widgets.paginasLibrolineEdit.text(),
                'descripción': widgets.descripcionLibrolineEdit.text(),
                'idioma': widgets.idiomaLibrolineEdit.text(),
                'isbn': widgets.isbnLibrolineEdit.text(),
                'identificadores': widgets.identificadoresLibrolineEdit.text(),
            }
        elif tipo_de_documento == "Sin tipo":
            return {
                'nombre_archivo': widgets.nombrearchivolineEdit.text(),
                'folder': widgets.folderlineEdit.text(),
            }

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
