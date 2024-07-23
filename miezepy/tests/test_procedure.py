import unittest
import numpy as np
import time
from pathlib import Path
import os
import sys
from PyQt5 import QtWidgets
from miezepy.core.module_data import DataStructure
from miezepy.core.module_environment import Environment


def createFakeDataset():
    data = DataStructure()

    loop = [(i, j, k, l)
            for i in range(0, 10)
            for j in range(0, 10)
            for k in range(0, 6)
            for l in range(0, 16)]

    loop_2 = [(j, k, l)
              for j in range(0, 10)
              for k in range(0, 6)
              for l in range(0, 16)]

    meta_dict = {}
    meta_dict['Wavelength'] = ['Wavelength', 'float', 6e-10, ""]
    meta_dict['Freq. first'] = ['Freq. first', 'float', 30, ""]
    meta_dict['Freq. second'] = ['Freq. second', 'float', 60, ""]
    meta_dict['lsd'] = ['lsd', 'float', 1200e9, ""]
    meta_dict['Monitor'] = ['Monitor', 'float', 100, ""]

    for i, j, k, l in loop:
        if k == 0 and l == 0:
            meta_dict['Freq. second'] = ['Freq. second', 'float', (60 + j), ""]
            data.addMetadataObject(meta_dict)
        data[i, 0, j, k, l] = generateMap([i, 0, j, k, l])

    for j, k, l in loop_2:
        if k == 0 and l == 0:
            meta_dict['Freq. second'] = ['Freq. second', 'float', (60 + j), ""]
            data.addMetadataObject(meta_dict)
        data[0, 1, j, k, l] = generateMap([0, 1, j, k, l])

    for j, k, l in loop_2:
        if k == 0 and l == 0:
            meta_dict['Freq. second'] = ['Freq. second', 'float', (60 + j), ""]
            data.addMetadataObject(meta_dict)
        data[1, 1, j, k, l] = generateMap([1, 1, j, k, l])

    data.metadata_class.addMetadata(
        'Creation date', value=str(time.ctime()), logical_type='str')
    data.metadata_class.addMetadata(
        'Source format', value="ToF files", logical_type='str')
    data.metadata_class.addMetadata(
        'Measurement type', value="MIEZE", logical_type='float')
    data.metadata_class.addMetadata(
        'Wavelength error', value=0.117, logical_type='float')
    data.metadata_class.addMetadata(
        'Distance error', value=0.0005, logical_type='float')
    data.metadata_class.addMetadata(
        'R_1', value=9., logical_type='float', unit='m')
    data.metadata_class.addMetadata(
        'R_2', value=5., logical_type='float', unit='m')
    data.metadata_class.addMetadata(
        'L_1', value=1200, logical_type='float', unit='m')
    data.metadata_class.addMetadata(
        'L_2', value=3500, logical_type='float', unit='m')
    data.metadata_class.addMetadata(
        'Wavelength in', value=6., logical_type='float', unit='A')
    data.metadata_class.addMetadata(
        'Pixel size', value=1.5625, logical_type='float', unit='mum')
    data.metadata_class.addMetadata(
        'Qy', value=0.035, logical_type='float', unit='-')

    return data


def generateMap(map_input):
    return np.fromfunction(
        lambda i, j: 100 + 50*np.sin((i-64)+(j-64)+map_input[-1]/16*2*np.pi),
        (128, 128),
        dtype=int)


