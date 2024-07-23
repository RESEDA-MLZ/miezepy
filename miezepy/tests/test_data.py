
import unittest
import numpy as np
import time
import os
from miezepy.core.module_data import DataStructure

def generateMap(map_input):
    return np.fromfunction(
        lambda i, j: 100 + 50*np.sin((i-64)+(j-64)+map_input[-1]/16*2*np.pi),
        (128, 128),
        dtype=int)

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
    data.metadata_class.addMetadata(
        'BOOL', value=True, logical_type='bool', unit='-')
    data.metadata_class.addMetadata(
        'INT', value=1, logical_type='int', unit='-')
    data.metadata_class.addMetadata(
        'FLOAT_ARRAY', value=[0.035, 0.035, 0.035], logical_type='float_array', unit='-')
    data.metadata_class.addMetadata(
        'INT_ARRAY', value=[0, 1, 2], logical_type='int_array', unit='-')

    return data

class Test_data_module(unittest.TestCase):

    def test_data_init(self):
        self.data = DataStructure()
        self.assertEqual(self.data.generated, False)
        self.assertEqual(self.data.map, None)
        self.assertEqual(self.data.axes, None)
        self.assertEqual(self.data.id, 0)
        self.assertEqual(self.data.meta_id, 0)
        self.assertEqual(len(self.data.data_objects), 0)
        self.assertEqual(len(self.data.data_addresses), 0)
        self.assertEqual(len(self.data.metadata_objects), 0)
        self.assertEqual(len(self.data.metadata_addresses), 0)
        self.assertEqual(self.data[0], None)

    @unittest.skipIf(
        ("APPVEYOR" in os.environ and os.environ["APPVEYOR"] == "True"),  "Skipping this test on Appveyor due to memory.")
    def test_data_creation(self):
        self.data = createFakeDataset()
        self.assertEqual(self.data.generated, False)
        self.assertEqual(self.data.map, None)
        self.assertEqual(self.data.axes, None)
        self.assertEqual(self.data.id, 11520)
        self.assertEqual(self.data.meta_id, 120)
        self.assertEqual(len(self.data.data_objects), 11520)
        self.assertEqual(len(self.data.data_addresses), 11520)
        self.assertEqual(len(self.data.metadata_objects), 120)
        self.assertEqual(len(self.data.metadata_addresses), 120)

        self.data.validate()
        self.map = self.data.map
        self.assertEqual(self.map[0, 0, 0, 0, 0], 0)
        self.assertEqual(self.map[2, 1, 0, 0, 0], -1)
        self.assertEqual(self.map[1, 1, 9, 5, 15], 11519)
        print(self.data)
        print(self.data.data_objects[0])
        print(self.data.metadata_objects[0])

    def test_data_getitem_subset(self):
        self.data = createFakeDataset()
        self.data.validate()
        
        new_data = self.data[0]
        self.assertEqual(new_data.generated, True)
        self.assertEqual(new_data.id, 1920)
        self.assertEqual(new_data.meta_id, 20)
        self.assertEqual(len(new_data.data_objects), 1920)
        self.assertEqual(len(new_data.data_addresses), 1920)
        self.assertEqual(len(new_data.metadata_objects), 20)
        self.assertEqual(len(new_data.metadata_addresses), 20)
        
    def test_data_get_slice(self):
        self.data = createFakeDataset()
        self.data.validate()
        
        new_data = self.data.get_slice([0])
        self.assertEqual(new_data.generated, True)
        self.assertEqual(new_data.id, 1920)
        self.assertEqual(new_data.meta_id, 20)
        self.assertEqual(len(new_data.data_objects), 1920)
        self.assertEqual(len(new_data.data_addresses), 1920)
        self.assertEqual(len(new_data.metadata_objects), 20)
        self.assertEqual(len(new_data.metadata_addresses), 20)

    def test_data_getitem_item(self):
        self.data = createFakeDataset()
        self.data.validate()
        
        new_data = self.data[0, 0, 0, 0, 0]
        self.assertEqual(np.sum(new_data), 1638245.058749192)

    def test_data_get_meta(self):
        self.data = createFakeDataset()
        self.data.validate()
        meta = self.data.get_metadata([0,0,0,0,0])[0].metadata
        self.assertEqual(
            self.data.get_metadata([0,0,0,0,0])[0].metadata,
            {
                'Wavelength': ['Wavelength', 'float', 6e-10, ''],
                'Freq. first': ['Freq. first', 'float', 30, ''],
                'Freq. second': ['Freq. second', 'float', 60, ''],
                'lsd': ['lsd', 'float', 1200000000000.0, ''],
                'Monitor': ['Monitor', 'float', 100, '']})
                         
    def test_data_remove_from_axis(self):
        self.data = createFakeDataset()
        self.data.validate()
        
        new_data = self.data.remove_from_axis(0, [0, 0, 0])
        self.assertEqual(new_data.generated, True)
        self.assertEqual(new_data.id, 11520)
        self.assertEqual(new_data.meta_id, 120)
        self.assertEqual(len(new_data.data_objects), 6720)
        self.assertEqual(len(new_data.data_addresses), 6720)
        self.assertEqual(len(new_data.metadata_objects), 70)
        self.assertEqual(len(new_data.metadata_addresses), 70)
        
    def test_data_sum_in_order(self):
        self.data = createFakeDataset()
        self.data.validate()
        
        self.data.sum_in_order()
        self.assertEqual(self.data.generated, True)
        self.assertEqual(self.data.id, 17280)
        self.assertEqual(self.data.meta_id, 5880)
        self.assertEqual(len(self.data.data_objects), 5760)
        self.assertEqual(len(self.data.data_addresses), 5760)
        self.assertEqual(len(self.data.metadata_objects), 5880)
        self.assertEqual(len(self.data.metadata_addresses), 5880)