# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        palette = QPalette()
        MainWindow.setPalette(palette)
        font = QFont()
        font.setStyleStrategy(QFont.NoAntialias)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"imgs/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#topMenu .QPushButton {\n"
"	border: 1px;\n"
"	color: #2A2F36;\n"
"	font-weight: 600;\n"
"	border-radius: 5%;\n"
"}\n"
"\n"
"#topMenu .QPushButton:hover {\n"
"	color: rgba(242,120,75,.95);\n"
"}\n"
"\n"
"#topMenu .QPushButton:pressed {\n"
"	color: rgba(42, 47, 54, .5);\n"
"}\n"
"\n"
"#crear_coleccion .QLineEdit {background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;}\n"
"\n"
"#crear_coleccion .QComboBox {background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"#crear_coleccion .QPlainTextEdit {background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"#config .QPushButton {\n"
"	background-position: left center;\n"
"  	background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,.7);\n"
"	color: #ffffff;\n"
"	border-radius: 5%;\n"
"}\n"
"#config .QPushButton:hover {\n"
"	background-color: #bf4040;\n"
"}\n"
"\n"
"#config .QPushButton:pressed {\n"
"	background-color: rgb(255"
                        ", 255, 255);\n"
"	color: #000000;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topMenu = QFrame(self.centralwidget)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"border: none;")
        self.topMenu.setFrameShape(QFrame.StyledPanel)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.topMenu.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.topMenu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.label = QLabel(self.topMenu)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.homeButton = QPushButton(self.topMenu)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.homeButton)

        self.coleccionesButton = QPushButton(self.topMenu)
        self.coleccionesButton.setObjectName(u"coleccionesButton")

        self.horizontalLayout_2.addWidget(self.coleccionesButton)

        self.configButton = QPushButton(self.topMenu)
        self.configButton.setObjectName(u"configButton")
        self.configButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.configButton)


        self.verticalLayout.addWidget(self.topMenu)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setCursor(QCursor(Qt.ArrowCursor))
        self.home.setStyleSheet(u"border-radius: 5%;")
        self.pages.addWidget(self.home)
        self.crear_coleccion = QWidget()
        self.crear_coleccion.setObjectName(u"crear_coleccion")
        self.colecciones_frame = QFrame(self.crear_coleccion)
        self.colecciones_frame.setObjectName(u"colecciones_frame")
        self.colecciones_frame.setGeometry(QRect(0, 0, 981, 37))
        self.colecciones_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.colecciones_frame.setFrameShape(QFrame.StyledPanel)
        self.colecciones_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.colecciones_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.colecciones_label = QLabel(self.colecciones_frame)
        self.colecciones_label.setObjectName(u"colecciones_label")
        self.colecciones_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(243, 243, 243);")

        self.horizontalLayout_5.addWidget(self.colecciones_label)

        self.infocoleccion_label = QLabel(self.crear_coleccion)
        self.infocoleccion_label.setObjectName(u"infocoleccion_label")
        self.infocoleccion_label.setGeometry(QRect(770, 40, 201, 451))
        self.infocoleccion_label.setCursor(QCursor(Qt.IBeamCursor))
        self.infocoleccion_label.setTextFormat(Qt.RichText)
        self.infocoleccion_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.infocoleccion_label.setWordWrap(True)
        self.infocoleccion_label.setMargin(5)
        self.infocoleccion_label.setOpenExternalLinks(True)
        self.infocoleccion_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.widget = QWidget(self.crear_coleccion)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 40, 751, 451))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contrasena_label_2 = QLabel(self.widget)
        self.contrasena_label_2.setObjectName(u"contrasena_label_2")

        self.gridLayout.addWidget(self.contrasena_label_2, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.contrasena_label_4 = QLabel(self.widget)
        self.contrasena_label_4.setObjectName(u"contrasena_label_4")

        self.gridLayout.addWidget(self.contrasena_label_4, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.contrasena_label_5 = QLabel(self.widget)
        self.contrasena_label_5.setObjectName(u"contrasena_label_5")

        self.gridLayout.addWidget(self.contrasena_label_5, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.contrasena_label_6 = QLabel(self.widget)
        self.contrasena_label_6.setObjectName(u"contrasena_label_6")

        self.gridLayout.addWidget(self.contrasena_label_6, 3, 0, 1, 1)

        self.descripcion_text = QPlainTextEdit(self.widget)
        self.descripcion_text.setObjectName(u"descripcion_text")
        self.descripcion_text.setMinimumSize(QSize(250, 80))

        self.gridLayout.addWidget(self.descripcion_text, 3, 1, 1, 1)

        self.contrasena_label_7 = QLabel(self.widget)
        self.contrasena_label_7.setObjectName(u"contrasena_label_7")

        self.gridLayout.addWidget(self.contrasena_label_7, 4, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.contrasena_label_8 = QLabel(self.widget)
        self.contrasena_label_8.setObjectName(u"contrasena_label_8")

        self.gridLayout.addWidget(self.contrasena_label_8, 5, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.contrasena_label_9 = QLabel(self.widget)
        self.contrasena_label_9.setObjectName(u"contrasena_label_9")

        self.gridLayout.addWidget(self.contrasena_label_9, 6, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_6, 6, 1, 1, 1)

        self.contrasena_label_10 = QLabel(self.widget)
        self.contrasena_label_10.setObjectName(u"contrasena_label_10")

        self.gridLayout.addWidget(self.contrasena_label_10, 7, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_7, 7, 1, 1, 1)

        self.contrasena_label_11 = QLabel(self.widget)
        self.contrasena_label_11.setObjectName(u"contrasena_label_11")

        self.gridLayout.addWidget(self.contrasena_label_11, 8, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_8, 8, 1, 1, 1)

        self.contrasena_label_12 = QLabel(self.widget)
        self.contrasena_label_12.setObjectName(u"contrasena_label_12")

        self.gridLayout.addWidget(self.contrasena_label_12, 9, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_9, 9, 1, 1, 1)

        self.contrasena_label_13 = QLabel(self.widget)
        self.contrasena_label_13.setObjectName(u"contrasena_label_13")

        self.gridLayout.addWidget(self.contrasena_label_13, 10, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit_10, 10, 1, 1, 1)

        self.contrasena_label_3 = QLabel(self.widget)
        self.contrasena_label_3.setObjectName(u"contrasena_label_3")

        self.gridLayout.addWidget(self.contrasena_label_3, 11, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(250, 20))

        self.gridLayout.addWidget(self.lineEdit, 11, 1, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton, 11, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_2, 12, 1, 1, 1)

        self.pages.addWidget(self.crear_coleccion)
        self.p3 = QWidget()
        self.p3.setObjectName(u"p3")
        self.pages.addWidget(self.p3)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.frame = QFrame(self.config)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 981, 37))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.config_label = QLabel(self.frame)
        self.config_label.setObjectName(u"config_label")
        self.config_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(243, 243, 243);")

        self.horizontalLayout_3.addWidget(self.config_label)

        self.configSendButton = QPushButton(self.config)
        self.configSendButton.setObjectName(u"configSendButton")
        self.configSendButton.setGeometry(QRect(480, 280, 80, 30))
        self.configSendButton.setMinimumSize(QSize(80, 30))
        self.configSendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.configSendButton.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.config)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 50, 971, 209))
        self.configuracion_layout = QHBoxLayout(self.layoutWidget)
        self.configuracion_layout.setSpacing(20)
        self.configuracion_layout.setObjectName(u"configuracion_layout")
        self.configuracion_layout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.hostname_label = QLabel(self.layoutWidget)
        self.hostname_label.setObjectName(u"hostname_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.hostname_label)

        self.host_line = QLineEdit(self.layoutWidget)
        self.host_line.setObjectName(u"host_line")
        self.host_line.setMinimumSize(QSize(200, 25))
        self.host_line.setStyleSheet(u"background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.host_line)

        self.usuario_label = QLabel(self.layoutWidget)
        self.usuario_label.setObjectName(u"usuario_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.usuario_label)

        self.usuario_line = QLineEdit(self.layoutWidget)
        self.usuario_line.setObjectName(u"usuario_line")
        self.usuario_line.setMinimumSize(QSize(200, 25))
        self.usuario_line.setStyleSheet(u"background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usuario_line)

        self.contrasena_label = QLabel(self.layoutWidget)
        self.contrasena_label.setObjectName(u"contrasena_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.contrasena_label)

        self.contrasena_line = QLineEdit(self.layoutWidget)
        self.contrasena_line.setObjectName(u"contrasena_line")
        self.contrasena_line.setMinimumSize(QSize(200, 25))
        self.contrasena_line.setStyleSheet(u"background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.contrasena_line)

        self.dbname_label = QLabel(self.layoutWidget)
        self.dbname_label.setObjectName(u"dbname_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.dbname_label)

        self.dbname_line = QLineEdit(self.layoutWidget)
        self.dbname_line.setObjectName(u"dbname_line")
        self.dbname_line.setMinimumSize(QSize(200, 25))
        self.dbname_line.setStyleSheet(u"background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dbname_line)

        self.tipoDB_label = QLabel(self.layoutWidget)
        self.tipoDB_label.setObjectName(u"tipoDB_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.tipoDB_label)

        self.tipoDB_cbox = QComboBox(self.layoutWidget)
        self.tipoDB_cbox.addItem("")
        self.tipoDB_cbox.addItem("")
        self.tipoDB_cbox.addItem("")
        self.tipoDB_cbox.addItem("")
        self.tipoDB_cbox.setObjectName(u"tipoDB_cbox")
        self.tipoDB_cbox.setMinimumSize(QSize(200, 25))
        self.tipoDB_cbox.setStyleSheet(u"background-color: rgb(243, 243, 243);\n"
"border-radius: 3px;")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.tipoDB_cbox)


        self.configuracion_layout.addLayout(self.formLayout)

        self.tipo_db = QLabel(self.layoutWidget)
        self.tipo_db.setObjectName(u"tipo_db")
        self.tipo_db.setMinimumSize(QSize(400, 0))
        self.tipo_db.setCursor(QCursor(Qt.IBeamCursor))
        self.tipo_db.setStyleSheet(u"background-color: rgba(255, 255, 255, .6);\n"
"font-family: \"Gill Sans Extrabold\", Helvetica, sans-serif;\n"
"border-radius: 10%;")
        self.tipo_db.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tipo_db.setWordWrap(False)
        self.tipo_db.setMargin(10)
        self.tipo_db.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.configuracion_layout.addWidget(self.tipo_db)

        self.pages.addWidget(self.config)
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.configSendButton.raise_()

        self.verticalLayout.addWidget(self.pages)

        self.foot = QFrame(self.centralwidget)
        self.foot.setObjectName(u"foot")
        self.foot.setStyleSheet(u"background-color: rgba(0, 0, 0,.2);")
        self.foot.setFrameShape(QFrame.StyledPanel)
        self.foot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.foot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.c_neogranadina = QLabel(self.foot)
        self.c_neogranadina.setObjectName(u"c_neogranadina")
        self.c_neogranadina.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.c_neogranadina)


        self.verticalLayout.addWidget(self.foot)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeoEscan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/logo_head\" height=\"50\"/></p></body></html>", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.coleccionesButton.setText(QCoreApplication.translate("MainWindow", u"Colecciones", None))
        self.configButton.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.colecciones_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Administrar colecciones</span></h3></body></html>", None))
        self.infocoleccion_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700; color:rgba(0,0,0,.8);\">Colecci\u00f3n</span></h3><p><span style=\" font-style:italic; color:rgba(0,0,0,.8);\">Un conjunto de documentos, libros, publicaciones seriadas o especiales (p. ej.: raros y manuscritos)</span></p></body></html>", None))
        self.contrasena_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Tipo de proyecto</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Colecci\u00f3n documental", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Colecci\u00f3n bibliogr\u00e1fica", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Peri\u00f3dicos y publicaciones seriadas", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Manuscritos", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Mapas", None))
        self.comboBox.setItemText(5, "")

        self.contrasena_label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Identificador</span></p></body></html>", None))
        self.contrasena_label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">T\u00edtulo</span></p></body></html>", None))
        self.contrasena_label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Descripci\u00f3n</span></p></body></html>", None))
        self.contrasena_label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Tama\u00f1o</span></p></body></html>", None))
        self.contrasena_label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Idioma</span></p></body></html>", None))
        self.contrasena_label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Formato</span></p></body></html>", None))
        self.contrasena_label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Derechos</span></p></body></html>", None))
        self.contrasena_label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Fecha</span></p></body></html>", None))
        self.contrasena_label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Instituci\u00f3n</span></p></body></html>", None))
        self.contrasena_label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Titular de los derechos</span></p></body></html>", None))
        self.contrasena_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Directorio del proyecto</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"buscar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"crear proyecto", None))
        self.config_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700; color:rgba(255,255,255,0.8);\">Configuraci\u00f3n de la base de datos</span></h3></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.configSendButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"Enviar la informaci\u00f3n de configuraci\u00f3n de la base de datos", None))
#endif // QT_CONFIG(whatsthis)
        self.configSendButton.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.hostname_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Hostname</span></p></body></html>", None))
        self.host_line.setText("")
        self.host_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.usuario_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Usuario</span></p></body></html>", None))
        self.usuario_line.setText("")
        self.usuario_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nombre de usuario", None))
        self.contrasena_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Contrase\u00f1a</span></p></body></html>", None))
        self.contrasena_line.setText("")
        self.contrasena_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contrase\u00f1a de la base de datos", None))
        self.dbname_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Base de datos</span></p></body></html>", None))
        self.dbname_line.setText("")
        self.dbname_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nombre de la base de datos", None))
        self.tipoDB_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;color:rgba(0,0,0,.8)\">Tipo de base de datos</span></p></body></html>", None))
        self.tipoDB_cbox.setItemText(0, QCoreApplication.translate("MainWindow", u"SQLite3", None))
        self.tipoDB_cbox.setItemText(1, QCoreApplication.translate("MainWindow", u"MariaDB", None))
        self.tipoDB_cbox.setItemText(2, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.tipoDB_cbox.setItemText(3, QCoreApplication.translate("MainWindow", u"PostgreSQL", None))

        self.tipo_db.setText(QCoreApplication.translate("MainWindow", u"placeholder", None))
        self.c_neogranadina.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">\u00a9 2021 Fundaci\u00f3n Hist\u00f3rica Neogranadina</span></p></body></html>", None))
    # retranslateUi