def createHTO(proc):

    env = Environment(None, 'test_phase')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    env.io.load_MIEZE_TOF(os.path.join(dir_path, 'ressources', 'LoadTest.txt'))
    env.data[0].axes.set_name(0, 'Parameter')
    env.data[0].axes.set_name(1, 'Measurement')
    env.data[0].axes.set_name(2, 'Echo Time')
    env.data[0].axes.set_name(3, 'Foil')
    env.data[0].axes.set_name(4, 'Time Channel')
    env.setCurrentData()

    # process the echos
    for meta_object in env.current_data.metadata_objects:
        meta_object.addMetadata(
            'Wavelength', value=8.e-10, logical_type='float', unit='A')

    env.mask.mask_dict["HTO_1"] = [{
        "Visible": ["Visible", "bool", True],
        "Position": {
            "x": ["x", "float", 63.5],
            "y": ["y", "float", 63.5],
            "z": ["z", "float", 0.0]},
        "Movable": ["Movable", "bool", False],
        "Angle": ["Angle", "float", 0.0],
        "Z": ["Z", "int", 0],
        "Dimensions": {
            "x": ["x", "float", 128.0],
            "y": ["y", "float", 128.0]},
        "Subdivisions": {
            "x": ["x", "int", 16],
            "y": ["y", "int", 16]},
        "Subdivision dimensions": {
            "Fill": ["Fill", "bool", True],
            "x": ["x", "float", 2.0],
            "y": ["y", "float", 2.0]},
        "Fill": {
            "0": ["0", "bool", True],
            "1": ["1", "color", [0, 0, 255, 255]]},
        "Line": {
            "Visible": ["Visible", "bool", True],
            "Thickness": ["Thickness", "float", 0.05],
            "Color": ["Color", "color", [0, 0, 0, 255]]},
        "Draw faces": ["Draw faces", "bool", True],
        "Draw edges": ["Draw edges", "bool", False],
        "Draw smooth": ["Draw smooth", "bool", True],
        "OpenGl mode": ["OpenGl mode", "str", "opaque"],
        "Name": "Mask Element", "Type": "Rectangle"}]

    env.mask.mask_dict["HTO_2"] = [{
        "Visible": ["Visible", "bool", True],
        "Position": {
            "x": ["x", "float", 63.5],
            "y": ["y", "float", 63.5],
            "z": ["z", "float", 0.0]},
        "Movable": ["Movable", "bool", False],
        "Angle": ["Angle", "float", 0.0], "Z": ["Z", "int", 0],
        "Dimensions": {
            "x": ["x", "float", 128.0],
            "y": ["y", "float", 128.0]},
        "Subdivisions": {
            "x": ["x", "int", 1],
            "y": ["y", "int", 1]},
        "Subdivision dimensions": {
            "Fill": ["Fill", "bool", True],
            "x": ["x", "float", 2.0],
            "y": ["y", "float", 2.0]},
        "Fill": {
            "0": ["0", "bool", True],
            "1": ["1", "color", [0, 0, 255, 255]]},
        "Line": {
            "Visible": ["Visible", "bool", True],
            "Thickness": ["Thickness", "float", 0.05],
            "Color": ["Color", "color", [0, 0, 0, 255]]},
        "Draw faces": ["Draw faces", "bool", True],
        "Draw edges": ["Draw edges", "bool", False],
        "Draw smooth": ["Draw smooth", "bool", True],
        "OpenGl mode": ["OpenGl mode", "str", "opaque"],
        "Name": "Mask Element", "Type": "Rectangle"}]

    foils_in_echo = []
    foils_in_echo.append([0, 0, 0, 0, 0, 0, 0, 1])
    foils_in_echo.append([0, 0, 0, 0, 0, 0, 0, 1])
    foils_in_echo.append([0, 0, 0, 0, 0, 0, 0, 1])

    # set the values to be processed as data
    Selected = ['reso', '5K', '50K']

    # set the reference value
    Reference = ['reso', 0]

    # set the background
    Background = None

    dir_path = os.path.dirname(os.path.realpath(__file__))
    foil_0 = np.loadtxt(os.path.join(
        dir_path, 'ressources', 'foilheight_final0.txt'))
    foil_1 = np.loadtxt(os.path.join(
        dir_path, 'ressources', 'foilheight_final1.txt'))
    foil_2 = np.loadtxt(os.path.join(
        dir_path, 'ressources', 'foilheight_final2.txt'))
    foil_5 = np.loadtxt(os.path.join(
        dir_path, 'ressources', 'foilheight_final3.txt'))
    foil_6 = np.loadtxt(os.path.join(
        dir_path, 'ressources', 'foilheight_final4.txt'))
    foil_7 = np.loadtxt(os.path.join(
        dir_path, 'ressources', 'foilheight_final5.txt'))

    surface_profile = [
        foil_0,
        foil_1,
        foil_2,
        np.zeros(foil_0.shape),
        np.zeros(foil_0.shape),
        foil_5,
        foil_6,
        foil_7
    ]

    surface_profile = np.array(surface_profile)

    env.fit.set_parameter(name='Select',           value=Selected)
    env.fit.set_parameter(name='Reference',        value=Reference)
    env.fit.set_parameter(name='Background',       value=Background)
    env.fit.set_parameter(name='foils_in_echo',    value=foils_in_echo)
    env.fit.set_parameter(name='surface_profile',  value=surface_profile)
    env.fit.set_parameter(name='processors',       value=proc)
    
    env.io.path = Path(__file__).resolve().parent

    return env


