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
        MainWindow.resize(1000, 669)
        MainWindow.setMinimumSize(QSize(1000, 480))
        font = QFont()
        font.setStyleStrategy(QFont.NoAntialias)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"imgs/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: transparent;")
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
        self.header.setMinimumSize(QSize(0, 0))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"background-color: rgba(0, 0, 0, .7);\n"
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
"background-color: transparent;\n"
"")
        self.neoLabel.setPixmap(QPixmap(u"imgs/Neogranadina_header_white.svg"))
        self.neoLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.neoLabel)

        self.versionLabel = QLabel(self.header)
        self.versionLabel.setObjectName(u"versionLabel")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.versionLabel.setFont(font1)
        self.versionLabel.setStyleSheet(u"padding-right: 10px;\n"
"background-color: transparent;\n"
"color: rgba(255,255,255,.7);")
        self.versionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.versionLabel)

        self.closeButton = QPushButton(self.header)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(50, 32))
        self.closeButton.setMaximumSize(QSize(50, 16777215))
        self.closeButton.setFont(font1)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"color: rgba(255, 255, 255,.7);\n"
"background-color:transparent;")
        self.closeButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.closeButton)


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
        brush = QBrush(QColor(255, 255, 255, 255))
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
        self.menu_bar.setAutoFillBackground(False)
        self.menu_bar.setStyleSheet(u"QFrame {background-color: rgba(0, 0, 0,.7);}\n"
"\n"
"QLabel {\n"
"	color: rgba(255,255,255,.9);\n"
"	background-color: transparent;\n"
"	background-position: center top;\n"
"	padding-bottom: 5px;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgba(255,255,255,.9);\n"
"	background-color: transparent;\n"
"	background-position: center top;\n"
"	padding-top: 5px;\n"
"	padding-bottom:5px;\n"
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
        self.frame = QFrame(self.menu_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.inicioButton = QPushButton(self.frame)
        self.inicioButton.setObjectName(u"inicioButton")
        self.inicioButton.setMinimumSize(QSize(0, 80))
        self.inicioButton.setMaximumSize(QSize(16777215, 80))
        self.inicioButton.setFont(font1)
        self.inicioButton.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(whatsthis)
        self.inicioButton.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.inicioButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"imgs/icons/pages-interface.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inicioButton.setIcon(icon1)
        self.inicioButton.setIconSize(QSize(40, 40))

        self.verticalLayout_21.addWidget(self.inicioButton)

        self.inicioLabel = QLabel(self.frame)
        self.inicioLabel.setObjectName(u"inicioLabel")
        self.inicioLabel.setMinimumSize(QSize(0, 18))
        self.inicioLabel.setMaximumSize(QSize(16777215, 18))
        self.inicioLabel.setFont(font1)
        self.inicioLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.inicioLabel)

        self.coleccionesButton = QPushButton(self.frame)
        self.coleccionesButton.setObjectName(u"coleccionesButton")
        self.coleccionesButton.setMinimumSize(QSize(0, 80))
        self.coleccionesButton.setMaximumSize(QSize(16777215, 80))
        self.coleccionesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.coleccionesButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"imgs/icons/window-of-four-rounded-squares.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.coleccionesButton.setIcon(icon2)
        self.coleccionesButton.setIconSize(QSize(40, 40))

        self.verticalLayout_21.addWidget(self.coleccionesButton)

        self.metadatosLabel = QLabel(self.frame)
        self.metadatosLabel.setObjectName(u"metadatosLabel")
        self.metadatosLabel.setMinimumSize(QSize(0, 18))
        self.metadatosLabel.setMaximumSize(QSize(16777215, 18))
        self.metadatosLabel.setFont(font1)
        self.metadatosLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.metadatosLabel)

        self.escanerButton = QPushButton(self.frame)
        self.escanerButton.setObjectName(u"escanerButton")
        self.escanerButton.setMinimumSize(QSize(0, 80))
        self.escanerButton.setMaximumSize(QSize(16777215, 80))
        self.escanerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.escanerButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"imgs/icons/camera-to-take-photos.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.escanerButton.setIcon(icon3)
        self.escanerButton.setIconSize(QSize(40, 40))

        self.verticalLayout_21.addWidget(self.escanerButton)

        self.escanerLabel = QLabel(self.frame)
        self.escanerLabel.setObjectName(u"escanerLabel")
        self.escanerLabel.setMinimumSize(QSize(0, 18))
        self.escanerLabel.setMaximumSize(QSize(16777215, 18))
        self.escanerLabel.setFont(font1)
        self.escanerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.escanerLabel)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 80))
        self.pushButton.setMaximumSize(QSize(16777215, 80))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"imgs/icons/cogwheel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(40, 40))

        self.verticalLayout_21.addWidget(self.pushButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 18))
        self.label.setMaximumSize(QSize(16777215, 18))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)


        self.verticalLayout_2.addWidget(self.frame)

        self.emptyframe = QFrame(self.menu_bar)
        self.emptyframe.setObjectName(u"emptyframe")
        self.emptyframe.setFrameShape(QFrame.StyledPanel)
        self.emptyframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.emptyframe)


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
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.nuevoProyectoButton = QPushButton(self.inicioPage)
        self.nuevoProyectoButton.setObjectName(u"nuevoProyectoButton")
        self.nuevoProyectoButton.setMinimumSize(QSize(40, 40))
        self.nuevoProyectoButton.setMaximumSize(QSize(40, 40))
        self.nuevoProyectoButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"imgs/icons/plus-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nuevoProyectoButton.setIcon(icon5)
        self.nuevoProyectoButton.setIconSize(QSize(20, 20))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.nuevoProyectoButton)


        self.verticalLayout_19.addLayout(self.formLayout_6)

        self.proyectos_actuales_label = QLabel(self.inicioPage)
        self.proyectos_actuales_label.setObjectName(u"proyectos_actuales_label")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.proyectos_actuales_label.setFont(font3)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 877, 499))
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
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.H1metadatosLabel.setFont(font3)

        self.horizontalLayout_9.addWidget(self.H1metadatosLabel)

        self.backtoInicioButton = QPushButton(self.headerMetadatos)
        self.backtoInicioButton.setObjectName(u"backtoInicioButton")
        self.backtoInicioButton.setMinimumSize(QSize(100, 42))
        self.backtoInicioButton.setMaximumSize(QSize(150, 42))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.backtoInicioButton.setFont(font4)
        self.backtoInicioButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"imgs/icons/left-arrowhead-in-a-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backtoInicioButton.setIcon(icon6)
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
        font5 = QFont()
        font5.setPointSize(10)
        self.tipodocLabel.setFont(font5)

        self.horizontalLayout_8.addWidget(self.tipodocLabel)

        self.tipodocComboBox = QComboBox(self.formChanger)
        icon7 = QIcon()
        icon7.addFile(u"imgs/icons/folder-check-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u"imgs/icons/documents-rounded-square-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u"imgs/icons/image-interface-symbol-with-a-landscape.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u"imgs/icons/news-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u"imgs/icons/open-book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u"imgs/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon12, "")
        self.tipodocComboBox.setObjectName(u"tipodocComboBox")
        self.tipodocComboBox.setMinimumSize(QSize(300, 34))
        self.tipodocComboBox.setMaximumSize(QSize(300, 34))
        self.tipodocComboBox.setFont(font5)

        self.horizontalLayout_8.addWidget(self.tipodocComboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.formChanger)

        self.tipoColeccion = QStackedWidget(self.widget)
        self.tipoColeccion.setObjectName(u"tipoColeccion")
        self.tipoColeccion.setStyleSheet(u"")
        self.formLegajo = QWidget()
        self.formLegajo.setObjectName(u"formLegajo")
        self.horizontalLayout_15 = QHBoxLayout(self.formLegajo)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.scrollArea = QScrollArea(self.formLegajo)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(648, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 842, 452))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.tituloLabel = QLabel(self.scrollAreaWidgetContents)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setFont(font5)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.tituloLabel)

        self.titulolineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.titulolineEdit.setObjectName(u"titulolineEdit")
        self.titulolineEdit.setMinimumSize(QSize(500, 34))
        self.titulolineEdit.setMaximumSize(QSize(500, 34))
        self.titulolineEdit.setFont(font5)
        self.titulolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.titulolineEdit)

        self.numextLabel = QLabel(self.scrollAreaWidgetContents)
        self.numextLabel.setObjectName(u"numextLabel")
        self.numextLabel.setFont(font5)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.numextLabel)

        self.descripcionlineEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.descripcionlineEdit.setObjectName(u"descripcionlineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descripcionlineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionlineEdit.setSizePolicy(sizePolicy)
        self.descripcionlineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionlineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionlineEdit.setFont(font5)
        self.descripcionlineEdit.setStyleSheet(u"Breve resumen del tema del expediente")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.descripcionlineEdit)

        self.creadorLabel = QLabel(self.scrollAreaWidgetContents)
        self.creadorLabel.setObjectName(u"creadorLabel")
        self.creadorLabel.setFont(font5)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.creadorLabel)

        self.creadorlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.creadorlineEdit.setObjectName(u"creadorlineEdit")
        self.creadorlineEdit.setMinimumSize(QSize(500, 34))
        self.creadorlineEdit.setMaximumSize(QSize(500, 34))
        self.creadorlineEdit.setFont(font5)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.creadorlineEdit)

        self.fechaILabel = QLabel(self.scrollAreaWidgetContents)
        self.fechaILabel.setObjectName(u"fechaILabel")
        self.fechaILabel.setFont(font5)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.fechaILabel)

        self.fechaIlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fechaIlineEdit.setObjectName(u"fechaIlineEdit")
        self.fechaIlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaIlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaIlineEdit.setFont(font5)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.fechaIlineEdit)

        self.fechaFLabel = QLabel(self.scrollAreaWidgetContents)
        self.fechaFLabel.setObjectName(u"fechaFLabel")
        self.fechaFLabel.setFont(font5)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.fechaFLabel)

        self.fechaFlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fechaFlineEdit.setObjectName(u"fechaFlineEdit")
        self.fechaFlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaFlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaFlineEdit.setFont(font5)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.fechaFlineEdit)

        self.coberturaLabel = QLabel(self.scrollAreaWidgetContents)
        self.coberturaLabel.setObjectName(u"coberturaLabel")
        self.coberturaLabel.setFont(font5)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.coberturaLabel)

        self.coberturalineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.coberturalineEdit.setObjectName(u"coberturalineEdit")
        self.coberturalineEdit.setMinimumSize(QSize(500, 34))
        self.coberturalineEdit.setMaximumSize(QSize(500, 34))
        self.coberturalineEdit.setFont(font5)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.coberturalineEdit)

        self.idiomaLabel = QLabel(self.scrollAreaWidgetContents)
        self.idiomaLabel.setObjectName(u"idiomaLabel")
        self.idiomaLabel.setFont(font5)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.idiomaLabel)

        self.idiomalineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.idiomalineEdit.setObjectName(u"idiomalineEdit")
        self.idiomalineEdit.setMinimumSize(QSize(500, 34))
        self.idiomalineEdit.setMaximumSize(QSize(500, 34))
        self.idiomalineEdit.setFont(font5)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.idiomalineEdit)

        self.numfolLabel = QLabel(self.scrollAreaWidgetContents)
        self.numfolLabel.setObjectName(u"numfolLabel")
        self.numfolLabel.setFont(font5)

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.numfolLabel)

        self.numfollineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.numfollineEdit.setObjectName(u"numfollineEdit")
        self.numfollineEdit.setMinimumSize(QSize(500, 34))
        self.numfollineEdit.setMaximumSize(QSize(500, 34))
        self.numfollineEdit.setFont(font5)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.numfollineEdit)

        self.identificadoreslineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.identificadoreslineEdit.setObjectName(u"identificadoreslineEdit")
        self.identificadoreslineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoreslineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoreslineEdit.setFont(font5)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.identificadoreslineEdit)

        self.identificadoresLabel = QLabel(self.scrollAreaWidgetContents)
        self.identificadoresLabel.setObjectName(u"identificadoresLabel")
        self.identificadoresLabel.setFont(font5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.identificadoresLabel)


        self.verticalLayout_7.addLayout(self.formLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_15.addWidget(self.scrollArea)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 842, 440))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.tituloLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.tituloLabel_3.setObjectName(u"tituloLabel_3")
        self.tituloLabel_3.setFont(font5)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_3)

        self.titulodoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.titulodoclineEdit.setObjectName(u"titulodoclineEdit")
        self.titulodoclineEdit.setMinimumSize(QSize(500, 34))
        self.titulodoclineEdit.setMaximumSize(QSize(500, 34))
        self.titulodoclineEdit.setFont(font5)
        self.titulodoclineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.titulodoclineEdit)

        self.numextLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.numextLabel_3.setObjectName(u"numextLabel_3")
        self.numextLabel_3.setFont(font5)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.numextLabel_3)

        self.descripciondoclineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.descripciondoclineEdit.setObjectName(u"descripciondoclineEdit")
        sizePolicy.setHeightForWidth(self.descripciondoclineEdit.sizePolicy().hasHeightForWidth())
        self.descripciondoclineEdit.setSizePolicy(sizePolicy)
        self.descripciondoclineEdit.setMinimumSize(QSize(500, 70))
        self.descripciondoclineEdit.setMaximumSize(QSize(500, 250))
        self.descripciondoclineEdit.setFont(font5)
        self.descripciondoclineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.descripciondoclineEdit)

        self.creadorLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.creadorLabel_3.setObjectName(u"creadorLabel_3")
        self.creadorLabel_3.setFont(font5)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.creadorLabel_3)

        self.creadordoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.creadordoclineEdit.setObjectName(u"creadordoclineEdit")
        self.creadordoclineEdit.setMinimumSize(QSize(500, 34))
        self.creadordoclineEdit.setMaximumSize(QSize(500, 34))
        self.creadordoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.creadordoclineEdit)

        self.fechaILabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.fechaILabel_3.setObjectName(u"fechaILabel_3")
        self.fechaILabel_3.setFont(font5)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.fechaILabel_3)

        self.fechaIdoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.fechaIdoclineEdit.setObjectName(u"fechaIdoclineEdit")
        self.fechaIdoclineEdit.setMinimumSize(QSize(500, 34))
        self.fechaIdoclineEdit.setMaximumSize(QSize(500, 34))
        self.fechaIdoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.fechaIdoclineEdit)

        self.fechaFLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.fechaFLabel_3.setObjectName(u"fechaFLabel_3")
        self.fechaFLabel_3.setFont(font5)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.fechaFLabel_3)

        self.fechaFdoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.fechaFdoclineEdit.setObjectName(u"fechaFdoclineEdit")
        self.fechaFdoclineEdit.setMinimumSize(QSize(500, 34))
        self.fechaFdoclineEdit.setMaximumSize(QSize(500, 34))
        self.fechaFdoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.fechaFdoclineEdit)

        self.coberturaLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.coberturaLabel_3.setObjectName(u"coberturaLabel_3")
        self.coberturaLabel_3.setFont(font5)

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.coberturaLabel_3)

        self.coberturadoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.coberturadoclineEdit.setObjectName(u"coberturadoclineEdit")
        self.coberturadoclineEdit.setMinimumSize(QSize(500, 34))
        self.coberturadoclineEdit.setMaximumSize(QSize(500, 34))
        self.coberturadoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.coberturadoclineEdit)

        self.idiomaLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.idiomaLabel_3.setObjectName(u"idiomaLabel_3")
        self.idiomaLabel_3.setFont(font5)

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.idiomaLabel_3)

        self.idiomadoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.idiomadoclineEdit.setObjectName(u"idiomadoclineEdit")
        self.idiomadoclineEdit.setMinimumSize(QSize(500, 34))
        self.idiomadoclineEdit.setMaximumSize(QSize(500, 34))
        self.idiomadoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.idiomadoclineEdit)

        self.numfolLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.numfolLabel_3.setObjectName(u"numfolLabel_3")
        self.numfolLabel_3.setFont(font5)

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.numfolLabel_3)

        self.numfoliodoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.numfoliodoclineEdit.setObjectName(u"numfoliodoclineEdit")
        self.numfoliodoclineEdit.setMinimumSize(QSize(500, 34))
        self.numfoliodoclineEdit.setMaximumSize(QSize(500, 34))
        self.numfoliodoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.numfoliodoclineEdit)

        self.identificadoresdoclineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.identificadoresdoclineEdit.setObjectName(u"identificadoresdoclineEdit")
        self.identificadoresdoclineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoresdoclineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoresdoclineEdit.setFont(font5)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.identificadoresdoclineEdit)

        self.identificadoresLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.identificadoresLabel_3.setObjectName(u"identificadoresLabel_3")
        self.identificadoresLabel_3.setFont(font5)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.identificadoresLabel_3)


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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 842, 400))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.tituloLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_4.setObjectName(u"tituloLabel_4")
        self.tituloLabel_4.setFont(font5)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_4)

        self.tituloimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.tituloimagenlineEdit.setObjectName(u"tituloimagenlineEdit")
        self.tituloimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.tituloimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.tituloimagenlineEdit.setFont(font5)
        self.tituloimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.tituloimagenlineEdit)

        self.tituloLabel_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_5.setObjectName(u"tituloLabel_5")
        self.tituloLabel_5.setFont(font5)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.tituloLabel_5)

        self.creadorimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.creadorimagenlineEdit.setObjectName(u"creadorimagenlineEdit")
        self.creadorimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.creadorimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.creadorimagenlineEdit.setFont(font5)
        self.creadorimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.creadorimagenlineEdit)

        self.tituloLabel_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_6.setObjectName(u"tituloLabel_6")
        self.tituloLabel_6.setFont(font5)

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.tituloLabel_6)

        self.fechaimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.fechaimagenlineEdit.setObjectName(u"fechaimagenlineEdit")
        self.fechaimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaimagenlineEdit.setFont(font5)
        self.fechaimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.fechaimagenlineEdit)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.coberturaespacialimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.coberturaespacialimagenlineEdit.setObjectName(u"coberturaespacialimagenlineEdit")
        self.coberturaespacialimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.coberturaespacialimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.coberturaespacialimagenlineEdit.setFont(font5)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.coberturaespacialimagenlineEdit)

        self.tituloLabel_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_7.setObjectName(u"tituloLabel_7")
        self.tituloLabel_7.setFont(font5)

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.tituloLabel_7)

        self.descripcionfisicaimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.descripcionfisicaimagenlineEdit.setObjectName(u"descripcionfisicaimagenlineEdit")
        self.descripcionfisicaimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.descripcionfisicaimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.descripcionfisicaimagenlineEdit.setFont(font5)
        self.descripcionfisicaimagenlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.descripcionfisicaimagenlineEdit)

        self.numextLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.numextLabel_4.setObjectName(u"numextLabel_4")
        self.numextLabel_4.setFont(font5)

        self.formLayout_4.setWidget(11, QFormLayout.LabelRole, self.numextLabel_4)

        self.descripcionimagenlineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_4)
        self.descripcionimagenlineEdit.setObjectName(u"descripcionimagenlineEdit")
        sizePolicy.setHeightForWidth(self.descripcionimagenlineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionimagenlineEdit.setSizePolicy(sizePolicy)
        self.descripcionimagenlineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionimagenlineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionimagenlineEdit.setFont(font5)
        self.descripcionimagenlineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_4.setWidget(11, QFormLayout.FieldRole, self.descripcionimagenlineEdit)

        self.identificadoresLabel_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.identificadoresLabel_5.setObjectName(u"identificadoresLabel_5")
        self.identificadoresLabel_5.setFont(font5)

        self.formLayout_4.setWidget(12, QFormLayout.LabelRole, self.identificadoresLabel_5)

        self.tipoimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.tipoimagenlineEdit.setObjectName(u"tipoimagenlineEdit")
        self.tipoimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.tipoimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.tipoimagenlineEdit.setFont(font5)

        self.formLayout_4.setWidget(12, QFormLayout.FieldRole, self.tipoimagenlineEdit)

        self.identificadoresimagenlineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.identificadoresimagenlineEdit.setObjectName(u"identificadoresimagenlineEdit")
        self.identificadoresimagenlineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoresimagenlineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoresimagenlineEdit.setFont(font5)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.identificadoresimagenlineEdit)

        self.identificadoresLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.identificadoresLabel_4.setObjectName(u"identificadoresLabel_4")
        self.identificadoresLabel_4.setFont(font5)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.identificadoresLabel_4)


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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 842, 446))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tituloLabel_8 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_8.setObjectName(u"tituloLabel_8")
        self.tituloLabel_8.setFont(font5)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.tituloLabel_8)

        self.nombreserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.nombreserlineEdit.setObjectName(u"nombreserlineEdit")
        self.nombreserlineEdit.setMinimumSize(QSize(500, 34))
        self.nombreserlineEdit.setMaximumSize(QSize(500, 34))
        self.nombreserlineEdit.setFont(font5)
        self.nombreserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.nombreserlineEdit)

        self.tituloLabel_9 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_9.setObjectName(u"tituloLabel_9")
        self.tituloLabel_9.setFont(font5)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.tituloLabel_9)

        self.volumenserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.volumenserlineEdit.setObjectName(u"volumenserlineEdit")
        self.volumenserlineEdit.setMinimumSize(QSize(500, 34))
        self.volumenserlineEdit.setMaximumSize(QSize(500, 34))
        self.volumenserlineEdit.setFont(font5)
        self.volumenserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.volumenserlineEdit)

        self.tituloLabel_10 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_10.setObjectName(u"tituloLabel_10")
        self.tituloLabel_10.setFont(font5)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.tituloLabel_10)

        self.ejemplarserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.ejemplarserlineEdit.setObjectName(u"ejemplarserlineEdit")
        self.ejemplarserlineEdit.setMinimumSize(QSize(500, 34))
        self.ejemplarserlineEdit.setMaximumSize(QSize(500, 34))
        self.ejemplarserlineEdit.setFont(font5)
        self.ejemplarserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.ejemplarserlineEdit)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.fechaserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.fechaserlineEdit.setObjectName(u"fechaserlineEdit")
        self.fechaserlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaserlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaserlineEdit.setFont(font5)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.fechaserlineEdit)

        self.tituloLabel_11 = QLabel(self.scrollAreaWidgetContents_5)
        self.tituloLabel_11.setObjectName(u"tituloLabel_11")
        self.tituloLabel_11.setFont(font5)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.tituloLabel_11)

        self.paginaserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.paginaserlineEdit.setObjectName(u"paginaserlineEdit")
        self.paginaserlineEdit.setMinimumSize(QSize(500, 34))
        self.paginaserlineEdit.setMaximumSize(QSize(500, 34))
        self.paginaserlineEdit.setFont(font5)
        self.paginaserlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.paginaserlineEdit)

        self.numextLabel_5 = QLabel(self.scrollAreaWidgetContents_5)
        self.numextLabel_5.setObjectName(u"numextLabel_5")
        self.numextLabel_5.setFont(font5)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.numextLabel_5)

        self.descripcionserlineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.descripcionserlineEdit.setObjectName(u"descripcionserlineEdit")
        sizePolicy.setHeightForWidth(self.descripcionserlineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionserlineEdit.setSizePolicy(sizePolicy)
        self.descripcionserlineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionserlineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionserlineEdit.setFont(font5)
        self.descripcionserlineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.descripcionserlineEdit)

        self.identificadoresLabel_6 = QLabel(self.scrollAreaWidgetContents_5)
        self.identificadoresLabel_6.setObjectName(u"identificadoresLabel_6")
        self.identificadoresLabel_6.setFont(font5)

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.identificadoresLabel_6)

        self.idiomaserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.idiomaserlineEdit.setObjectName(u"idiomaserlineEdit")
        self.idiomaserlineEdit.setMinimumSize(QSize(500, 34))
        self.idiomaserlineEdit.setMaximumSize(QSize(500, 34))
        self.idiomaserlineEdit.setFont(font5)

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.idiomaserlineEdit)

        self.identificadoresLabel_8 = QLabel(self.scrollAreaWidgetContents_5)
        self.identificadoresLabel_8.setObjectName(u"identificadoresLabel_8")
        self.identificadoresLabel_8.setFont(font5)

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.identificadoresLabel_8)

        self.issnserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.issnserlineEdit.setObjectName(u"issnserlineEdit")
        self.issnserlineEdit.setMinimumSize(QSize(500, 34))
        self.issnserlineEdit.setMaximumSize(QSize(500, 34))
        self.issnserlineEdit.setFont(font5)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.issnserlineEdit)

        self.identificadoreserlineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.identificadoreserlineEdit.setObjectName(u"identificadoreserlineEdit")
        self.identificadoreserlineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoreserlineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoreserlineEdit.setFont(font5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.identificadoreserlineEdit)

        self.identificadoresLabel_7 = QLabel(self.scrollAreaWidgetContents_5)
        self.identificadoresLabel_7.setObjectName(u"identificadoresLabel_7")
        self.identificadoresLabel_7.setFont(font5)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.identificadoresLabel_7)


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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 842, 612))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.tituloLabel_12 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_12.setObjectName(u"tituloLabel_12")
        self.tituloLabel_12.setFont(font5)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_12)

        self.titulolibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.titulolibrolineEdit.setObjectName(u"titulolibrolineEdit")
        self.titulolibrolineEdit.setMinimumSize(QSize(500, 34))
        self.titulolibrolineEdit.setMaximumSize(QSize(500, 34))
        self.titulolibrolineEdit.setFont(font5)
        self.titulolibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.titulolibrolineEdit)

        self.tituloLabel_16 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_16.setObjectName(u"tituloLabel_16")
        self.tituloLabel_16.setFont(font5)

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.tituloLabel_16)

        self.autorlibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.autorlibrolineEdit.setObjectName(u"autorlibrolineEdit")
        self.autorlibrolineEdit.setMinimumSize(QSize(500, 34))
        self.autorlibrolineEdit.setMaximumSize(QSize(500, 34))
        self.autorlibrolineEdit.setFont(font5)
        self.autorlibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.autorlibrolineEdit)

        self.tituloLabel_13 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_13.setObjectName(u"tituloLabel_13")
        self.tituloLabel_13.setFont(font5)

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.tituloLabel_13)

        self.volumelibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.volumelibrolineEdit.setObjectName(u"volumelibrolineEdit")
        self.volumelibrolineEdit.setMinimumSize(QSize(500, 34))
        self.volumelibrolineEdit.setMaximumSize(QSize(500, 34))
        self.volumelibrolineEdit.setFont(font5)
        self.volumelibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.volumelibrolineEdit)

        self.tituloLabel_14 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_14.setObjectName(u"tituloLabel_14")
        self.tituloLabel_14.setFont(font5)

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.tituloLabel_14)

        self.serieLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.serieLibrolineEdit.setObjectName(u"serieLibrolineEdit")
        self.serieLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.serieLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.serieLibrolineEdit.setFont(font5)
        self.serieLibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.serieLibrolineEdit)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.edicionLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.edicionLibrolineEdit.setObjectName(u"edicionLibrolineEdit")
        self.edicionLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.edicionLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.edicionLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.edicionLibrolineEdit)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.lugarLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lugarLibrolineEdit.setObjectName(u"lugarLibrolineEdit")
        self.lugarLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.lugarLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.lugarLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.lugarLibrolineEdit)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.label_11)

        self.editorialLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.editorialLibrolineEdit.setObjectName(u"editorialLibrolineEdit")
        self.editorialLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.editorialLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.editorialLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.editorialLibrolineEdit)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.formLayout_5.setWidget(13, QFormLayout.LabelRole, self.label_8)

        self.fechaLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.fechaLibrolineEdit.setObjectName(u"fechaLibrolineEdit")
        self.fechaLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.fechaLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.fechaLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(13, QFormLayout.FieldRole, self.fechaLibrolineEdit)

        self.tituloLabel_15 = QLabel(self.scrollAreaWidgetContents_6)
        self.tituloLabel_15.setObjectName(u"tituloLabel_15")
        self.tituloLabel_15.setFont(font5)

        self.formLayout_5.setWidget(14, QFormLayout.LabelRole, self.tituloLabel_15)

        self.paginasLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.paginasLibrolineEdit.setObjectName(u"paginasLibrolineEdit")
        self.paginasLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.paginasLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.paginasLibrolineEdit.setFont(font5)
        self.paginasLibrolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_5.setWidget(14, QFormLayout.FieldRole, self.paginasLibrolineEdit)

        self.numextLabel_6 = QLabel(self.scrollAreaWidgetContents_6)
        self.numextLabel_6.setObjectName(u"numextLabel_6")
        self.numextLabel_6.setFont(font5)

        self.formLayout_5.setWidget(17, QFormLayout.LabelRole, self.numextLabel_6)

        self.descripcionLibrolineEdit = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.descripcionLibrolineEdit.setObjectName(u"descripcionLibrolineEdit")
        sizePolicy.setHeightForWidth(self.descripcionLibrolineEdit.sizePolicy().hasHeightForWidth())
        self.descripcionLibrolineEdit.setSizePolicy(sizePolicy)
        self.descripcionLibrolineEdit.setMinimumSize(QSize(500, 70))
        self.descripcionLibrolineEdit.setMaximumSize(QSize(500, 250))
        self.descripcionLibrolineEdit.setFont(font5)
        self.descripcionLibrolineEdit.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_5.setWidget(17, QFormLayout.FieldRole, self.descripcionLibrolineEdit)

        self.identificadoresLabel_9 = QLabel(self.scrollAreaWidgetContents_6)
        self.identificadoresLabel_9.setObjectName(u"identificadoresLabel_9")
        self.identificadoresLabel_9.setFont(font5)

        self.formLayout_5.setWidget(18, QFormLayout.LabelRole, self.identificadoresLabel_9)

        self.idiomaLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.idiomaLibrolineEdit.setObjectName(u"idiomaLibrolineEdit")
        self.idiomaLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.idiomaLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.idiomaLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(18, QFormLayout.FieldRole, self.idiomaLibrolineEdit)

        self.identificadoresLabel_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.identificadoresLabel_10.setObjectName(u"identificadoresLabel_10")
        self.identificadoresLabel_10.setFont(font5)

        self.formLayout_5.setWidget(19, QFormLayout.LabelRole, self.identificadoresLabel_10)

        self.isbnLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.isbnLibrolineEdit.setObjectName(u"isbnLibrolineEdit")
        self.isbnLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.isbnLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.isbnLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(19, QFormLayout.FieldRole, self.isbnLibrolineEdit)

        self.identificadoresLibrolineEdit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.identificadoresLibrolineEdit.setObjectName(u"identificadoresLibrolineEdit")
        self.identificadoresLibrolineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoresLibrolineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoresLibrolineEdit.setFont(font5)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.identificadoresLibrolineEdit)

        self.identificadoresLabel_11 = QLabel(self.scrollAreaWidgetContents_6)
        self.identificadoresLabel_11.setObjectName(u"identificadoresLabel_11")
        self.identificadoresLabel_11.setFont(font5)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.identificadoresLabel_11)


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
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 859, 205))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tituloLabel_18 = QLabel(self.scrollAreaWidgetContents_7)
        self.tituloLabel_18.setObjectName(u"tituloLabel_18")
        self.tituloLabel_18.setMinimumSize(QSize(121, 0))
        self.tituloLabel_18.setFont(font5)

        self.gridLayout.addWidget(self.tituloLabel_18, 1, 0, 1, 1)

        self.folderlineEdit = QLineEdit(self.scrollAreaWidgetContents_7)
        self.folderlineEdit.setObjectName(u"folderlineEdit")
        self.folderlineEdit.setMinimumSize(QSize(450, 34))
        self.folderlineEdit.setMaximumSize(QSize(450, 34))
        self.folderlineEdit.setFont(font5)
        self.folderlineEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.folderlineEdit, 1, 1, 1, 1)

        self.nombrearchivolineEdit = QLineEdit(self.scrollAreaWidgetContents_7)
        self.nombrearchivolineEdit.setObjectName(u"nombrearchivolineEdit")
        self.nombrearchivolineEdit.setMinimumSize(QSize(500, 34))
        self.nombrearchivolineEdit.setMaximumSize(QSize(500, 34))
        self.nombrearchivolineEdit.setFont(font5)
        self.nombrearchivolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.nombrearchivolineEdit, 0, 1, 1, 2)

        self.browserDirButton = QPushButton(self.scrollAreaWidgetContents_7)
        self.browserDirButton.setObjectName(u"browserDirButton")
        self.browserDirButton.setMinimumSize(QSize(42, 42))
        self.browserDirButton.setMaximumSize(QSize(42, 42))
        self.browserDirButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.browserDirButton.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        icon13 = QIcon()
        icon13.addFile(u"imgs/icons/black-folder-shape-for-interface.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browserDirButton.setIcon(icon13)

        self.gridLayout.addWidget(self.browserDirButton, 1, 2, 1, 1)

        self.tituloLabel_17 = QLabel(self.scrollAreaWidgetContents_7)
        self.tituloLabel_17.setObjectName(u"tituloLabel_17")
        self.tituloLabel_17.setMinimumSize(QSize(121, 0))
        self.tituloLabel_17.setFont(font5)

        self.gridLayout.addWidget(self.tituloLabel_17, 0, 0, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_14.addWidget(self.scrollArea_6)

        self.tipoColeccion.addWidget(self.formSimple)

        self.verticalLayout.addWidget(self.tipoColeccion)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(150, 75))
        self.widget_3.setMaximumSize(QSize(16777215, 75))
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.line_3 = QFrame(self.widget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_3)

        self.zoom_dial = QDial(self.widget_3)
        self.zoom_dial.setObjectName(u"zoom_dial")
        self.zoom_dial.setMinimumSize(QSize(60, 60))
        self.zoom_dial.setMaximumSize(QSize(60, 60))
        self.zoom_dial.setMinimum(1)
        self.zoom_dial.setMaximum(50)
        self.zoom_dial.setSliderPosition(27)
        self.zoom_dial.setWrapping(True)
        self.zoom_dial.setNotchTarget(5.000000000000000)
        self.zoom_dial.setNotchesVisible(True)

        self.horizontalLayout_16.addWidget(self.zoom_dial)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.zoomLabel = QLabel(self.widget_3)
        self.zoomLabel.setObjectName(u"zoomLabel")
        self.zoomLabel.setMinimumSize(QSize(81, 10))
        self.zoomLabel.setMaximumSize(QSize(81, 10))
        self.zoomLabel.setFont(font5)

        self.verticalLayout_6.addWidget(self.zoomLabel)

        self.zoom_valuedit = QLineEdit(self.widget_3)
        self.zoom_valuedit.setObjectName(u"zoom_valuedit")
        self.zoom_valuedit.setMinimumSize(QSize(81, 34))
        self.zoom_valuedit.setMaximumSize(QSize(81, 34))

        self.verticalLayout_6.addWidget(self.zoom_valuedit)


        self.horizontalLayout_16.addLayout(self.verticalLayout_6)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_4)

        self.exposicionDial = QDial(self.widget_3)
        self.exposicionDial.setObjectName(u"exposicionDial")
        self.exposicionDial.setMinimumSize(QSize(60, 60))
        self.exposicionDial.setMaximumSize(QSize(60, 60))
        self.exposicionDial.setMinimum(1)
        self.exposicionDial.setMaximum(125)
        self.exposicionDial.setValue(25)
        self.exposicionDial.setWrapping(True)
        self.exposicionDial.setNotchTarget(10.000000000000000)
        self.exposicionDial.setNotchesVisible(True)

        self.horizontalLayout_16.addWidget(self.exposicionDial)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.exposicionLabel = QLabel(self.widget_3)
        self.exposicionLabel.setObjectName(u"exposicionLabel")
        self.exposicionLabel.setMinimumSize(QSize(95, 10))
        self.exposicionLabel.setMaximumSize(QSize(95, 10))

        self.verticalLayout_23.addWidget(self.exposicionLabel)

        self.exposicionValue = QLineEdit(self.widget_3)
        self.exposicionValue.setObjectName(u"exposicionValue")
        self.exposicionValue.setMinimumSize(QSize(95, 34))
        self.exposicionValue.setMaximumSize(QSize(95, 34))

        self.verticalLayout_23.addWidget(self.exposicionValue)


        self.horizontalLayout_16.addLayout(self.verticalLayout_23)

        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_16.addWidget(self.line)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.orientacionLabel = QLabel(self.widget_3)
        self.orientacionLabel.setObjectName(u"orientacionLabel")
        self.orientacionLabel.setMinimumSize(QSize(61, 0))
        self.orientacionLabel.setMaximumSize(QSize(61, 16777215))

        self.verticalLayout_24.addWidget(self.orientacionLabel)

        self.orientacionValue = QComboBox(self.widget_3)
        self.orientacionValue.addItem("")
        self.orientacionValue.addItem("")
        self.orientacionValue.setObjectName(u"orientacionValue")
        self.orientacionValue.setMinimumSize(QSize(120, 34))
        self.orientacionValue.setMaximumSize(QSize(120, 34))

        self.verticalLayout_24.addWidget(self.orientacionValue)


        self.horizontalLayout_16.addLayout(self.verticalLayout_24)

        self.line_5 = QFrame(self.widget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_5)

        self.dng_check = QCheckBox(self.widget_3)
        self.dng_check.setObjectName(u"dng_check")
        self.dng_check.setMinimumSize(QSize(122, 32))
        self.dng_check.setMaximumSize(QSize(122, 32))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.dng_check.setFont(font6)
        self.dng_check.setCursor(QCursor(Qt.PointingHandCursor))
        self.dng_check.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_16.addWidget(self.dng_check)

        self.line_2 = QFrame(self.widget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_2.setLineWidth(5)
        self.line_2.setMidLineWidth(5)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_2)

        self.horizontalSpacer_6 = QSpacerItem(302, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.widget_3)

        self.botones_metadata = QStackedWidget(self.widget)
        self.botones_metadata.setObjectName(u"botones_metadata")
        self.botones_metadata.setMinimumSize(QSize(0, 34))
        self.botones_metadata.setMaximumSize(QSize(16777215, 34))
        self.botones_metadata.setStyleSheet(u"QPushButton#enviarFormButton {\n"
"color: rgb(247,247,247);\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton#enviarFormButton::hover {\n"
"	background-color: rgba(0, 0, 0, .7);\n"
"}")
        self.enviar = QWidget()
        self.enviar.setObjectName(u"enviar")
        self.horizontalLayout_13 = QHBoxLayout(self.enviar)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.enviarFormButton = QPushButton(self.enviar)
        self.enviarFormButton.setObjectName(u"enviarFormButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enviarFormButton.sizePolicy().hasHeightForWidth())
        self.enviarFormButton.setSizePolicy(sizePolicy1)
        self.enviarFormButton.setMinimumSize(QSize(100, 34))
        self.enviarFormButton.setMaximumSize(QSize(100, 34))
        self.enviarFormButton.setFont(font5)
        self.enviarFormButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u"imgs/icons/fast-forward-double-right-arrows.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.enviarFormButton.setIcon(icon14)

        self.horizontalLayout_13.addWidget(self.enviarFormButton)

        self.botones_metadata.addWidget(self.enviar)
        self.editar = QWidget()
        self.editar.setObjectName(u"editar")
        self.horizontalLayout_14 = QHBoxLayout(self.editar)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.enviarFormEditButton = QPushButton(self.editar)
        self.enviarFormEditButton.setObjectName(u"enviarFormEditButton")
        sizePolicy1.setHeightForWidth(self.enviarFormEditButton.sizePolicy().hasHeightForWidth())
        self.enviarFormEditButton.setSizePolicy(sizePolicy1)
        self.enviarFormEditButton.setMinimumSize(QSize(100, 34))
        self.enviarFormEditButton.setMaximumSize(QSize(100, 34))
        self.enviarFormEditButton.setFont(font5)
        self.enviarFormEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u"imgs/icons/pencil-on-a-square-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.enviarFormEditButton.setIcon(icon15)

        self.horizontalLayout_14.addWidget(self.enviarFormEditButton)

        self.botones_metadata.addWidget(self.editar)

        self.verticalLayout.addWidget(self.botones_metadata)


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
        self.horizontalLayout_6.setSpacing(6)
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
        self.titulelementoIDLabel.setFont(font6)
        self.titulelementoIDLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.titulelementoIDLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.titulelementoIDLabel.setPixmap(QPixmap(u"imgs/icons/list-interface-symbol.svg"))
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
        self.titulelementoTituloLabel_2.setFont(font6)
        self.titulelementoTituloLabel_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_2.addWidget(self.titulelementoTituloLabel_2, 0, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_2)

        self.titulelementoTituloLabel = QLabel(self.controlPanel)
        self.titulelementoTituloLabel.setObjectName(u"titulelementoTituloLabel")
        self.titulelementoTituloLabel.setFont(font6)
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
        self.titulelementoTituloLabel_5.setFont(font6)
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
        icon16 = QIcon()
        icon16.addFile(u"imgs/icons/open-black-folder-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openFolderButton.setIcon(icon16)
        self.openFolderButton.setIconSize(QSize(24, 24))

        self.gridLayout_4.addWidget(self.openFolderButton, 0, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.titulelementoTituloLabel_6 = QLabel(self.controlPanel)
        self.titulelementoTituloLabel_6.setObjectName(u"titulelementoTituloLabel_6")
        self.titulelementoTituloLabel_6.setFont(font6)
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

        self.configtitle = QLabel(self.controlPanel)
        self.configtitle.setObjectName(u"configtitle")
        self.configtitle.setFont(font6)

        self.verticalLayout_18.addWidget(self.configtitle)

        self.configLabel = QLabel(self.controlPanel)
        self.configLabel.setObjectName(u"configLabel")
        self.configLabel.setMinimumSize(QSize(190, 90))
        self.configLabel.setMaximumSize(QSize(190, 90))
        self.configLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.configLabel.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.configLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer)


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

        self.statusbar = QFrame(self.layoutEscan)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 20))
        self.statusbar.setStyleSheet(u"")
        self.statusbar.setFrameShape(QFrame.StyledPanel)
        self.statusbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.statusbar)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QLabel(self.statusbar)
        self.statusLabel.setObjectName(u"statusLabel")
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(7)
        self.statusLabel.setFont(font7)
        self.statusLabel.setStyleSheet(u"color: rgba(0, 0, 0, .8);")
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setMargin(4)

        self.horizontalLayout_12.addWidget(self.statusLabel)


        self.verticalLayout_3.addWidget(self.statusbar)

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
        self.finalizarButton = QPushButton(self.captura)
        self.finalizarButton.setObjectName(u"finalizarButton")
        self.finalizarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u"imgs/icons/square-with-verification-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.finalizarButton.setIcon(icon17)
        self.finalizarButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.finalizarButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.capturaButton = QPushButton(self.captura)
        self.capturaButton.setObjectName(u"capturaButton")
        self.capturaButton.setMinimumSize(QSize(120, 35))
        self.capturaButton.setMaximumSize(QSize(16777215, 35))
        font8 = QFont()
        font8.setPointSize(11)
        self.capturaButton.setFont(font8)
        self.capturaButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u"imgs/icons/camera-to-take-photos_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.capturaButton.setIcon(icon18)
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
        self.validateButton.setFont(font8)
        self.validateButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u"imgs/icons/check-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.validateButton.setIcon(icon19)
        self.validateButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.validateButton)

        self.resetButton = QPushButton(self.validar)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(120, 35))
        self.resetButton.setMaximumSize(QSize(16777215, 35))
        self.resetButton.setFont(font8)
        self.resetButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u"imgs/icons/undo-circular-arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetButton.setIcon(icon20)
        self.resetButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.resetButton)

        self.controlesCamstackedWidget.addWidget(self.validar)

        self.horizontalLayout_7.addWidget(self.controlesCamstackedWidget)


        self.verticalLayout_3.addWidget(self.captureControl)


        self.horizontalLayout_5.addWidget(self.layoutEscan)

        self.stackedWidget.addWidget(self.escanerPage)
        self.configurationPage = QWidget()
        self.configurationPage.setObjectName(u"configurationPage")
        self.configtemplate = QWidget(self.configurationPage)
        self.configtemplate.setObjectName(u"configtemplate")
        self.configtemplate.setGeometry(QRect(9, 0, 880, 552))
        self.verticalLayout_33 = QVBoxLayout(self.configtemplate)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.configheader = QWidget(self.configtemplate)
        self.configheader.setObjectName(u"configheader")
        self.horizontalLayout_17 = QHBoxLayout(self.configheader)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.H1metadatosLabel_2 = QLabel(self.configheader)
        self.H1metadatosLabel_2.setObjectName(u"H1metadatosLabel_2")
        self.H1metadatosLabel_2.setFont(font3)

        self.verticalLayout_25.addWidget(self.H1metadatosLabel_2)

        self.label_3 = QLabel(self.configheader)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_3)


        self.horizontalLayout_17.addLayout(self.verticalLayout_25)


        self.verticalLayout_33.addWidget(self.configheader)

        self.configwidget = QWidget(self.configtemplate)
        self.configwidget.setObjectName(u"configwidget")
        self.horizontalLayout_23 = QHBoxLayout(self.configwidget)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.configbaseCams = QWidget(self.configwidget)
        self.configbaseCams.setObjectName(u"configbaseCams")
        self.verticalLayout_26 = QVBoxLayout(self.configbaseCams)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.configbaseCams)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.widget_5.setStyleSheet(u"")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.imagenizqLabel_2 = QLabel(self.widget_5)
        self.imagenizqLabel_2.setObjectName(u"imagenizqLabel_2")
        self.imagenizqLabel_2.setMinimumSize(QSize(320, 366))
        self.imagenizqLabel_2.setMaximumSize(QSize(320, 366))
        font9 = QFont()
        font9.setPointSize(23)
        self.imagenizqLabel_2.setFont(font9)
        self.imagenizqLabel_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.imagenizqLabel_2.setScaledContents(True)
        self.imagenizqLabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.imagenizqLabel_2)

        self.imagederLabel_2 = QLabel(self.widget_5)
        self.imagederLabel_2.setObjectName(u"imagederLabel_2")
        self.imagederLabel_2.setMinimumSize(QSize(320, 366))
        self.imagederLabel_2.setMaximumSize(QSize(320, 366))
        self.imagederLabel_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.imagederLabel_2.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.imagederLabel_2)


        self.verticalLayout_26.addWidget(self.widget_5)

        self.label_4 = QLabel(self.configbaseCams)
        self.label_4.setObjectName(u"label_4")
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setWeight(75)
        self.label_4.setFont(font10)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_4)

        self.widget_6 = QWidget(self.configbaseCams)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.comboBox = QComboBox(self.widget_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 20))
        self.comboBox.setMaximumSize(QSize(100, 20))
        self.comboBox.setFont(font6)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.comboBox)


        self.horizontalLayout_21.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.comboBox_2 = QComboBox(self.widget_8)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(100, 20))
        self.comboBox_2.setMaximumSize(QSize(100, 20))
        self.comboBox_2.setFont(font6)

        self.horizontalLayout_20.addWidget(self.comboBox_2)


        self.horizontalLayout_21.addWidget(self.widget_8)


        self.verticalLayout_26.addWidget(self.widget_6)


        self.horizontalLayout_23.addWidget(self.configbaseCams)

        self.widget_10 = QWidget(self.configwidget)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_32 = QVBoxLayout(self.widget_10)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_9 = QWidget(self.widget_10)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(120, 0))
        self.widget_9.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout_29 = QVBoxLayout(self.widget_9)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.exposicionLabel_2 = QLabel(self.widget_9)
        self.exposicionLabel_2.setObjectName(u"exposicionLabel_2")
        self.exposicionLabel_2.setMinimumSize(QSize(95, 10))
        self.exposicionLabel_2.setMaximumSize(QSize(95, 10))

        self.verticalLayout_27.addWidget(self.exposicionLabel_2)

        self.exposicionValue_2 = QLineEdit(self.widget_9)
        self.exposicionValue_2.setObjectName(u"exposicionValue_2")
        self.exposicionValue_2.setMinimumSize(QSize(95, 34))
        self.exposicionValue_2.setMaximumSize(QSize(95, 34))

        self.verticalLayout_27.addWidget(self.exposicionValue_2)


        self.verticalLayout_29.addLayout(self.verticalLayout_27)

        self.exposicionDial_2 = QDial(self.widget_9)
        self.exposicionDial_2.setObjectName(u"exposicionDial_2")
        self.exposicionDial_2.setMinimumSize(QSize(60, 60))
        self.exposicionDial_2.setMaximumSize(QSize(60, 60))
        self.exposicionDial_2.setMinimum(1)
        self.exposicionDial_2.setMaximum(125)
        self.exposicionDial_2.setValue(25)
        self.exposicionDial_2.setWrapping(True)
        self.exposicionDial_2.setNotchTarget(10.000000000000000)
        self.exposicionDial_2.setNotchesVisible(True)

        self.verticalLayout_29.addWidget(self.exposicionDial_2)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.zoomLabel_2 = QLabel(self.widget_9)
        self.zoomLabel_2.setObjectName(u"zoomLabel_2")
        self.zoomLabel_2.setMinimumSize(QSize(81, 10))
        self.zoomLabel_2.setMaximumSize(QSize(81, 10))
        self.zoomLabel_2.setFont(font5)

        self.verticalLayout_28.addWidget(self.zoomLabel_2)

        self.zoom_valuedit_2 = QLineEdit(self.widget_9)
        self.zoom_valuedit_2.setObjectName(u"zoom_valuedit_2")
        self.zoom_valuedit_2.setMinimumSize(QSize(81, 34))
        self.zoom_valuedit_2.setMaximumSize(QSize(81, 34))

        self.verticalLayout_28.addWidget(self.zoom_valuedit_2)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)

        self.zoom_dial_2 = QDial(self.widget_9)
        self.zoom_dial_2.setObjectName(u"zoom_dial_2")
        self.zoom_dial_2.setMinimumSize(QSize(60, 60))
        self.zoom_dial_2.setMaximumSize(QSize(60, 60))
        self.zoom_dial_2.setMinimum(1)
        self.zoom_dial_2.setMaximum(50)
        self.zoom_dial_2.setSliderPosition(27)
        self.zoom_dial_2.setWrapping(True)
        self.zoom_dial_2.setNotchTarget(5.000000000000000)
        self.zoom_dial_2.setNotchesVisible(True)

        self.verticalLayout_29.addWidget(self.zoom_dial_2)

        self.zoom_dial_2.raise_()
        self.exposicionDial_2.raise_()

        self.verticalLayout_32.addWidget(self.widget_9)

        self.verticalSpacer_4 = QSpacerItem(20, 107, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_4)

        self.testingbuttons = QWidget(self.widget_10)
        self.testingbuttons.setObjectName(u"testingbuttons")
        self.horizontalLayout_22 = QHBoxLayout(self.testingbuttons)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.testconfig = QPushButton(self.testingbuttons)
        self.testconfig.setObjectName(u"testconfig")
        self.testconfig.setMinimumSize(QSize(64, 40))
        self.testconfig.setMaximumSize(QSize(64, 40))
        self.testconfig.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u"imgs/icons/circle-of-arrows-couple.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.testconfig.setIcon(icon21)
        self.testconfig.setIconSize(QSize(32, 32))

        self.verticalLayout_31.addWidget(self.testconfig)

        self.testconfigLabel = QLabel(self.testingbuttons)
        self.testconfigLabel.setObjectName(u"testconfigLabel")
        self.testconfigLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.testconfigLabel)


        self.horizontalLayout_22.addLayout(self.verticalLayout_31)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.saveconfig = QPushButton(self.testingbuttons)
        self.saveconfig.setObjectName(u"saveconfig")
        self.saveconfig.setMinimumSize(QSize(64, 40))
        self.saveconfig.setMaximumSize(QSize(64, 40))
        self.saveconfig.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveconfig.setIcon(icon17)
        self.saveconfig.setIconSize(QSize(32, 32))
        self.saveconfig.setFlat(False)

        self.verticalLayout_30.addWidget(self.saveconfig)

        self.saveconfigLabel = QLabel(self.testingbuttons)
        self.saveconfigLabel.setObjectName(u"saveconfigLabel")
        self.saveconfigLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.saveconfigLabel)


        self.horizontalLayout_22.addLayout(self.verticalLayout_30)


        self.verticalLayout_32.addWidget(self.testingbuttons)


        self.horizontalLayout_23.addWidget(self.widget_10)


        self.verticalLayout_33.addWidget(self.configwidget)

        self.stackedWidget.addWidget(self.configurationPage)

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

        self.stackedWidget.setCurrentIndex(3)
        self.tipoColeccion.setCurrentIndex(0)
        self.botones_metadata.setCurrentIndex(0)
        self.controlesCamstackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeoEscan", None))
        self.neoLabel.setText("")
        self.versionLabel.setText("")
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"[salir]", None))
        self.inicioButton.setText("")
        self.inicioLabel.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.coleccionesButton.setText("")
        self.metadatosLabel.setText(QCoreApplication.translate("MainWindow", u"Metadatos", None))
        self.escanerButton.setText("")
        self.escanerLabel.setText(QCoreApplication.translate("MainWindow", u"Escaner", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
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

        self.tituloLabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo*", None))
        self.titulolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado al expediente", None))
        self.numextLabel.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripcionlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve resumen del tema del expediente", None))
        self.creadorLabel.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.creadorlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Persona o entidad responsable del contenido del expediente", None))
        self.fechaILabel.setText(QCoreApplication.translate("MainWindow", u"Fecha inicial", None))
        self.fechaIlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.fechaFLabel.setText(QCoreApplication.translate("MainWindow", u"Fecha final", None))
        self.fechaFlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.coberturaLabel.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturalineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localidad, ciudad, regi\u00f3n, pa\u00eds, reino", None))
        self.idiomaLabel.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.idiomalineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"por ejemplo: es (para espa\u00f1ol), en (ingl\u00e9s), fr (franc\u00e9s), la (lat\u00edn)", None))
        self.numfolLabel.setText(QCoreApplication.translate("MainWindow", u"N\u00fam. folios/p\u00e1gs.", None))
        self.numfollineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero de folios o p\u00e1ginas", None))
        self.identificadoreslineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.identificadoresLabel.setText(QCoreApplication.translate("MainWindow", u"Identificador*", None))
        self.tituloLabel_3.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo*", None))
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
        self.identificadoresdoclineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.identificadoresLabel_3.setText(QCoreApplication.translate("MainWindow", u"Identificador*", None))
        self.tituloLabel_4.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo*", None))
        self.tituloimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado a la imagen", None))
        self.tituloLabel_5.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.creadorimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Autor, dibujante, pintor", None))
        self.tituloLabel_6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.fechaimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturaespacialimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lugar de producci\u00f3n o representaci\u00f3n de la imagen", None))
        self.tituloLabel_7.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n f\u00edsica", None))
        self.descripcionfisicaimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"tipo, dimensiones", None))
        self.numextLabel_4.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.descripcionimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve descripci\u00f3n de lo representado en la imagen. ", None))
        self.identificadoresLabel_5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.tipoimagenlineEdit.setText("")
        self.tipoimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mapa, dibujo, ilustraci\u00f3n, plano...", None))
        self.identificadoresimagenlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.identificadoresLabel_4.setText(QCoreApplication.translate("MainWindow", u"Identificador*", None))
        self.tituloLabel_8.setText(QCoreApplication.translate("MainWindow", u"Nombre publicaci\u00f3n*", None))
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
        self.identificadoreserlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.identificadoresLabel_7.setText(QCoreApplication.translate("MainWindow", u"Identificador*", None))
        self.tituloLabel_12.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo*", None))
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
        self.identificadoresLibrolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.identificadoresLabel_11.setText(QCoreApplication.translate("MainWindow", u"Identificador*", None))
        self.tituloLabel_18.setText(QCoreApplication.translate("MainWindow", u"Guardar en...", None))
        self.folderlineEdit.setText("")
        self.folderlineEdit.setPlaceholderText("")
        self.nombrearchivolineEdit.setText("")
        self.nombrearchivolineEdit.setPlaceholderText("")
        self.browserDirButton.setText("")
        self.tituloLabel_17.setText(QCoreApplication.translate("MainWindow", u"Nombre del archivo*", None))
        self.zoomLabel.setText(QCoreApplication.translate("MainWindow", u"Nivel de zoom", None))
        self.zoom_valuedit.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.zoom_valuedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"# entre 0 y 50", None))
        self.exposicionLabel.setText(QCoreApplication.translate("MainWindow", u"Nivel de exposici\u00f3n", None))
        self.exposicionValue.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.orientacionLabel.setText(QCoreApplication.translate("MainWindow", u"Orientaci\u00f3n", None))
        self.orientacionValue.setItemText(0, QCoreApplication.translate("MainWindow", u"vertical (portrait)", None))
        self.orientacionValue.setItemText(1, QCoreApplication.translate("MainWindow", u"horizontal (landscape)", None))

        self.dng_check.setText(QCoreApplication.translate("MainWindow", u"Guardar en DNG", None))
        self.enviarFormButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.enviarFormEditButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.titulelementoIDLabel.setText("")
        self.elementoIDLabel.setText("")
        self.titulelementoTituloLabel_2.setText(QCoreApplication.translate("MainWindow", u"Identificador", None))
        self.titulelementoTituloLabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.elementoTituloLabel.setText("")
        self.titulelementoTituloLabel_5.setText(QCoreApplication.translate("MainWindow", u"Directorio im\u00e1genes", None))
        self.directorio_elementos.setText("")
        self.openFolderButton.setText("")
        self.titulelementoTituloLabel_6.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de imgs", None))
        self.cantidadimgsLabel.setText("")
        self.configtitle.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n del proyecto", None))
        self.configLabel.setText("")
        self.imagenizqLabel.setText("")
        self.imagederLabel.setText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Clic en capturar para iniciar", None))
        self.finalizarButton.setText(QCoreApplication.translate("MainWindow", u"Cerrar proyecto", None))
        self.capturaButton.setText(QCoreApplication.translate("MainWindow", u"capturar", None))
