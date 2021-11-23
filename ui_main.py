# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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
        icon.addFile(u"C:/Users/jairo/.designer/backup/imgs/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
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
        self.versionLabel.setStyleSheet(u"color: rgba(255,255,255,.7);\n"
"padding-right: 10px;")
        self.versionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.versionLabel)


        self.verticalLayout_5.addWidget(self.header)

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
        self.inicioButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/pages-interface.svg);\n"
"background-origin: content;")

        self.verticalLayout_2.addWidget(self.inicioButton)

        self.coleccionesButton = QPushButton(self.menu_bar)
        self.coleccionesButton.setObjectName(u"coleccionesButton")
        self.coleccionesButton.setMinimumSize(QSize(0, 81))
        self.coleccionesButton.setMaximumSize(QSize(16777215, 81))
        self.coleccionesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.coleccionesButton.setStyleSheet(u"background-image: url(:/imgs/imgs/icons/window-of-four-rounded-squares.svg);\n"
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
        self.inicioPage.setStyleSheet(u"QPushButton#nuevoProyectoButton {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background-color: rgb(0, 0, 0);\n"
"padding: 5px;}\n"
"\n"
"QPushButton#nuevoProyectoButton::hover {\n"
"	background-color: rgba(0,0,0,.7);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButto#nuevoProyectoButtonn::focus {\n"
"	background-color: #F2784B;\n"
"	border: none;\n"
"}\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.inicioPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_6.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_2 = QLabel(self.inicioPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.nuevoProyectoButton = QPushButton(self.inicioPage)
        self.nuevoProyectoButton.setObjectName(u"nuevoProyectoButton")
        self.nuevoProyectoButton.setMinimumSize(QSize(40, 40))
        self.nuevoProyectoButton.setMaximumSize(QSize(40, 40))
        self.nuevoProyectoButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"imgs/icons/plus-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nuevoProyectoButton.setIcon(icon1)
        self.nuevoProyectoButton.setIconSize(QSize(20, 20))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.nuevoProyectoButton)


        self.verticalLayout_19.addLayout(self.formLayout_6)

        self.proyectos_actuales_label = QLabel(self.inicioPage)
        self.proyectos_actuales_label.setObjectName(u"proyectos_actuales_label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.proyectos_actuales_label.setFont(font2)

        self.verticalLayout_19.addWidget(self.proyectos_actuales_label)

        self.scrollArea_7 = QScrollArea(self.inicioPage)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0, 0, 0, .7);\n"
"color: rgba(251,251,251,1);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(242,120,75,1);\n"
"color: rgba(0,0,0,.5);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"background-color: rgba(242,120,75,1);\n"
"border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"	border-top: 1px dotted;\n"
"}")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 677, 310))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_19.addWidget(self.scrollArea_7)

        self.stackedWidget.addWidget(self.inicioPage)
        self.metadataPage = QWidget()
        self.metadataPage.setObjectName(u"metadataPage")
        self.metadataPage.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QComboBox {\n"
"border-color: rgba(0,0,0,.7);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border-color: rgba(0,0,0,.7);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"border-color: rgba(0,0,0,.7);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgba(0,0,0,.7);\n"
"color: rgba(251,251,251,.7);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(242,120,75,1);\n"
"color: rgba(0,0,0,.5);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"background-color: rgba(242,120,75,1);\n"
"border: none;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.metadataPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.metadataPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerMetadatos = QFrame(self.widget)
        self.headerMetadatos.setObjectName(u"headerMetadatos")
        self.headerMetadatos.setMinimumSize(QSize(0, 65))
        self.headerMetadatos.setStyleSheet(u"QPushButton#backtoInicioButton {\n"
"color: rgb(247,247,247);\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton#backtoInicioButton::hover {\n"
"	background-color: rgba(0, 0, 0, .7);\n"
"}")
        self.headerMetadatos.setFrameShape(QFrame.StyledPanel)
        self.headerMetadatos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.headerMetadatos)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.H1metadatosLabel = QLabel(self.headerMetadatos)
        self.H1metadatosLabel.setObjectName(u"H1metadatosLabel")
        self.H1metadatosLabel.setFont(font2)

        self.horizontalLayout_9.addWidget(self.H1metadatosLabel)

        self.backtoInicioButton = QPushButton(self.headerMetadatos)
        self.backtoInicioButton.setObjectName(u"backtoInicioButton")
        self.backtoInicioButton.setMinimumSize(QSize(100, 42))
        self.backtoInicioButton.setMaximumSize(QSize(150, 42))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.backtoInicioButton.setFont(font3)
        self.backtoInicioButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/imgs/imgs/icons/left-arrowhead-in-a-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backtoInicioButton.setIcon(icon2)
        self.backtoInicioButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.backtoInicioButton)


        self.verticalLayout.addWidget(self.headerMetadatos)

        self.formChanger = QWidget(self.widget)
        self.formChanger.setObjectName(u"formChanger")
        self.formChanger.setMinimumSize(QSize(0, 45))
        self.formChanger.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.formChanger)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tipodocLabel = QLabel(self.formChanger)
        self.tipodocLabel.setObjectName(u"tipodocLabel")
        self.tipodocLabel.setMinimumSize(QSize(120, 0))
        self.tipodocLabel.setMaximumSize(QSize(120, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.tipodocLabel.setFont(font4)

        self.horizontalLayout_8.addWidget(self.tipodocLabel)

        self.tipodocComboBox = QComboBox(self.formChanger)
        icon3 = QIcon()
        icon3.addFile(u":/imgs/imgs/icons/folder-check-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/imgs/imgs/icons/documents-rounded-square-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/imgs/imgs/icons/image-interface-symbol-with-a-landscape.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/imgs/imgs/icons/news-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/imgs/imgs/icons/open-book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/imgs/imgs/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon8, "")
        self.tipodocComboBox.setObjectName(u"tipodocComboBox")
        self.tipodocComboBox.setMinimumSize(QSize(300, 34))
        self.tipodocComboBox.setMaximumSize(QSize(300, 34))
        self.tipodocComboBox.setFont(font4)

        self.horizontalLayout_8.addWidget(self.tipodocComboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.formChanger)

        self.tipoColeccion = QStackedWidget(self.widget)
        self.tipoColeccion.setObjectName(u"tipoColeccion")
        self.tipoColeccion.setStyleSheet(u"")
        self.formLegajo = QWidget()
        self.formLegajo.setObjectName(u"formLegajo")
        self.verticalLayout_6 = QVBoxLayout(self.formLegajo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea = QScrollArea(self.formLegajo)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 633, 468))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.tituloLabel = QLabel(self.scrollAreaWidgetContents)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.tituloLabel)

        self.titulolineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.titulolineEdit.setObjectName(u"titulolineEdit")
        self.titulolineEdit.setMinimumSize(QSize(500, 34))
        self.titulolineEdit.setMaximumSize(QSize(500, 34))
        self.titulolineEdit.setFont(font4)
        self.titulolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titulolineEdit)

        self.numextLabel = QLabel(self.scrollAreaWidgetContents)
        self.numextLabel.setObjectName(u"numextLabel")
        self.numextLabel.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.numextLabel)

        self.descripcionlineEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.descripcionlineEdit.setObjectName(u"descripcionlineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descripcionlineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionlineEdit.setSizePolicy(sizePolicy)
        self.descripcionlineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionlineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionlineEdit.setFont(font4)
        self.descripcionlineEdit.setStyleSheet(u"Breve resumen del tema del expediente")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.descripcionlineEdit)

        self.creadorlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.creadorlineEdit.setObjectName(u"creadorlineEdit")
        self.creadorlineEdit.setMinimumSize(QSize(500, 34))
        self.creadorlineEdit.setMaximumSize(QSize(500, 34))
        self.creadorlineEdit.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.creadorlineEdit)

        self.fechaILabel = QLabel(self.scrollAreaWidgetContents)
        self.fechaILabel.setObjectName(u"fechaILabel")
        self.fechaILabel.setFont(font4)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.fechaILabel)

        self.fechaIlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fechaIlineEdit.setObjectName(u"fechaIlineEdit")
        self.fechaIlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaIlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaIlineEdit.setFont(font4)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.fechaIlineEdit)

        self.fechaFLabel = QLabel(self.scrollAreaWidgetContents)
        self.fechaFLabel.setObjectName(u"fechaFLabel")
        self.fechaFLabel.setFont(font4)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.fechaFLabel)

        self.fechaFlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fechaFlineEdit.setObjectName(u"fechaFlineEdit")
        self.fechaFlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaFlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaFlineEdit.setFont(font4)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.fechaFlineEdit)

        self.idiomaLabel = QLabel(self.scrollAreaWidgetContents)
        self.idiomaLabel.setObjectName(u"idiomaLabel")
        self.idiomaLabel.setFont(font4)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.idiomaLabel)

        self.idiomalineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.idiomalineEdit.setObjectName(u"idiomalineEdit")
        self.idiomalineEdit.setMinimumSize(QSize(500, 34))
        self.idiomalineEdit.setMaximumSize(QSize(500, 34))
        self.idiomalineEdit.setFont(font4)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.idiomalineEdit)

        self.numfolLabel = QLabel(self.scrollAreaWidgetContents)
        self.numfolLabel.setObjectName(u"numfolLabel")
        self.numfolLabel.setFont(font4)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.numfolLabel)

        self.numfollineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.numfollineEdit.setObjectName(u"numfollineEdit")
        self.numfollineEdit.setMinimumSize(QSize(500, 34))
        self.numfollineEdit.setMaximumSize(QSize(500, 34))
        self.numfollineEdit.setFont(font4)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.numfollineEdit)

        self.identificadoresLabel = QLabel(self.scrollAreaWidgetContents)
        self.identificadoresLabel.setObjectName(u"identificadoresLabel")
        self.identificadoresLabel.setFont(font4)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.identificadoresLabel)

        self.identificadoreslineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.identificadoreslineEdit.setObjectName(u"identificadoreslineEdit")
        self.identificadoreslineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoreslineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoreslineEdit.setFont(font4)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.identificadoreslineEdit)

        self.enviarFormLegajoButton = QPushButton(self.scrollAreaWidgetContents)
        self.enviarFormLegajoButton.setObjectName(u"enviarFormLegajoButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enviarFormLegajoButton.sizePolicy().hasHeightForWidth())
        self.enviarFormLegajoButton.setSizePolicy(sizePolicy1)
        self.enviarFormLegajoButton.setMinimumSize(QSize(100, 34))
        self.enviarFormLegajoButton.setMaximumSize(QSize(100, 34))
        self.enviarFormLegajoButton.setFont(font4)
        self.enviarFormLegajoButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/imgs/imgs/icons/fast-forward-double-right-arrows.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.enviarFormLegajoButton.setIcon(icon9)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.enviarFormLegajoButton)

        self.creadorLabel = QLabel(self.scrollAreaWidgetContents)
        self.creadorLabel.setObjectName(u"creadorLabel")
        self.creadorLabel.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.creadorLabel)

        self.coberturaLabel = QLabel(self.scrollAreaWidgetContents)
        self.coberturaLabel.setObjectName(u"coberturaLabel")
        self.coberturaLabel.setFont(font4)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.coberturaLabel)

        self.coberturalineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.coberturalineEdit.setObjectName(u"coberturalineEdit")
        self.coberturalineEdit.setMinimumSize(QSize(500, 34))
        self.coberturalineEdit.setMaximumSize(QSize(500, 34))
        self.coberturalineEdit.setFont(font4)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.coberturalineEdit)


        self.verticalLayout_7.addLayout(self.formLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.tipoColeccion.addWidget(self.formLegajo)
        self.formDocumento = QWidget()
        self.formDocumento.setObjectName(u"formDocumento")
        self.formDocumento.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.formDocumento)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_2 = QScrollArea(self.formDocumento)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 633, 450))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.tituloLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.tituloLabel_3.setObjectName(u"tituloLabel_3")
        self.tituloLabel_3.setFont(font4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.tituloLabel_3)

        self.titulodoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.titulodoclineEdit.setObjectName(u"titulodoclineEdit")
        self.titulodoclineEdit.setMinimumSize(QSize(500, 34))
        self.titulodoclineEdit.setMaximumSize(QSize(500, 34))
        self.titulodoclineEdit.setFont(font4)
        self.titulodoclineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.titulodoclineEdit)

        self.numextLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.numextLabel_3.setObjectName(u"numextLabel_3")
        self.numextLabel_3.setFont(font4)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.numextLabel_3)

        self.descripciondoclineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.descripciondoclineEdit.setObjectName(u"descripciondoclineEdit")
        sizePolicy.setHeightForWidth(self.descripciondoclineEdit.sizePolicy().hasHeightForWidth())
        self.descripciondoclineEdit.setSizePolicy(sizePolicy)
        self.descripciondoclineEdit.setMinimumSize(QSize(500, 70))
        self.descripciondoclineEdit.setMaximumSize(QSize(500, 250))
        self.descripciondoclineEdit.setFont(font4)
        self.descripciondoclineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.descripciondoclineEdit)

        self.creadorLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.creadorLabel_3.setObjectName(u"creadorLabel_3")
        self.creadorLabel_3.setFont(font4)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.creadorLabel_3)

        self.creadordoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.creadordoclineEdit.setObjectName(u"creadordoclineEdit")
        self.creadordoclineEdit.setMinimumSize(QSize(500, 34))
        self.creadordoclineEdit.setMaximumSize(QSize(500, 34))
        self.creadordoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.creadordoclineEdit)

        self.fechaILabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.fechaILabel_3.setObjectName(u"fechaILabel_3")
        self.fechaILabel_3.setFont(font4)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.fechaILabel_3)

        self.fechaIdoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.fechaIdoclineEdit.setObjectName(u"fechaIdoclineEdit")
        self.fechaIdoclineEdit.setMinimumSize(QSize(500, 34))
        self.fechaIdoclineEdit.setMaximumSize(QSize(500, 34))
        self.fechaIdoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.fechaIdoclineEdit)

        self.fechaFLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.fechaFLabel_3.setObjectName(u"fechaFLabel_3")
        self.fechaFLabel_3.setFont(font4)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.fechaFLabel_3)

        self.fechaFdoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.fechaFdoclineEdit.setObjectName(u"fechaFdoclineEdit")
        self.fechaFdoclineEdit.setMinimumSize(QSize(500, 34))
        self.fechaFdoclineEdit.setMaximumSize(QSize(500, 34))
        self.fechaFdoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.fechaFdoclineEdit)

        self.coberturaLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.coberturaLabel_3.setObjectName(u"coberturaLabel_3")
        self.coberturaLabel_3.setFont(font4)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.coberturaLabel_3)

        self.coberturadoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.coberturadoclineEdit.setObjectName(u"coberturadoclineEdit")
        self.coberturadoclineEdit.setMinimumSize(QSize(500, 34))
        self.coberturadoclineEdit.setMaximumSize(QSize(500, 34))
        self.coberturadoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.coberturadoclineEdit)

        self.idiomaLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.idiomaLabel_3.setObjectName(u"idiomaLabel_3")
        self.idiomaLabel_3.setFont(font4)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.idiomaLabel_3)

        self.idiomadoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.idiomadoclineEdit.setObjectName(u"idiomadoclineEdit")
        self.idiomadoclineEdit.setMinimumSize(QSize(500, 34))
        self.idiomadoclineEdit.setMaximumSize(QSize(500, 34))
        self.idiomadoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.idiomadoclineEdit)

        self.numfolLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.numfolLabel_3.setObjectName(u"numfolLabel_3")
        self.numfolLabel_3.setFont(font4)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.numfolLabel_3)

        self.numfoliodoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.numfoliodoclineEdit.setObjectName(u"numfoliodoclineEdit")
        self.numfoliodoclineEdit.setMinimumSize(QSize(500, 34))
        self.numfoliodoclineEdit.setMaximumSize(QSize(500, 34))
        self.numfoliodoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.numfoliodoclineEdit)

        self.identificadoresLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.identificadoresLabel_3.setObjectName(u"identificadoresLabel_3")
        self.identificadoresLabel_3.setFont(font4)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.identificadoresLabel_3)

        self.identificadoresdoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.identificadoresdoclineEdit.setObjectName(u"identificadoresdoclineEdit")
        self.identificadoresdoclineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoresdoclineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoresdoclineEdit.setFont(font4)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.identificadoresdoclineEdit)

        self.enviarFormDocumentoButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.enviarFormDocumentoButton.setObjectName(u"enviarFormDocumentoButton")
        sizePolicy1.setHeightForWidth(self.enviarFormDocumentoButton.sizePolicy().hasHeightForWidth())
        self.enviarFormDocumentoButton.setSizePolicy(sizePolicy1)
        self.enviarFormDocumentoButton.setMinimumSize(QSize(100, 34))
        self.enviarFormDocumentoButton.setMaximumSize(QSize(100, 34))
        self.enviarFormDocumentoButton.setFont(font4)
        self.enviarFormDocumentoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormDocumentoButton.setIcon(icon9)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.enviarFormDocumentoButton)


        self.verticalLayout_9.addLayout(self.formLayout_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.tipoColeccion.addWidget(self.formDocumento)
        self.formImagen = QWidget()
        self.formImagen.setObjectName(u"formImagen")
        self.formImagen.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.formImagen)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_3 = QScrollArea(self.formImagen)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 633, 410))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.tituloLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_4.setObjectName(u"tituloLabel_4")
        self.tituloLabel_4.setFont(font4)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.tituloLabel_4)

        self.tituloimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.tituloimagenlineEdit.setObjectName(u"tituloimagenlineEdit")
        self.tituloimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.tituloimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.tituloimagenlineEdit.setFont(font4)
        self.tituloimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.tituloimagenlineEdit)

        self.tituloLabel_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_5.setObjectName(u"tituloLabel_5")
        self.tituloLabel_5.setFont(font4)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.tituloLabel_5)

        self.creadorimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.creadorimagenlineEdit.setObjectName(u"creadorimagenlineEdit")
        self.creadorimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.creadorimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.creadorimagenlineEdit.setFont(font4)
        self.creadorimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.creadorimagenlineEdit)

        self.tituloLabel_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_6.setObjectName(u"tituloLabel_6")
        self.tituloLabel_6.setFont(font4)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_6)

        self.fechaimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.fechaimagenlineEdit.setObjectName(u"fechaimagenlineEdit")
        self.fechaimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaimagenlineEdit.setFont(font4)
        self.fechaimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.fechaimagenlineEdit)

        self.tituloLabel_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_7.setObjectName(u"tituloLabel_7")
        self.tituloLabel_7.setFont(font4)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.tituloLabel_7)

        self.descripcionfisicaimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.descripcionfisicaimagenlineEdit.setObjectName(u"descripcionfisicaimagenlineEdit")
        self.descripcionfisicaimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.descripcionfisicaimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.descripcionfisicaimagenlineEdit.setFont(font4)
        self.descripcionfisicaimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.descripcionfisicaimagenlineEdit)

        self.numextLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.numextLabel_4.setObjectName(u"numextLabel_4")
        self.numextLabel_4.setFont(font4)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.numextLabel_4)

        self.descripcionimagenlineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_4)
        self.descripcionimagenlineEdit.setObjectName(u"descripcionimagenlineEdit")
        sizePolicy.setHeightForWidth(self.descripcionimagenlineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionimagenlineEdit.setSizePolicy(sizePolicy)
        self.descripcionimagenlineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionimagenlineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionimagenlineEdit.setFont(font4)
        self.descripcionimagenlineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.descripcionimagenlineEdit)

        self.identificadoresLabel_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.identificadoresLabel_5.setObjectName(u"identificadoresLabel_5")
        self.identificadoresLabel_5.setFont(font4)

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.identificadoresLabel_5)

        self.tipoimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.tipoimagenlineEdit.setObjectName(u"tipoimagenlineEdit")
        self.tipoimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.tipoimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.tipoimagenlineEdit.setFont(font4)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.tipoimagenlineEdit)

        self.identificadoresLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.identificadoresLabel_4.setObjectName(u"identificadoresLabel_4")
        self.identificadoresLabel_4.setFont(font4)

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.identificadoresLabel_4)

        self.identificadoresimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.identificadoresimagenlineEdit.setObjectName(u"identificadoresimagenlineEdit")
        self.identificadoresimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoresimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoresimagenlineEdit.setFont(font4)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.identificadoresimagenlineEdit)

        self.enviarFormImageButton = QPushButton(self.scrollAreaWidgetContents_4)
        self.enviarFormImageButton.setObjectName(u"enviarFormImageButton")
        sizePolicy1.setHeightForWidth(self.enviarFormImageButton.sizePolicy().hasHeightForWidth())
        self.enviarFormImageButton.setSizePolicy(sizePolicy1)
        self.enviarFormImageButton.setMinimumSize(QSize(100, 34))
        self.enviarFormImageButton.setMaximumSize(QSize(100, 34))
        self.enviarFormImageButton.setFont(font4)
        self.enviarFormImageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormImageButton.setIcon(icon9)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.enviarFormImageButton)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.coberturaespacialimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.coberturaespacialimagenlineEdit.setObjectName(u"coberturaespacialimagenlineEdit")
        self.coberturaespacialimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.coberturaespacialimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.coberturaespacialimagenlineEdit.setFont(font4)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.coberturaespacialimagenlineEdit)


        self.verticalLayout_11.addLayout(self.formLayout_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        self.tipoColeccion.addWidget(self.formImagen)
        self.formSeriada = QWidget()
        self.formSeriada.setObjectName(u"formSeriada")
        self.verticalLayout_12 = QVBoxLayout(self.formSeriada)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_4 = QScrollArea(self.formSeriada)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 638, 450))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tituloLabel_8 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_8.setObjectName(u"tituloLabel_8")
        self.tituloLabel_8.setFont(font4)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.tituloLabel_8)

        self.nombreserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.nombreserlineEdit.setObjectName(u"nombreserlineEdit")
        self.nombreserlineEdit.setMinimumSize(QSize(500, 34))
        self.nombreserlineEdit.setMaximumSize(QSize(500, 34))
        self.nombreserlineEdit.setFont(font4)
        self.nombreserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nombreserlineEdit)

        self.tituloLabel_9 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_9.setObjectName(u"tituloLabel_9")
        self.tituloLabel_9.setFont(font4)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.tituloLabel_9)

        self.volumenserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.volumenserlineEdit.setObjectName(u"volumenserlineEdit")
        self.volumenserlineEdit.setMinimumSize(QSize(500, 34))
        self.volumenserlineEdit.setMaximumSize(QSize(500, 34))
        self.volumenserlineEdit.setFont(font4)
        self.volumenserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.volumenserlineEdit)

        self.tituloLabel_10 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_10.setObjectName(u"tituloLabel_10")
        self.tituloLabel_10.setFont(font4)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_10)

        self.ejemplarserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.ejemplarserlineEdit.setObjectName(u"ejemplarserlineEdit")
        self.ejemplarserlineEdit.setMinimumSize(QSize(500, 34))
        self.ejemplarserlineEdit.setMaximumSize(QSize(500, 34))
        self.ejemplarserlineEdit.setFont(font4)
        self.ejemplarserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.ejemplarserlineEdit)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.fechaserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.fechaserlineEdit.setObjectName(u"fechaserlineEdit")
        self.fechaserlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaserlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaserlineEdit.setFont(font4)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.fechaserlineEdit)

        self.tituloLabel_11 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_11.setObjectName(u"tituloLabel_11")
        self.tituloLabel_11.setFont(font4)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.tituloLabel_11)

        self.paginaserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.paginaserlineEdit.setObjectName(u"paginaserlineEdit")
        self.paginaserlineEdit.setMinimumSize(QSize(500, 34))
        self.paginaserlineEdit.setMaximumSize(QSize(500, 34))
        self.paginaserlineEdit.setFont(font4)
        self.paginaserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.paginaserlineEdit)

        self.numextLabel_5 = QLabel(self.scrollAreaWidgetContents_5)
        self.numextLabel_5.setObjectName(u"numextLabel_5")
        self.numextLabel_5.setFont(font4)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.numextLabel_5)

        self.descripcionserlineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.descripcionserlineEdit.setObjectName(u"descripcionserlineEdit")
        sizePolicy.setHeightForWidth(self.descripcionserlineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionserlineEdit.setSizePolicy(sizePolicy)
        self.descripcionserlineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionserlineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionserlineEdit.setFont(font4)
        self.descripcionserlineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.descripcionserlineEdit)

        self.identificadoresLabel_6 = QLabel(self.scrollAreaWidgetContents_5)
        self.identificadoresLabel_6.setObjectName(u"identificadoresLabel_6")
        self.identificadoresLabel_6.setFont(font4)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.identificadoresLabel_6)

        self.idiomaserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.idiomaserlineEdit.setObjectName(u"idiomaserlineEdit")
        self.idiomaserlineEdit.setMinimumSize(QSize(500, 34))
        self.idiomaserlineEdit.setMaximumSize(QSize(500, 34))
        self.idiomaserlineEdit.setFont(font4)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.idiomaserlineEdit)

        self.identificadoresLabel_8 = QLabel(self.scrollAreaWidgetContents_5)
        self.identificadoresLabel_8.setObjectName(u"identificadoresLabel_8")
        self.identificadoresLabel_8.setFont(font4)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.identificadoresLabel_8)

        self.issnserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.issnserlineEdit.setObjectName(u"issnserlineEdit")
        self.issnserlineEdit.setMinimumSize(QSize(500, 34))
        self.issnserlineEdit.setMaximumSize(QSize(500, 34))
        self.issnserlineEdit.setFont(font4)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.issnserlineEdit)

        self.identificadoresLabel_7 = QLabel(self.scrollAreaWidgetContents_5)
        self.identificadoresLabel_7.setObjectName(u"identificadoresLabel_7")
        self.identificadoresLabel_7.setFont(font4)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.identificadoresLabel_7)

        self.identificadoreserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.identificadoreserlineEdit.setObjectName(u"identificadoreserlineEdit")
        self.identificadoreserlineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoreserlineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoreserlineEdit.setFont(font4)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.identificadoreserlineEdit)

        self.enviarFormSeriadaButton = QPushButton(self.scrollAreaWidgetContents_5)
        self.enviarFormSeriadaButton.setObjectName(u"enviarFormSeriadaButton")
        sizePolicy1.setHeightForWidth(self.enviarFormSeriadaButton.sizePolicy().hasHeightForWidth())
        self.enviarFormSeriadaButton.setSizePolicy(sizePolicy1)
        self.enviarFormSeriadaButton.setMinimumSize(QSize(100, 34))
        self.enviarFormSeriadaButton.setMaximumSize(QSize(100, 34))
        self.enviarFormSeriadaButton.setFont(font4)
        self.enviarFormSeriadaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormSeriadaButton.setIcon(icon9)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.enviarFormSeriadaButton)


        self.verticalLayout_15.addLayout(self.formLayout_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_12.addWidget(self.scrollArea_4)

        self.tipoColeccion.addWidget(self.formSeriada)
        self.formLibro = QWidget()
        self.formLibro.setObjectName(u"formLibro")
        self.verticalLayout_13 = QVBoxLayout(self.formLibro)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_5 = QScrollArea(self.formLibro)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 610, 610))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.tituloLabel_12 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_12.setObjectName(u"tituloLabel_12")
        self.tituloLabel_12.setFont(font4)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.tituloLabel_12)

        self.titulolibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.titulolibrolineEdit.setObjectName(u"titulolibrolineEdit")
        self.titulolibrolineEdit.setMinimumSize(QSize(500, 34))
        self.titulolibrolineEdit.setMaximumSize(QSize(500, 34))
        self.titulolibrolineEdit.setFont(font4)
        self.titulolibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.titulolibrolineEdit)

        self.tituloLabel_16 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_16.setObjectName(u"tituloLabel_16")
        self.tituloLabel_16.setFont(font4)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.tituloLabel_16)

        self.autorlibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.autorlibrolineEdit.setObjectName(u"autorlibrolineEdit")
        self.autorlibrolineEdit.setMinimumSize(QSize(500, 34))
        self.autorlibrolineEdit.setMaximumSize(QSize(500, 34))
        self.autorlibrolineEdit.setFont(font4)
        self.autorlibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.autorlibrolineEdit)

        self.tituloLabel_13 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_13.setObjectName(u"tituloLabel_13")
        self.tituloLabel_13.setFont(font4)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_13)

        self.volumelibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.volumelibrolineEdit.setObjectName(u"volumelibrolineEdit")
        self.volumelibrolineEdit.setMinimumSize(QSize(500, 34))
        self.volumelibrolineEdit.setMaximumSize(QSize(500, 34))
        self.volumelibrolineEdit.setFont(font4)
        self.volumelibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.volumelibrolineEdit)

        self.tituloLabel_14 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_14.setObjectName(u"tituloLabel_14")
        self.tituloLabel_14.setFont(font4)

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.tituloLabel_14)

        self.serieLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.serieLibrolineEdit.setObjectName(u"serieLibrolineEdit")
        self.serieLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.serieLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.serieLibrolineEdit.setFont(font4)
        self.serieLibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.serieLibrolineEdit)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.edicionLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.edicionLibrolineEdit.setObjectName(u"edicionLibrolineEdit")
        self.edicionLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.edicionLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.edicionLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.edicionLibrolineEdit)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.lugarLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lugarLibrolineEdit.setObjectName(u"lugarLibrolineEdit")
        self.lugarLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.lugarLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.lugarLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lugarLibrolineEdit)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_11)

        self.editorialLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.editorialLibrolineEdit.setObjectName(u"editorialLibrolineEdit")
        self.editorialLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.editorialLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.editorialLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.editorialLibrolineEdit)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.fechaLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.fechaLibrolineEdit.setObjectName(u"fechaLibrolineEdit")
        self.fechaLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.fechaLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.fechaLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.fechaLibrolineEdit)

        self.tituloLabel_15 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_15.setObjectName(u"tituloLabel_15")
        self.tituloLabel_15.setFont(font4)

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.tituloLabel_15)

        self.paginasLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.paginasLibrolineEdit.setObjectName(u"paginasLibrolineEdit")
        self.paginasLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.paginasLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.paginasLibrolineEdit.setFont(font4)
        self.paginasLibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.paginasLibrolineEdit)

        self.numextLabel_6 = QLabel(self.scrollAreaWidgetContents_6)
        self.numextLabel_6.setObjectName(u"numextLabel_6")
        self.numextLabel_6.setFont(font4)

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.numextLabel_6)

        self.descripcionLibrolineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.descripcionLibrolineEdit.setObjectName(u"descripcionLibrolineEdit")
        sizePolicy.setHeightForWidth(self.descripcionLibrolineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionLibrolineEdit.setSizePolicy(sizePolicy)
        self.descripcionLibrolineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionLibrolineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionLibrolineEdit.setFont(font4)
        self.descripcionLibrolineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.descripcionLibrolineEdit)

        self.identificadoresLabel_9 = QLabel(self.scrollAreaWidgetContents_6)
        self.identificadoresLabel_9.setObjectName(u"identificadoresLabel_9")
        self.identificadoresLabel_9.setFont(font4)

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.identificadoresLabel_9)

        self.idiomaLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.idiomaLibrolineEdit.setObjectName(u"idiomaLibrolineEdit")
        self.idiomaLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.idiomaLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.idiomaLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.idiomaLibrolineEdit)

        self.identificadoresLabel_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.identificadoresLabel_10.setObjectName(u"identificadoresLabel_10")
        self.identificadoresLabel_10.setFont(font4)

        self.formLayout_5.setWidget(11, QFormLayout.LabelRole, self.identificadoresLabel_10)

        self.isbnLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.isbnLibrolineEdit.setObjectName(u"isbnLibrolineEdit")
        self.isbnLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.isbnLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.isbnLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(11, QFormLayout.FieldRole, self.isbnLibrolineEdit)

        self.identificadoresLabel_11 = QLabel(self.scrollAreaWidgetContents_6)
        self.identificadoresLabel_11.setObjectName(u"identificadoresLabel_11")
        self.identificadoresLabel_11.setFont(font4)

        self.formLayout_5.setWidget(12, QFormLayout.LabelRole, self.identificadoresLabel_11)

        self.identificadoresLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.identificadoresLibrolineEdit.setObjectName(u"identificadoresLibrolineEdit")
        self.identificadoresLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoresLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoresLibrolineEdit.setFont(font4)

        self.formLayout_5.setWidget(12, QFormLayout.FieldRole, self.identificadoresLibrolineEdit)

        self.enviarFormLibroButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.enviarFormLibroButton.setObjectName(u"enviarFormLibroButton")
        sizePolicy1.setHeightForWidth(self.enviarFormLibroButton.sizePolicy().hasHeightForWidth())
        self.enviarFormLibroButton.setSizePolicy(sizePolicy1)
        self.enviarFormLibroButton.setMinimumSize(QSize(100, 34))
        self.enviarFormLibroButton.setMaximumSize(QSize(100, 34))
        self.enviarFormLibroButton.setFont(font4)
        self.enviarFormLibroButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormLibroButton.setIcon(icon9)

        self.formLayout_5.setWidget(13, QFormLayout.FieldRole, self.enviarFormLibroButton)


        self.verticalLayout_16.addLayout(self.formLayout_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_13.addWidget(self.scrollArea_5)

        self.tipoColeccion.addWidget(self.formLibro)
        self.formSimple = QWidget()
        self.formSimple.setObjectName(u"formSimple")
        self.verticalLayout_14 = QVBoxLayout(self.formSimple)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea_6 = QScrollArea(self.formSimple)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 647, 148))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tituloLabel_17 = QLabel(self.scrollAreaWidgetContents_7)
        self.tituloLabel_17.setObjectName(u"tituloLabel_17")
        self.tituloLabel_17.setMinimumSize(QSize(121, 0))
        self.tituloLabel_17.setFont(font4)

        self.gridLayout.addWidget(self.tituloLabel_17, 0, 0, 1, 1)

        self.nombrearchivolineEdit = QLineEdit(self.scrollAreaWidgetContents_7)
        self.nombrearchivolineEdit.setObjectName(u"nombrearchivolineEdit")
        self.nombrearchivolineEdit.setMinimumSize(QSize(500, 34))
        self.nombrearchivolineEdit.setMaximumSize(QSize(500, 34))
        self.nombrearchivolineEdit.setFont(font4)
        self.nombrearchivolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.nombrearchivolineEdit, 0, 1, 1, 2)

        self.tituloLabel_18 = QLabel(self.scrollAreaWidgetContents_7)
        self.tituloLabel_18.setObjectName(u"tituloLabel_18")
        self.tituloLabel_18.setMinimumSize(QSize(121, 0))
        self.tituloLabel_18.setFont(font4)

        self.gridLayout.addWidget(self.tituloLabel_18, 1, 0, 1, 1)

        self.folderlineEdit = QLineEdit(self.scrollAreaWidgetContents_7)
        self.folderlineEdit.setObjectName(u"folderlineEdit")
        self.folderlineEdit.setMinimumSize(QSize(450, 34))
        self.folderlineEdit.setMaximumSize(QSize(450, 34))
        self.folderlineEdit.setFont(font4)
        self.folderlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.folderlineEdit, 1, 1, 1, 1)

        self.browserDirButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.browserDirButton.setObjectName(u"browserDirButton")
        self.browserDirButton.setMinimumSize(QSize(42, 42))
        self.browserDirButton.setMaximumSize(QSize(42, 42))
        self.browserDirButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.browserDirButton.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        icon10 = QIcon()
        icon10.addFile(u":/imgs/imgs/icons/black-folder-shape-for-interface.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browserDirButton.setIcon(icon10)

        self.gridLayout.addWidget(self.browserDirButton, 1, 2, 1, 1)

        self.enviarFormSimpleButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.enviarFormSimpleButton.setObjectName(u"enviarFormSimpleButton")
        sizePolicy1.setHeightForWidth(self.enviarFormSimpleButton.sizePolicy().hasHeightForWidth())
        self.enviarFormSimpleButton.setSizePolicy(sizePolicy1)
        self.enviarFormSimpleButton.setMinimumSize(QSize(100, 34))
        self.enviarFormSimpleButton.setMaximumSize(QSize(100, 34))
        self.enviarFormSimpleButton.setFont(font4)
        self.enviarFormSimpleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormSimpleButton.setIcon(icon9)

        self.gridLayout.addWidget(self.enviarFormSimpleButton, 2, 1, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_14.addWidget(self.scrollArea_6)

        self.tipoColeccion.addWidget(self.formSimple)

        self.verticalLayout.addWidget(self.tipoColeccion)


        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.metadataPage)
        self.escanerPage = QWidget()
        self.escanerPage.setObjectName(u"escanerPage")
        self.escanerPage.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.escanerPage)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.layoutEscan = QWidget(self.escanerPage)
        self.layoutEscan.setObjectName(u"layoutEscan")
        self.layoutEscan.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.layoutEscan)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.layoutEscan)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.controlPanel = QWidget(self.widget_2)
        self.controlPanel.setObjectName(u"controlPanel")
        self.controlPanel.setMinimumSize(QSize(210, 0))
        self.controlPanel.setMaximumSize(QSize(225, 16777215))
        self.controlPanel.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.verticalLayout_18 = QVBoxLayout(self.controlPanel)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.titulelementoIDLabel = QLabel(self.controlPanel)
        self.titulelementoIDLabel.setObjectName(u"titulelementoIDLabel")
        self.titulelementoIDLabel.setEnabled(True)
        self.titulelementoIDLabel.setMinimumSize(QSize(16, 16))
        self.titulelementoIDLabel.setMaximumSize(QSize(16, 16))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.titulelementoIDLabel.setFont(font5)
        self.titulelementoIDLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.titulelementoIDLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.titulelementoIDLabel.setPixmap(QPixmap(u":/imgs/imgs/icons/list-interface-symbol.svg"))
        self.titulelementoIDLabel.setScaledContents(True)

        self.gridLayout_2.addWidget(self.titulelementoIDLabel, 0, 0, 1, 1)

        self.elementoIDLabel = QLabel(self.controlPanel)
        self.elementoIDLabel.setObjectName(u"elementoIDLabel")
        self.elementoIDLabel.setMinimumSize(QSize(75, 25))
        self.elementoIDLabel.setMaximumSize(QSize(190, 25))
        self.elementoIDLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.elementoIDLabel, 0, 2, 1, 1)

        self.titulelementoTituloLabel_2 = QLabel(self.controlPanel)
        self.titulelementoTituloLabel_2.setObjectName(u"titulelementoTituloLabel_2")
        self.titulelementoTituloLabel_2.setFont(font5)
        self.titulelementoTituloLabel_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_2.addWidget(self.titulelementoTituloLabel_2, 0, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_2)

        self.titulelementoTituloLabel = QLabel(self.controlPanel)
        self.titulelementoTituloLabel.setObjectName(u"titulelementoTituloLabel")
        self.titulelementoTituloLabel.setFont(font5)
        self.titulelementoTituloLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_18.addWidget(self.titulelementoTituloLabel)

        self.elementoTituloLabel = QLabel(self.controlPanel)
        self.elementoTituloLabel.setObjectName(u"elementoTituloLabel")
        self.elementoTituloLabel.setMinimumSize(QSize(190, 70))
        self.elementoTituloLabel.setMaximumSize(QSize(190, 70))
        self.elementoTituloLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.elementoTituloLabel.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.elementoTituloLabel)

        self.titulelementoTituloLabel_5 = QLabel(self.controlPanel)
        self.titulelementoTituloLabel_5.setObjectName(u"titulelementoTituloLabel_5")
        self.titulelementoTituloLabel_5.setFont(font5)
        self.titulelementoTituloLabel_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_18.addWidget(self.titulelementoTituloLabel_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.directorio_elementos = QLabel(self.controlPanel)
        self.directorio_elementos.setObjectName(u"directorio_elementos")
        self.directorio_elementos.setMinimumSize(QSize(150, 25))
        self.directorio_elementos.setMaximumSize(QSize(190, 25))
        self.directorio_elementos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.directorio_elementos, 0, 0, 1, 1)

        self.openFolderButton = QPushButton(self.controlPanel)
        self.openFolderButton.setObjectName(u"openFolderButton")
        self.openFolderButton.setMinimumSize(QSize(42, 42))
        self.openFolderButton.setMaximumSize(QSize(42, 42))
        self.openFolderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.openFolderButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(182, 182, 182);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/imgs/imgs/icons/open-black-folder-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openFolderButton.setIcon(icon11)
        self.openFolderButton.setIconSize(QSize(24, 24))

        self.gridLayout_4.addWidget(self.openFolderButton, 0, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.titulelementoTituloLabel_6 = QLabel(self.controlPanel)
        self.titulelementoTituloLabel_6.setObjectName(u"titulelementoTituloLabel_6")
        self.titulelementoTituloLabel_6.setFont(font5)
        self.titulelementoTituloLabel_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_5.addWidget(self.titulelementoTituloLabel_6, 0, 0, 1, 1)

        self.cantidadimgsLabel = QLabel(self.controlPanel)
        self.cantidadimgsLabel.setObjectName(u"cantidadimgsLabel")
        self.cantidadimgsLabel.setMinimumSize(QSize(70, 25))
        self.cantidadimgsLabel.setMaximumSize(QSize(70, 25))
        self.cantidadimgsLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout_5.addWidget(self.cantidadimgsLabel, 0, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_5)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.folioIzqLabel = QLabel(self.controlPanel)
        self.folioIzqLabel.setObjectName(u"folioIzqLabel")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.folioIzqLabel)

        self.folioizqLineEdit = QLineEdit(self.controlPanel)
        self.folioizqLineEdit.setObjectName(u"folioizqLineEdit")
        self.folioizqLineEdit.setMinimumSize(QSize(0, 25))
        self.folioizqLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.folioizqLineEdit)


        self.verticalLayout_18.addLayout(self.formLayout_7)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.folioderLabel = QLabel(self.controlPanel)
        self.folioderLabel.setObjectName(u"folioderLabel")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.folioderLabel)

        self.folioderLineEdit = QLineEdit(self.controlPanel)
        self.folioderLineEdit.setObjectName(u"folioderLineEdit")
        self.folioderLineEdit.setMinimumSize(QSize(0, 25))
        self.folioderLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.folioderLineEdit)


        self.verticalLayout_18.addLayout(self.formLayout_8)


        self.horizontalLayout_6.addWidget(self.controlPanel)

        self.imagenizqLabel = QLabel(self.widget_2)
        self.imagenizqLabel.setObjectName(u"imagenizqLabel")
        self.imagenizqLabel.setMinimumSize(QSize(200, 0))
        self.imagenizqLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.imagenizqLabel.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.imagenizqLabel)

        self.imagederLabel = QLabel(self.widget_2)
        self.imagederLabel.setObjectName(u"imagederLabel")
        self.imagederLabel.setMinimumSize(QSize(200, 0))
        self.imagederLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.imagederLabel.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.imagederLabel)


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
        self.controlesCamstackedWidget = QStackedWidget(self.captureControl)
        self.controlesCamstackedWidget.setObjectName(u"controlesCamstackedWidget")
        self.controlesCamstackedWidget.setMinimumSize(QSize(200, 0))
        self.captura = QWidget()
        self.captura.setObjectName(u"captura")
        self.horizontalLayout_10 = QHBoxLayout(self.captura)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.capturaButton = QPushButton(self.captura)
        self.capturaButton.setObjectName(u"capturaButton")
        self.capturaButton.setMinimumSize(QSize(120, 35))
        self.capturaButton.setMaximumSize(QSize(16777215, 35))
        font6 = QFont()
        font6.setPointSize(11)
        self.capturaButton.setFont(font6)
        self.capturaButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/imgs/imgs/icons/camera-to-take-photos_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.capturaButton.setIcon(icon12)
        self.capturaButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.capturaButton)

        self.controlesCamstackedWidget.addWidget(self.captura)
        self.validar = QWidget()
        self.validar.setObjectName(u"validar")
        self.horizontalLayout_11 = QHBoxLayout(self.validar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.validateButton = QPushButton(self.validar)
        self.validateButton.setObjectName(u"validateButton")
        self.validateButton.setMinimumSize(QSize(120, 35))
        self.validateButton.setMaximumSize(QSize(16777215, 35))
        self.validateButton.setFont(font6)
        self.validateButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/imgs/imgs/icons/check-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.validateButton.setIcon(icon13)
        self.validateButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.validateButton)

        self.resetButton = QPushButton(self.validar)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(120, 35))
        self.resetButton.setMaximumSize(QSize(16777215, 35))
        self.resetButton.setFont(font6)
        self.resetButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/imgs/imgs/icons/undo-circular-arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon14)
        self.resetButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.resetButton)

        self.controlesCamstackedWidget.addWidget(self.validar)

        self.horizontalLayout_7.addWidget(self.controlesCamstackedWidget)


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
        self.stackedWidget.addWidget(self.exportarPage)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.pages)


        self.verticalLayout_5.addWidget(self.main)

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


        self.verticalLayout_5.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.header.raise_()
        self.footer.raise_()
        self.main.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tipoColeccion.setCurrentIndex(0)
        self.controlesCamstackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeoEscan", None))
        self.neoLabel.setText("")
        self.versionLabel.setText("")
        self.inicioButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Inicio", None))
        self.coleccionesButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Metadatos", None))
        self.escanerButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Esc\u00e1ner", None))
        self.imagenesButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Im\u00e1genes", None))
        self.exportarButton.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"Exportar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Iniciar nuevo proyecto", None))
        self.nuevoProyectoButton.setText("")
        self.proyectos_actuales_label.setText(QCoreApplication.translate("MainWindow", u"Proyectos actuales", None))
        self.H1metadatosLabel.setText(QCoreApplication.translate("MainWindow", u"Metadatos", None))
        self.backtoInicioButton.setText(QCoreApplication.translate("MainWindow", u"  Volver al inicio", None))
        self.tipodocLabel.setText(QCoreApplication.translate("MainWindow", u"Tipo de documento", None))
        self.tipodocComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Legajo", None))
        self.tipodocComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Documento", None))
        self.tipodocComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Imagen", None))
        self.tipodocComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Peri\u00f3dico / revista", None))
        self.tipodocComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Libro", None))
        self.tipodocComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sin tipo", None))

        self.tituloLabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.titulolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado al expediente", None))
        self.numextLabel.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripcionlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve resumen del tema del expediente", None))
        self.creadorlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Persona o entidad responsable del contenido del expediente", None))
        self.fechaILabel.setText(QCoreApplication.translate("MainWindow", u"Fecha inicial", None))
        self.fechaIlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.fechaFLabel.setText(QCoreApplication.translate("MainWindow", u"Fecha final", None))
        self.fechaFlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.idiomaLabel.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.idiomalineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"por ejemplo: es (para espa\u00f1ol), en (ingl\u00e9s), fr (franc\u00e9s), la (lat\u00edn)", None))
        self.numfolLabel.setText(QCoreApplication.translate("MainWindow", u"N\u00fam. folios/p\u00e1gs.", None))
        self.numfollineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero de folios o p\u00e1ginas", None))
        self.identificadoresLabel.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoreslineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormLegajoButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.creadorLabel.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.coberturaLabel.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturalineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localidad, ciudad, regi\u00f3n, pa\u00eds, reino", None))
        self.tituloLabel_3.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.titulodoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado al documento", None))
        self.numextLabel_3.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripciondoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve resumen del tema del expediente", None))
        self.creadorLabel_3.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.creadordoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Persona o entidad responsable del contenido del documento", None))
        self.fechaILabel_3.setText(QCoreApplication.translate("MainWindow", u"Fecha inicial", None))
        self.fechaIdoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.fechaFLabel_3.setText(QCoreApplication.translate("MainWindow", u"Fecha final", None))
        self.fechaFdoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.coberturaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturadoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localidad, ciudad, regi\u00f3n, pa\u00eds, reino", None))
        self.idiomaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.idiomadoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"por ejemplo: es (para espa\u00f1ol), en (ingl\u00e9s), fr (franc\u00e9s), la (lat\u00edn)", None))
        self.numfolLabel_3.setText(QCoreApplication.translate("MainWindow", u"N\u00fam. folios/p\u00e1gs.", None))
        self.numfoliodoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero de folios o p\u00e1ginas", None))
        self.identificadoresLabel_3.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoresdoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormDocumentoButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.tituloLabel_4.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.tituloimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado a la imagen", None))
        self.tituloLabel_5.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.creadorimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Autor, dibujante, pintor", None))
        self.tituloLabel_6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.fechaimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.tituloLabel_7.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n f\u00edsica", None))
        self.descripcionfisicaimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"tipo, dimensiones", None))
        self.numextLabel_4.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripcionimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve descripci\u00f3n de lo representado en la imagen. ", None))
        self.identificadoresLabel_5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.tipoimagenlineEdit.setText("")
        self.tipoimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mapa, dibujo, ilustraci\u00f3n, plano...", None))
        self.identificadoresLabel_4.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoresimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormImageButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturaespacialimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lugar de producci\u00f3n o representaci\u00f3n de la imagen", None))
        self.tituloLabel_8.setText(QCoreApplication.translate("MainWindow", u"Nombre publicaci\u00f3n", None))
        self.nombreserlineEdit.setText("")
        self.nombreserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre del peri\u00f3dico o revista", None))
        self.tituloLabel_9.setText(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.volumenserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero del vol\u00famen o serie", None))
        self.tituloLabel_10.setText(QCoreApplication.translate("MainWindow", u"Ejemplar", None))
        self.ejemplarserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El n\u00famero del ejemplar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.fechaserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.tituloLabel_11.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ginas", None))
        self.paginaserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero de p\u00e1ginas", None))
        self.numextLabel_5.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripcionserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve descripci\u00f3n del ejemplar", None))
        self.identificadoresLabel_6.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.idiomaserlineEdit.setText("")
        self.idiomaserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"idioma principal del ejemplar", None))
        self.identificadoresLabel_8.setText(QCoreApplication.translate("MainWindow", u"ISSN", None))
        self.issnserlineEdit.setText("")
        self.issnserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero estandarizado", None))
        self.identificadoresLabel_7.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoreserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormSeriadaButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.tituloLabel_12.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.titulolibrolineEdit.setText("")
        self.titulolibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00edtulo y subt\u00edtulo del libro", None))
        self.tituloLabel_16.setText(QCoreApplication.translate("MainWindow", u"Autor(es)", None))
        self.autorlibrolineEdit.setText("")
        self.autorlibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Autor o autores del libro", None))
        self.tituloLabel_13.setText(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.volumelibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero del vol\u00famen o serie", None))
        self.tituloLabel_14.setText(QCoreApplication.translate("MainWindow", u"Serie", None))
        self.serieLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de la serie de la colecci\u00f3n de libros", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Edici\u00f3n", None))
        self.edicionLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero de la edici\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lugar", None))
        self.lugarLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ciudad de publicaci\u00f3n", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Editorial", None))
        self.editorialLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre del impresor o editorial", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.fechaLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA", None))
        self.tituloLabel_15.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ginas", None))
        self.paginasLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero de p\u00e1ginas", None))
        self.numextLabel_6.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripcionLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve descripci\u00f3n del libro", None))
        self.identificadoresLabel_9.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.idiomaLibrolineEdit.setText("")
        self.idiomaLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"idioma principal del ejemplar", None))
        self.identificadoresLabel_10.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.isbnLibrolineEdit.setText("")
        self.isbnLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero estandarizado", None))
        self.identificadoresLabel_11.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoresLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormLibroButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.tituloLabel_17.setText(QCoreApplication.translate("MainWindow", u"Nombre del archivo", None))
        self.nombrearchivolineEdit.setText("")
        self.nombrearchivolineEdit.setPlaceholderText("")
        self.tituloLabel_18.setText(QCoreApplication.translate("MainWindow", u"Guardar en...", None))
        self.folderlineEdit.setText("")
        self.folderlineEdit.setPlaceholderText("")
        self.browserDirButton.setText("")
        self.enviarFormSimpleButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.titulelementoIDLabel.setText("")
        self.elementoIDLabel.setText("")
        self.titulelementoTituloLabel_2.setText(QCoreApplication.translate("MainWindow", u"ID elemento", None))
        self.titulelementoTituloLabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.elementoTituloLabel.setText("")
        self.titulelementoTituloLabel_5.setText(QCoreApplication.translate("MainWindow", u"Directorio im\u00e1genes", None))
        self.directorio_elementos.setText("")
        self.openFolderButton.setText("")
        self.titulelementoTituloLabel_6.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de imgs", None))
        self.cantidadimgsLabel.setText("")
        self.folioIzqLabel.setText(QCoreApplication.translate("MainWindow", u"folio izq.", None))
        self.folioizqLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"# folio recto", None))
        self.folioderLabel.setText(QCoreApplication.translate("MainWindow", u"folio der.", None))
        self.folioderLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"# folio verso", None))
        self.imagenizqLabel.setText("")
        self.imagederLabel.setText("")
        self.capturaButton.setText(QCoreApplication.translate("MainWindow", u"capturar", None))
        self.validateButton.setText(QCoreApplication.translate("MainWindow", u"validar", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"retomar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IM\u00c1GENES", None))
        self.c_neogranadina.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><a href=\"https://neogranadina.org/\" target=\"_blank\"><span style=\" font-size:7pt; text-decoration: underline;color:rgba(251,251,251,.8)\">\u00a9 2021 Fundaci\u00f3n Hist\u00f3rica Neogranadina</span></a></body></html>", None))
        self.down_arrow.setText("")
    # retranslateUi

