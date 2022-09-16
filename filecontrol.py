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

import json
import shutil
import sys
import chdkptp.util as util
from pathlib import Path
import os
import datetime
from db_handler import getElementIdByMetadata, wrap_imageWithElement
from exif import Image
import logging
import configparser
import bagit
from logcontrol import LogControl as log

# config

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'setup/config.cfg')
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

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
                'Website': 'neogranadina.org',
                'Nombre proyecto': self.nombre_proyecto})
            
            # aditional files
            # create metadata.json if not exists
            if not os.path.exists(f'{img_dir}/metadata.json'):
                with open(f'{img_dir}/metadata.json', 'w', encoding='utf-8') as fp:
                    json.dump({}, fp)

            # move metadata.json to bagit root
            if not img_dir.endswith('test_config'):
                shutil.move(f'{img_dir}/data/config_project.json', f'{img_dir}/config_project.json')


        img_dir = os.path.join(IMGDIR, self.nombre_proyecto, 'data', f"{tipo_img.upper()}")
        os.makedirs(img_dir, exist_ok=True)

        return img_dir


    def image_name(self, img_path):
        '''
        nombre de la imagen
        '''
        return img_path.split("/")[-1]


    def descarga_jpg(self, orientacion):
        '''
        crea imagen jpg a partir del binario (imgdata)
        '''
        jpg_path = os.path.join(self.img_dir('jpg'), f"{self.folio}.jpg")

        with open(jpg_path, 'wb') as fp:
            fp.write(self.imgdata)
            self.associateImageWithElement(
                self.nombre_proyecto, jpg_path, 'jpg')
        if orientacion == "vertical":
            img_num = int(jpg_path.split("/")[-1].split(".")[0])
            orient = [8 if img_num % 2 == 0 else 6][0]
        elif orientacion == "horizontal":
            orient = 1

        # asegurar orientación correcta
        with open(jpg_path, 'rb') as fr: # V0.1.710 fixed error "str" object has no "read" attribute
            img = Image(fr)
            img.orientation = orient

        with open(jpg_path, 'wb') as fp:
            fp.write(img.get_file())

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
        with open(image_path, 'rb') as fp:
            img = Image(fp)


        # Agregar exif labels de acuerdo con img.list_all()
        imgmetadata = {
        'image_description': img.get('image_description'),
        'datetime_original': img.get('datetime_original'),
        'ResolutionUnit': img.get('resolution_unit'),
        'Make': img.get('make'),
        'Model': img.get('model'),
        'Orientation': img.get('orientation'),
        'ShutterSpeedValue': img.get('shutter_speed_value'),
        'FlashFired': f"{img.get('flash.flash_fired')}",
        'RedEyeReduction': f"{img.get('flash.red_eye_reduction_supported')}",
        'WhiteBalance': img.get('white_balance'),
        'ExposureMode': img.get('exposure_mode'),
        'FocalLength': img.get('focal_length'),
        'ExposureTime': img.get('exposure_time'),
        'ExifVersion': img.get('exif_version'),
        'ApertureValue': img.get('aperture_value'),
        }

        return imgmetadata

    def write_metadata_json(self, img_path, metadata):
        '''
        escribe los metadatos en un archivo json
        '''
        print(img_path)
        metadata_path = os.path.join(img_path[:-18], "metadata.json")

        if not os.path.exists(metadata_path):
            with open(metadata_path, 'w', encoding='utf-8') as fp:
                json.dump({}, fp)

        with open(metadata_path, 'r+', encoding='utf-8') as fp:
            data = json.load(fp)
            data[self.image_name(img_path)] = metadata
            fp.seek(0)
            json.dump(data, fp, indent=4, ensure_ascii=False)


    def associateImageWithElement(self, metadata_text, img_path, tipo_img):
        '''
        get the metadata of each image and associate it with the element
        and write it in database
        '''
        element_id = getElementIdByMetadata(metadata_text)

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

        # metadatos de la imagen
        
        dcmetadata = {
        'element_id': element_id,
        'order': order,
        'img_path': img_path,
        'tipo_img': tipo_img,
        'size': size,
        'mime_type': mime_type,
        'filename': filename,
        'path': path,
        }

        # metadatos de la imagen
        dcmetadata.update(img_metadata)
        
        self.write_metadata_json(img_path, dcmetadata)

        wrap_imageWithElement(element_id, order, size, mime_type, filename,
                              path, img_timestamp, img_modified_ts,
                              img_metadata)
