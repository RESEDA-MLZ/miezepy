import unittest
from mock import Mock

from miezepy.core.fit_modules.fit_general import FitHandler
from miezepy.core.fit_modules.fit_mieze import Fit_MIEZE

class Test_FitHandler(unittest.TestCase):
    
    def setUp(self) -> None:
        self.handler  = FitHandler()
        self.handler.log.addLog('error', 'This is an error')
        self.handler.log.addLog('info', 'This is an info')
        self.handler.log.addLog('warning', 'This is an warning')
        
        self.handler.fun_dict['some_func'] = None
        self.handler.ptr_dict['some_ptr'] = 'some_routing_ptr'
        
    def test_loging(self):
        self.assertEqual('This is an error', self.handler['error'][1])
        self.assertEqual('This is an info', self.handler['info'][1])
        self.assertEqual('This is an warning', self.handler['warning'][1])
        
    def test_set_method(self):
        self.handler.set_method('some_func', 'some_ptr')
        self.assertEqual(self.handler['some_func'], 'some_routing_ptr')

    def test_parameter(self):
        self.assertEqual('some_func', self.handler.test_parameter('some_func', None, None, None))
        
class Test_Fit_MIEZE(unittest.TestCase):
    
    def setUp(self) -> None:
        self.handler  = Fit_MIEZE()
        self.target = Mock(
            get_axis=Mock(wraps=self.getAxis), 
            get_axis_len=Mock(wraps=self.getAxisLen))
        
    def getAxis(self, value):
        if value == self.handler.para_dict['para_name']:
            return ['para_name_0', 'para_name_1']
        if value == self.handler.para_dict['echo_name']:
            return ['echo_name_0', 'echo_name_1', 'echo_name_2']
        if value == self.handler.para_dict['foil_name']:
            return ['foil_name_0', 'foil_name_1', 'foil_name_2', 'foil_name_3']
        
    def getAxisLen(self, value):
        if value == self.handler.para_dict['para_name']:
            return 2
        if value == self.handler.para_dict['echo_name']:
            return 3
        if value == self.handler.para_dict['foil_name']:
            return 4

    def test_parameter_select(self):
        self.handler.para_dict['Select'] = 1
        self.assertRaises(Exception, self.handler.test_parameter, 'Select', self.target, None, None)
        
        self.handler.para_dict['Select'] = 'para_name_5'
        self.assertRaises(Exception, self.handler.test_parameter, 'Select', self.target, None, None)
        
        self.handler.para_dict['Select'] = ['all']
        self.assertEquals(
            self.getAxis(self.handler.para_dict['para_name']),
            self.handler.test_parameter('Select', self.target, None, None))
        
        self.handler.para_dict['Select'] = ['para_name_0']
        self.assertEquals(
            ['para_name_0'],
            self.handler.test_parameter('Select', self.target, None, None))
        
    def test_parameter_foils_in_echo(self):
        self.handler.para_dict['foils_in_echo'] = []
        self.assertRaises(Exception, self.handler.test_parameter, 'foils_in_echo', self.target, None, None)
        
        self.handler.para_dict['foils_in_echo'] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertRaises(Exception, self.handler.test_parameter, 'foils_in_echo', self.target, None, None)
        
        self.handler.para_dict['foils_in_echo'] = [[0, 0, 0, 0], [0, 0, 0], [0, 0]]
        self.assertRaises(Exception, self.handler.test_parameter, 'foils_in_echo', self.target, None, None)
        
        self.handler.para_dict['foils_in_echo'] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEquals(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            self.handler.test_parameter('foils_in_echo', self.target, None, None))
        
    def test_parameter_Background(self):
        self.handler.para_dict['Background'] = 'para_name_5'
        self.assertRaises(Exception, self.handler.test_parameter, 'Background', self.target, None, None)
        
        self.handler.para_dict['Background'] = 'para_name_0'
        self.assertEquals(
            'para_name_0',
            self.handler.test_parameter('Background', self.target, None, None))
        
    def test_parameter_Reference(self):
        self.handler.para_dict['Reference'] = 'para_name_5'
        self.assertRaises(Exception, self.handler.test_parameter, 'Reference', self.target, None, None)
        
        self.handler.para_dict['Reference'] = ['para_name_0']
        self.assertEquals(
            ['para_name_0'],
            self.handler.test_parameter('Reference', self.target, None, None))
        
    def test_parameter_NoTest(self):
        self.assertRaises(Exception, self.handler.test_parameter, 'NONE', self.target, None, None)
        
        