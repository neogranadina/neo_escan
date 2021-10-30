'''
connect pyside2 form with database and sqlite3
and populate the tables of the database
'''

import logging
from pathlib import Path

from PySide2.QtCore import QDir, Qt, Slot
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel


def connectToDatabase():
    '''
    Connect to the database
    '''
    db = QSqlDatabase.addDatabase('QSQLITE')
    if not db.isValid():
        logging.error('No es posible conectarse a la base de datos')
        return False
    write_dir = QDir("db")

    if not write_dir.exists():
        try:
            write_dir.mkpath(".")
        except Exception as e:
            logging.error(e)
            return False

    db.setDatabaseName(str(Path(write_dir.absolutePath(), 'neo_escan.db')))

    if not db.open():
        logging.error('No es posible conectarse a la base de datos')
        return False
    return db


def insertInfoProy(tipoDocDict, user_id):
    '''
    retrieve data from metadataPage forms and insert into database
    '''

    columnas = ', '.join(str(key) for key in tipoDocDict.keys())
    valores = ', '.join(str(value) for value in tipoDocDict.values())
    sql = f"INSERT INTO elements ({columnas}) VALUES ({valores})"
    db = connectToDatabase()
    if not db:
        return False
    query = QSqlQuery()
    query.exec(sql)

    element_id = query.lastInsertId()
    sqluser = f"INSERT INTO projects (user_id, element_id) VALUES ('{user_id}, {element_id}')"
    query.exec(sqluser)

    return True