#if QT_CONFIG(shortcut)
        self.capturaButton.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.validateButton.setText(QCoreApplication.translate("MainWindow", u"continuar", None))
#if QT_CONFIG(shortcut)
        self.validateButton.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"retomar", None))
#if QT_CONFIG(shortcut)
        self.resetButton.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.H1metadatosLabel_2.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Desde aqu\u00ed configure las caracter\u00edsticas predeterminadas de la aplicaci\u00f3n.", None))
        self.imagenizqLabel_2.setText("")
        self.imagederLabel_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"posici\u00f3n de las c\u00e1maras", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"izquierda", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"derecha", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"derecha", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"izquierda", None))

        self.exposicionLabel_2.setText(QCoreApplication.translate("MainWindow", u"Nivel de exposici\u00f3n", None))
        self.exposicionValue_2.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.zoomLabel_2.setText(QCoreApplication.translate("MainWindow", u"Nivel de zoom", None))
        self.zoom_valuedit_2.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.zoom_valuedit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"# entre 0 y 50", None))
        self.testconfig.setText("")
        self.testconfigLabel.setText(QCoreApplication.translate("MainWindow", u"probar\n"
"configuraci\u00f3n", None))
        self.saveconfig.setText("")
        self.saveconfigLabel.setText(QCoreApplication.translate("MainWindow", u"guardar\n"
"configuraci\u00f3n", None))
        self.c_neogranadina.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><a href=\"https://neogranadina.org/\" target=\"_blank\"><span style=\" font-size:7pt; text-decoration: underline;color:rgba(251,251,251,.8)\">\u00a9 2021 Fundaci\u00f3n Hist\u00f3rica Neogranadina</span></a></body></html>", None))
        self.down_arrow.setText("")
    # retranslateUi

Error: main.ui: Warning: Z-order assignment: 'layoutWidget' is not a valid widget.
main.ui: Warning: Z-order assignment: 'layoutWidget_2' is not a valid widget.

while executing 'e:\proyectos\neogranadina\neo_escan\escan_env\lib\site-packages\PySide2\uic -g python main.ui'
