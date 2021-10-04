echo actualizar pip
python -m pip install --upgrade pip
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
