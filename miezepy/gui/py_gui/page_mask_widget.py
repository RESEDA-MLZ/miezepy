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

#public dependencies
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog
import numpy as np
import os

#private dependencies
from ..qt_gui.main_mask_editor_ui   import Ui_mask_editor
from ...gui.py_gui.dialog           import dialog 
from ..qt_gui.new_mask_ui           import Ui_new_msk

#private plotting library
from simpleplot.multi_canvas import Multi_Canvas

class PageMaskWidget(Ui_mask_editor):
    
    def __init__(self, stack, parent, mask_model):
    
        Ui_mask_editor.__init__(self)
        self.parent         = parent
        self.stack          = stack
        self.local_widget   = QtWidgets.QWidget() 
        self.mask_model     = mask_model
        self.setupUi(self.local_widget)
        self.setup()
        self.connect()
        self.initialize()

    def initialize(self):
        '''
        Reset all the inputs and all the fields
        present in the current view.
        '''
        self.mask_core      = None

    def setup(self):
        '''
        This is the initial setup method that will 
        build the layout and introduce the graphics
        area
        '''
        self.mask_model.connectView('main', self.mask_list_loaded)
        self.mask_model.connectDrop('main', self.comboBox)

        self.my_canvas    = Multi_Canvas(
            self.mask_widget_visual,
            grid        = [[True]],
            x_ratios    = [1],
            y_ratios    = [1],
            background  = "w",
            highlightthickness = 0)

        self.ax = self.my_canvas.get_subplot(0,0)
        self.ax.pointer['Sticky'] = 3
        self.my_canvas.canvas_objects[0][0][0].grid_layout.setMargin(0)

    def link(self, mask_core):
        '''
        This routine will link to the io manager class
        from the core. 
        '''
        self.mask_core = mask_core
        self.mask_model.link(self.mask_core)
        self.updateSelector()
        self.mask_model.setDropText()

    def connect(self):
        '''
        Connect the interactive elements to their
        respective methods.
        '''
        self.mask_button_add.clicked.connect(self.addElement)
        self.mask_button_remove.clicked.connect(self.removeElement)
        self.mask_model.mask_updated.connect(self.parseAndSend)

    def updateSelector(self, default = None):
        '''
        The selector in the top of the window allows to 
        switch between lists and therefore needs to 
        be updated with the content
        '''
        try:
            self.comboBox.currentIndexChanged.disconnect(self.updateSelection)
        except:
            pass
        keys = [key for key in self.mask_core.mask_dict.keys()]
        self.mask_model.setDropItems(keys + ['new ...'] + ['reset defaults ...']+ ['refresh ...'])
        if not default == None:
            self.comboBox.setCurrentIndex(keys.index(default))
        self.comboBox.currentIndexChanged.connect(self.updateSelection)

    def updateSelection(self, idx):
        '''
        Tell the mask class that we switched element.
        '''
        keys = [key for key in self.mask_core.mask_dict.keys()]

        if idx == len(keys):
            self.openNewMaskWindow()

        elif idx == len(keys) + 1:
            mask_dict = self.mask_core.generateDefaults()
            for key in mask_dict.keys():
                self.mask_core.mask_dict[key] = mask_dict[key]
            self.updateSelector(default = self.mask_core.current_mask)
            self.mask_model.setModel()
            self.parseAndSend()

        elif idx == len(keys) + 2:
            self.updateSelector(default = self.mask_core.current_mask)

    def openNewMaskWindow(self):
        '''
        open the new window to allow the user to 
        pick a new mask.
        '''
        self.new_mask_window = NewMaskWindow(self.local_widget)
        self.new_mask_window.cancel_button.clicked.connect(self.closeNewMaskWindow)
        self.new_mask_window.ok_button.clicked.connect(self.addMaskItem)

    def closeNewMaskWindow(self):
        '''
        close the window after actions have been
        performed.
        '''
        self.new_mask_window.cancel_button.clicked.disconnect(self.closeNewMaskWindow)
        self.new_mask_window.ok_button.clicked.disconnect(self.addMaskItem)
        self.new_mask_window.close()

    def addMaskItem(self):
        '''
        Due to a bug in windows we had to separate the 
        addition of a new mask here. with a separate window
        '''
        if not self.new_mask_window.new_mask_name.text() == '':
            self.mask_core.addMask(self.new_mask_window.new_mask_name.text())
            self.updateSelector(default = self.new_mask_window.new_mask_name.text())
            self.mask_model.setModel()
            self.parseAndSend()
            self.closeNewMaskWindow()

    def addElement(self):
        '''
        Add an element into the list which is loaded 
        from a custom widget. If the element is part of
        the default series create a new one
        called by the default name with the appendix '_mod'
        '''
        sample_dict = self.mask_core.generateDefaults()
        if self.mask_core.current_mask in sample_dict.keys():
            self.mask_core.addMask(self.mask_core.current_mask + '_mod')
            self.mask_core.mask_dict[self.mask_core.current_mask] = list(
                sample_dict[self.mask_core.current_mask.split('_mod')[0]])
            self.updateSelector(default = self.mask_core.current_mask)

        self.mask_core.addElement([
            'arc',
            (31,35),
            50, 
            (0,5), 
            (0,360)])

        self.mask_model.setModel()
        self.parseAndSend()

    def removeElement(self):
        '''
        Add an element into the list which is loaded 
        from a custom widget.
        '''
        element_indexes = self.mask_list_loaded.selectedIndexes()[0]
        item = self.mask_model.model.itemFromIndex(element_indexes)
        if not item.parent() == None:
            item = item.parent()

        self.mask_model.clearItemChildren(item)
        self.mask_model.model.removeRow(item.index().row())
        self.mask_model.generateMask()
        self.parseAndSend()

    def parseAndSend(self):
        '''
        This routine will simply grab the parameters of each of the 
        mask widgets and parse it to the linked mask class
        '''
        if not self.mask_core == None:
            self.mask_core.sendToGenerator(recreate = True)
            self.mask_core.generateMask(
                int(self.mask_input_x.text()), 
                int(self.mask_input_y.text()))
            self.updateGraph()

    def updateGraph(self):
        '''
        '''
        data = self.mask_core.mask_gen.mask
        try:
            self.ax.clear()
        except:
            pass
        self.ax.add_plot(
            'Bin', 
            [ i for i in range(data.shape[0])], 
            [ i for i in range(data.shape[1])], 
            data, Name = 'bin' )
        self.ax.redraw()
        
    def saveSingle(self):
        '''
        
        '''
        filters     = "mask_save.txt"
        file_path   = QtWidgets.QFileDialog.getSaveFileName(
                self.parent.window, 
                'Select file',
                filters)[0]

        if not file_path == '':
            self.mask_core.saveSingleMask(os.path.abspath(file_path))

    def saveMultiple(self):
        '''
        
        '''
        filters     = "masks_save.txt"
        file_path   = QtWidgets.QFileDialog.getSaveFileName(
                self.parent.window, 
                'Select file',
                filters)[0]

        if not file_path == '':
            self.mask_core.saveAllMasks(os.path.abspath(file_path))

    def loadSingle(self):
        '''
        
        '''
        filters = "*.txt"

        file_path = QtWidgets.QFileDialog.getOpenFileName(
                self.parent.window, 
                'Select file',
                filters)[0]

        if not file_path == '':
            self.mask_core.loadSingleMask(os.path.abspath(file_path))
            self.updateSelector(self.mask_core.current_mask)
            self.populateAll()

    def loadMultiple(self):
        '''
        
        '''
        filters = "*.txt"

        file_path = QtWidgets.QFileDialog.getOpenFileName(
                self.parent.window, 
                'Select file',
                filters)[0]

        if not file_path == '':
            self.mask_core.loadAllMasks(os.path.abspath(file_path))
            self.updateSelector(self.mask_core.current_mask)
            self.populateAll()

