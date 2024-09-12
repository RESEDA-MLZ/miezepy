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


import csv
import os
import re
import glob
import numpy as np
import time

from .io_modules.import_mieze_tof import Import_MIEZE_TOF
from .io_modules.import_sans_pad import Import_SANS_PAD
from .module_data import DataStructure
from .fit_modules.library_fit import miezeTauCalculation


IO_NO_PATH = 'The environement has no save path set. Please first save the environemnt.'
IO_PATH_DELETED = 'The initially defined path of the environment does not exist. Was the project moved ?'
IO_PATH_PERMISSION = 'The creation of the result directory failed. It could be a write permission issue.'
def loadData(env, gui):
    return ''


class IOStructure:

    def __init__(self, env):

        self.verbose = True
        self.env = env
        self.path = None
        self.generator = Generator()
        self.import_objects = []
        self.extra_folders = []

    def setEnvPath(self, path):
        self.path = path

    def envPath(self):
        return self.path

    def grabFromOther(self, other):
        '''
        This method is to allow cross
        environnement transfer of the
        elements.

        Parameters
        ----------
        other : ScriptStructure
            The script structure to use
        '''
        self.import_objects = list(other.import_objects)

    def addObject(self):
        self.import_objects.append(ImportObject(self))

    def remObject(self, index):
        del self.import_objects[index]

    def reset(self):
        self.import_objects = []
        self.extra_folders = []

    def load(self, path, gui=None):
        '''
        The load dispatcher
        '''
        self.reset()
        if path.split(".")[-1] == "py":
            self.loadFromPython(path, gui)
        else:
            self.loadFromText(path)

    def saveToPython(self, path):
        '''
        Save the whole system to a python script
        '''
        script = ""
        indent = 1

        script += "def loadData(env, gui = None):\n"
        script += indent * "    " + "if not gui == None:\n"
        script += (indent+1) * "    " + "for i in range(" + \
            str(len(self.import_objects))+"):\n"
        script += (indent+2) * "    " + "gui.addElement()\n"
        script += indent * "    " + "else:\n"
        script += (indent+1) * "    " + "for i in range(" + \
            str(len(self.import_objects))+"):\n"
        script += (indent+2) * "    " + "env.io.addObject()\n"

        script += indent * "    " + \
            "import_result  = [None]*"+str(len(self.import_objects))+"\n"

        for i, element in enumerate(self.import_objects):
            script += indent * "    " + \
                "import_result["+str(i)+"] = loadData_"+str(i) + \
                "(env.io.import_objects["+str(i)+"])\n"

        script += indent * "    " + \
            "passed = all([all([subelement[0] for subelement in element]) for element in import_result])\n"
        script += indent * "    " + "if not gui == None:\n"
        script += (indent+1) * "    " + "for i in range(" + \
            str(len(self.import_objects))+"):\n"
        script += (indent+2) * "    " + "gui.setCurrentElement(i)\n"
        script += (indent+2) * "    " + "if passed:\n"
        script += (indent+3) * "    " + "gui.populate()\n"
        script += indent * "    " + "else:\n"
        script += (indent+1) * "    " + "for i in range(" + \
            str(len(self.import_objects))+"):\n"
        script += (indent+2) * "    " + "if passed:\n"
        script += (indent+3) * "    " + \
            "env.io.import_objects[i].processObject()\n"
        script += indent * "    " + "return import_result\n"

        for i, element in enumerate(self.import_objects):
            script += "\ndef loadData_"+str(i)+"(import_object):\n"
            script += indent * "    " + "#################################\n"
            script += indent * "    " + "########## add element ##########\n"
            script += indent * "    " + "current_object  = import_object\n"
            script += indent * "    " + "meta_files_found = [True,'']\n"
            script += indent * "    " + "data_files_found = [True,'']\n"
            script += element.script(indent)

        with open(path, 'w') as f:
            f.write(script)

    def loadFromPython(self, path, gui=None, extra_folder=[]):
        '''
        load from a python script generated by
        the previous self.saveToPython
        '''
        self.reset()
        self.extra_folders = extra_folder

        with open(path) as f:
            code = compile(f.read(), path, 'exec')
            exec(code, globals())

        result = loadData(self.env, gui)

        try:
            self.generate()
        except:
            pass

        return result

    def loadFromText(self, path, gui=None):
        '''
        load from a python script generated by
        the previous self.saveToPython
        '''
        print('I am a text')

    def generate(self, thread=None):
        '''
        This is the method that will create a data
        structure populate it and then send it's
        content to the main environment handler.
        '''
        data, sanity = self.generator.generate(self.import_objects, thread=thread)
        if not sanity[0] is None:
            return sanity
        else:
            self.env.data[0] = data
            self.env.setCurrentData(0)
            return sanity

    def load_MIEZE_TOF(self, load_path):
        '''
        This function will manage the load of tof
        files through different smaller import
        components
        '''
        Import_MIEZE_TOF(load_path, self.env.current_data)

    def load_MIEZE_HD5(self, load_path):
        '''
        This function will manage the load of tof
        files through different smaller import
        components
        '''

    def load_SANS_PAD(self, load_path):
        '''
        This function will import the data from the
        PAD format.
        '''
        Import_SANS_PAD(load_path, self.env.current_data)
        
    def prepareResultDump(self, append_name):
        '''
        This function will handle the management of the results
        dumping after each consecutive run. Here we are going to 
        check the 
        '''
        if self.path is None:
            return ('io_no_path_provided', IO_NO_PATH)
        
        if not os.path.exists(self.path):
            return ('io_path_deleted', IO_PATH_DELETED)
        
        if not os.path.exists(os.path.join(self.path, self.env.name)): 
            try:
                os.mkdir(os.path.join(self.path, self.env.name))
            except:
                return ('io_path_permission_0', IO_PATH_PERMISSION)    
        
        if not os.path.exists(os.path.join(self.path, self.env.name, 'results')):
            try:
                os.mkdir(os.path.join(self.path, self.env.name, 'results'))
            except:
                return ('io_path_permission_1', IO_PATH_PERMISSION)
            
        try:
            path = os.path.join(self.path, self.env.name, 'results', time.strftime("%Y%m%d-%H%M%S_result"))
            os.mkdir(path+'_'+append_name)
        except:
            return ('io_path_permission_2', IO_PATH_PERMISSION)
        
        return path+'_'+append_name

    def dumpResultMeta(self, dir_path, mask=None):
        '''
        This function will handle the csv dumping
        '''
        dir_name = os.path.basename(dir_path)
        date_rep = dir_name.split('-')
        date = date_rep[0]
        time = date_rep[1]
        meta_list = [
            dir_name,
            dir_name,
            ' '.join([
                '.'.join([date[:4], date[4:6], date[6:8]]),
                'at',
                ':'.join([time[:2], time[2:4], time[4:6]])])]
        
        with open(os.path.join(dir_path, 'meta.txt'), 'w') as meta_file:
            meta_file.write('\n'.join(meta_list) + '\n')
        
    def dumpCSVResults(self, data, path):
        '''
        This function will handle the csv dumping
        '''
        #-------------------------------------------------------
        # This is for the corrected data
        lines = []

        #Build the header
        header = []
        for key in data[0]:
            for pointer, name in {'x': 'tau_ns', 'y': 'contrast', 'y_error': 'cerr'}.items():
                header.append(key+'_'+name)
        lines.append(header)
        
        # Set the data
        end_reached = False
        line_num = -1
        while not end_reached:
            line_num +=1
            line = []
            for key in data[0]:
                for pointer, name in {'x': 'tau_ns', 'y': 'contrast', 'y_error': 'cerr'}.items():
                    line.append(data[2][key][pointer][line_num] if line_num<len(data[2][key][pointer]) else None)
                    
            if all([item is None for item in line]):
                end_reached = True
                break
            
            lines.append(line)
            
        # Write to file
        with open(os.path.join(path, 'contrast_result.csv'), 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(lines)
        
        #-------------------------------------------------------
        # This is for the non-corrected data
        lines = []
        
        #Build the header
        header = []
        for key in data[0]:
            for pointer, name in {'x': 'tau_ns', 'y_raw': 'contrast', 'y_raw_error': 'cerr'}.items():
                header.append(key+'_'+name)
        lines.append(header)
        
        # Set the data
        end_reached = False
        line_num = -1
        while not end_reached:
            line_num +=1
            line = []
            for key in data[0]:
                for pointer, name in {'x': 'tau_ns_raw', 'y_raw': 'contrast_raw', 'y_raw_error': 'cerr_raw'}.items():
                    line.append(data[2][key][pointer][line_num] if line_num<len(data[2][key][pointer]) else None)
                    
            if all([item is None for item in line]):
                end_reached = True
                break
            
            lines.append(line)
            
        # Write to file
        with open(os.path.join(path, 'raw_result.csv'), 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(lines)

class Generator:

    def generate(self, import_objects, thread=None):
        '''
        Main generator function that will manage the
        import of all the required elements
        '''
        if thread is not None: 
            thread.action.emit(['Spawned dataset generator', 0])
            
        if thread is not None: 
            thread.action.emit(['Processed data axes', 10])
        axes, idx = self._getAxes(import_objects)
        
        if thread is not None: 
            thread.action.emit(['Read data', 25])
        data = self._populateData(axes, idx, import_objects, thread=thread)
        
        if thread is not None: 
            thread.action.emit(['Generate axes for data', 50])
        data = self._setAxes(data, axes)
        
        if thread is not None: 
            thread.action.emit(['Sanity check', 75])
        sanity = self._axesSanityCheck(axes, import_objects)
        
        if thread is not None: 
            thread.action.emit(['Complete', 100])
        return data, sanity

    def _axesSanityCheck(self, axes, import_objects):
        '''
        Check the sanity of the axes and a
        ll definitions
        '''
        reference = self._getReference(import_objects)
        if reference is None:
            return ['No reference', None]

        reference_axis = import_objects[[
            import_object.data_handler.parameter for import_object in import_objects].index(reference)].getAxes()[2]
        inside = [element in reference_axis for element in axes[2]]
        if not all(inside):
            out = (np.array(axes[2])[np.argwhere(
                np.array([inside]) == False)]).tolist()
            return ['Echo issue', out]

        return [None, None]

    def _getAxes(self, import_objects):
        '''
        compute the axes from all the import objects
        and then stick them together and finally
        remove repetitions through sets
        '''
        temp_axes = []
        for item in import_objects:
            item.processObject()
            temp_axes.append(item.getAxes())

        axes = [[] for i in range(len(temp_axes[0]))]
        for i in range(len(temp_axes)):
            for j in range(len(temp_axes[0])):
                axes[j] += temp_axes[i][j]

        for j in range(len(temp_axes[0])):
            axes[j] = list(set(axes[j]))

        idx = [[[]for j in range(len(temp_axes[i][2]))]
               for i in range(len(temp_axes))]
        for i in range(len(temp_axes)):
            for j in range(len(temp_axes[i][2])):
                idx[i][j] = [
                    axes[0].index(temp_axes[i][0][0]),
                    axes[1].index(temp_axes[i][1][0]),
                    axes[2].index(temp_axes[i][2][j])]

        return axes, idx

    def _setAxes(self, data, axes):
        '''
        This routine will grab the axes and put them
        into the datastructure.
        '''
        data.axes.set_name(0, 'Parameter')
        data.axes.set_name(1, 'Measurement')
        data.axes.set_name(2, 'Echo Time')
        data.axes.set_name(3, 'Foil')
        data.axes.set_name(4, 'Time Channel')

        data.axes.set_axis(0, axes[0])
        data.axes.set_axis(1, axes[1])
        data.axes.set_axis(2, axes[2])
        data.axes.set_axis(3, [e for e in range(
            len(data.axes.axes[3]))])
        data.axes.set_axis(4,  [e for e in range(
            len(data.axes.axes[4]))])

        # data.axes.set_name(0, 'Parameter')
        # data.axes.set_name(1, 'Measurement')
        # data.axes.set_name(2, 'Echo time')
        # data.axes.set_name(3, 'Foil')
        # data.axes.set_name(4, 'Time channel')

        return data

    def _populateData(self, axes, idx, import_objects, thread=None):
        '''
        compute the axes from all the import objects
        and then stick them together and finally
        remove repetitions through sets
        '''
        data_structure = DataStructure()
        
        total_length = [len([path for path in import_object.file_handler.total_path_files]) for import_object in import_objects]

        for i, import_object in enumerate(import_objects):
            for j, path in enumerate(import_object.file_handler.total_path_files):
                data_structure.addMetadataObject(
                    self._generateMetadata(import_object, j))
                
                if thread is not None: 
                    thread.action.emit(['Generate axes for data', 50+10/sum(total_length)*(sum(total_length[:i])+j)])
                    
                with open(path, 'rb') as f:
                    loadeddata = np.fromfile(f, dtype=np.int32)[
                        :np.prod(import_object.data_handler.dimension)]
                    data = loadeddata.reshape(
                        *import_object.data_handler.dimension)

                for idx_1 in range(import_object.data_handler.dimension[0]):
                    for idx_2 in range(import_object.data_handler.dimension[1]):
                        address = list(idx[i][j]) + [idx_1, idx_2]
                        data_structure[address] = np.transpose(
                            data[idx_1, idx_2, :, :])

        data_structure.validate()

        data_structure.metadata_class.addMetadata(
            'Selected foils',
            value='[1,1,1,0,0,1,1,1]',
            logical_type='int_array',
            unit='-')

        reference = self._getReference(import_objects)
        data_structure.metadata_class.addMetadata(
            'Reference',
            value=reference,
            logical_type='float',
            unit='K')

        background = self._getBackground(import_objects)
        data_structure.metadata_class.addMetadata(
            'Background',
            value=str(background),
            logical_type='float',
            unit='K')

        return data_structure

    def _generateMetadata(self, import_object, index):
        '''
        Here is the routine managing the metadata
        handling.
        '''
        metadata = {}
        for key in import_object.meta_handler.values.keys():
            metadata[key] = [
                key,
                'float',
                import_object.meta_handler.values[key][index],
                '-'
            ]
        return metadata

    def _getReference(self, import_objects):
        '''
        Grab the reference from the widgets if possible
        '''
        reference = None
        for import_object in import_objects:
            if import_object.data_handler.reference:
                reference = import_object.data_handler.parameter
        return reference

    def _getBackground(self, import_objects):
        '''
        Grab the reference from the widgets if possible
        '''
        background = None
        for import_object in import_objects:
            if import_object.data_handler.background:
                background = import_object.data_handler.parameter
        return background


class ImportObject:

    def __init__(self, parent):

        self.parent = parent
        self.meta_handler = MetaHandler()
        self.file_handler = FileHandler()
        self.data_handler = DataHandler()

        # set the default
        self.meta_handler.defaultMeta()
        self.file_handler.extra_folders = list(self.parent.extra_folders)

    def processObject(self):
        '''
        This function will be called when the object
        is being process and all parameters are being
        calculated.
        '''
        self.meta_handler.prepareExtract()

        for file in self.file_handler.total_path_files:
            self.meta_handler.extractMeta(file)

        self.meta_handler.finalizeExtract(self.parent.env.fit)

    def script(self, indent):
        '''
        This will generate the script of the current
        object.
        '''
        script = ""

        script += self.meta_handler.script(indent)
        script += self.file_handler.script(indent)
        script += self.data_handler.script(indent)

        return script

    def getAxes(self):
        '''
        '''
        axis = []

        try:
            axis.append([float(self.data_handler.parameter)])
        except:
            axis.append([self.data_handler.parameter])
        try:
            axis.append([float(self.data_handler.meas)])
        except:
            axis.append([self.data_handler.meas])

        if self.meta_handler.values['Echo'] == 'Not given':
            axis.append(
                [i for i in range(len(self.file_handler.total_path_files))])
        else:
            axis.append(self.meta_handler.values['Echo'])

        axis.append([i for i in range(self.data_handler.dimension[0])])
        axis.append([i for i in range(self.data_handler.dimension[1])])

        return axis


class DataHandler:

    def __init__(self):
        self.initialize()

    def initialize(self):
        '''
        This will initialize the different arrays and
        can be used to reset the class.
        '''
        self.dimension = [8, 16, 128, 128]
        self.parameter = 'None'
        self.meas = 0
        self.reference = False
        self.background = False

    def script(self, indent):
        '''
        This will generate the script of the current
        object.
        '''
        script = ""

        script += indent * "    " + "########## The data handler ##########\n"
        script += indent * "    " + "current_object.data_handler.dimension = " + \
            str(self.dimension) + "\n"
        script += indent * "    " + "current_object.data_handler.parameter = '" + \
            str(self.parameter) + "'\n"
        script += indent * "    " + \
            "current_object.data_handler.meas = '"+str(self.meas) + "'\n"
        script += indent * "    " + "current_object.data_handler.reference = " + \
            str(self.reference) + "\n"
        script += indent * "    " + "current_object.data_handler.background = " + \
            str(self.background) + "\n"
        script += indent * "    " + \
            "return [meta_files_found, data_files_found]\n"

        return script


class FileHandler:

    def __init__(self):
        self.initialize()

    def initialize(self):
        '''
        This will initialize the different arrays and
        can be used to reset the class.
        '''
        self.total_path_files = []
        self.nice_path_files = []
        self.extra_folders = []

    def filesExist(self, file_path_array):
        '''
        Checks if all the files in a path array actually exist
        '''
        files_present = []
        for path in file_path_array:
            if os.path.isfile(path):
                files_present.append(True)
            elif not os.path.isfile(path):
                for folder_path in self.extra_folders:
                    found_names = glob.glob(os.path.realpath(
                        os.path.abspath(folder_path)
                        + os.path.sep
                        + '**'
                        + os.path.sep
                        + os.path.abspath(path).split(os.path.sep)[-1]),
                        recursive=True)
                    if len(found_names) > 0:
                        files_present.append(True)
                        break
            else:
                files_present.append(False)

        return files_present

    def addFiles(self, file_path_array):
        '''
        This routine will get the file names and try
        to test store them and create a nice
        representation for the display.
        '''
        for element in file_path_array:
            if not element.split(os.path.sep)[-1] in self.nice_path_files:
                if os.path.isfile(element):
                    path = element
                else:
                    for folder_path in self.extra_folders:

                        path_list = glob.glob(os.path.realpath(
                            os.path.abspath(folder_path)
                            + os.path.sep
                            + '**'
                            + os.path.sep
                            + os.path.abspath(element).split(os.path.sep)[-1]),
                            recursive=True)

                        if len(path_list) == 1:
                            path = path_list[0]

                self.total_path_files.append(path)
                self.nice_path_files.append(path.split(os.path.sep)[-1])

    def removeFile(self, index):
        '''
        This routine will get the file names and try
        to test store them and create a nice
        representation for the display.
        '''
        del self.total_path_files[index]
        del self.nice_path_files[index]

    def genPrev(self, index, sum_axes=(0, 1), log=True):
        '''
        Generate a preview of a file
        '''
        target = self.total_path_files[index]

        with open(target) as f:
            loadeddata = np.fromfile(f, dtype=np.int32)[:8*16*128*128]
            data = loadeddata.reshape(8, 16, 128, 128)
            data = np.transpose(data, (0, 1, 3, 2))
            for element in list(set(sum_axes))[::-1]:
                data = np.sum(data, axis=element)

        if log:
            self.current_preview = np.log10(data+1)
        else:
            self.current_preview = data

    def getElement(self, index):
        '''
        Generate a preview of a file
        '''
        target = self.total_path_files[index]

        with open(target) as f:
            loadeddata = np.fromfile(f, dtype=np.int32)[:8*16*128*128]
            data = loadeddata.reshape(8, 16, 128, 128)
            data = np.transpose(data, (0, 1, 3, 2))

        return data

    def script(self, indent):
        '''
        This will generate the script of the current
        object.
        '''
        common_path = str(os.path.sep).join(
            os.path.commonprefix(self.total_path_files).split(os.path.sep)[:-1])

        script = ""
        script += indent * "    " + "\n"
        script += indent * "    " + "########## The file paths ##########\n"
        script += (indent+0) * "    " + "common_path = '" + common_path + "'\n"

        if len(self.total_path_files) > 0:
            script += (indent+0) * "    " + "path_list = [\n"
            for item in self.total_path_files:
                if common_path == "":
                    script += (indent+1) * "    " + "'" + item + "',\n"
                else:
                    script += (indent+1) * "    " + "'" + str(os.path.sep).join(
                        item.split(common_path)[1].split(os.path.sep)[1:]) + "',\n"
            script = script[:-2]
            script += "]\n"
            script += (indent+0) * "    " + \
                "if current_object.file_handler.filesExist([\n"
            script += (indent+1) * "    " + \
                "os.path.join(common_path,item) for item in path_list]):\n"
            script += (indent+1) * "    " + \
                "current_object.file_handler.addFiles([\n"
            script += (indent+2) * "    " + \
                "os.path.join(common_path,item) for item in path_list])\n"
            script += indent * "    " + "else:\n"
            script += (indent+1) * "    " + \
                "data_files_found = [False,common_path]\n"
        return script


class MetaHandler:

    def __init__(self):
        self.path = ''
        self.selected_meta = []

    def script(self, indent):
        '''
        This will generate the script of the current
        object.
        '''
        script = ""
        script += indent * "    " + "\n"
        script += indent * "    " + "########## The meta info ##########\n"
        script += indent * "    " + "try:\n"
        script += (indent+1) * "    " + "path = '"+self.path+"'\n"
        script += (indent+1) * "    " + \
            "current_object.meta_handler.buildMeta(path)\n"
        if len(self.selected_meta) > 0:
            script += (indent+1) * "    " + "selected_meta = ["
            for element in self.selected_meta:
                script += "\n" + (indent+2) * "    " + "["
                for item in element:
                    script += "'"+item + "' ,"
                script = script[:-1]
                script += "],"
            script = script[:-1]
            script += "]\n"
        else:
            script += (indent+1) * "    " + "selected_meta = []\n"
        script += (indent+1) * "    " + \
            "current_object.meta_handler.selected_meta = selected_meta\n"
        script += indent * "    " + "except:\n"
        script += (indent+1) * "    " + "meta_files_found = [False,path]\n"
        return script

    def buildMeta(self, file_path):
        '''
        Create a list of the available metadata in the
        file and then
        '''
        self.path = file_path
        self.metadata_temp = []
        if not self.path == '':
            with open(file_path, 'rb') as f:
                line = f.readlines()

                for binaryLine in line:
                    try:
                        line = binaryLine.decode('ascii').replace('\n', '')
                        nums = re.findall('-?\d*\.?\d+', line.split(" : ")[1])
                        if len(nums) == 0:
                            pass
                        else:
                            self.metadata_temp.append([
                                False,
                                line.split(" : ")[0].replace(" ", ""),
                                line.split(" : ")[1].split(nums[len(nums) - 1])[1].replace(" ", "").replace(")", "")])
                    except:
                        pass

    def flipBool(self, name, value):
        '''
        This method will flip a boolean value when
        selected
        '''
        for element in self.metadata_temp:
            if element[1] == name:
                element[0] = value
                break

    def setMeta(self):
        '''
        This will retrieve the set metadata information
        '''
        self.selected_meta = []

        for element in self.metadata_temp:
            if element[0]:
                self.selected_meta.append(element[1:3]+['None', '1', ''])

    def defaultMeta(self):
        '''
        Allow the metadata to be set quickly with a default...
        '''
        self.selected_meta = [
            ['cbox_0a_fg_freq_value', 'Hz', 'Freq. first', '1', ''],
            ['cbox_0b_fg_freq_value', 'Hz', 'Freq. second', '1', ''],
            ['psd_distance_value', 'm', 'lsd', '1e9', ''],
            ['selector_lambda_value', 'A', 'Wavelength', '1e-10', ''],
            ['monitor1', '', 'Monitor', '1', '']]

    def checkPresence(self):
        '''
        This will retrieve the set metadata information
        '''
        for element in self.selected_meta:
            for item in self.metadata_temp:
                if element[0] == item[1]:
                    item[0] = True

    def removeElement(self, row):
        '''
        reset the output
        '''
        try:
            del self.metadata_temp[row]
        except:
            pass
        try:
            del self.selected_meta[row]
        except:
            pass

    def reset(self):
        '''
        reset the output
        '''
        self.selected_meta = []

    def editValue(self, array):
        '''
        Edit the value or definition of an element
        '''
        for i in range(len(self.selected_meta)):
            if self.selected_meta[i][0] == array[0]:
                self.selected_meta[i] = list(array)
                break

    def prepareExtract(self):
        '''
        Preates the metadata dictionary for the file
        '''
        self.values = {}
        self.values_set = {}

        for element in self.selected_meta:
            self.values[element[0]] = []

    def extractMeta(self, file_path):
        '''
        '''
        with open(file_path, 'rb') as f:
            line = f.readlines()
            
        for element in self.selected_meta:
            self.values_set[element[0]] = False

        for binaryLine in line:
            try:
                line = binaryLine.decode('ascii').replace('\n', '')
                nums = re.findall(
                    '[-+]?(\d+([.,]\d*)?)([eE][-+]?\d+)?', line.split(" : ")[1])
                if len(nums) == 0:
                    pass
                else:
                    marker = line.split(" : ")[0].replace(" ", "")

                    for element in self.selected_meta:
                        if element[0] == marker and not self.values_set[element[0]]:
                            self.values[element[0]].append(
                                nums[0][0] + nums[0][-1])
                            self.values_set[element[0]] = True
            except:
                pass

    def finalizeExtract(self, fit_handler):
        '''
        Preates the metadata dictionary for the file
        '''
        self.values['Parameter'] = ['Not given']
        self.values['Measurement'] = ['Not given']
        self.values['Echo'] = ['Not given']

        for element in self.selected_meta:
            if element[2] == 'Parameter':
                self.processMeta('Parameter', True, element)
            elif element[2] == 'Measurement':
                self.processMeta('Measurement', True, element)
            elif element[2] == 'Echo':
                self.processMeta('Echo', False, element)
            elif element[2] == 'Wavelength':
                self.processMeta('Wavelength', False, element)
            elif element[2] == 'Freq. second':
                self.processMeta('Freq. second', False, element)
            elif element[2] == 'Freq. first':
                self.processMeta('Freq. first', False, element)
            elif element[2] == 'lsd':
                self.processMeta('lsd', False, element)
            elif element[2] == 'Monitor':
                self.processMeta('Monitor', False, element)

        if all([(element in self.values.keys()) for element in [
                'Freq. first', 'Freq. second', 'Wavelength', 'lsd']]) and self.values['Echo'][0] == 'Not given':

            self.values['Echo'] = [0]*len(self.values['Wavelength'])

            for i in range(len(self.values['Wavelength'])):
                self.values['Echo'][i], val = miezeTauCalculation(
                    float(self.values['Wavelength'][i]),
                    float(self.values['Freq. first'][i]),
                    float(self.values['Freq. second'][i]),
                    float(self.values['lsd'][i])
                )
                del val
            if len(self.values['Echo']) == 0:
                self.values['Echo'] = ['Not given']

        if self.values['Parameter'][0] == 'Not given':
            del self.values['Parameter']
        if self.values['Measurement'][0] == 'Not given':
            del self.values['Measurement']
        if self.values['Echo'][0] == 'Not given':
            del self.values['Echo']

    def processMeta(self, ptr, mean, element):
        '''
        This will process the value for the given
        ptr value. if mean is true a summation will
        be performed.
        '''
        # check for the manual manipulation
        temp_list = list(self.values[element[0]])
        if len(element) < 5:
            element += ['']

        if not element[4] == '':
            array = self.getArray(element[4])
            if len(array) == 1 and not array[0] == None:
                for i in range(len(temp_list)):
                    temp_list[i] = array[0]
            else:
                for i in range(len(array)):
                    if not array[i] == None:
                        temp_list[i] = array[i]

        # perform it
        if mean:
            self.values[ptr] = str(np.mean([
                float(e)*float(element[3])
                for e in temp_list]))
        else:
            self.values[ptr] = [
                float(e)*float(element[3])
                for e in temp_list]

    def getArray(self, string_element):
        '''
        This will produce an array of floats
        of the string array provided. Note that
        the '_' symbol corresponds to inserting
        None in the list.
        '''
        formated_string = string_element.split(',')
        if len(formated_string) == 1:
            try:
                return [float(string_element)]
            except:
                return [None]
        else:
            try:
                return [float(e) if not e == '_' else None for e in formated_string]
            except:
                return [None]
