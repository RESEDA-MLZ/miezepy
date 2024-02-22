#  -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2017 by the NSE analysis contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Alexander Schober <alexander.schober@mac.com>
#
# *****************************************************************************

from setuptools import setup, find_packages
import subprocess
import miezepy
import pip
import os
from io import BytesIO

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for line in lines:
    subprocess.run(['python', '-m', 'pip', 'install', line])
    #pip.main(['install', line]) deprecated?

try:
    import simpleplot
except:
    import requests
    import zipfile
    url = "https://github.com/AlexanderSchober/simpleplot_qt/archive/refs/heads/master.zip"
    req = requests.get(url)
    zipfile = zipfile.ZipFile(BytesIO(req.content))
    zipfile.extractall(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'simpleplot_qt'))
    path = os.getcwd()
    os.chdir(os.path.join(os.path.dirname(os.path.realpath(
        __file__)), 'simpleplot_qt', 'simpleplot_qt-master'))
    os.system('python setup.py install')
    os.chdir(os.path.join(os.path.dirname(os.path.realpath(
        __file__))))

setup(
    name='miezepy',
    version=miezepy.__version__,
    license='GPL',
    author='Dr. Alexander Schober',
    author_email='alex.schober@mac.com',
    description='Mieze analysis package',
    packages=find_packages(exclude=['doc', 'test']),
    package_data={
        'miezepy': ['RELEASE-VERSION'],
        'miezepy.core.process_modules.defaults': ['*.txt'],
        'miezepy.core.instrument_modules.Reseda': ['*.npy']},

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Physics',
    ],
)
