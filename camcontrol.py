# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.3
# 2022-03-18
#
# camcontrol:
# módulo para facilitar la comunicación con chdkptp.py a través de dos cámaras
#
# Documentación de chdkptp.py en https://chdkptppy.readthedocs.io/en/latest/
# ///////////////////////////////////////////////////////////////

from fractions import Fraction
import inspect
import os
from pathlib import Path
import chdkptp
from chdkptp.lua import LuaContext
import multiprocessing as mp
from filecontrol import DescargarIMGS
import time
import configparser


config = configparser.ConfigParser()
config.read(Path('config.cfg'))

# logs
try:
    os.makedirs("logs", exist_ok=True)
except OSError:
    raise


def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    error = open("logs/neoscan_log.log", "a")
    error.write(ts + ": " + msg + "\n")
    error.close()

class Cam:
    def __init__(self):
        self.camaras = chdkptp.list_devices()
        self.devs = self.devs()

    def test(self):
        '''
        función para probar la conexión de la cámara
        '''
        try:
            len(self.devs)
        except TypeError:
            return False

    def cam_order(self):
        '''
        Convierte las dispositivos en ChdkDevices. Regresa los objetos como lista.
        Se llama como Cam().devs (not callable)
        '''

        seriales = [camara.serial_num for camara in self.camaras]
        cam1 = seriales[0]
        cam2 = seriales[1]

        cam_izq = config['camaras']['serial_izq']
        cam_der = config['camaras']['serial_der']

        if cam1 == cam_izq and cam2 == cam_der:
            return {'cam_izq': cam1, 'cam_der': cam2}
        elif cam1 == cam_der and cam2 == cam_izq:
            return {'cam_izq': cam2, 'cam_der': cam1}
        else:
            # write serials in config file
            config['camaras']['serial_izq'] = cam1
            config['camaras']['serial_der'] = cam2
            with open('config.cfg', 'w') as configfile:
                config.write(configfile)
            return {'cam_izq': cam1, 'cam_der': cam2}


    def single_cam(self):
        '''
        regresa la cámara activa, indica si es izquierda o derecha
        '''
        cam_izq = config['camaras']['serial_izq']
        cam_der = config['camaras']['serial_der']
        cams = self.camaras
        if cam_izq == cams[0].serial_num:
            return {'cam_izq': cams[0]}
        elif cam_der == cams[0].serial_num:
            return {'cam_der': cams[0]}

    def devs(self):
        
        if len(self.camaras) == 0:
            log("No hay dispositivos conectados")
            return None
        elif len(self.camaras) == 1:
            log("Solo hay un dispositivo conectado")
            camid = self.single_cam()
            if camid.keys == 'cam_izq':
                dev_left = [chdkptp.ChdkDevice(d) for d in self.camaras if d.serial_num == camid['cam_izq']]
                return dev_left[0], None
            elif camid.keys == 'cam_der':
                dev_right = [chdkptp.ChdkDevice(d) for d in self.camaras if d.serial_num == camid['cam_der']]
                return None, dev_right[0]
        elif len(self.camaras) == 2:
            cams = self.cam_order()
            try:
                dev_left = [chdkptp.ChdkDevice(d) for d in self.camaras if d.serial_num == cams['cam_izq']]
                dev_right = [chdkptp.ChdkDevice(d) for d in self.camaras if d.serial_num == cams['cam_der']]
                return dev_left[0], dev_right[0]
            except Exception as e:
                # write error in log file
                log(f"ERROR: {str(e)}")
                raise


    def cam_init(self, dev):
        '''
        dev = objeto chdkptp conectado
        función llamada por self.cam() para asegurar que la cámara esté en modo
        record y pueda iniciar la captura de imágenes.
        usar de modo asincrónico para que no levante el error lupa._lupa.LuaRuntime.execute
        '''
        if not dev.mode == 'record':
            dev.switch_mode('record')

    def cam(self):
        '''
        Asegura que una o ambas cámaras estén en modo record.
        devs = recibe un listado con ChdkDevices (usar Cam().devs())
        Si hay más de dos dispositivos conectados solamente procesará 
        los dos primeros en .list_devices()
        '''

        log(f"Conexión en {self.devs}")

        try:
            if len(self.devs) == 2:
                c1_on = mp.Process(target=self.cam_init, args=(self.devs[0],))
                c2_on = mp.Process(target=self.cam_init, args=(self.devs[1],))
                c1_on.start()
                c2_on.start()
            elif len(self.devs) == 1:
                if self.devs[0] is None:
                    self.cam_init(self.devs[1])
                else:
                    self.cam_init(self.devs[0])
            elif len(self.devs) == 0:
                log(f"WARNING: No hay dispositivos conectados. En {__file__} line {inspect.currentframe().f_lineno}")
                return False
        except TypeError as e:
            log(f"ERROR: {str(e)}")
        except Exception as e:
            # write error in log file
            log(f"ERROR: {str(e)}")
            raise

    def _shoot(self, dev, element_id, folio, dng=True):
        '''
        dev = el dispositivo conectado y en modo rec() [usar camcontrol.Cam().cam()]
        dng = True. En modo False no guarda imágenes dng en la memoria de la cámara. 
              Marca error si stream=True.
        '''

        # el binario jpg se guarda en imgdata
        imgdata = dev.shoot(wait=True, dng=dng, stream=False,
                            download_after=True, remove_after=True,
                            shutter_speed=chdkptp.util.shutter_to_tv96(
                                float(Fraction(u"1/25"))),
                            zoom_level=3)

        obj_descarga = DescargarIMGS(imgdata, element_id, folio, dev)
        # descarga jpg
        obj_descarga.descarga_jpg()
        if not dng == False:
            # descarga dng
            obj_descarga.descarga_dng()


    def captura(self, element_id, left_folio, right_folio):
        '''
        Realiza la captura en ambas cámaras casi simultáneamente.
        element_id string con el id del elemento
        left_folio int con la serie de la izquierda
        right_folio int con la serie de la derecha
        '''

        left_camera = self.devs[0] if not self.devs[0] is None else None
        right_camera = self.devs[1] if not self.devs[1] is None else None


        if len(self.devs) == 1:
            if self.devs[0] is None:
                self._shoot(right_camera, element_id, right_folio)
            else:
                self._shoot(left_camera, element_id, left_folio)
        elif len(self.devs) == 2:
            c1 = mp.Process(target=self._shoot, args=(
                left_camera, element_id, left_folio))
            c2 = mp.Process(target=self._shoot, args=(
                right_camera, element_id, right_folio))
            c1.start()
            c2.start()
        elif len(self.devs) < 1:
            return False

    def close_dev(self):
        '''
        Desconecta los devs
        '''
        [dev.switch_mode('play') for dev in self.devs if dev.mode == 'record']

        for cam in self.camaras:
            info = cam
            _lua = LuaContext()
            _lua.globals.devspec = info._asdict()
            _lua.pexecute("""
            con = chdku.connection({bus = devspec.bus_num,
                                dev = devspec.device_num})
            con:disconnect()
            """)
