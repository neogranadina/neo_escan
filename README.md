# NeoScan

> :warning: Este programa requiere [Lua](http://www.lua.org/home.html), por lo que se recomienda su instalación en sistemas Unix. El programa está construido para Raspberry Pi OS 32 bit "Buster".

[Descargar la imagen de Raspberry desde este enlace](https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-full.zip)

Es importante también que se trabaje con un sistema de archivos expandido para permitir que el programa pueda modificar archivos de imagen.

Para ello, ejecutar el siguiente comando:

```shell
sudo raspi-config
```

Seleccionar "7 opciones avanzadas" y posteriormente “A1 Expand filesystem”.

## Instalación

En entornos de desarrollo es recomendado crear previamente un entorno virtual (opcional):

```shell
python3 -m venv escan_env --system-site-packages
source escan_env/bin/activate
```

Para instalar esta versión en desarrollo, simplemente clonar este repo:

```shell
git clone https://github.com/neogranadina/neo_escan.git
```

Ir al directorio del repositorio:

```shell
cd neo_escan
```

Posteriormente ejecutar `install_escan.sh` para instalar todas las dependencias necesarias. Puede ser necesario cambiar los permisos para la instalación:

```shell
chmod +x install_escan.sh
./install_escan.sh
```

> :warning: Se reiniciará el sistema después de ejecutar el script.

## Uso

> :warning: Antes de iniciar la aplicación, encienda ambas cámaras.

En el escritorio de Raspberry pi OS se crea el archivo `neo_escan.sh` que puede ser ejecutado directamente
o en una terminal.

También puede iniciarse la aplicación desde una terminal, desde el directorio de la aplicación:

```shell
cd ~/Public/neo_escan
python3 main.py
```

## Contribuir al proyecto

Es posible contribuir a este proyecto proponiendo commits directamente a este repositorio.

### Proponer cambios a la interface gráfica de usuario (GUI)

Realizar estas modificaciones solamente al archivo `main.ui`. Se recomienda hacerlas desde 'Qt Designer', 'Qt Creator' o 'Qt Design Studio' para **Qt5**. No se planea una actualización a Qt6 hasta que exista una versión estable de PySide6 compatible con Raspberry OS.

Es posible crear el objeto `Ui_MainWindow` directamente con PySide2, para ello simplemente correr el siguiente comando después de hacer los cambios en `main.ui`:

```shell
pyside2-uic main.ui > ui_main.py
```

> :warning: En Windows es posible que lance un error "ValueError: source code string cannot contain null bytes". Puede consultar una posible solución al error en <https://es.stackoverflow.com/a/322753>

### Proponer cambios a la funcionalidad de la aplicación

Mejoras al comportamiento de la aplicación deberán proponerse para el archivo `main.py`. Propuestas para mejorar la interconectividad con la base de datos, pueden hacerse al archivo `db.py`.

### Cambios a la interacción con las cámaras

La conexión con las cámaras se realiza mediante la librería `chdkptp.py`. La versión que usa este aplicativo es <https://github.com/jairomelo/chdkptp.py>. Las mejoras deben ser propuestas directamente a ese repositorio.

> :point_right: Para otro tipo de modificación o resolución de problemas particulares, crear un *issue*.

## Solución de problemas

Algunos problemas identificados pueden consultarse en la [Wiki](https://github.com/neogranadina/neo_escan/wiki/Error-track) del proyecto.

## Control de cambios

Desde la versión 0.1.429 del proyecto se ha documentado el control de cambios. Está disponible en [changelog.md](changelog.md)

## Logs

El archivo de logs se encuentra en `logs/neoscan_log.log` del directorio de la aplicación.

## Atribución

Icons made by [Freepik](https://www.freepik.com) and [Pixel perfect](https://www.flaticon.com/authors/pixel-perfect) from [www.flaticon.com](https://www.flaticon.com/)
