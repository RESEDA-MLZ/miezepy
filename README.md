[![Nosetests](https://github.com/RESEDA-MLZ/MIEZEPY/actions/workflows/miezepy_tests.yml/badge.svg)](https://github.com/RESEDA-MLZ/MIEZEPY/actions/workflows/miezepy_tests.yml)
# Mieze data management and reduction tool
Neutron Spin Echo software package

## Installation

Open a terminal window in the directory of the distribution and execute the following commands. The python requirements will be fetched from the requirements.txt file except two git bsed dependencies.

- Linux:
```
sudo apt-get install python3.7
sudo apt-get install python3-pip
sudo python setup.py install
```
        
- MacOs:
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
sudo python setup.py install
```
        
- Windows:
```
python setup.py install
```
        
## Running the package

<<<<<<< HEAD
The software can be launched from the python interpreter through 'from mieze_python.mieze import Mieze'. it is equally possible to launch it from a jupyter notebook using the same instruction. 
=======
The software can be launched from the python interpreter through 'from mieze_python.main import Manager as mieze'. it is equally possible to launch it from a jupyter notebook using the same instruction. Otherwise it is also possible to launch the program through: ```python miezepy.py```

>>>>>>> master
