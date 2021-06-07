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

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QDialog,
                               QLineEdit, QVBoxLayout, QMainWindow, QMessageBox)
from PySide6.QtCore import Slot, QDir, QTranslator, QLibraryInfo
from PySide6.QtSql import QSqlDatabase

from ui_main import Ui_MainWindow
from db import connectToDatabase, db_config_info, db_configurar

# logs

logging.basicConfig(filename="logs/neo_escan.log",
                    level=logging.DEBUG)
logger = logging.getLogger("logger")



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
        widgets.homeButton.clicked.connect(self.buttonClick)
        widgets.coleccionesButton.clicked.connect(self.buttonClick)
        widgets.configButton.clicked.connect(self.buttonClick)

        # Seleccionar página de inicio
        widgets.pages.setCurrentWidget(widgets.home)

        # Página de configuración
        # Muestra la información actual de la base de datos
        widgets.tipo_db.setText(db_config_info())

        # Regresa los valores de la configuración de la base de datos
        widgets.configSendButton.clicked.connect(self.configInfo)


    def buttonClick(self):
        # nombre del botón
        btn = self.sender()
        btnName = btn.objectName()

        # muestra la página de inicio
        if btnName == "homeButton":
            widgets.pages.setCurrentWidget(widgets.home)

        if btnName == "coleccionesButton":
            widgets.pages.setCurrentWidget(widgets.crear_coleccion)

        # muestra la página de configuración
        if btnName == "configButton":
            widgets.pages.setCurrentWidget(widgets.config)


    def configInfo(self):
        dialogo = QMessageBox.warning(
            self, "Advertencia", "¿Estás seguro de aplicar los cambios?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel)

        if dialogo == QMessageBox.Apply:
            # obtener el texto del formulario de configuración
            db = widgets.tipoDB_cbox.currentText()
            host = widgets.host_line.text()
            usuario_config = widgets.usuario_line.text()
            contra = widgets.contrasena_line.text()
            basedd = widgets.dbname_line.text()
            # escribe la nueva información en config.ini
            db_configurar(db, host, basedd, usuario_config, contra)
        
            # actualiza la información de la base de datos
            widgets.tipo_db.setText(db_config_info())


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
    sys.exit(app.exec())
