# Escáner de Neogranadina *Nombre por definir :p

> :warning: Este programa requiere [Lua](http://www.lua.org/home.html), por lo que se recomienda su instalación en sistemas Unix (Ubuntu, Debian, Raspbian, Mac OS X). Para Windows es necesario [compilar Lua](http://lua-users.org/wiki/BuildingLua) o simplemente intentar con [Lua Rocks](https://github.com/luarocks/luarocks/wiki/Installation-instructions-for-Windows)  

## Instalación

Para instalar esta versión en desarrollo, simplemente clonar este repo:

```shell
git clone https://github.com/neogranadina/neo_escan.git
```

Es sumamente recomendado crear un entorno virtual previamente:

```shell
python -m venv escan_env
source escan_env/bin activate
```

Posteriormente ejecutar `install_chdkptp.py.sh` para instalar `chdkptp.py` y `PySide6` con todas las dependencias necesarias.

```shell
./install_chdkptp.py.sh
```

Lanzar la aplicación con

```shell
python main.py
```

## Contribuir al proyecto

Es posible contribuir a este proyecto proponiendo commits directamente a este repositorio.

### Proponer cambios a la interface gráfica de usuario (GUI)

Realizar estas modificaciones solamente al archivo `main.ui`. Se recomienda hacerlas desde 'Qt Designer', 'Qt Creator' o 'Qt Design Studio' para Qt6. Modificaciones en Qt5 deben asegurar la compatibilidad con Qt6, para ello se recomienda consultar el documento [Qt5 and Qt6 compatibility](https://doc-snapshots.qt.io/qt6-dev/cmake-qt5-and-qt6-compatibility.html).

### Proponer cambios a la funcionalidad de la aplicación

Mejoras al comportamiento de la aplicación deberán proponerse para el archivo `main.py`. Propuestas para mejorar la interconectividad con la base de datos, pueden hacerse al archivo `db.py`.

### Cambios a la interacción con las cámaras

La conexión con las cámaras se realiza mediante la librería `chdkptp.py`. La versión que usa este aplicativo es <https://github.com/jairomelo/chdkptp.py>. Las mejoras deben ser propuestas directamente a ese repositorio.

> :point_right: Para otro tipo de modificación o resolución de problemas particulares, crear un *issue*.

## Solución de problemas

Algunos problemas identificados pueden consultarse en la [Wiki](https://github.com/neogranadina/neo_escan/wiki/Error-track) del proyecto.
