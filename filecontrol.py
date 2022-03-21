# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.0-alpha
# 2022-02-07
#
# filecontrol:
# módulo para leer y guardar las capturas de la cámara
#
# ///////////////////////////////////////////////////////////////

import shutil
import sys
import chdkptp.util as util
from pathlib import Path
import os
import datetime
from db_handler import getLastElementID, wrap_imageWithElement
from PIL import Image, ExifTags
import logging
import configparser
import bagit


# logs

logging.basicConfig(filename="neo_escan.log",
                    level=logging.DEBUG)
logger = logging.getLogger("logger")

# config

config = configparser.ConfigParser()
config.read(Path('config.cfg'))

# Check compatibility and return images directory

if sys.platform == 'linux':
    IMGDIR = config['DEFAULT']['img_dir']
elif sys.platform == 'win32':
    IMGDIR = config['DEFAULT']['images_dir_windows']
else:
    ctypes.windll.user32.MessageBoxW(
        0, "Sistema operativo no soportado", "Error", 0)
    sys.exit(0)


class DescargarIMGS:

    def __init__(self, imgdata, nombre_proyecto, folio, dev) -> None:
        '''
        imgdata(bin) = datos binarios de la imagen capturada (jpg)
        nombre_proyecto(str) = nombre del proyecto
        dev(object) = objeto chdkptp.ChdkDevice()
        '''
        self.dev = dev  # necesario para comunicarse con los archivos remotos
        self.imgdata = imgdata
        self.nombre_proyecto = nombre_proyecto
        self.folio = folio


    def check_dir(self):
        '''
        En caso de que la base de datos esté vacía pero existan capturas en el directorio
        se hace un backup de las capturas y se prepara la carpeta para reiniciar las capturas
        '''
        r = getLastElementID()
        if r is '':
            dir = os.listdir(IMGDIR)
            if len(dir) != 0:
                for files in dir:
                    if files != 'old_backup':
                        shutil.move(os.path.join(IMGDIR, files), os.path.join(IMGDIR, 'old_backup', files))
        else:
            print(r)
        

    def img_dir(self, tipo_img):
        '''
        tipo_img(str) = tipo de imagen (jpg, dng)
        Crea directorio si no existe y lo configura como BagIt
        return dirección del subdirectorio para la subida de imagen por tipo
        '''

        img_dir = os.path.join(IMGDIR, self.nombre_proyecto)
        os.makedirs(img_dir, exist_ok=True)

        # if img_dir is empty create bag:
        if not os.path.exists(f'{img_dir}/bagit.txt'):
            bag = bagit.make_bag(img_dir, {
                'Contact-Name': 'Fundación histórica Neogranadina',
                'Contact-Email': 'coordinacion@neogranadina.org',
                'Website': 'neogranadina.org'})

        img_dir = os.path.join(IMGDIR, self.nombre_proyecto, 'data', f"{tipo_img.upper()}")
        os.makedirs(img_dir, exist_ok=True)

        return img_dir


    def image_name(self, img_path):
        '''
        nombre de la imagen
        '''
        return img_path.split("/")[-1]


    def descarga_jpg(self):
        '''
        crea imagen jpg a partir del binario (imgdata)
        '''
        jpg_path = os.path.join(self.img_dir('jpg'), f"{self.folio}.jpg")

        with open(jpg_path, 'wb') as fp:
            fp.write(self.imgdata)
            self.associateImageWithElement(
                self.nombre_proyecto, jpg_path, 'jpg')
            print(f"descargada img {jpg_path}")

        # update bag
        bag = bagit.Bag(os.path.join(IMGDIR, self.nombre_proyecto))
        bag.save(manifests=True)

    def descarga_dng(self):
        '''
        copia la imagen dng desde la memoria de la cámara
        '''
        img_path = self.dng_remoto()

        raw_img = self.dev.download_file(img_path)
        if img_path.endswith(".DNG"):
            dng_path = os.path.join(self.img_dir('dng'), f"{self.folio}.dng")

        if not os.path.exists(dng_path):
            with open(dng_path, "wb") as fp:
                fp.write(raw_img)
                self.associateImageWithElement(
                    self.nombre_proyecto, dng_path, 'dng')
                print(f"descargada img {dng_path}")

        # update bag
        bag = bagit.Bag(os.path.join(IMGDIR, self.nombre_proyecto))
        bag.save(manifests=True)

        self.dev.delete_files(img_path)

    def imgs_camara(self, detailed=True):
        '''
        lista de archivos guardados en la cámara remota
        '''
        ruta_dirCam = self.dev.list_files()[-1:][0][:-1]
        rp = util.to_camerapath(ruta_dirCam)
        flist = self.dev._lua.call("con:listdir", rp, dirsonly=False,
                                   stat="*" if detailed else "/")

        return flist

    def dng_remoto(self):
        '''
        ruta a la última imagen tomada por la cámara
        '''
        flist = self.imgs_camara()
        ruta_dirCam = self.dev.list_files()[-1:][0][:-1]
        ruta_camara = util.to_camerapath(ruta_dirCam)

        for l in flist.values():
            listac = [f"{ruta_camara}/{v}" for k,
                      v in l.items() if k == 'name']

        return listac[-1]

    def imageMetadata(self, image_path):
        '''
        obtiene los metadatos de una imagen
        '''
        image = Image.open(image_path)
        if image.format == "JPEG":
            img_exif = image._getexif()
        elif image.format == "DNG":
            img_exif = image.getexif()
        else:
            img_exif = None

        if img_exif is not None:
            exif = {ExifTags.TAGS.get(
                k, "etiqueta desconocida"): v for k, v in img_exif.items()}
            return exif
        else:
            return {'No metadata': 'No metadata'}

    def associateImageWithElement(self, element_id, img_path, tipo_img):
        '''
        get the metadata of each image and associate it with the element
        and write it in database
        '''
        element_id = int(element_id)

        if tipo_img == 'jpg':
            lista = os.listdir(self.img_dir('jpg'))
            order = len(lista)
        elif tipo_img == 'dng':
            lista = os.listdir(self.img_dir('dng'))
            order = len(lista)

        size = os.path.getsize(img_path)

        mime_type = 'image/jpeg' if tipo_img == 'jpg' else 'image/x-adobe-dng'

        filename = os.path.basename(img_path)
        path = os.path.dirname(img_path)
        img_timestamp = datetime.datetime.now()
        img_modified_ts = datetime.datetime.now()
        img_metadata = self.imageMetadata(img_path)

        # debug
        '''
        print(f"element_id: {element_id}")
        print(f"order: {order}")
        print(f"img_path: {img_path}")
        print(f"tipo_img: {tipo_img}")
        print(f"size: {size}")
        print(f"mime_type: {mime_type}")
        print(f"filename: {filename}")
        print(f"path: {path}")
        print(f"img_timestamp: {img_timestamp}")
        print(f"img_modified_ts: {img_modified_ts}")
        print(f"img_metadata: {img_metadata}")
        '''

        wrap_imageWithElement(element_id, order, size, mime_type, filename,
                              path, img_timestamp, img_modified_ts,
                              img_metadata)
