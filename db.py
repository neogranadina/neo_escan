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
    query.prepare(
        "SELECT element_metadata_id FROM elements_metadata WHERE name = :key")
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


def getLastElementID():
    '''
    get last element inserted
    '''
    # get id from last element inserted

    query = QSqlQuery()
    query.prepare("SELECT max(element_id) FROM elements")
    query.exec_()
    query.first()
    id_elemento = query.value(0)
    return id_elemento


def getElementInfo(id_elemento):
    '''
    get info from last element inserted
    '''

    query = QSqlQuery()
    query.prepare(
        "SELECT element_metadata, text FROM elements_metadata_text WHERE element_id = :element_id")
    query.bindValue(':element_id', id_elemento)
    query.exec_()
    info = {}
    while query.next():
        info[query.value(0)] = query.value(1)
    return info


def count_elementos():
    """
    count rows in element table
    """
    query = QSqlQuery()
    query.prepare("SELECT count(*) FROM elements")
    query.exec_()
    query.first()
    return query.value(0)


def listofIDs():
    '''
    get all ids from elements table
    '''
    query = QSqlQuery()
    query.prepare("SELECT element_id FROM elements")
    query.exec_()
    ids = []
    while query.next():
        ids.append(query.value(0))
    return ids


def getElementInfobyID(id_elemento):
    '''
    get the title and description of an element
    '''
    query = QSqlQuery()
    query.prepare(
        "SELECT element_metadata, text FROM elements_metadata_text WHERE element_id = :element_id")
    query.bindValue(':element_id', id_elemento)
    query.exec_()
    info = {}
    while query.next():
        info[query.value(0)] = query.value(1)
    return info


def wrap_imageWithElement(element_id, order, size, mime_type,
                          filename, path, img_timestamp,
                          img_modified_ts, img_metadata):
    '''
    insert image in images table
    '''

    query = QSqlQuery()
    query.prepare(
        """
        INSERT INTO 
        images (element_id, "order", size, mime_type, filename, path, img_ts, img_modified_ts, img_metadata) 
        VALUES (:element_id, :order, :size, :mime_type, :filename, :path, :created_ts, :modified_ts, :metadata)
        """)
    query.bindValue(':element_id', element_id)
    query.bindValue(':order', order)
    query.bindValue(':size', size)
    query.bindValue(':mime_type', mime_type)
    query.bindValue(':filename', filename)
    query.bindValue(':path', path)
    query.bindValue(':created_ts', img_timestamp)
    query.bindValue(':modified_ts', img_modified_ts)
    query.bindValue(':metadata', img_metadata)

    if not query.exec_():
        logging.error(query.lastError().text())
        return False
    return True

