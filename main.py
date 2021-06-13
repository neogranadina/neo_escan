# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

import sys
import logging
from configparser import ConfigParser
from locale import getdefaultlocale

from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import QTranslator, QLibraryInfo

from ui_main import Ui_MainWindow
from db import connectToDatabase

# logs

logging.basicConfig(filename="logs/neo_escan.log",
                    level=logging.DEBUG)
logger = logging.getLogger("logger")

# Entorno de la aplicación

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
        widgets.tipoColeccion.currentIndexChanged.connect(self.indexChange)


    # Navegar por las páginas desde el menú principal

    def buttonClick(self):
        # nombre del botón
        btn = self.sender()
        btnName = btn.objectName()

        # navega por cada una de las páginas
        if btnName == "inicioButton":
            widgets.stackedWidget.setCurrentWidget(widgets.inicioPage)
        elif btnName == "coleccionesButton":
            widgets.stackedWidget.setCurrentWidget(widgets.coleccionesPage)
        elif btnName == "escanerButton":
            widgets.stackedWidget.setCurrentWidget(widgets.escanerPage)
        elif btnName == "imagenesButton":
            widgets.stackedWidget.setCurrentWidget(widgets.imgsPage)
        elif btnName == "exportarButton":
            widgets.stackedWidget.setCurrentWidget(widgets.exportarPage)

    # navegar por los widgets de las colecciones

    def indexChange(self):
        index = widgets.tipoColeccion.currentIndex()

        if not index == 4:
            widgets.formulariosColeccion.setCurrentWidget(widgets.udocComp)
        else:
            widgets.formulariosColeccion.setCurrentWidget(widgets.udocSimple)


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
    sys.exit(app.exec())
