[![Nosetests](https://github.com/RESEDA-MLZ/MIEZEPY/actions/workflows/miezepy_tests.yml/badge.svg)](https://github.com/RESEDA-MLZ/MIEZEPY/actions/workflows/miezepy_tests.yml)
# Mieze data management and reduction tool
Neutron Spin Echo software package

## Installation

We present installation directions for installation in a conda virtual environment, which works analogously between
linux and windows:

First extract the folder and navigate to it. The execute the following commands.
- Linux:
```
conda create --name miezepyenv python==3.7
conda activate miezepyenv
python -m pip install -U pip setuptools
python setup.py install
```

- MacOs (not sure about this one):
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
sudo python setup.py install
```

- Windows:
```
conda create --name miezepyenv python==3.7
conda activate miezepyenv
python -m pip install -U pip setuptools
python setup.py install
```

## Running the package

<<<<<<< HEAD
The software can be launched from the python interpreter through 'from mieze_python.mieze import Mieze'. it is equally possible to launch it from a jupyter notebook using the same instruction.
=======
The software can be launched from the python interpreter through 'from mieze_python.main import Manager as mieze'. it is equally possible to launch it from a jupyter notebook using the same instruction. Otherwise it is also possible to launch the program through: ```python miezepy.py```

>>>>>>> master
