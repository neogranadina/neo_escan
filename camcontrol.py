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

    def _shoot(self, dev):
        shutter = 1/15.0
        iso = 400
        distancia = 150
        dev.shoot(shutter_speed=shutter, real_iso=iso, distance=distancia)

    def captura(self, dev_list):

        c1 = mp.Process(target=self._shoot, args=(dev_list[0],))
        c2 = mp.Process(target=self._shoot, args=(dev_list[1],))

        inicio = time.time()
        c1.start()
        c2.start()
        final = time.time()
        print(final - inicio)

    def descarga_img(self, img_path, ddestino, dev):
        raw_img = dev.download_file(img_path)
        if img_path.endswith(".DNG"):
            filename = os.path.join(ddestino, "RAW", img_path.split("/")[-1])
        else:
            filename = os.path.join(ddestino, "JPG", img_path.split("/")[-1])

        if not os.path.exists(filename):
            with open(filename, "wb") as fp:
                fp.write(raw_img)

        dev.delete_files(img_path)

    def archivos_descarga(self, dev_list, detailed=True):
        a_desc = []
        for d in dev_list:
            ruta_dirCam = d.list_files()[-1:][0][:-1]
            rp = util.to_camerapath(ruta_dirCam)
            flist = d._lua.call("con:listdir", rp, dirsonly=False,
                                stat="*" if detailed else "/")
            a_desc.append(flist)

        return a_desc

    def descarga_imgs(self, dev_list, dir_destino='test/imgs'):
        try:
            os.makedirs(os.path.join(dir_destino, "RAW"), exist_ok=True)
            os.makedirs(os.path.join(dir_destino, "JPG"), exist_ok=True)
        except OSError as error:
            print(error)
            raise

        flist = self.archivos_descarga(dev_list)

        ruta_dirCam = [dev.list_files()[-1:][0][:-1] for dev in dev_list]

        # ruta a la cámara
        rp = [util.to_camerapath(r) for r in ruta_dirCam]

        listal = []
        listar = []
        for l, r in zip(flist[0].values(), flist[1].values()):
            for k, v in l.items():
                if k == 'name':
                    listal.append(f"{rp[0]}/{v}")
            for k, v in r.items():
                if k == 'name':
                    listar.append(f"{rp[1]}/{v}")

        with cf.ThreadPoolExecutor(max_workers=5) as executor:
            futura_izq = {executor.submit(
                self.descarga_img, li, dir_destino, dev_list[0]): li for li in listal}
            futura_der = {executor.submit(
                self.descarga_img, lr, dir_destino, dev_list[1]): lr for lr in listar}

        for fut, futur in zip(futura_izq, futura_der):
            fut, futur


if __name__ == 'main':
    Cam()
