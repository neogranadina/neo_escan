# -*- coding: utf-8 -*-

# Copyright (C) 2021 Fundación Histórica Neogranadina
# https://neogranadina.org/
# Developer Jairo Antonio Melo Flórez jairomelo@neogranadina.org

import chdkptp
import os
import glob
import base64
import traceback
import time


def nombre_img(directorio):
    """
    Regresa nombres secuenciales y evita sobreescritura
    TODO: Lógica de folios, anversos y reversos.
    """
    imgs = glob.glob(os.path.join(directorio, "*.jpg"))
    ultima_img = [im.split("/")[-1] for im in imgs[-1:]]
    try:
        base_nombre = ultima_img[0].split(".")[0]
        consecutivo = int(base_nombre[4:]) + 1
        serie = str(consecutivo).zfill(5)
        nombre = f"{base_nombre[0:4]}{serie}.jpg"
        return os.path.join(directorio, nombre)
    except IndexError:
        # primera imagen en directorio vacío
        serie = "1".zfill(5)
        nombre = f"img_{serie}.jpg"
        return os.path.join(directorio, nombre)


def cam(camaras=chdkptp.list_devices()):
    try:
        dev_1 = chdkptp.ChdkDevice(camaras[0])
        dev_2 = chdkptp.ChdkDevice(camaras[1])
        return dev_1, dev_2
    except IndexError:
        print("Neograndina escan error: \n No hay cámaras conectadas o están apagadas \n")
        print(traceback.print_stack())
    except:
        raise


def shoots():
    try:
        cam()[0].switch_mode('record')
        cam()[1].switch_mode('record')
    except TypeError:
        print(f"No es posible seleccionar la cámara.")
        raise
    
    inicio_tiempo = time.time()

    imgdata_1 = cam()[0].shoot(
        stream=False, download_after=True, remove_after=True)
    imgdata_2 = cam()[1].shoot(
        stream=False, download_after=True, remove_after=True)

    final_tiempo = time.time()
    print(final_tiempo - inicio_tiempo)

    return imgdata_1, imgdata_2


def toma(dir = "imgs"):
    """
    dir = "imgs" o ruta personalizada
    """
    try:
        os.makedirs(dir, exist_ok=True)
    except:
        pass

    for s in shoots():
        with open(nombre_img(dir), "wb") as f:
            f.write(s)
            print(f"Guardada exitosamente la imagen {f.name}")
            f.close()


if __name__ == "__main__":
    toma()
