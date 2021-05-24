1) Crear un ambiente virtual con venv

```bash
python -m venv escaner
``` 

2) Activar el ambiente virtual

```
source escaner/bin/activate
```

3) Clonar el repositorio actualizado

```
git clone --recursive -j8 https://github.com/jairomelo/chdkptp.py.git
```

4) Entrar al repo

```
cd chdkptp.py
```

5) Instalar las dependencias

```
pip install -r requirements.txt
```

6) Preparar el paquete con el comando distutils

```
python setup.py sdist
```

7) Instalar el paquete

```
python setup.py install
```

8) Regresar al directorio principal

```
cd ..
```

9) Probar la instalación

```python
>>> import chdkptp
>>> chdkptp.list_devices()
[]
>>>
```

# USO


Para tomar fotografías (requiere dos cámaras). Desde el directorio `neo_escan` 

```python
>>> import shoot
>>> shoot.toma()
Guardada exitosamente la imagen imgs/img_00001.jpg
Guardada exitosamente la imagen imgs/img_00002.jpg
```

La función toma() acepta un parámetro para indicar la ruta del directorio para guardar las imágenes:

```python
>>> shoot.toma("mi_directorio")
Guardada exitosamente la imagen mi_directorio/img_00001.jpg
Guardada exitosamente la imagen mi_directorio/img_00002.jpg
```

# GUI

1) Instalar PySide2

```
pip install PySide2==5.15.2
```

o 

Instalar 

`pip install pyqt5 pyqt5-tools`