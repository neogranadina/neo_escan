import chdkptp
import chdkptp.util as util
import concurrent.futures as cf
import time
import os

class Cam:
    def __init__(self):
        self.camaras = chdkptp.list_devices()

    def devs(self, index_cam):
        dev = chdkptp.ChdkDevice(self.camaras[index_cam])
        dev.switch_mode('record')
        return dev

    def cam(self):
        devs = []
        with cf.ThreadPoolExecutor(len(self.camaras)) as executor:
            future_cam = {executor.submit(
                self.devs, i): i for i in range(len(self.camaras))}
            for future in cf.as_completed(future_cam):
                devs.append(future.result())
        return devs

    def _shoot(self, dev):
        dev.shoot(dng=True, stream=False,
                            download_after=False, remove_after=False)

    def captura(self, dev_list):
        

        with cf.ThreadPoolExecutor(len(dev_list)) as executor:
            future_shoot = {executor.submit(
                self._shoot, dev): dev for dev in dev_list}
            for futur in future_shoot:
                futur

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
            for k,v in l.items():
                if k == 'name':
                    listal.append(f"{rp[0]}/{v}")
            for k,v in r.items():
                if k == 'name':
                    listar.append(f"{rp[1]}/{v}")
        
        with cf.ThreadPoolExecutor(max_workers=5) as executor:
            futura_izq = {executor.submit(self.descarga_img, li, dir_destino, dev_list[0]): li for li in listal}
            futura_der = {executor.submit(self.descarga_img, lr, dir_destino, dev_list[1]): lr for lr in listar}
        
        for fut, futur in zip(futura_izq, futura_der):
            fut, futur

if __name__ == 'main':
    Cam()