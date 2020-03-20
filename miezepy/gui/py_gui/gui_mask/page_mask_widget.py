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
import numpy as np
import os

#private dependencies
from ...qt_gui.main_mask_editor_ui  import Ui_mask_editor
from ..gui_common.dialog            import dialog 
from ...qt_gui.new_mask_ui          import Ui_new_msk
from .panel_worker                  import PanelWorker

#private plotting library
from simpleplot.canvas.multi_canvas import MultiCanvasItem
from simpleplot.ploting.graph_items.pie_item import PieItem
from simpleplot.ploting.graph_items.rectangle_item import RectangleItem
from simpleplot.ploting.graph_items.triangle_item import TriangleItem
from simpleplot.ploting.graph_items.ellipse_item import EllipseItem
from simpleplot.gui_main.widgets.scientific_combobox import ScientificComboBox

class PageMaskWidget(Ui_mask_editor):
    
    def __init__(self, stack, parent, mask_interface):
    
        Ui_mask_editor.__init__(self)

        #set the local pointers
        self.parent         = parent
        self.stack          = stack
        self.local_widget   = QtWidgets.QWidget() 
        self.mask_interface = mask_interface 

        #build GUI
        self.setupUi(self.local_widget)
        self.para_group = QtWidgets.QGroupBox(self.local_widget)
        self._setup()
        self._initialize()
        self._connect()

    def _resetPara(self):
        '''
        Reset the parameter setting group
        '''
        try:
            self.para_group.deleteLater()
        except:
            pass

        self.para_group = QtWidgets.QGroupBox(self.local_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Fixed)
        self.para_group.setSizePolicy(sizePolicy)
        self.mask_layout_control.addWidget(self.para_group)

    def _setup(self):
        '''
        This is the initial setup method that will 
        build the layout and introduce the graphics
        area
        '''
        #initialise the widgets
        self.tree               = self.mask_interface.getTreeView()
        self.mask_combo_box     = self.mask_interface.getComboBox()
        self.add_mask_button    = QtWidgets.QPushButton("+")
        self.remove_mask_button = QtWidgets.QPushButton("-")

        self.mask_tree_layout.addWidget(self.tree)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed)
        self.mask_combo_box.setSizePolicy(size_policy)
        self.combo_layout.addWidget(self.mask_combo_box)
        self.combo_layout.addWidget(self.add_mask_button)
        self.combo_layout.addWidget(self.remove_mask_button)

        #initialise the graphs
        self.my_canvas    = MultiCanvasItem(
            self.mask_widget_visual,
            grid        = [[True]],
            x_ratios    = [1],
            y_ratios    = [1],
            background  = "w",
            highlightthickness = 0)
        self.ax = self.my_canvas.getSubplot(0,0)
        self.ax.axes.general_handler['Aspect ratio'] = [True, 1.]
        self.ax.pointer.pointer_handler['Sticky'] = 2
        self.my_canvas.canvas_nodes[0][0][0].grid_layout.setMargin(0)
        self.ax.draw()

    def _initialize(self):
        '''
        Reset all the inputs and all the fields
        present in the current view.
        '''
        self.mask_core = None
        self._plot_item = []
        self.current_data = None

    def _connect(self):
        '''
        Connect the interactive elements to their
        respective methods.
        '''
        self.mask_button_add.clicked.connect(self.addItem)
        self.mask_button_remove.clicked.connect(self.removeItem)
        self.mask_interface.mask_updated.connect(self._parseAndSend)

        self.add_mask_button.clicked.connect(self.newMask)
        self.remove_mask_button.clicked.connect(self.mask_interface.removeCurrentMask)

    def _populateSelectors(self):
        '''
        populate the window layout. The grid is the main
        input of this method and all elements will be 
        placed accordingly.
        '''
        #Visual selector
        self._visual_mask_pixel     = QtWidgets.QRadioButton("View pixel mask")
        self._visual_mask_data      = QtWidgets.QRadioButton("View data")
        self._visual_button_group   = QtWidgets.QButtonGroup(self.widget)
        self._visual_button_group.addButton(self._visual_mask_pixel, 0)
        self._visual_button_group.addButton(self._visual_mask_data, 1)

        self.visual_select = QtWidgets.QHBoxLayout()
        self.visual_select.addWidget(self._visual_mask_pixel)
        self.visual_select.addWidget(self._visual_mask_data)

        self.para_vbox  = QtWidgets.QVBoxLayout()
        self.para_grid  = QtWidgets.QGridLayout()
        self.para_vbox.addLayout(self.visual_select)
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
        self.widget_list[-1][0].addItems([ 
            str(val) for val in self.env.current_data.get_axis('Parameter') ])
        self.para_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Measurement:', parent = self.para_group),
            1, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            1, 1, 1, 1, None])
        self.widget_list[-1][0].addItems([ 
            str(val) for val in self.env.current_data.get_axis('Measurement') ])
        self.meas_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Echo time:', parent = self.para_group),
            2, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            ScientificComboBox( parent = self.para_group),
            2, 1, 1, 1, None])
        self.widget_list[-1][0].addItems(self.env.current_data.get_axis('Echo Time'))
        self.echo_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Foil:'),
            3, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            3, 1, 1, 1, None])
        self.widget_list[-1][0].addItems([ 
            str(val) for val in self.env.current_data.get_axis('Foil') ])
        self.foil_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QCheckBox('Log view:'),
            4, 1, 1, 1, None])
        self.log_view = self.widget_list[-1][0]

        ##############################################
        #add the tabs
        for element in self.widget_list:
            self.para_grid.addWidget(
                element[0], 
                element[1], 
                element[2], 
                element[3], 
                element[4])

            if not element[5] is None:
                element[0].setAlignment(element[5])

    def _connectSelectors(self):
        '''
        Set the selectors to their methods
        '''
        self.widget_list[1][0].currentIndexChanged.connect(self._prepareData)
        self.widget_list[3][0].currentIndexChanged.connect(self._prepareData)
        self.widget_list[5][0].currentIndexChanged.connect(self._prepareData)
        self.widget_list[7][0].currentIndexChanged.connect(self._prepareData)
        self.widget_list[8][0].clicked.connect(self._prepareData)
        self._visual_mask_pixel.clicked.connect(self._handleVis)
        self._visual_mask_data.clicked.connect(self._handleVis)

    def _handleVis(self):
        '''
        the computation will be done in a thread and 
        if not finished interupted to allow the UI to
        run smoothly
        '''
        if self._visual_button_group.checkedId() == 0:
            for child in self.widget_list:
                child[0].setVisible(False)
            self._updateGraph()
        else:
            for child in self.widget_list:
                child[0].setVisible(True)
            self._prepareData()

    def _prepareData(self):
        '''
        the computation will be done in a thread and 
        if not finished interupted to allow the UI to
        run smoothly
        '''

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
            self.env.current_data.axes.names[0], para)
        meas_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[1], meas)
        echo_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[2], echo)
        foil_idx = self.env.current_data.get_axis_idx(
            self.env.current_data.axes.names[3], foil)

        data = self.data[para_idx,meas_idx,echo_idx,foil_idx,:]
        data = np.sum(data,axis=(0))

        if self.log_view.isChecked():
            data = np.log10(data+1)

        self.current_data = data
        self._updateGraph()

    def newMask(self):
        '''
        This routine will create an input dialog
        and then get it
        '''
        text, ok = QtWidgets.QInputDialog.getText(
            self.widget, 'New mask name', 'Name of the new mask:')
        if ok:
            self.mask_interface.insertNewMask(text)

    def link(self, mask_core, env):
        '''
        This routine will link to the io manager class
        from the core. 
        '''
        self._resetPara()
        self._initialize()

        self.env        = env
        self.data       = self.env.current_data.returnAsNumpy()
        self.mask_core  = mask_core
        
        self._populateSelectors()
        self._connectSelectors()

    def unlink(self):
        '''
        To remove the item
        '''
        self.mask_core = None

    def addItem(self):
        '''
        Add an element into the list which is loaded 
        from a custom widget. If the element is part of
        the default series create a new one
        called by the default name with the appendix '_mod'
        '''
        self.mask_interface.addItem()

    def removeItem(self):
        '''
        Add an element into the list which is loaded 
        from a custom widget.
        '''
        index = self.tree.selectionModel().currentIndex()
        self.mask_interface.removeItem(index.row())

    def _parseAndSend(self):
        '''
        This routine will simply grab the parameters of each of the 
        mask widgets and parse it to the linked mask class
        '''
        if not self.mask_core == None:
            self.mask_core.sendToGenerator(recreate = True)
            self.mask_core.generateMask(
                int(self.mask_input_x.text()), 
                int(self.mask_input_y.text())) 
            self._updateGraph()

    def _checkUpdateNeed(self):
        '''
        Check what has to be actually updated
        '''
        if len(self._plot_item) != self.tree.model().root()._children:
            self.ax.clear()
            self.mask_plot = self.ax.addPlot('Surface', Name = 'Mask area')
            self._plot_item = []
            for child in self.tree.model().root()._children:
                self._plot_item.append(self.ax.addItem(child._value))
            self.ax.draw()

        else:
            for i,child in enumerate(self.tree.model().root()._children):
                if child._value != self._plot_item[i]._name:
                    self.ax.removeItem(self._plot_item[i])
                    self._plot_item[i] = self.ax.addItem(child._value)

    def _updateGraph(self):
        '''
        '''
        self._checkUpdateNeed()

        for i,child in enumerate(self.tree.model().root()._children):
            self._plot_item[i].load(child.save())

        if self._visual_button_group.checkedId() == 0:
            self.mask_plot.setData(
                x = np.array([ i for i in range(self.mask_core.mask_gen.mask.shape[0])]), 
                y = np.array([ i for i in range(self.mask_core.mask_gen.mask.shape[1])]), 
                z = self.mask_core.mask_gen.mask)
        elif not self.current_data is None:
            self.mask_plot.setData(
                x = np.array([ i for i in range(self.mask_core.mask_gen.mask.shape[0])]), 
                y = np.array([ i for i in range(self.mask_core.mask_gen.mask.shape[1])]), 
                z = self.current_data)
        
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

