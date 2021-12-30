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

from PySide2.QtCore import QDir
from PySide2.QtSql import QSqlDatabase, QSqlQuery


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

    query = QSqlQuery()
    query.prepare("INSERT INTO elements (document_type, user_id, public, created_ts, modified_ts) VALUES (:doctype, :user, :public, :created_at, :updated_at)")
    query.bindValue(':doctype', tipo_elemento)
    query.bindValue(':user', usuario)
    query.bindValue(':public', publico)
    query.bindValue(
        ':created_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    query.bindValue(
        ':updated_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

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
    get info from element table
    '''
    query = QSqlQuery()
    query.prepare(
        "SELECT document_type, user_id, public, created_ts, modified_ts FROM elements WHERE element_id = :element_id")
    query.bindValue(':element_id', id_elemento)
    query.exec_()
    query.first()
    info = {}
    info['document_type'] = query.value(0)
    info['user_id'] = query.value(1)
    info['public'] = query.value(2)
    info['created_ts'] = query.value(3)
    info['modified_ts'] = query.value(4)
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


def getElementMetadatabyID(id_elemento):
    '''
    get all metadata text from id
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


def editInfo(element_id, data):
    '''
    update rows by values in dict in element_metadata_text table
    '''
    query = QSqlQuery()
    query.prepare(
        """
        UPDATE elements_metadata_text 
        SET text = :value
        WHERE element_id = :element_id AND element_metadata = :key
        """)
    query.bindValue(':element_id', element_id)
    for key, value in data.items():
        key = metadata_id(key)
        query.bindValue(':key', key)
        query.bindValue(':value', value)
        if not query.exec_():
            logging.error(query.lastError().text())
            return False
    # update element updated_at
    query.prepare(
        """
        UPDATE elements
        SET updated_at = :updated_at
        WHERE element_id = :element_id
        """)
    query.bindValue(':element_id', element_id)
    query.bindValue(
        ':updated_at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if not query.exec_():
        logging.error(query.lastError().text())
        return False
    return True


def erase_element(element_id):
    '''
    delete element info, metadata and images info from element
    '''
    query = QSqlQuery()
    query.prepare(
        """
        begin;
        DELETE FROM elements_metadata_text WHERE element_id = :element_id;
        DELETE FROM images WHERE element_id = :element_id;
        DELETE FROM elements WHERE element_id = :element_id;
        commit;
        """
    )
    query.bindValue(':element_id', element_id)
    if not query.exec_():
        logging.error(query.lastError().text())
        return False
    return True


def export_data(element_id):
    '''
    get all info in database from element_id
    '''
    query = QSqlQuery()
    query.prepare(
        """
        SELECT elements_metadata_text.element_metadata, elements_metadata_text.text, images.order, images.size, images.mime_type, images.filename, images.path, images.img_ts, images.img_modified_ts, images.img_metadata
        FROM elements_metadata_text
        INNER JOIN elements ON elements.element_id = elements_metadata_text.element_id
        INNER JOIN images ON images.element_id = elements.element_id
        WHERE elements.element_id = :element_id
        """
    )
    query.bindValue(':element_id', element_id)
    query.exec_()
    data = {}
    while query.next():
        data[query.value(0)] = query.value(1)
        data['order'] = query.value(2)
        data['size'] = query.value(3)
        data['mime_type'] = query.value(4)
        data['filename'] = query.value(5)
        data['path'] = query.value(6)
        data['img_ts'] = query.value(7)
        data['img_modified_ts'] = query.value(8)
        data['img_metadata'] = query.value(9)
    return data
