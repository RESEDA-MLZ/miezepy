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

import traceback
from PyQt5 import QtCore


class ThreadWrapper(QtCore.QThread):
    error = QtCore.pyqtSignal(dict)
    success = QtCore.pyqtSignal(list)
    running = QtCore.pyqtSignal(bool)
    action_setup = QtCore.pyqtSignal(list)
    action = QtCore.pyqtSignal(list)
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.env = self.parent()
        self.mask_ids = []
        self.canceled = False

    def generateDataset(self):
        '''
        This routine will call the generator for the
        currently active object.
        '''
        self.action_setup.emit([])
        sanity = self.parent().io.generate(thread=self)
        
        if sanity[0] is None:
            self.success.emit(['success', 100])
        elif sanity[0] == 'Echo issue':
                self.error.emit({
                    'icon':'error',
                    'title':'Data echo time point has no reference',
                    'message':'Some echo time values could not be found in the reference:\n'+str(sanity[1][0]),
                    'add_message':'The reference measurment is important to process the contrast value. There should be one measuremnt for every echo time of the dataset. You can specify which measurement should be the reference by checking the reference checkbox within the widget.'})
        elif sanity[0] == 'No reference':
                self.error.emit({
                    'icon':'error',
                    'title':'No reference set',
                    'message':'You did not specify which one of the measurements should be set as reference. See details...',
                    'add_message':'The reference measurment is important to process the contrast value. There should be one measuremnt for every echo time of the dataset. You can specify which measurement should be the reference by checking the reference checkbox within the widget.'})

        self.stop()
            
    def runPhaseCorrection(self):
        '''
        This is the run method that will determine the measure
        to undertake.
        '''
        success = True
        success = self._runPythonCode(0)
        success = self._runPythonCode(1) if success else False
        success = self._runPythonCode(2) if success else False
        self.success.emit(['success', 100])
        self.stop()

    def runReduction(self):
        '''
        This is the run method that will determine the measure
        to undertake.
        '''
        for mask_id in self.mask_ids:
            container = {}
            container['mask'] = str(mask_id)
            self.parent().scripts.synthesizeReductionScript(container)
            
            self._runPythonCode(3)
            
        self.success.emit(['success', 100])
        self.stop()
            
    def _runPythonCode(self, index:int)->bool:
        '''
        Parse and run python code.
        '''
        code_array, meta_array = self.parent().scripts.preprocessScript(index)
        self.action_setup.emit([code_array, meta_array])
        success = True

        for i in range(len(code_array)):
            self.action.emit([meta_array[i].strip('\n'), i])
            try:
                exec(code_array[i])
            except Exception as e:
                error = e
                self.error.emit({
                    'icon':'error',
                    'title':'Script error',
                    'message':'Your script has encountered an error.',
                    'add_message':str(e),
                    'det_message':traceback.format_exc()})
                success = False
                break

        if success:
            self.action.emit(['Script ended with success', len(meta_array)])

        else:
            self.action.emit([str(error), i])
            self.stop()
            
        return success
    
    def stop(self):
        '''
        Stop the thread processing
        '''
        self.quit()
        self.canceled = False
        
    def isCanceled(self):
        '''
        This will beasiclly check if the thread got canceled fomr the
        outised and then flag it
        '''
        return self.canceled
    
        