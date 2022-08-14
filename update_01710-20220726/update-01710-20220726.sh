#!/bin/bash

timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

touch /home/pi/Public/neo_escan/logs/update.txt
echo "Actualización 01710-202220726" >> /home/pi/Public/neo_escan/logs/update.txt
echo "Inicio de la actualización: $(timestamp)" >> /home/pi/Public/neo_escan/logs/update.txt

echo replace old files to /home/pi/Public/neo_escan
sudo cp -a $PWD/neo_escan /home/pi/Public
echo "Reemplazados los archivos nuevos" >> /home/pi/Public/neo_escan/logs/update.txt

echo install new requirements
python3 -m pip install -r /home/pi/Public/neo_escan/requirements.txt
echo "Instalados las nuevas librerías" >> /home/pi/Public/neo_escan/logs/update.txt

echo move config.cfg to /setup/config.cfg
sudo install -d -m 0777 /home/pi/Public/neo_escan/setup
sudo mv /home/pi/Public/neo_escan/config.cfg /home/pi/Public/neo_escan/setup/config.cfg
echo "Movido el archivo config.cfg" >> /home/pi/Public/neo_escan/logs/update.txt

echo create a direct access to neo_escan
echo delete old neo_escan.sh
sudo rm /home/pi/Desktop/neo_escan.sh

echo crear un ejecutable para el escáner
touch /home/pi/Desktop/neo_escan.sh
echo "#!/usr/bin/env bash" >> /home/pi/Desktop/neo_escan.sh
echo "echo abrir Neo Escan" >> /home/pi/Desktop/neo_escan.sh
echo "cd /home/pi/Public/neo_escan" >> /home/pi/Desktop/neo_escan.sh
echo "python3 main.py" >> /home/pi/Desktop/neo_escan.sh
chmod +x /home/pi/Desktop/neo_escan.sh
sudo mkdir /usr/share/neo-escan
sudo mv /home/pi/Desktop/neo_escan.sh /usr/share/neo-escan/neo_escan.sh

echo crear un archivo desktop para la aplicación
touch /home/pi/Desktop/neo_escan.desktop
echo "[Desktop Entry]" >> /home/pi/Desktop/neo_escan.desktop
echo "Encoding=UTF-8" >> /home/pi/Desktop/neo_escan.desktop
echo "Version=1.0" >> /home/pi/Desktop/neo_escan.desktop
echo "Type=Application" >> /home/pi/Desktop/neo_escan.desktop
echo "Terminal=false" >> /home/pi/Desktop/neo_escan.desktop
echo "Name[en]=NeoEscan" >> /home/pi/Desktop/neo_escan.desktop
echo "Comment[en]=Primary Sources Scanner" >> /home/pi/Desktop/neo_escan.desktop
echo "Name[es]=NeoEscan" >> /home/pi/Desktop/neo_escan.desktop
echo "Comment[es]=Escáner para fuentes primarias" >> /home/pi/Desktop/neo_escan.desktop
echo "Exec=/usr/share/neo-escan/neo_escan.sh" >> /home/pi/Desktop/neo_escan.desktop
echo "Icon=/home/pi/Public/neo_escan/imgs/logo.png" >> /home/pi/Desktop/neo_escan.desktop
echo "Category=Accesories;Image Capture;Production;" >> /home/pi/Desktop/neo_escan.desktop

sudo mv /home/pi/Desktop/neo_escan.desktop /usr/share/applications/neo_escan.desktop

echo "Creado el acceso directo" >> /home/pi/Public/neo_escan/logs/update.txt
echo "Actualización completa: $(timestamp)" >> /home/pi/Public/neo_escan/logs/update.txt

echo update config Version
python3 $PWD/update_scripts/update_version.py

echo deleting updating files
sudo rm -r $PWD
