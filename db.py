# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

import logging
from configparser import ConfigParser, Error

from PySide6.QtCore import Qt, Slot, QDir
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel


config = ConfigParser()
config.read('config.ini')
# configuración general
tipo = config.get('db', 'tipo')
try:
    host = config.get('db', 'hostname')
    db_name = config.get('db', 'database')
    user = config.get('db', 'username')
    password = config.get('db', 'password')
except Error:
    pass


def connectToDatabase():
    '''
    Conecta a la base de datos a través de la clase QSqlDatabase
    https://doc.qt.io/qt-6/qsqldatabase.html
    '''
    database = QSqlDatabase.database()

    # Conecta a una base de datos dependiendo el tipo de base de datos
    # según se declare en el archivo de configuración

    if not database.isValid():
        if tipo == 'QSQLITE':
            database = QSqlDatabase.addDatabase(tipo)
        else:
            database = QSqlDatabase.addDatabase(tipo)
            database.setHostName(host)
            database.setDatabaseName(db_name)
            database.setUserName(user)
            database.setPassword(password)

            if not database.isValid():
                logging.error("No es posible conectarse a la base de datos")

    write_dir = QDir("db")
    if not write_dir.mkpath("."):
        logging.error("No fue posible escribir en el directorio")

    # Garantizar la escritura en cualquier dispositivo
    abs_path = write_dir.absolutePath()
    filename = f"{abs_path}/neo_scan.sqlite3"

    # En SQLite, si no  existe la base de datos, esta es creada
    database.setDatabaseName(filename)
    if not database.open():
        logging.error("No fue posible abrir la base de datos")


def db_config_info():
    '''
    Regresa la información de configuración de la base de datos en una lista HTML
    '''

    config = ConfigParser()
    config.read('config.ini')
    # configuración general
    tipo = config.get('db', 'tipo')
    try:
        host = config.get('db', 'hostname')
        db_name = config.get('db', 'database')
        user = config.get('db', 'username')
    except Error:
        pass


    if tipo == 'QSQLITE':
        info = f"""<h3>Configuración actual:</h3>
                    <ul>
                    <li>Tipo de db: {tipo}</li>
                    <li>Host: Ninguno</li>
                    <li>Base de datos: Ninguno</li>
                    <li>Usuario: Ninguno</li>
                    </ul>"""
    else:
        info = f"""<h3>Configuración actual:</h3>
                    <ul>
                    <li>Tipo de db: {tipo}</li>
                    <li>Host: {host}</li>
                    <li>Base de datos: {db_name}</li>
                    <li>Usuario: {user}</li>
                    </ul>"""
    return info


def db_configurar(tipo_db, localhost, databasename, username, password):
    if tipo_db == 'SQLite3':
        tipo_db = 'QSQLITE'
    elif tipo_db == 'MariaDB' or tipo_db == 'MySQL':
        tipo_db = 'QMYSQL'
    elif tipo_db == 'PostgreSQL':
        tipo_db = 'QPSQL'

    db = config['db']

    # actualizar información
    db['tipo'] = tipo_db
    db['hostname'] = localhost
    db['database'] = databasename
    db['username'] = username
    db['password'] = password

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
