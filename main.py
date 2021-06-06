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

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QDialog,
                               QLineEdit, QVBoxLayout, QMainWindow)
from PySide6.QtCore import Slot, QDir
from PySide6.QtSql import QSqlDatabase

from ui_main import Ui_MainWindow

from db import connectToDatabase, db_config_info, db_configurar


# logs

logging.basicConfig(filename="neo_escan.log",
                    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
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
        widgets.configButton.clicked.connect(self.buttonClick)

        # Seleccionar página de inicio
        widgets.pages.setCurrentWidget(widgets.home)

        # Página de configuración
        # Muestra la información actual de la base de datos
        widgets.tipo_db.setText(db_config_info())

        # Regresa los valores de la configuración de la base de datos
        widgets.configSendButton.clicked.connect(self.configInfo)


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "homeButton":
            widgets.pages.setCurrentWidget(widgets.home)

        # SHOW config PAGE
        if btnName == "configButton":
            widgets.pages.setCurrentWidget(widgets.config)


    def configInfo(self):
        db = widgets.tipoDB_cbox.currentText()
        host = widgets.host_line.text()
        usuario_config = widgets.usuario_line.text()
        contra = widgets.contrasena_line.text()
        basedd = widgets.dbname_line.text()
        # escribe la nueva información en cofig.ini
        db_configurar(db, host, basedd, usuario_config, contra)
        # actualiza la información de la base de datos
        widgets.tipo_db.setText(db_config_info())


if __name__ == '__main__':
    # crear una aplicación Qt
    app = QApplication(sys.argv)
    # Crear y mostrar la forma
    window = MainWindow()
    window.show()
    # correr el loop principal Qt
    sys.exit(app.exec())
