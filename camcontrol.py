# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

import chdkptp
import chdkptp.util as util
import concurrent.futures as cf
import os
import multiprocessing as mp
import time


class Cam:
    def __init__(self):
        self.camaras = chdkptp.list_devices()

    def devs(self):
        try:
            return [chdkptp.ChdkDevice(dev) for dev in self.camaras]
        except:
            raise

    def cam_init(self, dev):
        if not dev.mode == 'record':
            dev.switch_mode('record')

    def cam(self, devs):

        c1_on = mp.Process(target=self.cam_init, args=(devs[0],))
        c2_on = mp.Process(target=self.cam_init, args=(devs[1],))

        c1_on.start()
        c2_on.start()

    def _shoot(self, dev,dng=True):

        fileformat = "dng"
        shutter = 1/15.0
        iso = 400
        distancia = 150
        
        dir = "tmp_dir/JPG" # directorio = "nombre_de_proyecto/JPG"
        os.makedirs(os.path.join(dir), exist_ok=True)
        lista = os.listdir(dir)
        print(lista)
        number_files = len(lista)

        fpath = os.path.join(dir, f"stream_{number_files + 1}.jpg")

        imgdata = dev.shoot(wait=True, dng=dng, stream=False, download_after=True, remove_after=True)
        if os.path.exists(fpath):
            dup_name = fpath.split("/")[-1]
            nombre_file = dup_name.split(".")[0]
            serie = nombre_file.split("_")[1]
            fpath = os.path.join(dir, f"stream_{int(serie) + 1}.jpg") # ¿Podría ser R - V?
        with open(fpath, 'wb') as fp:
            fp.write(imgdata)


    def captura(self, dev_list):

        c1 = mp.Process(target=self._shoot, args=(dev_list[0],))
        c2 = mp.Process(target=self._shoot, args=(dev_list[1],))

        c1.start()
        c2.start()
