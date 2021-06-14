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
from pathlib import Path

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
        logging.error(
            f"{datetime.datetime.now()} - No fue posible escribir en el directorio")

    # Garantizar la escritura en cualquier dispositivo
    abs_path = write_dir.absolutePath()
    filename = f"{abs_path}/neo_scan.sqlite3"

    # En SQLite, si no  existe la base de datos, esta es creada
    database.setDatabaseName(filename)
    if not database.open():
        logging.error(
            f"{datetime.datetime.now()} - No fue posible abrir la base de datos")


def insertInfo(tipo, refCode, titulo, fechas, alcance, ubicacion):
    '''
    Escribe la información de un proyecto en la base de datos
    '''

    if ubicacion == Path("."):
        ubicacion = Path(f"archivos_proyectos/{tipo}/{titulo}")

    query_script = f"""
        SELECT id_tipo_proyecto
        FROM tipos_proyecto
        WHERE nombre_tipo_proyecto = "{tipo}"
        """

    query = QSqlQuery()
    if not query.exec(query_script):
        logging.info(query)

    query.first()
    tipo_id = query.value(0)

    # Este id deberá modificarse si se hace un cambio a la dinámica de instituciones
    default_institucion = 1

    if not query.exec(f"""
    INSERT INTO proyectos 
    (nombre_proyecto, tipo_proyecto, institucion_proyecto, 
    ts_creacion_proyecto, path_proyecto, cobertura_temporal, cobertura_espacial)
    VALUES
    ("{titulo}", {tipo_id}, {default_institucion}, "{datetime.datetime.now()}", "{ubicacion}", "{fechas}", "")
    """):
        logging.info(query)

    # Ahora guarda la información en la tabla de unidades documentales compuestas

    if not query.exec("SELECT id_proyecto FROM proyectos ORDER BY id_proyecto DESC LIMIT 1"):
        logging.info(query)

    query.first()
    proyecto_id = query.value(0)

    if not query.exec(f"""
    INSERT INTO unidad_documental (id_proyecto, codigo_referencia, titulo, fechas)
    VALUES
    ({proyecto_id}, "{refCode}", "{titulo}", "{fechas}")
    """):
        logging.info(query)


def testProyDuplicados(titulo):
    '''
    Busca coincidencia del título de un proyecto
    '''
    query = QSqlQuery()
    if not query.exec(f"""SELECT * FROM unidad_documental WHERE titulo = "{titulo}" """):
        logging.info(query)

    return query.first()

def regresa_info_proyecto(titulo):
    query = QSqlQuery()
    if not query.exec(f"""
    SELECT * FROM unidad_documental WHERE titulo = "{titulo}"
    """):
        logging.info(query)

    query.first()
    return f"Proyecto: {query.value(3)} \nCódigo: {query.value(2)} \nFechas: {query.value(4)}"

def checkDirectorio(ruta):
    '''
    Busca coincidencia del directorio de un proyecto
    '''
    query = QSqlQuery()
    if not query.exec(f"""SELECT * FROM proyectos WHERE path_proyecto = "{ruta}" """):
        logging.info(query)

    return query.first()