class PanelPageMaskWidget(PageMaskWidget):

    def __init__(self, stack, parent, mask_model):
        PageMaskWidget.__init__(self, stack, parent, mask_model)
        self.local_widget.setStyleSheet(
            "#mask_editor{background:transparent;}")
        self.thread = QtCore.QThread()

    def link(self, mask_core, env):
        '''
        This routine will link to the io manager class
        from the core. 
        '''
        try:
            self.para_group.deleteLater()
        except:
            pass

        self.para_group = QtWidgets.QGroupBox(self.local_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, 
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.para_group.setSizePolicy(sizePolicy)
        self.para_group.setMinimumSize(QtCore.QSize(425, 0))
        self.para_group.setMaximumSize(QtCore.QSize(425, 16777215))
        self.para_group.setBaseSize(QtCore.QSize(425, 200))
        self.para_group.setObjectName("para_group")
        self.mask_layout_control.addWidget(self.para_group)
        
        self.initialize()
        self.env        = env
        self.data       = self.env.current_data.return_as_np()
        self.mask_core  = mask_core
        self.mask_model.link(self.mask_core)
        self.populateSelectors()
        self.updateSelector()
        self.connectSelectors()

    def connect(self):
        '''
        Connect the interactive elements to their
        respective methods.
        '''
        self.mask_button_add.clicked.connect(self.addElement)
        self.mask_button_remove.clicked.connect(self.removeElement)
        self.mask_model.mask_updated.connect(self.parseAndSend)

    def connectSelectors(self):
        '''
        Set the selectors to their methods
        '''
        self.widget_list[1][0].currentIndexChanged.connect(self.buildThread)
        self.widget_list[3][0].currentIndexChanged.connect(self.buildThread)
        self.widget_list[5][0].currentIndexChanged.connect(self.buildThread)
        self.widget_list[7][0].currentIndexChanged.connect(self.buildThread)

    def setup(self):
        '''
        This is the initial setup method that will 
        build the layout and introduce the graphics
        area
        '''
        self.mask_model.connectView('panel', self.mask_list_loaded)
        self.mask_model.connectDrop('panel', self.comboBox)

        self.my_canvas    = Multi_Canvas(
            self.mask_widget_visual,
            grid        = [[True,True],[True,True]],
            x_ratios    = [2,3],
            y_ratios    = [2,2],
            background  = "w",
            highlightthickness = 0)

        #set the subplots as local
        self.ax = self.my_canvas.get_subplot(0,0)
        self.bx = self.my_canvas.get_subplot(0,1)
        self.cx = self.my_canvas.get_subplot(1,0)
        self.dx = self.my_canvas.get_subplot(1,1)

        self.dx.zoomer.set_fixed(fixed = [False,True], fixed_range = [
            None,
            None,
            0,1
        ])

        self.ax.draw()
        self.bx.draw()
        self.cx.draw()
        self.dx.draw()

        self.ax.pointer['Sticky'] = 3
        self.bx.pointer['Sticky'] = 3

        self.cx.pointer['Label_Precision'] = ('.4','.4','.4','.4')
        self.dx.pointer['Label_Precision'] = ('.4','.4','.4','.4')

    def populateSelectors(self):
        '''
        populate the window layout. The grid is the main
        input of this method and all elements will be 
        placed accordingly.
        '''
        self.para_vbox  = QtWidgets.QVBoxLayout()
        self.para_grid  = QtWidgets.QGridLayout()
        self.para_vbox.addLayout(self.para_grid)
        self.para_vbox.addStretch(1)
        self.para_group.setLayout(self.para_vbox)

        #initialise the tab
        self.widget_list    = []

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Parameter:', parent = self.para_group),
            0, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            0, 1, 1, 1, None])
        self.widget_list[-1][0].addItems([ str(val) for val in self.env.current_data.get_axis('Parameter') ])
        self.para_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Measurement:', parent = self.para_group),
            0, 2, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            0, 3, 1, 1, None])
        self.widget_list[-1][0].addItems([ str(val) for val in self.env.current_data.get_axis('Measurement') ])
        self.meas_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Echo time:', parent = self.para_group),
            1, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            1, 1, 1, 1, None])
        self.widget_list[-1][0].addItems([ str(val) for val in self.env.current_data.get_axis('Echo Time') ])
        self.echo_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Foil:'),
            1, 2, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            1, 3, 1, 1, None])
        self.widget_list[-1][0].addItems([ str(val) for val in self.env.current_data.get_axis('Foil') ])
        self.foil_drop = self.widget_list[-1][0]

        ##############################################
        #add the tabs
        for element in self.widget_list:
            self.para_grid.addWidget(
                element[0], 
                element[1], 
                element[2], 
                element[3], 
                element[4])

            if not element[5] == None:
                element[0].setAlignment(element[5])

    def parseAndSend(self):
        '''
        This routine will simply grab the parameters of each of the 
        mask widgets and parse it to the linked mask class
        '''
        if not self.mask_core == None:
            self.mask_core.sendToGenerator(recreate = True)
            self.mask_core.generateMask(
                int(self.mask_input_x.text()), 
                int(self.mask_input_y.text()))
            self.buildThread()

    def updateGraph(self):
        '''
        '''
        self.buildThread()

    def buildThread(self):
        '''
        the computation will be done in a thread and 
        if not finished interupted to allow the UI to
        run smoothly
        '''
        self.thread.terminate()
        self.thread.wait()
        parameters = self.prepareThread()
        self.worker = Worker(parameters)
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.updateVisual)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def prepareThread(self):
        '''
        the computation will be done in a thread and 
        if not finished interupted to allow the UI to
        run smoothly
        '''
        try:
            self.env.get_result('Shift calculation')
        except:
            self.env.process.calculate_echo()
            self.env.process.remove_foils()
            self.env.fit.fake_calc_shift(
                self.env.current_data, 
                self.env.mask, 
                self.env.results)

        ##############################################
        #grab the parameters from the UI
        para    = self.env.current_data.get_axis(
            self.env.current_data.axes.names[0])[
                self.widget_list[1][0].currentIndex()]
        meas    = self.env.current_data.get_axis(
            self.env.current_data.axes.names[1])[
                self.widget_list[3][0].currentIndex()]
        echo    = self.env.current_data.get_axis(
            self.env.current_data.axes.names[2])[
                self.widget_list[5][0].currentIndex()]
        foil    = self.env.current_data.get_axis(
            self.env.current_data.axes.names[3])[
                self.widget_list[7][0].currentIndex()]

        ##############################################
        #process index
        para_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[0],
            para)
        meas_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[1],
            meas)
        echo_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[2],
            echo)
        foil_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[3], 
            foil)

        self.mask = self.env.mask.mask

        return [
            self.data[para_idx,meas_idx,:,:,:],
            para,meas,
            echo,foil,
            para_idx, meas_idx,
            echo_idx, foil_idx,
            self.env,
            self.mask]

    def updateVisual(self):
        '''
        Update the visual component from a thread
        '''

        try:
            para            = self.worker.parameters[1]
            self.reshaped   = self.worker.parameters[0]
            self.process    = self.worker.process
            self.counts     = self.worker.counts
            self.fit        = self.worker.fit

        except:
            return None

        try:
            self.ax.clear()
            self.bx.clear()
            self.cx.clear()
            self.dx.clear()

        except:
            pass

        x = np.arange(0,128,1)
        y = np.arange(0,128,1)
        x_1 = np.arange(0,15,0.01)

        #set the two bin
        self.ax.add_plot(
            'Bin', x, y, np.log10(np.sum(
                self.reshaped[
                    self.echo_drop.currentIndex(),
                    self.foil_drop.currentIndex()], 
                    axis=(0))+1), Name = 'bin' )

        self.bx.add_plot(
            'Bin', x, y, np.log10(
                self.mask * np.sum(
                    self.reshaped[
                        self.echo_drop.currentIndex(),
                        self.foil_drop.currentIndex()
                    ], axis=(0))+1 ), Name = 'bin')

        #set the main scatter plot of the counts
        self.cx.add_plot(
            'Scatter', 
            range(16), 
            self.counts, 
            Style   = ['s','10'], 
            Log     = [False,False],
            Error   = {
                'bottom': np.sqrt(self.counts),
                'top': np.sqrt(self.counts)})

        if not self.fit == None:
            self.cx.add_plot(
                'Scatter', x_1, 
                self.fit['ampl']*np.cos(x_1/16.*2*np.pi+self.fit['phase'])+self.fit['mean'], 
                Style   = ['-'], 
                Log     = [False,False])

        if not self.process == None:
            self.dx.add_plot(
                'Scatter', 
                self.process['Axis'][para], 
                self.process['Contrast'][para], 
                Style   = ['-','s','10'], 
                Log     = [True,False])

        self.ax.redraw()
        self.bx.redraw()
        self.cx.redraw()
        self.dx.redraw()

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    intReady = QtCore.pyqtSignal(int)

    def __init__(self, parameters):
        '''
        define the parameters
        ———————
        Input: 
        - 0 data as numpy array
        - 1 para
        - 2 meas
        - 3 echo
        - 4 foil
        - 5 para
        - 6 meas
        - 7 echo
        - 8 foil
        - 9 env
        - 10 mask
        '''
        QtCore.QObject.__init__(self)
        self.parameters = parameters
        
    @QtCore.pyqtSlot()
    def run(self): 
        '''
        define the parameters
        '''
        para        = self.parameters[1]
        foil        = self.parameters[4]
        echo_idx    = self.parameters[7]
        foil_idx    = self.parameters[8]

        self.reshaped       = self.parameters[0]
        self.mask           = self.parameters[10]
        self.env            = self.parameters[9]
        self.counts         = [
            np.sum(self.mask * self.reshaped[echo_idx,foil_idx,timechannel]) 
            for timechannel in range(16)]

        try:
            self.env.fit.fit_data_cov(
                self.env.results, 
                self.counts, 
                np.sqrt(self.counts), 
                Qmin=0.)

            self.fit = self.env.get_result('Fit data covariance')
        except:
            self.fit = None
        self.env.fit.calcCtrstMain( 
                self.env.current_data,
                self.env.mask,
                self.env.results,
                select = [para],
                foil = foil)

        self.process = self.env.get_result('Contrast calculation')
        try:
            self.env.fit.calcCtrstMain( 
                    self.env.current_data,
                    self.env.mask,
                    self.env.results,
                    select = [para],
                    foil = foil)

            self.process = self.env.get_result('Contrast calculation')
        except:
            self.process = None

        self.finished.emit()

class NewMaskWindow(QtWidgets.QMainWindow,Ui_new_msk):
    '''
    In this class we install a window that will allow the 
    user to set a new mask. 
    '''
    def __init__(self, parent):
    
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        Ui_new_msk.__init__(self)
        self.setupUi(self)
        self.show()