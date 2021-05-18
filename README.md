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


