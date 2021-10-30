# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# retrieve form fields:
# module to retrieve form fields from a form and return a dictionary
#
# ///////////////////////////////////////////////////////////////

from PySide2.QtWidgets import QFileDialog
from ui_main import Ui_MainWindow


global widgets
widgets = Ui_MainWindow()

# fields from Legajo form
legajo = {
    'titulo': widgets.titulolineEdit.text(),
    'descripción': widgets.descripcionlineEdit.text(),
    'creador': widgets.creadorlineEdit.text(),
    'fecha_inicial': widgets.fechaIlineEdit.text(),
    'fecha_final': widgets.fechaFlineEdit.text(),
    'cobertura_espacial': widgets.coberturalineEdit.text(),
    'idioma': widgets.idiomalineEdit.text(),
    'num_folios': widgets.numfollineEdit.text(),
    'identificadores': widgets.identificadoreslineEdit.text(),
}

documento = {
    'titulo': widgets.titulodoclineEdit.text(),
    'descripción': widgets.descripciondoclineEdit.text(),
    'creador': widgets.creadordoclineEdit.text(),
    'fecha_inicial': widgets.fechaIdoclineEdit.text(),
    'fecha_final': widgets.fechaFdoclineEdit.text(),
    'cobertura_espacial': widgets.coberturadoclineEdit.text(),
    'idioma': widgets.idiomadoclineEdit.text(),
    'num_folios': widgets.numfoliodoclineEdit.text(),
    'identificadores': widgets.identificadoresdoclineEdit.text(),
}

imagen = {
    'titulo': widgets.tituloimagenlineEdit.text(),
    'descripción': widgets.descripcionimagenlineEdit.text(),
    'creador': widgets.creadorimagenlineEdit.text(),
    'fecha': widgets.fechaimagenlineEdit.text(),
    'cobertura_espacial': widgets.coberturaespacialimagenlineEdit.text(),
    'descripción_física': widgets.descripcionfisicaimagenlineEdit.text(),
    'tipo': widgets.tipoimagenlineEdit.text(),
    'identificadores': widgets.identificadoresimagenlineEdit.text(),
}

seriada = {
    'nombre': widgets.nombreserlineEdit.text(),
    'volumen': widgets.volumenserlineEdit.text(),
    'ejemplar': widgets.ejemplarserlineEdit.text(),
    'fecha': widgets.fechaserlineEdit.text(),
    'páginas': widgets.paginaserlineEdit.text(),
    'descripción': widgets.descripcionserlineEdit.text(),
    'idioma': widgets.idiomaserlineEdit.text(),
    'issn': widgets.issnserlineEdit.text(),
    'identificadores': widgets.identificadoreserlineEdit.text(),
}

libro = {
    'título': widgets.titulolibrolineEdit.text(),
    'autor': widgets.autorlibrolineEdit.text(),
    'volumen': widgets.volumelibrolineEdit.text(),
    'serie': widgets.serieLibrolineEdit.text(),
    'edición': widgets.edicionLibrolineEdit.text(),
    'lugar': widgets.lugarLibrolineEdit.text(),
    'editorial': widgets.editorialLibrolineEdit.text(),
    'fecha': widgets.fechaLibrolineEdit.text(),
    'páginas': widgets.paginasLibrolineEdit.text(),
    'descripción': widgets.descripcionLibrolineEdit.text(),
    'idioma': widgets.idiomaLibrolineEdit.text(),
    'isbn': widgets.isbnLibrolineEdit.text(),
    'identificadores': widgets.identificadoresLibrolineEdit.text(),
}


def getDirName():
    '''
    get the directory name
    '''
    response = QFileDialog.getExistingDirectory(
        None, 'Seleccione una carpeta', './')
    widgets.rutaLine.setText(response)


def get_fields_info(tipo_de_documento):
    '''
    get the info for a specific form fields and return a dictionary
    '''
    if tipo_de_documento == 'Legajo':
        return legajo
    elif tipo_de_documento == 'Documento':
        return documento
    elif tipo_de_documento == 'Imagen':
        return imagen
    elif tipo_de_documento == 'Periódico / revista':
        return seriada
    elif tipo_de_documento == 'Libro':
        return libro
    else:
        return None


