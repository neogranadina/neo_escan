# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSlhlaC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

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
        self.versionLabel.setStyleSheet(u"padding-right: 10px;")
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
        self.label = QLabel(self.inicioPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 49, 16))
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
        self.headerMetadatos.setMinimumSize(QSize(0, 30))
        self.headerMetadatos.setStyleSheet(u"")
        self.headerMetadatos.setFrameShape(QFrame.StyledPanel)
        self.headerMetadatos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.headerMetadatos)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.H1metadatosLabel = QLabel(self.headerMetadatos)
        self.H1metadatosLabel.setObjectName(u"H1metadatosLabel")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.H1metadatosLabel.setFont(font1)

        self.horizontalLayout_9.addWidget(self.H1metadatosLabel)


        self.verticalLayout.addWidget(self.headerMetadatos)

        self.formChanger = QWidget(self.widget)
        self.formChanger.setObjectName(u"formChanger")
        self.formChanger.setMinimumSize(QSize(0, 30))
        self.formChanger.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.formChanger)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tipodocLabel = QLabel(self.formChanger)
        self.tipodocLabel.setObjectName(u"tipodocLabel")
        self.tipodocLabel.setMinimumSize(QSize(120, 0))
        self.tipodocLabel.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.tipodocLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.tipodocLabel)

        self.tipodocComboBox = QComboBox(self.formChanger)
        icon1 = QIcon()
        icon1.addFile(u":/imgs/imgs/icons/folder-check-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/imgs/imgs/icons/documents-rounded-square-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/imgs/imgs/icons/image-interface-symbol-with-a-landscape.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/imgs/imgs/icons/news-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/imgs/imgs/icons/open-book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/imgs/imgs/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tipodocComboBox.addItem(icon6, "")
        self.tipodocComboBox.setObjectName(u"tipodocComboBox")
        self.tipodocComboBox.setMinimumSize(QSize(300, 34))
        self.tipodocComboBox.setMaximumSize(QSize(300, 34))
        self.tipodocComboBox.setFont(font2)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 660, 468))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.tituloLabel = QLabel(self.scrollAreaWidgetContents)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.tituloLabel)

        self.titulolineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.titulolineEdit.setObjectName(u"titulolineEdit")
        self.titulolineEdit.setMinimumSize(QSize(500, 34))
        self.titulolineEdit.setMaximumSize(QSize(500, 34))
        self.titulolineEdit.setFont(font2)
        self.titulolineEdit.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titulolineEdit)

        self.numextLabel = QLabel(self.scrollAreaWidgetContents)
        self.numextLabel.setObjectName(u"numextLabel")
        self.numextLabel.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.numextLabel)

        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QSize(500, 70))
        self.plainTextEdit.setMaximumSize(QSize(500, 250))
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setStyleSheet(u"Breve resumen del tema del expediente")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit)

        self.creadorlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.creadorlineEdit.setObjectName(u"creadorlineEdit")
        self.creadorlineEdit.setMinimumSize(QSize(500, 34))
        self.creadorlineEdit.setMaximumSize(QSize(500, 34))
        self.creadorlineEdit.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.creadorlineEdit)

        self.fechaILabel = QLabel(self.scrollAreaWidgetContents)
        self.fechaILabel.setObjectName(u"fechaILabel")
        self.fechaILabel.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.fechaILabel)

        self.fechaIlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fechaIlineEdit.setObjectName(u"fechaIlineEdit")
        self.fechaIlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaIlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaIlineEdit.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.fechaIlineEdit)

        self.fechaFLabel = QLabel(self.scrollAreaWidgetContents)
        self.fechaFLabel.setObjectName(u"fechaFLabel")
        self.fechaFLabel.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.fechaFLabel)

        self.fechaFlineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fechaFlineEdit.setObjectName(u"fechaFlineEdit")
        self.fechaFlineEdit.setMinimumSize(QSize(500, 34))
        self.fechaFlineEdit.setMaximumSize(QSize(500, 34))
        self.fechaFlineEdit.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.fechaFlineEdit)

        self.idiomaLabel = QLabel(self.scrollAreaWidgetContents)
        self.idiomaLabel.setObjectName(u"idiomaLabel")
        self.idiomaLabel.setFont(font2)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.idiomaLabel)

        self.idiomalineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.idiomalineEdit.setObjectName(u"idiomalineEdit")
        self.idiomalineEdit.setMinimumSize(QSize(500, 34))
        self.idiomalineEdit.setMaximumSize(QSize(500, 34))
        self.idiomalineEdit.setFont(font2)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.idiomalineEdit)

        self.numfolLabel = QLabel(self.scrollAreaWidgetContents)
        self.numfolLabel.setObjectName(u"numfolLabel")
        self.numfolLabel.setFont(font2)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.numfolLabel)

        self.numfollineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.numfollineEdit.setObjectName(u"numfollineEdit")
        self.numfollineEdit.setMinimumSize(QSize(500, 34))
        self.numfollineEdit.setMaximumSize(QSize(500, 34))
        self.numfollineEdit.setFont(font2)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.numfollineEdit)

        self.identificadoresLabel = QLabel(self.scrollAreaWidgetContents)
        self.identificadoresLabel.setObjectName(u"identificadoresLabel")
        self.identificadoresLabel.setFont(font2)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.identificadoresLabel)

        self.identificadoreslineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.identificadoreslineEdit.setObjectName(u"identificadoreslineEdit")
        self.identificadoreslineEdit.setMinimumSize(QSize(500, 34))
        self.identificadoreslineEdit.setMaximumSize(QSize(500, 34))
        self.identificadoreslineEdit.setFont(font2)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.identificadoreslineEdit)

        self.enviarFormButton = QPushButton(self.scrollAreaWidgetContents)
        self.enviarFormButton.setObjectName(u"enviarFormButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enviarFormButton.sizePolicy().hasHeightForWidth())
        self.enviarFormButton.setSizePolicy(sizePolicy1)
        self.enviarFormButton.setMinimumSize(QSize(100, 34))
        self.enviarFormButton.setMaximumSize(QSize(100, 34))
        self.enviarFormButton.setFont(font2)
        self.enviarFormButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/imgs/imgs/icons/fast-forward-double-right-arrows.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.enviarFormButton.setIcon(icon7)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.enviarFormButton)

        self.creadorLabel = QLabel(self.scrollAreaWidgetContents)
        self.creadorLabel.setObjectName(u"creadorLabel")
        self.creadorLabel.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.creadorLabel)

        self.coberturaLabel = QLabel(self.scrollAreaWidgetContents)
        self.coberturaLabel.setObjectName(u"coberturaLabel")
        self.coberturaLabel.setFont(font2)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.coberturaLabel)

        self.coberturalineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.coberturalineEdit.setObjectName(u"coberturalineEdit")
        self.coberturalineEdit.setMinimumSize(QSize(500, 34))
        self.coberturalineEdit.setMaximumSize(QSize(500, 34))
        self.coberturalineEdit.setFont(font2)

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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 660, 450))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.tituloLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.tituloLabel_3.setObjectName(u"tituloLabel_3")
        self.tituloLabel_3.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.tituloLabel_3)

        self.titulolineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.titulolineEdit_3.setObjectName(u"titulolineEdit_3")
        self.titulolineEdit_3.setMinimumSize(QSize(500, 34))
        self.titulolineEdit_3.setMaximumSize(QSize(500, 34))
        self.titulolineEdit_3.setFont(font2)
        self.titulolineEdit_3.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.titulolineEdit_3)

        self.numextLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.numextLabel_3.setObjectName(u"numextLabel_3")
        self.numextLabel_3.setFont(font2)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.numextLabel_3)

        self.plainTextEdit_3 = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        sizePolicy.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy)
        self.plainTextEdit_3.setMinimumSize(QSize(500, 70))
        self.plainTextEdit_3.setMaximumSize(QSize(500, 250))
        self.plainTextEdit_3.setFont(font2)
        self.plainTextEdit_3.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.plainTextEdit_3)

        self.creadorLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.creadorLabel_3.setObjectName(u"creadorLabel_3")
        self.creadorLabel_3.setFont(font2)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.creadorLabel_3)

        self.creadorlineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.creadorlineEdit_3.setObjectName(u"creadorlineEdit_3")
        self.creadorlineEdit_3.setMinimumSize(QSize(500, 34))
        self.creadorlineEdit_3.setMaximumSize(QSize(500, 34))
        self.creadorlineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.creadorlineEdit_3)

        self.fechaILabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.fechaILabel_3.setObjectName(u"fechaILabel_3")
        self.fechaILabel_3.setFont(font2)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.fechaILabel_3)

        self.fechaIlineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.fechaIlineEdit_3.setObjectName(u"fechaIlineEdit_3")
        self.fechaIlineEdit_3.setMinimumSize(QSize(500, 34))
        self.fechaIlineEdit_3.setMaximumSize(QSize(500, 34))
        self.fechaIlineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.fechaIlineEdit_3)

        self.fechaFLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.fechaFLabel_3.setObjectName(u"fechaFLabel_3")
        self.fechaFLabel_3.setFont(font2)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.fechaFLabel_3)

        self.fechaFlineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.fechaFlineEdit_3.setObjectName(u"fechaFlineEdit_3")
        self.fechaFlineEdit_3.setMinimumSize(QSize(500, 34))
        self.fechaFlineEdit_3.setMaximumSize(QSize(500, 34))
        self.fechaFlineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.fechaFlineEdit_3)

        self.coberturaLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.coberturaLabel_3.setObjectName(u"coberturaLabel_3")
        self.coberturaLabel_3.setFont(font2)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.coberturaLabel_3)

        self.coberturalineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.coberturalineEdit_3.setObjectName(u"coberturalineEdit_3")
        self.coberturalineEdit_3.setMinimumSize(QSize(500, 34))
        self.coberturalineEdit_3.setMaximumSize(QSize(500, 34))
        self.coberturalineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.coberturalineEdit_3)

        self.idiomaLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.idiomaLabel_3.setObjectName(u"idiomaLabel_3")
        self.idiomaLabel_3.setFont(font2)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.idiomaLabel_3)

        self.idiomalineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.idiomalineEdit_3.setObjectName(u"idiomalineEdit_3")
        self.idiomalineEdit_3.setMinimumSize(QSize(500, 34))
        self.idiomalineEdit_3.setMaximumSize(QSize(500, 34))
        self.idiomalineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.idiomalineEdit_3)

        self.numfolLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.numfolLabel_3.setObjectName(u"numfolLabel_3")
        self.numfolLabel_3.setFont(font2)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.numfolLabel_3)

        self.numfollineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.numfollineEdit_3.setObjectName(u"numfollineEdit_3")
        self.numfollineEdit_3.setMinimumSize(QSize(500, 34))
        self.numfollineEdit_3.setMaximumSize(QSize(500, 34))
        self.numfollineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.numfollineEdit_3)

        self.identificadoresLabel_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.identificadoresLabel_3.setObjectName(u"identificadoresLabel_3")
        self.identificadoresLabel_3.setFont(font2)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.identificadoresLabel_3)

        self.identificadoreslineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.identificadoreslineEdit_3.setObjectName(u"identificadoreslineEdit_3")
        self.identificadoreslineEdit_3.setMinimumSize(QSize(500, 34))
        self.identificadoreslineEdit_3.setMaximumSize(QSize(500, 34))
        self.identificadoreslineEdit_3.setFont(font2)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.identificadoreslineEdit_3)

        self.enviarFormButton_3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.enviarFormButton_3.setObjectName(u"enviarFormButton_3")
        sizePolicy1.setHeightForWidth(self.enviarFormButton_3.sizePolicy().hasHeightForWidth())
        self.enviarFormButton_3.setSizePolicy(sizePolicy1)
        self.enviarFormButton_3.setMinimumSize(QSize(100, 34))
        self.enviarFormButton_3.setMaximumSize(QSize(100, 34))
        self.enviarFormButton_3.setFont(font2)
        self.enviarFormButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormButton_3.setIcon(icon7)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.enviarFormButton_3)


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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 660, 410))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.tituloLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_4.setObjectName(u"tituloLabel_4")
        self.tituloLabel_4.setFont(font2)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.tituloLabel_4)

        self.titulolineEdit_4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.titulolineEdit_4.setObjectName(u"titulolineEdit_4")
        self.titulolineEdit_4.setMinimumSize(QSize(500, 34))
        self.titulolineEdit_4.setMaximumSize(QSize(500, 34))
        self.titulolineEdit_4.setFont(font2)
        self.titulolineEdit_4.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.titulolineEdit_4)

        self.tituloLabel_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_5.setObjectName(u"tituloLabel_5")
        self.tituloLabel_5.setFont(font2)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.tituloLabel_5)

        self.titulolineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.titulolineEdit_5.setObjectName(u"titulolineEdit_5")
        self.titulolineEdit_5.setMinimumSize(QSize(500, 34))
        self.titulolineEdit_5.setMaximumSize(QSize(500, 34))
        self.titulolineEdit_5.setFont(font2)
        self.titulolineEdit_5.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.titulolineEdit_5)

        self.tituloLabel_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_6.setObjectName(u"tituloLabel_6")
        self.tituloLabel_6.setFont(font2)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.tituloLabel_6)

        self.titulolineEdit_6 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.titulolineEdit_6.setObjectName(u"titulolineEdit_6")
        self.titulolineEdit_6.setMinimumSize(QSize(500, 34))
        self.titulolineEdit_6.setMaximumSize(QSize(500, 34))
        self.titulolineEdit_6.setFont(font2)
        self.titulolineEdit_6.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.titulolineEdit_6)

        self.tituloLabel_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.tituloLabel_7.setObjectName(u"tituloLabel_7")
        self.tituloLabel_7.setFont(font2)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.tituloLabel_7)

        self.titulolineEdit_7 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.titulolineEdit_7.setObjectName(u"titulolineEdit_7")
        self.titulolineEdit_7.setMinimumSize(QSize(500, 34))
        self.titulolineEdit_7.setMaximumSize(QSize(500, 34))
        self.titulolineEdit_7.setFont(font2)
        self.titulolineEdit_7.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.titulolineEdit_7)

        self.numextLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.numextLabel_4.setObjectName(u"numextLabel_4")
        self.numextLabel_4.setFont(font2)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.numextLabel_4)

        self.plainTextEdit_4 = QPlainTextEdit(self.scrollAreaWidgetContents_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        sizePolicy.setHeightForWidth(self.plainTextEdit_4.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_4.setSizePolicy(sizePolicy)
        self.plainTextEdit_4.setMinimumSize(QSize(500, 70))
        self.plainTextEdit_4.setMaximumSize(QSize(500, 250))
        self.plainTextEdit_4.setFont(font2)
        self.plainTextEdit_4.setStyleSheet(u"Breve resumen del tema del documento")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.plainTextEdit_4)

        self.identificadoresLabel_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.identificadoresLabel_5.setObjectName(u"identificadoresLabel_5")
        self.identificadoresLabel_5.setFont(font2)

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.identificadoresLabel_5)

        self.identificadoreslineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.identificadoreslineEdit_5.setObjectName(u"identificadoreslineEdit_5")
        self.identificadoreslineEdit_5.setMinimumSize(QSize(500, 34))
        self.identificadoreslineEdit_5.setMaximumSize(QSize(500, 34))
        self.identificadoreslineEdit_5.setFont(font2)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.identificadoreslineEdit_5)

        self.identificadoresLabel_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.identificadoresLabel_4.setObjectName(u"identificadoresLabel_4")
        self.identificadoresLabel_4.setFont(font2)

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.identificadoresLabel_4)

        self.identificadoreslineEdit_4 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.identificadoreslineEdit_4.setObjectName(u"identificadoreslineEdit_4")
        self.identificadoreslineEdit_4.setMinimumSize(QSize(500, 34))
        self.identificadoreslineEdit_4.setMaximumSize(QSize(500, 34))
        self.identificadoreslineEdit_4.setFont(font2)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.identificadoreslineEdit_4)

        self.enviarFormButton_4 = QPushButton(self.scrollAreaWidgetContents_4)
        self.enviarFormButton_4.setObjectName(u"enviarFormButton_4")
        sizePolicy1.setHeightForWidth(self.enviarFormButton_4.sizePolicy().hasHeightForWidth())
        self.enviarFormButton_4.setSizePolicy(sizePolicy1)
        self.enviarFormButton_4.setMinimumSize(QSize(100, 34))
        self.enviarFormButton_4.setMaximumSize(QSize(100, 34))
        self.enviarFormButton_4.setFont(font2)
        self.enviarFormButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarFormButton_4.setIcon(icon7)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.enviarFormButton_4)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(500, 34))
        self.lineEdit.setMaximumSize(QSize(500, 34))
        self.lineEdit.setFont(font2)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit)


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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 677, 306))
        self.label_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 60, 181, 91))
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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 677, 306))
        self.label_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 50, 231, 121))
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
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 677, 306))
        self.label_5 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 50, 251, 131))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_14.addWidget(self.scrollArea_6)

        self.tipoColeccion.addWidget(self.formSimple)

        self.verticalLayout.addWidget(self.tipoColeccion)


        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.metadataPage)
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
        self.proyectData = QLabel(self.controlPanel)
        self.proyectData.setObjectName(u"proyectData")
        self.proyectData.setGeometry(QRect(10, 50, 151, 161))
        self.proyectData.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.controlPanel)

        self.layoutEscan = QWidget(self.escanerPage)
        self.layoutEscan.setObjectName(u"layoutEscan")
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
        font3 = QFont()
        font3.setPointSize(11)
        self.capturaButton.setFont(font3)
        self.capturaButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/imgs/imgs/icons/camera-to-take-photos_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.capturaButton.setIcon(icon8)
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

        self.stackedWidget.setCurrentIndex(1)
        self.tipoColeccion.setCurrentIndex(2)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.H1metadatosLabel.setText(QCoreApplication.translate("MainWindow", u"Metadatos", None))
        self.tipodocLabel.setText(QCoreApplication.translate("MainWindow", u"Tipo de documento", None))
        self.tipodocComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Legajo (unidad documental compuesta)", None))
        self.tipodocComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Documento (unidad documental simple)", None))
        self.tipodocComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Imagen (dibujo, plano, mapa, pintura)", None))
        self.tipodocComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Peri\u00f3dico / revista (publicaci\u00f3n seriada)", None))
        self.tipodocComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Libro (encuadernados)", None))
        self.tipodocComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sin tipo (captura simple)", None))

        self.tituloLabel.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.titulolineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado al expediente", None))
        self.numextLabel.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve resumen del tema del expediente", None))
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
        self.enviarFormButton.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.creadorLabel.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.coberturaLabel.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturalineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localidad, ciudad, regi\u00f3n, pa\u00eds, reino", None))
        self.tituloLabel_3.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.titulolineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado al documento", None))
        self.numextLabel_3.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve resumen del tema del expediente", None))
        self.creadorLabel_3.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.creadorlineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Persona o entidad responsable del contenido del documento", None))
        self.fechaILabel_3.setText(QCoreApplication.translate("MainWindow", u"Fecha inicial", None))
        self.fechaIlineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.fechaFLabel_3.setText(QCoreApplication.translate("MainWindow", u"Fecha final", None))
        self.fechaFlineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.coberturaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.coberturalineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localidad, ciudad, regi\u00f3n, pa\u00eds, reino", None))
        self.idiomaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.idiomalineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"por ejemplo: es (para espa\u00f1ol), en (ingl\u00e9s), fr (franc\u00e9s), la (lat\u00edn)", None))
        self.numfolLabel_3.setText(QCoreApplication.translate("MainWindow", u"N\u00fam. folios/p\u00e1gs.", None))
        self.numfollineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"n\u00famero de folios o p\u00e1ginas", None))
        self.identificadoresLabel_3.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoreslineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormButton_3.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.tituloLabel_4.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.titulolineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"El nombre dado a la imagen", None))
        self.tituloLabel_5.setText(QCoreApplication.translate("MainWindow", u"Creador", None))
        self.titulolineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Autor, dibujante, pintor", None))
        self.tituloLabel_6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.titulolineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AAAA-MM-DD", None))
        self.tituloLabel_7.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n f\u00edsica", None))
        self.titulolineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"tipo, dimensiones", None))
        self.numextLabel_4.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Breve descripci\u00f3n de lo representado en la imagen. ", None))
        self.identificadoresLabel_5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.identificadoreslineEdit_5.setText("")
        self.identificadoreslineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mapa, dibujo, ilustraci\u00f3n, plano...", None))
        self.identificadoresLabel_4.setText(QCoreApplication.translate("MainWindow", u"Identificadores", None))
        self.identificadoreslineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"referencia, \u00edndice, n\u00famero de catalogaci\u00f3n...", None))
        self.enviarFormButton_4.setText(QCoreApplication.translate("MainWindow", u"enviar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cobertura espacial", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lugar de producci\u00f3n o representaci\u00f3n de la imagen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EN PROCESO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EN PROCESO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EN PROCESO", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.proyectData.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.capturaButton.setText(QCoreApplication.translate("MainWindow", u"capturar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IM\u00c1GENES", None))
        self.c_neogranadina.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><a href=\"https://neogranadina.org/\" target=\"_blank\"><span style=\" font-size:7pt; text-decoration: underline;color:rgba(251,251,251,.8)\">\u00a9 2021 Fundaci\u00f3n Hist\u00f3rica Neogranadina</span></a></body></html>", None))
        self.down_arrow.setText("")
    # retranslateUi

