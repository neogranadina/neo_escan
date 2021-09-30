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
import multiprocessing as mp
import os


class DescargarIMG:

    def __init__(self, devs, nombre_img) -> None:
        self.devs = devs  # lista de devices
        self.dir_destino = 'capturas/imgs'
        self.nombre_img = nombre_img

    def descarga_img(self, lista_imgs, dev):
        for img_path in lista_imgs:
            print(img_path)
            raw_img = dev.download_file(img_path)
            if img_path.endswith(".DNG"):
                filename = os.path.join(
                    self.dir_destino, "RAW", img_path.split("/")[-1])
            else:
                filename = os.path.join(
                    self.dir_destino, "JPG", img_path.split("/")[-1])
            
            if not os.path.exists(filename):
                with open(filename, "wb") as fp:
                    fp.write(raw_img)
                    print(f"descargada {filename}")

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

    def listado_imgs(self):
        flist = self.archivos_descarga(self.devs)

        ruta_dirCam = [dev.list_files()[-1:][0][:-1] for dev in self.devs]

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

        print(listal)
        print(listar)
        return listal, listar

    def descarga_imgs(self):
        try:
            os.makedirs(os.path.join(self.dir_destino, "RAW"), exist_ok=True)
            os.makedirs(os.path.join(self.dir_destino, "JPG"), exist_ok=True)
        except OSError as error:
            print(error)
            raise

        lista_imgs = self.listado_imgs()
        imgs_left = lista_imgs[0]  # listal
        imgs_der = lista_imgs[1]  # listar

        descargar_l = mp.Process(
            target=self.descarga_img, args=(imgs_left, self.devs[0],))
        descargar_r = mp.Process(
            target=self.descarga_img, args=(imgs_der, self.devs[1]))

        descargar_l.start()
        descargar_r.start()

        print("Inicio del proceso de  descarga")

'''
if __name__ == '__main__':
    cam = chdkptp.list_devices()
    dev = [chdkptp.ChdkDevice(cs) for cs in cam]
    imgs = DescargarIMG(dev, "testing_project")
    descarga = imgs.descarga_imgs()
'''