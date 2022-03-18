# ///////////////////////////////////////////////////////////////
#
# Hecho por: Jairo Antonio Melo Flórez
# Realizado con: Qt Designer y PySide6
# © 2021 Fundación Histórica Neogranadina
# V: 0.1.0-alpha
#
# camcontrol:
# módulo para facilitar la comunicación con chdkptp.py a través de dos cámaras
#
# Documentación de chdkptp.py en https://chdkptppy.readthedocs.io/en/latest/
# ///////////////////////////////////////////////////////////////

from fractions import Fraction
import chdkptp
from chdkptp.lua import LuaContext
import multiprocessing as mp
from filecontrol import DescargarIMGS
#import configparser


class Cam:
    def __init__(self):
        self.camaras = chdkptp.list_devices()

    def devs(self):
        '''
        Convierte las dispositivos en ChdkDevices. Regresa dos objetos como lista.
        Técnicamente, si se reconocen más de dos dispositivos, se crean igual cantidad
        de ChdkDevices.
        '''
        try:
            return [chdkptp.ChdkDevice(dev) for dev in self.camaras]
        except:
            raise

    def cam_init(self, dev):
        '''
        función llamada por self.cam() para asegurar que la cámara esté en modo
        record y pueda iniciar la captura de imágenes.
        usar de modo asincrónico para que no levante el error lupa._lupa.LuaRuntime.execute
        '''
        if not dev.mode == 'record':
            dev.switch_mode('record')

    def cam(self, devs):
        '''
        Asegura que ambas cámaras estén en modo record.
        devs = recibe un listado con ChdkDevices (usar Cam().devs())
        Si hay más de dos dispositivos conectados solamente procesará 
        los dos primeros en .list_devices()
        '''

        c1_on = mp.Process(target=self.cam_init, args=(devs[0],))
        c2_on = mp.Process(target=self.cam_init, args=(devs[1],))

        c1_on.start()
        c2_on.start()

    def _shoot(self, dev, element_id, folio, dng=True):
        '''
        dev = el dispositivo conectado y en modo rec() [usar camcontrol.Cam().cam()]
        dng = True. En modo False no guarda imágenes dng en la memoria de la cámara. 
              Marca error si stream=True.
        '''

        #shutter = 1/15.0
        #iso = 400
        #distancia = 150

        # el binario jpg se guarda en imgdata
        imgdata = dev.shoot(wait=True, dng=dng, stream=False,
                            download_after=True, remove_after=True, 
                            shutter_speed = chdkptp.util.shutter_to_tv96(float(Fraction(u"1/25"))),
                            zoom_level=3)

        obj_descarga = DescargarIMGS(imgdata, element_id, folio, dev)
        # descarga jpg
        obj_descarga.descarga_jpg()
        if not dng == False:
            # descarga dng
            obj_descarga.descarga_dng()

    def captura(self, dev_list, element_id, left_folio, right_folio):
        '''
        Realiza la captura en ambas cámaras casi simultáneamente.
        '''

        c1 = mp.Process(target=self._shoot, args=(dev_list[0], element_id, left_folio))
        c2 = mp.Process(target=self._shoot, args=(dev_list[1], element_id, right_folio))

        c1.start()
        c2.start()

    def close_dev(self, dev_list):
        '''
        Disconnect devs
        '''
        [dev.switch_mode('play') for dev in dev_list if dev.mode == 'record']

        for cam in self.camaras:
            info = cam
            _lua = LuaContext()
            _lua.globals.devspec = info._asdict()
            _lua.pexecute("""
            con = chdku.connection({bus = devspec.bus_num,
                                dev = devspec.device_num})
            con:disconnect()
            """)
