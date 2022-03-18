# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.0
# 2021-12-29
#
# camcontrol:
# módulo para facilitar la comunicación con chdkptp.py a través de dos cámaras
#
# Documentación de chdkptp.py en https://chdkptppy.readthedocs.io/en/latest/
# ///////////////////////////////////////////////////////////////

import sqlite3
from sqlite3 import Error
import os

def crear_basededatos(db_file, schema_file="db/schema.sql"):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # create a cursor
        print(sqlite3.version)
        cursor = conn.cursor()
        # encode the schema file as UTF-8
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = f.read()
        # execute the schema
        cursor.executescript(schema)
        # commit the schema
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    if not os.path.exists("db/neo_escan.db"):
        crear_basededatos("db/neo_escan.db")
    else:
        print("La base de datos ya existe")