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
#   Alexander Schober <alex.schober@mac.com>
#
# *****************************************************************************

#############################
#import main components
from .core.core_handler             import CoreHandler
from .gui.py_gui.window_handlers    import WindowHandler
import os

# python 10 fix
import collections
collections.Callable = collections.abc.Callable

import argparse
parser = argparse.ArgumentParser(description='Miezepy data analysis software for MIEZE measurements.')
parser.add_argument(
    "-p", 
    "--project_path",
    type=str,
    help="The location fo the project folder.",
    default=None)
parser.add_argument(
    "-d",
    "--data_paths",
    action='append',
    help="The location to look up data if not found in the initial paths.",
    default=[])
parser.add_argument(
    "-lm",
    "--load_masks",
    type=bool,
    help="Load the project associated data.",
    default=True)
parser.add_argument(
    "-ld",
    "--load_data",
    type=bool,
    help="Load the project associated masks.",
    default=True)
parser.add_argument(
    "-ls",
    "--load_scripts",
    type=bool,
    help="Load the project associated scripts.",
    default=True)
args = parser.parse_args()

class Mieze(CoreHandler):
    '''
    Here lies the main NSE tool manager class. It can be
    accessed in the python terminal through: 
    "from NSE.Main import Manager as NSE"
    '''

    def __init__(self, GUI = False):
        '''
        initialise app components
        '''
        self.success = False
        self.checkRessources()
        
        #initiate the core manager  
        CoreHandler.__init__(self)

        #initiate the GUI manager if need be
        if GUI == True:
            self.gui = WindowHandler()
            self.gui.initialize(self)

        self.success = True
        
        if args.project_path is not None:
            self.prepSessionLoad(
                args.project_path,
                data_bool=args.load_data,
                mask_bool=args.load_masks,
                script_bool=args.load_scripts,
                folder_list=args.data_paths
            )
            self.sessionLoad(False)
            self.gui.main_window.target.widgetClasses[0].refreshList()
             

    def checkRessources(self):
        '''
        The ressources are not part of the git package
        and may not be present on first launch. This littel
        function will try to lacate the files and then take
        the appropriate measures.
        '''
        base = str(os.path.realpath(__file__)).split(os.path.sep)[0:-1]

        #resources directory
        ressource_directory_path = os.path.realpath(os.path.sep.join(
            base + ['ressources', '']))
        if not os.path.isdir(ressource_directory_path):
            os.mkdir(ressource_directory_path)

        #the default post processing save path
        default_post_path = os.path.realpath(os.path.sep.join(
            base + ['ressources', 'default_post_path.txt']))
        if not os.path.isfile(default_post_path):
            with open(default_post_path,'w') as f:
                f.write('')

    def run(self, test = False):
        '''
        Execute the application upon initialization
        '''
        self.gui.run()

if __name__ == '__main__':

    app = Mieze(GUI = True)
    app.run()
