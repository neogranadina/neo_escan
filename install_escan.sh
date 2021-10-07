echo iniciando instalación
cd ..

echo instalar dpendencias para LUA y chdkptp
sudo apt-get install libreadline-dev
sudo apt-get install libusb-dev
sudo apt autoremove

echo preparando LUA
curl -R -O http://www.lua.org/ftp/lua-5.2.4.tar.gz
tar zxf lua-5.2.4.tar.gz

echo aplicar patch a LUA
cp -f neo_escan/lua/Makefile lua-5.2.4/Makefile
cp -f neo_escan/lua/src/Makefile lua-5.2.4/src/Makefile

echo entrar a lua-5.2.4
cd lua-5.2.4

echo construir LUA
make linux
make test
sudo make install

echo instalar liblua
sudo apt install liblua5.2-dev

echo salir de lua-5.2.4 y entrar a neo_escan
cd ..
cd neo_escan

echo actualizar pip
python -m pip install --upgrade pip

echo preparar chdkptp.py
rm -rf chdkptp.py
git clone --recursive -j8  https://github.com/jairomelo/chdkptp.py.git

echo clonado el directorio chdkptp.py
cd chdkptp.py

echo en el directorio chdkptp.py. Instalar Lupa
pip install lupa --install-option='--no-luajit'

echo preparar la instalación
python setup.py sdist

echo instalar chdkptp.py
python setup.py install
cd ..

echo instalar dependencias
pip install -r requirements.txt

echo deshabilitar gphoto2 para evitar conflictos con chdkptp
sudo mv /usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service /usr/share/dbus-1/services/disable_org.gtk.vfs.GPhoto2VolumeMonitor.service
sudo mv /usr/share/gvfs/mounts/gphoto2.mount /usr/share/gvfs/disable_mounts/gphoto2.mount
sudo mv /usr/share/gvfs/remote-volume-monitors/gphoto2.monitor /usr/share/gvfs/remote-volume-monitors/disable_gphoto2.monitor
sudo mv /usr/lib/gvfs/gvfs-gphoto2-volume-monitor /usr/lib/gvfs/disable_gvfs-gphoto2-volume-monitor

