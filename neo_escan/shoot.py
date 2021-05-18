import chdkptp
import os
import base64

camaras = chdkptp.list_devices()

# device 1
# Conectar al dispositivo
try:
    dev_1 = chdkptp.ChdkDevice(camaras[0])
except IndexError:
    print("La cámara está apagada")
    raise

# device 2
# Conectar al dispositivo
try:
    dev_2 = chdkptp.ChdkDevice(camaras[1])
except IndexError:
    print("La cámara está apagada")
    raise

# cambiar a modo grabación

dev_1.switch_mode('record')
# cambiar a modo grabación

dev_2.switch_mode('record')



imgdata_1 = dev_1.shoot(stream=False, download_after=True, remove_after=True)

imgdata_2 = dev_2.shoot(stream=False, download_after=True, remove_after=True)

with open("img_3.jpg", "wb") as f:
    f.write(imgdata_1)


with open("img_4.jpg", "wb") as f:
    f.write(imgdata_2)