class PanelPageMaskWidget(PageMaskWidget):

    def __init__(self, stack, parent, mask_interface):
        PageMaskWidget.__init__(self, stack, parent, mask_interface)
        self.local_widget.setStyleSheet(
            "#mask_editor{background:transparent;}")
        self._threads = []

    def link(self, mask_core, env):
        '''
        This routine will link to the io manager class
        from the core. 
        '''
        self._resetPara()
        self._initialize()

        self.env        = env
        self.data       = self.env.current_data.returnAsNumpy()
        self.mask_core  = mask_core
        
        self._populateSelectors()
        self._connectSelectors()

    def _resetPara(self):
        '''
        Reset the parameter setting group
        '''
        try:
            self.para_group.deleteLater()
        except:
            pass

        self.para_group = QtWidgets.QGroupBox(self.local_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Fixed)
        self.para_group.setSizePolicy(sizePolicy)
        self.mask_layout_control.addWidget(self.para_group)

    def _setup(self):
        '''
        This is the initial setup method that will 
        build the layout and introduce the graphics
        area
        '''
        #initialise the widgets
        self._live = False

        self.tree               = self.mask_interface.getTreeView()
        self.mask_combo_box     = self.mask_interface.getComboBox()
        self.add_mask_button    = QtWidgets.QPushButton("+")
        self.remove_mask_button = QtWidgets.QPushButton("-")

        self.mask_tree_layout.addWidget(self.tree)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed)
        self.mask_combo_box.setSizePolicy(size_policy)
        self.combo_layout.addWidget(self.mask_combo_box)
        self.combo_layout.addWidget(self.add_mask_button)
        self.combo_layout.addWidget(self.remove_mask_button)

        #initialise the graphs
        self.my_canvas    = MultiCanvasItem(
            self.mask_widget_visual,
            grid        = [[True,True],[True,True]],
            x_ratios    = [1,1],
            y_ratios    = [1,1],
            background  = "w",
            highlightthickness = 0)

        #set the subplots as local
        self.ax = self.my_canvas.getSubplot(0,0)
        self.ax.axes.label_handler['Active']    = [True, True, True, True]
        self.ax.axes.label_handler['Text']      = ['py', 'px', 'None', 'None']

        self.bx = self.my_canvas.getSubplot(0,1)
        self.bx.axes.label_handler['Active']    = [True, True, True, True]
        self.bx.axes.label_handler['Text']      = ['py', 'px', 'None', 'None']

        self.cx = self.my_canvas.getSubplot(1,0)
        self.cx.axes.label_handler['Active']    = [True, True, True, True]
        self.cx.axes.label_handler['Text']      = ['Intensity', 'Time channel', 'None', 'None']

        self.dx = self.my_canvas.getSubplot(1,1)
        self.dx.axes.label_handler['Active']    = [True, True, True, True]
        self.dx.axes.label_handler['Text']      = ['Contrast', 'Echo Time', 'None', 'None']
        self.dx.axes.general_handler['Log']     = [True, False]

        self.dx.zoomer['Zoom fixed']            = [False,True]
        self.dx.zoomer['Zoom fixed range']      = [0,1,0,1]

        #set the two bin
        self.first_surface_plot = self.ax.addPlot('Surface', Name = 'Data area' )
        self.second_surface_plot = self.bx.addPlot('Surface',Name = 'Mask and Data area')
        histogram_0 = self.first_surface_plot.childFromName('Surface').childFromName('Shader').getHistogramItem()
        self.ax.addHistogramItem('right', histogram_0)
        histogram_1 = self.second_surface_plot.childFromName('Surface').childFromName('Shader').getHistogramItem()
        self.bx.addHistogramItem('right', histogram_1)

        #set the main scatter plot of the counts
        self.sine_data_plot = self.cx.addPlot(
            'Scatter', 
            Name    = 'Raw phase', 
            Style   = ['s','10'])

        self.sine_fit_2_plot = self.cx.addPlot(
            'Scatter',
            Name    = 'Fitted phase', 
            Style   = ['-'])

        self.contrast_plot = self.dx.addPlot(
            'Scatter',
            Name    = 'Contrast', 
            Style   = ['-','s','10'])

        self.ax.draw()
        self.bx.draw()
        self.cx.draw()
        self.dx.draw()

        self.ax.pointer.pointer_handler['Sticky'] = '2'
        self.bx.pointer.pointer_handler['Sticky'] = '2'
        self.cx.pointer.pointer_handler['Sticky'] = '3'
        self.dx.pointer.pointer_handler['Sticky'] = '3'

        self.my_canvas.canvas_nodes[0][0][0].grid_layout.setMargin(0)
        self.my_canvas.canvas_nodes[0][1][0].grid_layout.setMargin(0)
        self.my_canvas.canvas_nodes[1][0][0].grid_layout.setMargin(0)
        self.my_canvas.canvas_nodes[1][1][0].grid_layout.setMargin(0)

    def _populateSelectors(self):
        '''
        populate the window layout. The grid is the main
        input of this method and all elements will be 
        placed accordingly.
        '''
        #Visual selector
        self._visual_data_raw       = QtWidgets.QRadioButton("Raw data")
        self._visual_data_corrected = QtWidgets.QRadioButton("Corrected data")
        self._visual_button_group   = QtWidgets.QButtonGroup(self.widget)
        self._visual_button_group.addButton(self._visual_data_raw, 0)
        self._visual_button_group.addButton(self._visual_data_corrected, 1)

        self.visual_select = QtWidgets.QHBoxLayout()
        self.visual_select.addWidget(self._visual_data_raw)
        self.visual_select.addWidget(self._visual_data_corrected)

        self.para_vbox  = QtWidgets.QVBoxLayout()
        self.para_grid  = QtWidgets.QGridLayout()
        self.para_vbox.addLayout(self.visual_select)
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
        self.widget_list[-1][0].addItems([ 
            str(val) for val in self.env.current_data.get_axis('Parameter') ])
        self.para_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Measurement:', parent = self.para_group),
            1, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            1, 1, 1, 1, None])
        self.widget_list[-1][0].addItems([ 
            str(val) for val in self.env.current_data.get_axis('Measurement') ])
        self.meas_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Echo time:', parent = self.para_group),
            2, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            ScientificComboBox( parent = self.para_group),
            2, 1, 1, 1, None])
        self.widget_list[-1][0].addItems(self.env.current_data.get_axis('Echo Time'))
        self.echo_drop = self.widget_list[-1][0]

        #---
        self.widget_list.append([
            QtWidgets.QLabel('Foil:'),
            3, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter])
        self.widget_list.append([
            QtWidgets.QComboBox( parent = self.para_group),
            3, 1, 1, 1, None])
        self.widget_list[-1][0].addItems([ 
            str(val) for val in self.env.current_data.get_axis('Foil') ])
        self.foil_drop = self.widget_list[-1][0]

       #---
        self.widget_list.append([
            QtWidgets.QCheckBox('Log view:'),
            4, 0, 1, 1, None])
        self.log_view = self.widget_list[-1][0]

        self.widget_list.append([
            QtWidgets.QCheckBox('Live refresh',parent = self.para_group),
            4, 1, 1, 1, None])
        self.widget_list[-1][0].setChecked(False)

        self.widget_list.append([
            QtWidgets.QPushButton('Compute', parent = self.para_group),
            5, 1, 1, 1, None])
        self.compute_button = self.widget_list[-1][0]

        ##############################################
        #add the tabs
        for element in self.widget_list:
            self.para_grid.addWidget(
                element[0], 
                element[1], 
                element[2], 
                element[3], 
                element[4])

            if not element[5] is None:
                element[0].setAlignment(element[5])

    def _connectSelectors(self):
        '''
        Set the selectors to their methods
        '''
        self._visual_data_raw.clicked.connect(self._parseAndSend)
        self._visual_data_corrected.clicked.connect(self._parseAndSend)
        self.widget_list[1][0].currentIndexChanged.connect(self._parseAndSend)
        self.widget_list[3][0].currentIndexChanged.connect(self._parseAndSend)
        self.widget_list[5][0].currentIndexChanged.connect(self._parseAndSend)
        self.widget_list[7][0].currentIndexChanged.connect(self._parseAndSend)
        self.widget_list[10][0].clicked.connect(self._parseAndSendManual)
        self.widget_list[9][0].stateChanged.connect(self._setLive)      

    def _setLive(self, num):
        '''
        set the state of the live computation
        '''
        if num == 2:
            self._live = True
        else:
            self._live = False

    def _parseAndSend(self):
        '''
        This routine will simply grab the parameters of each of the 
        mask widgets and parse it to the linked mask class
        '''
        if not self.mask_core == None and self._live:
            self.mask_core.sendToGenerator(recreate = True)
            self.mask_core.generateMask(
                int(self.mask_input_x.text()), 
                int(self.mask_input_y.text()))
            self._buildThread()

    def _parseAndSendManual(self):
        '''
        This routine will simply grab the parameters of each of the 
        mask widgets and parse it to the linked mask class
        '''
        if not self.mask_core == None:
            self.mask_core.sendToGenerator(recreate = True)
            self.mask_core.generateMask(
                int(self.mask_input_x.text()), 
                int(self.mask_input_y.text()))
            self._buildThread()

    def _updateGraph(self):
        '''
        '''
        self._updateVisual()

    def _buildThread(self):
        '''
        the computation will be done in a thread and 
        if not finished interupted to allow the UI to
        run smoothly
        '''
        for i in range(len(self._threads))[::-1]:
            if self._threads[i][0].isFinished():
                del self._threads[i]

        parameters = self._prepareThread()
        worker = PanelWorker(self.env.process.calcContrastSingle)
        worker.setParameters(*parameters)

        thread = QtCore.QThread()
        worker.moveToThread(thread)
        worker.finished.connect(self._updateVisual)
        worker.finished.connect(thread.quit)
        thread.started.connect(worker.run)
        thread.start()

        self._threads.append([thread,worker])

    def _prepareThread(self):
        '''
        the computation will be done in a thread and 
        if not finished interupted to allow the UI to
        run smoothly
        '''
        results = self.env.results.generateResult(name = 'Contrast mode')
        if self._visual_button_group.checkedId() == 0:
            self.env.process.calculateEcho()
            self.env.fit.noCorrection(self.env.current_data,self.env.results)
            self.data = self.env.results.getLastResult('Uncorrected Phase', 'Shift')
            results['Mode'] = 'Uncorrected'
        else:
            self.data = self.env.results.getLastResult('Corrected Phase', 'Shift')
            results['Mode'] = 'Corrected'
        results.setComplete()

        return [
            self.data[self.widget_list[1][0].currentText()][int(float(self.widget_list[3][0].currentText()))][float(self.widget_list[5][0].currentData())][int(self.widget_list[7][0].currentText())],
            self.widget_list[1][0].currentText(),
            int(self.widget_list[7][0].currentText()),
            self.env.mask.mask,self.env.results, 
            self.env.fit.para_dict['time_channels']]

    def _updateVisual(self):
        '''
        Update the visual component from a thread
        '''
        for i in range(len(self._threads))[::-1]:
            if self._threads[i][1]._finished:
                self.worker = self._threads[i][1]
                break
        try:

            para    = self.worker.para
            data    = self.worker.data
            process = self.worker.process
            counts  = self.worker.counts
            fit     = self.worker.fit

        except:
            return None

        x   = np.arange(0,128,1)
        y   = np.arange(0,128,1)
        x_1 = np.arange(0,15,0.01)

        #set the two bin
        self.first_surface_plot.setData(
            x = x,
            y = y, 
            z = np.log10(np.sum(data,axis=(0))+1))

        self.second_surface_plot.setData(
            x = x,
            y = y, 
            z = np.log10(self.env.mask.mask * np.sum(data, axis=(0))+1 ))

        #set the main scatter plot of the counts
        self.sine_data_plot.setData(
            x = np.array([i for i in range(len(counts))]),
            y = np.array(counts),
            error = {
                'height':None,
                'bottom': np.sqrt(counts),
                'top': np.sqrt(counts)})

        if not fit == None:
            self.sine_fit_2_plot.setData(
                x = x_1, 
                y = fit['amplitude']*np.cos(x_1/16.*2*np.pi+fit['phase'])+fit['mean'])

        if not process == None:
            self.contrast_plot.setData(                
                x = process['Axis'][para], 
                y = process['Contrast'][para] )
        
        self.ax.zoomer.zoom()
        self.bx.zoomer.zoom()
        self.cx.zoomer.zoom()
        self.dx.zoomer.zoom()
