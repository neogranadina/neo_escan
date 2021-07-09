# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

import chdkptp
import os
import traceback
import time
import chdkptp.util as util

def renombrar_img(nombre_img):
    pass

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


def descarga_img(f, rp, ddestino, cam):
    try:
        os.makedirs(os.path.join(ddestino, "RAW"), exist_ok=True)
        os.makedirs(os.path.join(ddestino, "JPG"), exist_ok=True)
    except OSError as error:
        print(error)
        raise

    for k,v in f.items():
        if k == 'name':
            img_path = f"{rp}/{v}"
            print(img_path)
            
            raw_img = cam.download_file(img_path)
            if v.endswith(".DNG"):
                filename = os.path.join(ddestino, "RAW", v)
            else:
                filename = os.path.join(ddestino, "JPG", v)
            if not os.path.exists(filename):
                with open(filename, "wb") as fp:
                    fp.write(raw_img)
            
            cam.delete_files(img_path)

def descarga_imgs(dir_destino='test/imgs'):
    '''
    dir_origen y dir_destino son iguales para ambas cámaras
    '''
    detailed = True
    cam()[0].switch_mode('play')
    cam()[1].switch_mode('play')

    # directorios en la tarjeta de las cámaras

    ruta_dirCam1 = cam()[0].list_files()[-1:][0][:-1]
    ruta_dirCam2 = cam()[1].list_files()[-1:][0][:-1]

    # ruta a la cámara

    rp1 = util.to_camerapath(ruta_dirCam1)
    rp2 = util.to_camerapath(ruta_dirCam2)

    flist1 = cam()[0]._lua.call("con:listdir", rp1, dirsonly=False,
                               stat="*" if detailed else "/")
    flist2 = cam()[1]._lua.call("con:listdir", rp2, dirsonly=False,
                               stat="*" if detailed else "/")

    for l, r in zip(flist1.values(), flist2.values()):
        descarga_img(l, rp1, dir_destino, cam()[0])
        descarga_img(r, rp2, dir_destino, cam()[1])

    cam()[0].switch_mode('record')
    cam()[1].switch_mode('record')

def shoots():
    try:
        cam()[0].switch_mode('record')
        cam()[1].switch_mode('record')
    except TypeError:
        print(f"No es posible seleccionar la cámara.")
        raise
    
    inicio_tiempo = time.time()

    imgdata_1 = cam()[0].shoot(dng=True, stream=False, download_after=False, remove_after=False)
    imgdata_2 = cam()[1].shoot(dng=True, stream=False, download_after=False, remove_after=False)

    final_tiempo = time.time()
    print(final_tiempo - inicio_tiempo)

    return imgdata_1, imgdata_2


def captura():
    shoots()
    descarga_imgs()
