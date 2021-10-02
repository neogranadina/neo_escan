# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.0-alpha
#
# filecontrol:
# módulo para leer y guardar las capturas de la cámara 
#
# ///////////////////////////////////////////////////////////////

import chdkptp.util as util
import multiprocessing as mp
from pathlib import Path
import os

DIR = Path("../capturas")

class DescargarIMGS:

    def __init__(self, imgdata, nombre_proyecto, dev) -> None:
        '''
        imgdata(bin) = datos binarios de la imagen capturada (jpg)
        nombre_proyecto(str) = nombre del proyecto
        dev(object) = objeto chdkptp.ChdkDevice()
        '''
        self.dev = dev  # necesario para comunicarse con los archivos remotos
        self.imgdata = imgdata
        self.nombre_proyecto = nombre_proyecto

    def nombrar_img(self, tipo_img):
        '''
        crea un nombre único para cada captura
        TODO: comprobar errores de sincronización que lleven a que los dng no coincidan con los jpg
        '''
        img_dir = os.path.join(DIR, self.nombre_proyecto,
                               f"{tipo_img.upper()}")
        os.makedirs(img_dir, exist_ok=True)
        lista = os.listdir(img_dir)
        # print(lista)
        number_files = len(lista)
        # print(number_files)
        fpath = os.path.join(img_dir, f"IMG_{number_files + 1}.{tipo_img}")

        if os.path.exists(fpath):
            dup_name = fpath.split("/")[-1]
            nombre_file = dup_name.split(".")[0]
            serie = nombre_file.split("_")[1]
            # ¿Podría ser R - V?
            fpath = os.path.join(img_dir, f"IMG_{int(serie) + 1}.{tipo_img}")

        return fpath

    def descarga_jpg(self):
        '''
        crea imagen jpg a partir del binario (imgdata)
        '''
        jpg_path = self.nombrar_img('jpg')
        with open(jpg_path, 'wb') as fp:
            fp.write(self.imgdata)
            print(f"descargada img {jpg_path}")

    def descarga_dng(self):
        '''
        copia la imagen dng desde la memoria de la cámara
        '''
        img_path = self.dng_remoto()

        raw_img = self.dev.download_file(img_path)
        if img_path.endswith(".DNG"):
            dng_path = self.nombrar_img('dng')

        if not os.path.exists(dng_path):
            with open(dng_path, "wb") as fp:
                fp.write(raw_img)
                print(f"descargada img {dng_path}")

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
