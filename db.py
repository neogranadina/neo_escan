# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# db:
# módulo para comunicar PySide2 con la base de datos sqlite3
#
# ///////////////////////////////////////////////////////////////

import datetime
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


def createElement(tipo_elemento, usuario, publico):
    '''
    Create new item in elements table
    '''
    now = datetime.datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")

    query = QSqlQuery()
    query.prepare("INSERT INTO elements (document_type, user_id, public, created_ts, modified_ts) VALUES (:doctype, :user, :public, :created_at, :updated_at)")
    query.bindValue(':doctype', tipo_elemento)
    query.bindValue(':user', usuario)
    query.bindValue(':public', publico)
    query.bindValue(':created_at', ts)
    query.bindValue(':updated_at', ts)

    if not query.exec_():
        logging.error(query.lastError().text())
        return False


def getLastId():
    '''
    Get last id from elements table
    '''
    query = QSqlQuery()
    query.prepare("SELECT last_insert_rowid()")
    query.exec_()
    query.first()
    return query.value(0)


def metadata_id(key):
    '''
    Get metadata id from metadata table
    '''
    query = QSqlQuery()
    query.prepare("SELECT element_metadata_id FROM elements_metadata WHERE name = :key")
    query.bindValue(':key', key)
    query.exec_()
    query.first()
    return query.value(0)


def insertInfo(id_elemento, info):
    '''
    Insert info in info table from dictionary
    '''

    query = QSqlQuery()
    query.prepare(
        "INSERT INTO elements_metadata_text (element_id, element_metadata, text) VALUES (:element_id, :key, :value)")
    query.bindValue(':element_id', id_elemento)

    for key, value in info.items():
        key = metadata_id(key)
        query.bindValue(':key', key)
        query.bindValue(':value', value)
        if not query.exec_():
            logging.error(query.lastError().text())
            return False
    return True
