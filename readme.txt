install kivy:

python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv
kivy_venv\Scripts\activate
source kivy_venv/Scripts/activate
source kivy_venv/bin/activate

python -m pip install "kivy[base,media]" kivy_examples

or

python -m pip install "kivy[full]" kivy_examples

or 

python -m pip install "kivy[base,media] @ https://github.com/kivy/kivy/archive/master.zip"

or

python -m pip install --pre "kivy[base,media]" kivy_examples

or

python -m pip install kivy --pre --no-deps --index-url  https://kivy.org/downloads/simple/
python -m pip install "kivy[base,media]" --pre --extra-index-url https://kivy.org/downloads/simple/

or

Development install:

git clone git://github.com/kivy/kivy.git
cd kivy
python -m pip install -e ".[dev,full]"
python setup.py build_ext --inplace


CREATE APP:
in app folder in terminal:
buildozer init


