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
python3 -m pip install --upgrade pip

echo preparar chdkptp.py
rm -rf chdkptp.py
git clone --recursive -j8  https://github.com/jairomelo/chdkptp.py.git

echo clonado el directorio chdkptp.py
cd chdkptp.py

echo en el directorio chdkptp.py. Instalar Lupa
pip3 install lupa --install-option='--no-luajit'

echo preparar la instalación
python3 setup.py sdist

echo instalar chdkptp.py
python3 setup.py install --user
cd ..

echo instalar pandas en Raspberry Pi
sudo apt-get install python3-pandas

echo instalar dependencias
pip3 install -r requirements.txt

echo instalar PySide2 en Raspberry Os:
sudo apt-get install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns python3-pyside2uic

echo deshabilitar gphoto2 para evitar conflictos con chdkptp
sudo mv /usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service /usr/share/dbus-1/services/disable_org.gtk.vfs.GPhoto2VolumeMonitor.service
sudo mv /usr/share/gvfs/mounts/gphoto2.mount /usr/share/gvfs/disable_mounts/gphoto2.mount
sudo mv /usr/share/gvfs/remote-volume-monitors/gphoto2.monitor /usr/share/gvfs/remote-volume-monitors/disable_gphoto2.monitor
sudo mv /usr/lib/gvfs/gvfs-gphoto2-volume-monitor /usr/lib/gvfs/disable_gvfs-gphoto2-volume-monitor

