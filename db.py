# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

import logging
import datetime

from PySide6.QtCore import Qt, Slot, QDir
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel


def connectToDatabase():
    '''
    Conecta a la base de datos a través de la clase QSqlDatabase
    https://doc.qt.io/qt-6/qsqldatabase.html
    '''
    database = QSqlDatabase.database()
    database = QSqlDatabase.addDatabase('QSQLITE')
    if not database.isValid():
        logging.error("No es posible conectarse a la base de datos")

    write_dir = QDir("db")

    if not write_dir.mkpath("."):
        logging.error(f"{datetime.datetime.now()} - No fue posible escribir en el directorio")

    # Garantizar la escritura en cualquier dispositivo
    abs_path = write_dir.absolutePath()
    filename = f"{abs_path}/neo_scan.sqlite3"

    # En SQLite, si no  existe la base de datos, esta es creada
    database.setDatabaseName(filename)
    if not database.open():
        logging.error(f"{datetime.datetime.now()} - No fue posible abrir la base de datos")


