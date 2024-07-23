import unittest
import os
from miezepy.core.module_scripts import ScriptStructure

class Test_Scripts(unittest.TestCase):
    def setUp(self) -> None:
        self.scrip_structure = ScriptStructure()

    def test_Init(self):
    
        self.default_scripts = []
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'import_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'set_fit_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core', 'script_modules', 'phase_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'reduction_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'post_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
            
        self.assertEquals(self.default_scripts, self.scrip_structure.default_scripts)
        
    def test_Reset(self):
    
        self.default_scripts = []
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'import_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'set_fit_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core', 'script_modules', 'phase_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'reduction_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'post_process.py'), 'r') as f:
            self.default_scripts.append(f.read())
            
        self.scrip_structure.editable_scripts  = ['not', 'the', 'real', 'thing', '...']
        self.assertNotEquals(self.default_scripts, self.scrip_structure.editable_scripts )
        
        [self.scrip_structure.resetScript(i) for i in range(5)]
        
        self.assertEquals(self.default_scripts, self.scrip_structure.editable_scripts)
        
    def test_Reformat(self):
        
        text_array = []
        text_array.append('add_metadata')
        text_array.append('get_result')
        text_array.append('calculate_echo')
        text_array.append('calculate_shift')
        text_array.append('calculate_ref_contrast')
        text_array.append('calculate_contrast')
        text_array.append('environnement.process.remove_foils()\n')
        text = ' '.join(text_array)
        
        text = self.scrip_structure.reformatScript(text)
        for text_element in text_array:
            self.assertNotIn(text_element, text)
            
    def test_ReadFromScripts(self):
        
        comparison_dict = {
            'foils_in_echo': [
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0]],
            'Selected': [278.0, 288.0, 300.0, 313.0, 328.0],
            'Reference': ['Reso', 0],
            'Background': None,
            'foil_check': [1, 1, 1, 1, 1, 1, 1, 1],
            'phase_mask': 'Pre_SkX_peak_Sixfold',
            'reduction_mask': 'SkX_peak_Sixfold',
            'instrument': 'Reseda',
            'detector': 14032019,
            'exposure': False,
            'time_channels': [],
            'sum_foils': True}
        
        output_dict = self.scrip_structure.readFromScripts()
        self.assertDictEqual(comparison_dict, output_dict)

    def test_parseCode(self):
        
        comparisson_code_array = [
            'environnement = self.env',
            'foils_in_echo = []',
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])', 
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 0, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 0, 1, 1, 1])',
            'foils_in_echo.append([0, 0, 0, 0, 1, 0])',
            'foils_in_echo.append([0, 0, 0, 0, 1, 0])',
            'Selected = [ 278.0, 288.0, 300.0, 313.0, 328.0]',
            'TimeChannels = []',
            'Background = None',
            "Reference = ['Reso',0]",
            "instrument = 'Reseda'",
            'detector = 14032019',
            'exposure = False',
            'sum_foils = True',
            "environnement.fit.set_parameter( name = 'Select',        value = Selected     )",
            "environnement.fit.set_parameter( name = 'Reference',     value = Reference    )",
            "environnement.fit.set_parameter( name = 'Background',    value = Background   )",
            "environnement.fit.set_parameter( name = 'foils_in_echo', value = foils_in_echo)",
            "environnement.fit.set_parameter( name = 'processors',    value = 1)",
            "environnement.fit.set_parameter( name = 'exposure',      value = exposure)",
            "environnement.fit.set_parameter( name = 'time_channels', value = TimeChannels)",
            "environnement.fit.set_parameter( name = 'sum_foils',     value = sum_foils)",
            'environnement.instrument.setDetector(instrument, detector)']
        
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'set_fit_process.py'), 'r') as f:
            self.default_scripts = f.read()
            
        code_array = self.scrip_structure._parseCode(self.default_scripts)
        
        self.assertEquals(comparisson_code_array, code_array)
        
    def test_parseMeta(self):
        
        comparisson_meta_array = [
            'environnement = self.env',
            'foils_in_echo = []',
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])", 
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])", 
            "'function' foils_in_echo.append with the parameters ([1, 1, 0, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([1, 1, 0, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([0, 0, 0, 0, 1, 0])",
            "'function' foils_in_echo.append with the parameters ([0, 0, 0, 0, 1, 0])",
            'Selected = [ 278.0, 288.0, 300.0, 313.0,',
            'TimeChannels = []',
            'Background = None',
            "Reference = ['Reso',0]",
            "instrument = 'Reseda'",
            'detector = 14032019',
            'exposure = False', 'sum_foils = True',
            "'function' environnement.fit.set_parameter with the parameters ( name = 'Select',        value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'Reference',     value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'Background',    value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'foils_in_echo', value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'processors',    value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'exposure',      value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'time_channels', value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'sum_foils',     value)",
            "'function' environnement.instrument.setDetector with the parameters (instrument, detector)"]
        
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', 'core','script_modules', 'set_fit_process.py'), 'r') as f:
            self.default_scripts = f.read()
            
        code_array = self.scrip_structure._parseCode(self.default_scripts)
        meta_array = self.scrip_structure._parseMeta(code_array)
        
        self.assertEquals(comparisson_meta_array, meta_array)

    def test_preprocessScript(self):
        
        comparisson_code_array = [
            'environnement = self.env',
            'foils_in_echo = []',
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])', 
            'foils_in_echo.append([1, 1, 1, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 0, 1, 1, 1])',
            'foils_in_echo.append([1, 1, 0, 1, 1, 1])',
            'foils_in_echo.append([0, 0, 0, 0, 1, 0])',
            'foils_in_echo.append([0, 0, 0, 0, 1, 0])',
            'Selected = [ 278.0, 288.0, 300.0, 313.0, 328.0]',
            'TimeChannels = []',
            'Background = None',
            "Reference = ['Reso',0]",
            "instrument = 'Reseda'",
            'detector = 14032019',
            'exposure = False',
            'sum_foils = True',
            "environnement.fit.set_parameter( name = 'Select',        value = Selected     )",
            "environnement.fit.set_parameter( name = 'Reference',     value = Reference    )",
            "environnement.fit.set_parameter( name = 'Background',    value = Background   )",
            "environnement.fit.set_parameter( name = 'foils_in_echo', value = foils_in_echo)",
            "environnement.fit.set_parameter( name = 'processors',    value = 1)",
            "environnement.fit.set_parameter( name = 'exposure',      value = exposure)",
            "environnement.fit.set_parameter( name = 'time_channels', value = TimeChannels)",
            "environnement.fit.set_parameter( name = 'sum_foils',     value = sum_foils)",
            'environnement.instrument.setDetector(instrument, detector)']
        
        comparisson_meta_array = [
            'environnement = self.env',
            'foils_in_echo = []',
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])", 
            "'function' foils_in_echo.append with the parameters ([1, 1, 1, 1, 1, 1])", 
            "'function' foils_in_echo.append with the parameters ([1, 1, 0, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([1, 1, 0, 1, 1, 1])",
            "'function' foils_in_echo.append with the parameters ([0, 0, 0, 0, 1, 0])",
            "'function' foils_in_echo.append with the parameters ([0, 0, 0, 0, 1, 0])",
            'Selected = [ 278.0, 288.0, 300.0, 313.0,',
            'TimeChannels = []',
            'Background = None',
            "Reference = ['Reso',0]",
            "instrument = 'Reseda'",
            'detector = 14032019',
            'exposure = False', 'sum_foils = True',
            "'function' environnement.fit.set_parameter with the parameters ( name = 'Select',        value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'Reference',     value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'Background',    value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'foils_in_echo', value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'processors',    value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'exposure',      value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'time_channels', value)",
            "'function' environnement.fit.set_parameter with the parameters ( name = 'sum_foils',     value)",
            "'function' environnement.instrument.setDetector with the parameters (instrument, detector)"]
        
        code_array, meta_array = self.scrip_structure.preprocessScript(1)
        
        self.assertEquals(comparisson_code_array, code_array)
        self.assertEquals(comparisson_meta_array, meta_array)
        
    def test_synthetize(self):
        input_dict = {
            'foils_in_echo': [
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]],
            'selected': [278.0, 1.0, 300.0, 313.0, 328.0],
            'Reference': '["Reso_test", 0]',
            'Background': '"Reso_test"',
            'foil_check': [1, 1, 1, 1, 1, 1, 1, 1],
            'mask': 'Pre_SkX_peak_Sixfold_1',
            'Instrument': 'Reseda_1',
            'detector': str(140320195),
            'exposure': 'True',
            'time_channels': '[1]',
            'sum_foils': 'False'}
        
        comparison_dict = {
            'foils_in_echo': [
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [1, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]],
            'Selected': [278.0, 1.0, 300.0, 313.0, 328.0],
            'Reference': ['Reso_test', 0],
            'Background': 'Reso_test',
            'foil_check': [1, 1, 1, 1, 1, 1, 1, 1],
            'phase_mask': 'Pre_SkX_peak_Sixfold_1',
            'reduction_mask': 'Pre_SkX_peak_Sixfold_1',
            'instrument': 'Reseda_1',
            'detector': 140320195,
            'exposure': True,
            'time_channels': [1],
            'sum_foils': False}
        
        self.scrip_structure.synthesizeDataScript(input_dict)
        self.scrip_structure.synthesizeFitScript(input_dict)
        self.scrip_structure.synthesizePhaseScript(input_dict)
        self.scrip_structure.synthesizeReductionScript(input_dict)
        
        output = self.scrip_structure.readFromScripts()
        self.assertDictEqual(comparison_dict, output)
        