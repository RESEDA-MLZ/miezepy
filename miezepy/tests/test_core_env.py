import unittest
import os
import sys
from PyQt5 import QtWidgets
import tempfile

from miezepy.core.module_environment import Environment
from miezepy.core.core_handler import CoreHandler

class Test_Environment(unittest.TestCase):
    handler = CoreHandler()

    def test_Environment_0(self):
        self.env = Environment(None, 'dummy')
        self.assertEqual(len(self.env.data), 1)
    
    def test_save_load(self):
        #self.app = QtWidgets.QApplication(sys.argv)
        
        ######################################################
        # Create realistic dataset
        self.save_env = self.handler.addEnv(title='hey')
        folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ressources', 'testsave', 'hto')
        self.handler.prepSessionLoad(folder, data_bool=True, mask_bool=True, script_bool=True, folder_list=[os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ressources')])
        self.handler.sessionLoad(False)
        
        data_sum = 0
        for data_object in self.handler.current_env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)
        
        ######################################################
        # Save to temp directory
        tempdir = tempfile.mkdtemp(prefix="miezepy-")
        self.handler.saveSession(tempdir, data_bool=True, mask_bool=True, script_bool=True)
        
        ######################################################
        # Save to temp directory
        self.load_env = self.handler.addEnv(title='ho')
        self.handler.prepSessionLoad(tempdir, data_bool=True, mask_bool=True, script_bool=True)
        self.handler.sessionLoad(False)
        
        data_sum = 0
        for data_object in self.handler.current_env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)
        
    def test_grab(self): 
        #self.app = QtWidgets.QApplication(sys.argv)
        
        ######################################################
        # Create realistic dataset
        self.from_env = self.handler.addEnv(title='from_env')
        folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ressources', 'testsave', 'hto')
        self.handler.prepSessionLoad(folder, data_bool=True, mask_bool=True, script_bool=True, folder_list=[os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ressources')])
        self.handler.sessionLoad(False)
        
        data_sum = 0
        for data_object in self.handler.current_env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)
        
        self.to_env = self.handler.addEnv(title='to_env')
        
        self.handler.processOperation('hto', 'data', 'to_env')
        self.handler.processOperation('hto', 'mask', 'to_env')
        self.handler.processOperation('hto', 'scripts', 'to_env')
        self.to_env.io.generate()
        
        data_sum = 0
        for data_object in self.handler.current_env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)
        
