# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBJUEAM.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        font = QFont()
        font.setStyleStrategy(QFont.NoAntialias)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"imgs/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"background-color: rgba(0, 0, 0, .45);\n"
"border: none;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.neoLabel = QLabel(self.header)
        self.neoLabel.setObjectName(u"neoLabel")
        self.neoLabel.setMinimumSize(QSize(170, 0))
        self.neoLabel.setMaximumSize(QSize(175, 16777215))
        self.neoLabel.setStyleSheet(u"padding-left: 25px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"")
        self.neoLabel.setPixmap(QPixmap(u":/imgs/imgs/Neogranadina_header_white.svg"))
        self.neoLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.neoLabel)

        self.versionLabel = QLabel(self.header)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setStyleSheet(u"padding-right: 10px;")
        self.versionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.versionLabel)


        self.verticalLayout.addWidget(self.header)

        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: #ffffff;\n"
"border: none;")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.main.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QWidget(self.main)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(105, 0))
        self.menu_bar.setMaximumSize(QSize(105, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 178))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.menu_bar.setPalette(palette)
        self.menu_bar.setStyleSheet(u"QWidget {background-color: rgba(0, 0, 0,.7);}\n"
"\n"
"QPushButton {\n"
"	color: rgba(255,255,255,.9);\n"
"	background-color: transparent;\n"
"	background-position: center top;\n"
"	padding-top: 15px;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgba(0,0,0,.1);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	background-color: #F2784B;\n"
"	border: none;\n"
"}\n"
"\n"
"Line {\n"
"background-color: rgba(255, 255, 255,.5);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.menu_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.inicioButton = QPushButton(self.menu_bar)
        self.inicioButton.setObjectName(u"inicioButton")
        self.inicioButton.setMinimumSize(QSize(0, 81))
        self.inicioButton.setMaximumSize(QSize(16777215, 81))
        self.inicioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.inicioButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/window-of-four-rounded-squares.svg);\n"
"background-origin: content;")

        self.verticalLayout_2.addWidget(self.inicioButton)

        self.coleccionesButton = QPushButton(self.menu_bar)
        self.coleccionesButton.setObjectName(u"coleccionesButton")
        self.coleccionesButton.setMinimumSize(QSize(0, 81))
        self.coleccionesButton.setMaximumSize(QSize(16777215, 81))
        self.coleccionesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.coleccionesButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/pages-interface.svg);\n"
"background-origin: content;")

        self.verticalLayout_2.addWidget(self.coleccionesButton)

        self.escanerButton = QPushButton(self.menu_bar)
        self.escanerButton.setObjectName(u"escanerButton")
        self.escanerButton.setMinimumSize(QSize(0, 81))
        self.escanerButton.setMaximumSize(QSize(16777215, 81))
        self.escanerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.escanerButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/camera-to-take-photos.svg);\n"
"background-origin: content;\n"
"")

        self.verticalLayout_2.addWidget(self.escanerButton)

        self.imagenesButton = QPushButton(self.menu_bar)
        self.imagenesButton.setObjectName(u"imagenesButton")
        self.imagenesButton.setMinimumSize(QSize(0, 81))
        self.imagenesButton.setMaximumSize(QSize(16777215, 81))
        self.imagenesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.imagenesButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/images-interface-symbol.svg);\n"
"background-origin: content;")
        self.imagenesButton.setIconSize(QSize(34, 34))

        self.verticalLayout_2.addWidget(self.imagenesButton)

        self.exportarButton = QPushButton(self.menu_bar)
        self.exportarButton.setObjectName(u"exportarButton")
        self.exportarButton.setMinimumSize(QSize(0, 81))
        self.exportarButton.setMaximumSize(QSize(16777215, 81))
        self.exportarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportarButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/download-symbol.svg);\n"