class TestPhaseCorrection(unittest.TestCase):

    @unittest.skipIf(("CI" in os.environ and os.environ["CI"] == "true"), "Skipping this test on CI.")
    def TestPhaseCorrection_mask(self):
        self.env = Environment(None, 'test_phase')
        self.env.data[0] = createFakeDataset()
        self.env.data[0].validate()
        self.env.data[0].axes.set_name(0, 'Parameter')
        self.env.data[0].axes.set_name(1, 'Measurement')
        self.env.data[0].axes.set_name(2, 'Echo Time')
        self.env.data[0].axes.set_name(3, 'Foil')
        self.env.data[0].axes.set_name(4, 'Time Channel')
        self.env.setCurrentData()

        environnement = self.env
        foils_in_echo = []
        foils_in_echo.append([1, 1, 1, 1, 1, 1])
        foils_in_echo.append([1, 1, 1, 1, 1, 1])
        foils_in_echo.append([1, 1, 1, 1, 1, 1])
        foils_in_echo.append([1, 1, 1, 1, 1, 1])
        foils_in_echo.append([1, 1, 0, 1, 1, 1])
        foils_in_echo.append([1, 1, 0, 1, 1, 1])
        foils_in_echo.append([0, 0, 0, 0, 1, 0])
        foils_in_echo.append([0, 0, 0, 0, 1, 0])
        foils_in_echo.append([0, 0, 0, 0, 1, 0])
        foils_in_echo.append([0, 0, 0, 0, 1, 0])

        # set the values to be processed as data
        Selected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # set the reference value
        Reference = [0, 0]

        # set the background
        Background = 0

        environnement.fit.set_parameter(name='Select',        value=Selected)
        environnement.fit.set_parameter(name='Reference',     value=Reference)
        environnement.fit.set_parameter(name='Background',    value=Background)
        environnement.fit.set_parameter(
            name='foils_in_echo', value=foils_in_echo)

        # override mask
        self.env.mask.mask = np.fromfunction(
            lambda i, j: (i+j*16), (16, 16), dtype=int)
        self.env.mask.mask = np.kron(
            self.env.mask.mask, np.ones((8, 8), dtype=int))

        # process the echos
        self.env.process.calculateEcho()
        self.assertEqual(
            self.env.current_data.metadata_objects[0]['tau'], 0.09937249956783661)

        # proceed with the buffering
        self.env.process.prepareBuffer()
        self.assertEqual(self.env.current_data.bufferedData.shape,
                         (10, 2, 10, 6, 16, 128, 128))
        self.assertEqual(self.env.current_data.bufferedData.__getitem__(
            (0, 0)).shape, (10, 6, 16, 128, 128))

        # do the phase calculation
        self.env.fit.extractPhaseMask(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        # check the result
        result = self.env.results.getLastResult('Phase calculation')['Phase']
        keys = [key for key in result.keys()]
        self.assertEqual(int(result[keys[0]].sum()), 305827)

        # correct the phase
        self.env.fit.correctPhase(
            self.env.current_data,
            self.env.mask,
            self.env.results)
        result = self.env.results.getLastResult('Corrected Phase')['Shift']
        keys = [key for key in result.keys()]
        self.assertEqual(int(
            result[0][0][self.env.current_data.get_axis('Echo Time')[0]].sum()), 156672000)

    @unittest.skipIf(("CI" in os.environ and os.environ["CI"] == "true"), "Skipping this test on CI.")
    def TestPhaseCorrection_exposure(self):
        self.env = Environment(None, 'test_phase')
        self.env.data[0] = createFakeDataset()
        self.env.data[0].validate()
        self.env.data[0].axes.set_name(0, 'Parameter')
        self.env.data[0].axes.set_name(1, 'Measurement')
        self.env.data[0].axes.set_name(2, 'Echo Time')
        self.env.data[0].axes.set_name(3, 'Foil')
        self.env.data[0].axes.set_name(4, 'Time Channel')
        self.env.setCurrentData()
        self.env.instrument.setDetector('Reseda', 14032019)

        environnement = self.env
        foils_in_echo = []
        foils_in_echo.append([1, 1, 1, 0, 0, 1, 1, 1])
        foils_in_echo.append([1, 1, 1, 0, 0, 1, 1, 1])
        foils_in_echo.append([1, 1, 1, 0, 0, 1, 1, 1])
        foils_in_echo.append([1, 1, 1, 0, 0, 1, 1, 1])
        foils_in_echo.append([1, 1, 0, 0, 0, 1, 1, 1])
        foils_in_echo.append([1, 1, 0, 0, 0, 1, 1, 1])
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 1, 0])
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 1, 0])
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 1, 0])
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 1, 0])

        # set the values to be processed as data
        Selected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # set the reference value
        Reference = [0, 0]

        # set the background
        Background = 0

        dir_path = os.path.dirname(os.path.realpath(__file__))
        foil_0 = np.loadtxt(os.path.join(
            dir_path, 'ressources', 'foilheight_final0.txt'))
        foil_1 = np.loadtxt(os.path.join(
            dir_path, 'ressources', 'foilheight_final1.txt'))
        foil_2 = np.loadtxt(os.path.join(
            dir_path, 'ressources', 'foilheight_final2.txt'))
        foil_5 = np.loadtxt(os.path.join(
            dir_path, 'ressources', 'foilheight_final3.txt'))
        foil_6 = np.loadtxt(os.path.join(
            dir_path, 'ressources', 'foilheight_final4.txt'))
        foil_7 = np.loadtxt(os.path.join(
            dir_path, 'ressources', 'foilheight_final5.txt'))
        surface_profile = [
            foil_0,
            foil_1,
            foil_2,
            np.zeros(foil_0.shape),
            np.zeros(foil_0.shape),
            foil_5,
            foil_6,
            foil_7
        ]
        surface_profile = np.array(surface_profile)

        environnement.fit.set_parameter(
            name='Select',           value=Selected)
        environnement.fit.set_parameter(
            name='Reference',        value=Reference)
        environnement.fit.set_parameter(
            name='Background',       value=Background)
        environnement.fit.set_parameter(
            name='foils_in_echo',    value=foils_in_echo)
        environnement.fit.set_parameter(
            name='surface_profile',  value=surface_profile)

        # override mask
        self.env.mask.mask = np.fromfunction(
            lambda i, j: (i+j*16), (16, 16), dtype=int)
        self.env.mask.mask = np.kron(
            self.env.mask.mask, np.ones((8, 8), dtype=int))

        # process the echos
        self.env.process.calculateEcho()
        self.assertEqual(
            self.env.current_data.metadata_objects[0]['tau'], 0.09937249956783661)

        # proceed with the buffering
        self.env.process.prepareBuffer()
        self.assertEqual(self.env.current_data.bufferedData.shape,
                         (10, 2, 10, 6, 16, 128, 128))
        self.assertEqual(self.env.current_data.bufferedData.__getitem__(
            (0, 0)).shape, (10, 6, 16, 128, 128))

        # do the phase calculation
        self.env.fit.correctPhaseExposure(
            self.env.current_data,
            self.env.mask,
            self.env.instrument,
            self.env.results)

        result = self.env.results.getLastResult('Corrected Phase')['Shift']
        self.assertEqual(int(
            result[0][0][self.env.current_data.get_axis('Echo Time')[0]].sum()), 157286400)

        self.env.mask.mask = np.zeros((128, 128))
        self.env.mask.mask[32:92, 32:92] = 1

        self.env.fit.calcContrastRef(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        result = self.env.results.getLastResult(
            'Reference contrast calculation')

        self.env.fit.calcContrastMain(
            self.env.current_data,
            self.env.mask,
            self.env.results,
            select=self.env.current_data.get_axis('Parameter'))

        self.env.fit.contrastFit(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        self.result = self.env.results.getLastResult('Contrast fit')[
            'Parameters']

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def test_single_proc_mask_data(self):
        self.phase_correction_mask_data(1)

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def test_multi_proc_mask_data(self):
        self.phase_correction_mask_data(12)

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def test_single_proc_exposure_data_summation_on(self):
        self.phase_correction_exposure_data_summation_on(1)

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def test_multi_proc_exposure_data_summation_on(self):
        self.phase_correction_exposure_data_summation_on(12)

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def test_single_proc_exposure_data_summation_off(self):
        self.phase_correction_exposure_data_summation_off(1)

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def test_multi_proc_exposure_data_summation_off(self):
        self.phase_correction_exposure_data_summation_off(12)

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def phase_correction_mask_data(self, proc):
        #self.app = QtWidgets.QApplication(sys.argv)
        ######################################################
        # test the dataset
        self.env = createHTO(proc)
        data_sum = 0
        for data_object in self.env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)

        ######################################################
        # Prepare the phase process
        self.env.mask.setMask("HTO_1")
        self.env.mask.generateMask(128, 128)
        self.env.process.calculateEcho()
        self.env.process.prepareBuffer()

        self.assertEqual(
            self.env.current_data.bufferedData.shape,
            (3, 1, 3, 8, 16, 128, 128))

        self.assertEqual(
            self.env.current_data.bufferedData.__getitem__((0, 0)).shape,
            (3, 8, 16, 128, 128))

        # do the phase calculation
        self.env.process.calcShift()

        result = self.env.results.getLastResult('Corrected Phase')['Shift']
        self.assertEqual(
            int(result['50K'][0][self.env.current_data.get_axis('Echo Time')[0]].sum()), 4539)

        ######################################################
        # do the contrast
        self.env.mask.setMask("HTO_2")
        
        self.env.process.calcContrastRef()
        self.env.process.calcContrastMain()
        
        self.result = self.env.results.getLastResult('Contrast fit')[
            'Parameters']

        self.assertEqual(self.result['reso']['y'].tolist(), [1, 1, 1])
        self.assertEqual(
            [round(e, 4) for e in self.result['5K']['y'].tolist()],
            [round(e, 4) for e in [0.8325602710429816, 0.7798115451405204, 0.676853422535165]])
        self.assertEqual(
            [round(e, 4) for e in self.result['50K']['y'].tolist()],
            [round(e, 4) for e in [0.8443877313400946, 0.5086612494351186, 0.32389345108503953]])

    def test_phase_correction_single_mask_data(self):
        #self.app = QtWidgets.QApplication(sys.argv)
        ######################################################
        # test the dataset
        env = createHTO(1)
        data_sum = 0
        for data_object in env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)

        ######################################################
        # Prepare the phase process
        env.mask.setMask("HTO_1")
        env.mask.generateMask(128, 128)
        env.process.calculateEcho()
        env.process.prepareBuffer()
        
        # do the phase calculation
        env.process.calcShift()
        ######################################################
        # do the contrast
        env.mask.setMask("HTO_2")
        env.process.calcContrastRef()

        env.process.calcContrastSingle('5K', 7)
        result = env.results.getLastResult('Contrast calculation')['Contrast'] 

        self.assertEqual(
            {key: round(e, 4) for key, e in result['5K'].items()},
            {key: round(e, 4) for key, e in ({0.1047018557163469: 0.6570727822172627, 1.3424437890424732: 0.5376098600101173, 1.9753414318373752: 0.2879263018807539}).items()})


    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def phase_correction_exposure_data_summation_on(self, proc):
        #self.app = QtWidgets.QApplication(sys.argv)

        ######################################################
        # test the dataset
        self.env = createHTO(proc)
        self.env.instrument.setDetector('Reseda', 14032019)
        self.env.fit.para_dict['sum_foils'] = True
        data_sum = 0
        for data_object in self.env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)

        ######################################################
        # Prepare the phase process
        self.env.process.calculateEcho()
        self.env.process.prepareBuffer()

        self.assertEqual(
            self.env.current_data.bufferedData.shape,
            (3, 1, 3, 8, 16, 128, 128))

        self.assertEqual(
            self.env.current_data.bufferedData.__getitem__((0, 0)).shape,
            (3, 8, 16, 128, 128))

        # do the phase calculation
        self.env.fit.correctPhaseExposure(
            self.env.current_data,
            self.env.mask,
            self.env.instrument,
            self.env.results)

        result = self.env.results.getLastResult('Corrected Phase')['Shift']
        self.assertEqual(
            int(result['50K'][0][self.env.current_data.get_axis('Echo Time')[0]].sum()), 4539)

        self.env.mask.mask = np.zeros((128, 128))
        self.env.mask.mask[32:92, 32:92] = 1

        self.env.fit.calcContrastRef(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        result = self.env.results.getLastResult(
            'Reference contrast calculation')
        print(result)

        self.env.fit.calcContrastMain(
            self.env.current_data,
            self.env.mask,
            self.env.results,
            select=self.env.current_data.get_axis('Parameter'))

        self.env.fit.contrastFit(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        self.result = self.env.results.getLastResult('Contrast fit')[
            'Parameters']
        self.assertEqual(self.result['reso']['y'].tolist(), [1, 1, 1])
        self.assertEqual(
            [round(e, 4) for e in self.result['5K']['y'].tolist()],
            [round(e, 4) for e in [0.9201912409994355, 0.8954817524620975, 0.8198329763249551]])
        self.assertEqual(
            [round(e, 4) for e in self.result['50K']['y'].tolist()],
            [round(e, 4) for e in [0.7607151726522323, 0.5407819350675142, 0.13512816355553667]])

    @unittest.skipIf((
        "CI" in os.environ and os.environ["CI"] == "true"),
        "Skipping this test on CI.")
    def phase_correction_exposure_data_summation_off(self, proc):
        #self.app = QtWidgets.QApplication(sys.argv)

        ######################################################
        # test the dataset
        self.env = createHTO(proc)
        self.env.instrument.setDetector('Reseda', 14032019)

        foils_in_echo = []
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 0, 1])
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 0, 1])
        foils_in_echo.append([0, 0, 0, 0, 0, 0, 0, 1])

        self.env.fit.set_parameter(
            name='foils_in_echo',
            value=foils_in_echo)

        self.env.fit.para_dict['sum_foils'] = False

        data_sum = 0
        for data_object in self.env.current_data.data_objects:
            data_sum += data_object.data.sum()
        self.assertEqual(data_sum, 696802)

        ######################################################
        # Prepare the phase process
        self.env.process.calculateEcho()
        self.env.process.prepareBuffer()

        self.assertEqual(
            self.env.current_data.bufferedData.shape,
            (3, 1, 3, 8, 16, 128, 128))

        self.assertEqual(
            self.env.current_data.bufferedData.__getitem__((0, 0)).shape,
            (3, 8, 16, 128, 128))

        # do the phase calculation
        self.env.fit.correctPhaseExposure(
            self.env.current_data,
            self.env.mask,
            self.env.instrument,
            self.env.results)

        result = self.env.results.getLastResult('Corrected Phase')['Shift']
        self.assertEqual(
            int(result['50K'][0][self.env.current_data.get_axis('Echo Time')[0]].sum()), 4539)

        self.env.mask.mask = np.zeros((128, 128))
        self.env.mask.mask[32:92, 32:92] = 1

        self.env.fit.calcContrastRef(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        result = self.env.results.getLastResult(
            'Reference contrast calculation')

        self.env.fit.calcContrastMain(
            self.env.current_data,
            self.env.mask,
            self.env.results,
            select=self.env.current_data.get_axis('Parameter'))

        self.env.fit.contrastFit(
            self.env.current_data,
            self.env.mask,
            self.env.results)

        self.result = self.env.results.getLastResult('Contrast fit')[
            'Parameters']
        self.assertEqual(self.result['reso']['y'].tolist(), [1, 1, 1])
        self.assertEqual(
            [round(e, 4) for e in self.result['5K']['y'].tolist()],
            [round(e, 4) for e in [0.9201912409994355, 0.8954817524620975, 0.8198329763249551]])
        self.assertEqual(
            [round(e, 4) for e in self.result['50K']['y'].tolist()],
            [round(e, 4) for e in [0.7607151726522323, 0.5407819350675142, 0.13512816355553667]])
