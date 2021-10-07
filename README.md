# Escáner de Neogranadina *Nombre por definir :p

> :warning: Este programa requiere [Lua](http://www.lua.org/home.html), por lo que se recomienda su instalación en sistemas Unix (Ubuntu, Debian, Raspbian, Mac OS X).   

## Instalación

Para instalar esta versión en desarrollo, simplemente clonar este repo:

```shell
git clone https://github.com/neogranadina/neo_escan.git
```

Es sumamente recomendado crear un entorno virtual previamente:

```shell
python3 -m venv escan_env --system-site-packages
source escan_env/bin/activate
```

Ir al directorio del repositorio:

```shell
cd neo_escan
```

Posteriormente ejecutar `install_chdkptp.py.sh` para instalar `chdkptp.py`con todas las dependencias necesarias. Puede ser necesario cambiar los permisos para la instalación:

```shell
chmod +x install_chdkptp.py.sh
./install_chdkptp.py.sh
```

Instalar PySide2 en Raspberry Os:

```shell
apt-get install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns python3-pyside2uic
```

Lanzar la aplicación con

```shell
python main.py
```

## Contribuir al proyecto

Es posible contribuir a este proyecto proponiendo commits directamente a este repositorio.

### Proponer cambios a la interface gráfica de usuario (GUI)

Realizar estas modificaciones solamente al archivo `main.ui`. Se recomienda hacerlas desde 'Qt Designer', 'Qt Creator' o 'Qt Design Studio' para Qt6. Modificaciones en Qt5 deben asegurar la compatibilidad con Qt6, para ello se recomienda consultar el documento [Qt5 and Qt6 compatibility](https://doc-snapshots.qt.io/qt6-dev/cmake-qt5-and-qt6-compatibility.html).

Imágenes e íconos se vinculan desde el objeto `resources_rc.py`. Para proponer cambios añadirlos al archivo `resources.qrc` y realizar la conversión a binarios con `pyside2-rcc resources.qrc -o resources_rc.py`.

### Proponer cambios a la funcionalidad de la aplicación

Mejoras al comportamiento de la aplicación deberán proponerse para el archivo `main.py`. Propuestas para mejorar la interconectividad con la base de datos, pueden hacerse al archivo `db.py`.

### Cambios a la interacción con las cámaras

La conexión con las cámaras se realiza mediante la librería `chdkptp.py`. La versión que usa este aplicativo es <https://github.com/jairomelo/chdkptp.py>. Las mejoras deben ser propuestas directamente a ese repositorio.

> :point_right: Para otro tipo de modificación o resolución de problemas particulares, crear un *issue*.

## Solución de problemas

Algunos problemas identificados pueden consultarse en la [Wiki](https://github.com/neogranadina/neo_escan/wiki/Error-track) del proyecto.

## Atribución

Icons made by [Freepik](https://www.freepik.com) and [Pixel perfect](https://www.flaticon.com/authors/pixel-perfect) from [www.flaticon.com](https://www.flaticon.com/)