"background-origin: content;")

        self.verticalLayout_2.addWidget(self.exportarButton)

        self.verticalSpacer = QSpacerItem(20, 384, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.menu_bar)

        self.pages = QWidget(self.main)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.pages)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.inicioPage = QWidget()
        self.inicioPage.setObjectName(u"inicioPage")
        self.label = QLabel(self.inicioPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 49, 16))
        self.stackedWidget.addWidget(self.inicioPage)
        self.coleccionesPage = QWidget()
        self.coleccionesPage.setObjectName(u"coleccionesPage")
        self.verticalLayout_4 = QVBoxLayout(self.coleccionesPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.coleccionesPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.coleccionHeader = QWidget(self.widget_3)
        self.coleccionHeader.setObjectName(u"coleccionHeader")
        self.coleccionHeader.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.tipoColeccion = QComboBox(self.coleccionHeader)
        self.tipoColeccion.addItem("")
        self.tipoColeccion.addItem("")
        self.tipoColeccion.addItem("")
        self.tipoColeccion.addItem("")
        self.tipoColeccion.addItem("")
        self.tipoColeccion.setObjectName(u"tipoColeccion")
        self.tipoColeccion.setGeometry(QRect(270, 90, 221, 22))

        self.verticalLayout_5.addWidget(self.coleccionHeader)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.formulariosColeccion = QStackedWidget(self.widget)
        self.formulariosColeccion.setObjectName(u"formulariosColeccion")
        self.formulariosColeccion.setGeometry(QRect(350, 50, 120, 80))
        self.formulariosColeccion.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.udocComp = QWidget()
        self.udocComp.setObjectName(u"udocComp")
        self.formulariosColeccion.addWidget(self.udocComp)
        self.udocSimple = QWidget()
        self.udocSimple.setObjectName(u"udocSimple")
        self.udocSimple.setStyleSheet(u"background-color: rgb(170, 170, 0);")
        self.formulariosColeccion.addWidget(self.udocSimple)

        self.verticalLayout_5.addWidget(self.widget)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.coleccionesPage)
        self.escanerPage = QWidget()
        self.escanerPage.setObjectName(u"escanerPage")
        self.horizontalLayout_5 = QHBoxLayout(self.escanerPage)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.controlPanel = QWidget(self.escanerPage)
        self.controlPanel.setObjectName(u"controlPanel")
        self.controlPanel.setMinimumSize(QSize(210, 0))
        self.controlPanel.setMaximumSize(QSize(225, 16777215))
        self.controlPanel.setStyleSheet(u"background-color: rgba(0, 0, 0, .3);")
        self.pushButton = QPushButton(self.controlPanel)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 75, 24))

        self.horizontalLayout_5.addWidget(self.controlPanel)

        self.layoutEscan = QWidget(self.escanerPage)
        self.layoutEscan.setObjectName(u"layoutEscan")
        self.verticalLayout_3 = QVBoxLayout(self.layoutEscan)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.layoutEscan)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.leftCamera = QGraphicsView(self.widget_2)
        self.leftCamera.setObjectName(u"leftCamera")
        self.leftCamera.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.leftCamera)

        self.rightCamera = QGraphicsView(self.widget_2)
        self.rightCamera.setObjectName(u"rightCamera")
        self.rightCamera.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.rightCamera)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.captureControl = QWidget(self.layoutEscan)
        self.captureControl.setObjectName(u"captureControl")
        self.captureControl.setMinimumSize(QSize(0, 70))
        self.captureControl.setMaximumSize(QSize(16777215, 70))
        self.captureControl.setStyleSheet(u"QWidget {background-color: transparent;}\n"
"\n"
"QPushButton {\n"
"	color:  rgba(0, 0, 0, .7);\n"
"	background-color: transparent;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {background-color: rgba(242, 120, 75, .7);}\n"
"\n"
"QPushButton::pressed {background-color: rgba(242, 120, 75, 1);}")
        self.horizontalLayout_7 = QHBoxLayout(self.captureControl)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.capturaButton = QPushButton(self.captureControl)
        self.capturaButton.setObjectName(u"capturaButton")
        self.capturaButton.setMinimumSize(QSize(120, 35))
        self.capturaButton.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setPointSize(11)
        self.capturaButton.setFont(font1)
        self.capturaButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/imgs/imgs/icons/camera-to-take-photos_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.capturaButton.setIcon(icon1)
        self.capturaButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.capturaButton)

        self.horizontalSpacer_3 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.captureControl)


        self.horizontalLayout_5.addWidget(self.layoutEscan)

        self.stackedWidget.addWidget(self.escanerPage)
        self.imgsPage = QWidget()
        self.imgsPage.setObjectName(u"imgsPage")
        self.label_4 = QLabel(self.imgsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(118, 50, 81, 20))
        self.stackedWidget.addWidget(self.imgsPage)
        self.exportarPage = QWidget()
        self.exportarPage.setObjectName(u"exportarPage")
        self.label_5 = QLabel(self.exportarPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 120, 91, 16))
        self.stackedWidget.addWidget(self.exportarPage)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 20))
        self.footer.setMaximumSize(QSize(16777215, 20))
        self.footer.setStyleSheet(u"background-color: rgba(0, 0, 0, .7);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.footer.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.c_neogranadina = QLabel(self.footer)
        self.c_neogranadina.setObjectName(u"c_neogranadina")
        self.c_neogranadina.setMinimumSize(QSize(0, 20))
        self.c_neogranadina.setMaximumSize(QSize(16777215, 20))
        self.c_neogranadina.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_neogranadina.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 5px;")
        self.c_neogranadina.setLineWidth(0)
        self.c_neogranadina.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c_neogranadina.setMargin(0)
        self.c_neogranadina.setOpenExternalLinks(True)
        self.c_neogranadina.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.horizontalLayout_4.addWidget(self.c_neogranadina)

        self.down_arrow = QLabel(self.footer)
        self.down_arrow.setObjectName(u"down_arrow")
        self.down_arrow.setMinimumSize(QSize(20, 0))
        self.down_arrow.setMaximumSize(QSize(20, 16777215))
        self.down_arrow.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.down_arrow.setStyleSheet(u"background-color: transparent;\n"
"padding: 2px;")
        self.down_arrow.setPixmap(QPixmap(u":/imgs/imgs/icons/resize.svg"))
        self.down_arrow.setScaledContents(True)
        self.down_arrow.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_4.addWidget(self.down_arrow)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.header.raise_()
        self.footer.raise_()
        self.main.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeoEscan", None))
        self.neoLabel.setText("")
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color: rgba(255,255,255,.7);\">V. beta01</span></p></body></html>", None))
        self.inicioButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Inicio", None))
        self.coleccionesButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Colecciones", None))
        self.escanerButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Esc\u00e1ner", None))
        self.imagenesButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Im\u00e1genes", None))
        self.exportarButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Exportar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.tipoColeccion.setItemText(0, QCoreApplication.translate("MainWindow", u"Legajo / expediente", None))
        self.tipoColeccion.setItemText(1, QCoreApplication.translate("MainWindow", u"Libro / manuscrito", None))
        self.tipoColeccion.setItemText(2, QCoreApplication.translate("MainWindow", u"Mapa / fotograf\u00eda / dibujo", None))
        self.tipoColeccion.setItemText(3, QCoreApplication.translate("MainWindow", u"Unidad documental simple", None))
        self.tipoColeccion.setItemText(4, QCoreApplication.translate("MainWindow", u"Toma simple", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.capturaButton.setText(QCoreApplication.translate("MainWindow", u"capturar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IM\u00c1GENES", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR", None))
        self.c_neogranadina.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><a href=\"https://neogranadina.org/\" target=\"_blank\"><span style=\" font-size:7pt; text-decoration: underline;color:rgba(251,251,251,.8)\">\u00a9 2021 Fundaci\u00f3n Hist\u00f3rica Neogranadina</span></a></body></html>", None))
        self.down_arrow.setText("")
    # retranslateUi
