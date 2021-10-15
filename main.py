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

    def leg_db(self):
        # comprueba la ruta del proyecto y crea el directorio si no existe y no está en uso
        # por otro proyecto
        ubicacion = Path(widgets.rutaLine.text())
        if not checkDirectorio(ubicacion):
            if len(os.listdir(ubicacion)) == 0:
                try:
                    os.makedirs(ubicacion, exist_ok=True)

                    # recupera el texto de los demás campos del formulario

                    tipo = widgets.tipoColeccion.currentText()
                    refCode = widgets.codRefLegLine.text()
                    titulo = widgets.titulLegajo.text()
                    fechas = widgets.fechasLegLine.text()
                    alcance = widgets.alcanceLegLine.text()

                    # comprueba que no haya un proyecto con el mismo título

                    if not testProyDuplicados(titulo):
                        try:
                            insertInfo(tipo, refCode, titulo,
                                       fechas, alcance, ubicacion)

                            # mensaje de éxito
                            msg = QMessageBox()
                            msg.setText(
                                f"El proyecto {titulo} fue creado exitosamente")
                            msg.exec()

                            # Limpia el formulario
                            widgets.rutaLine.setText("")
                            widgets.codRefLegLine.setText("")
                            widgets.titulLegajo.setText("")
                            widgets.fechasLegLine.setText("")
                            widgets.alcanceLegLine.setText("")

                            # Muestra la página del escáner y el proyecto correspondiente
                            widgets.stackedWidget.setCurrentWidget(
                                widgets.escanerPage)
                            widgets.proyectData.setText(
                                regresa_info_proyecto(titulo))

                        # Mensajes de error
                        except Exception as e:
                            msg = QMessageBox().warning(
                                self, "Error desconocido", f"{e}", QMessageBox.Discard)
                            logger.info(e)
                    else:
                        msg = QMessageBox().warning(self, "Posible duplicado",
                                                    "Ya existe un proyecto con ese título", QMessageBox.Discard)
                except OSError as error:
                    msg = QMessageBox().warning(self, "Error al crear el directorio",
                                                f"{error}", QMessageBox.Discard)
                    logger.info(error)
            else:
                msg = QMessageBox().warning(self, "Error al crear el directorio",
                                            "El directorio no está vacío", QMessageBox.Discard)
        else:
            msg = QMessageBox().warning(self, "Error al crear el directorio",
                                        "El directorio ya está en uso por otro proyecto", QMessageBox.Discard)

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
