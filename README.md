# Escáner de Neogranadina *Nombre por definir :p

> :warning: Este programa requiere [Lua](http://www.lua.org/home.html), por lo que se recomienda su instalación en sistemas Unix. El programa está construido para Raspberry Pi OS, pueden presentarse errores en Ubuntu, Debian u otras distribuciones de Linux.

## Instalación

En entornos de desarrollo es sumamente recomendado crear previamente un entorno virtual:

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

> :warning: En Raspberry es necesario reiniciar la máquina para que la aplicación corra sin errores.

Lanzar la aplicación con

```shell
python main.py
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
