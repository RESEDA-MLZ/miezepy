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


# public dependencies
import numpy as np
from PyQt5 import QtWidgets
import pyqtgraph as pg

# private dependencies
from ...qt_gui.display_data_raw_ui import Ui_raw_display

# private plotting library
#from simpleplot.canvas.multi_canvas import MultiCanvasItem


class DisplayRawWindowLayout(Ui_raw_display):
    '''
    This class will manage the raw import
    machinery. the UI is inherited through
    Ui_main_window from the Qt designer anf then
    converted through pyuic5
    '''

    def __init__(self, window, window_manager):

        ##############################################
        # Local pointers
        Ui_raw_display.__init__(self)

        self.window_manager = window_manager
        self.window = window
        self.setup()

    def setup(self):
        '''
        This is the initial setup method that will
        build the layout and introduce the graphics
        area
        '''
        self.setupUi(self.window)


    def link(self, import_object, mode='3D'):
        '''
        This routine will link to the io manager class
        from the core.
        '''
        self._mode = mode
        self.import_object = import_object
        self.initialize()
        self.connect()

    def initialize(self):
        '''
        This routine will link to the io manager class
        from the core.
        '''
        self.echo_drop.addItems(
            [str(e) for e in self.import_object.meta_handler.values['Echo']])
        self.foil_spin.setMinimum(0)
        self.foil_spin.setMaximum(
            self.import_object.data_handler.dimension[0] - 1)
        self.time_spin.setMinimum(0)
        self.time_spin.setMaximum(
            self.import_object.data_handler.dimension[1] - 1)

        if self._mode == '3D':
            self.time_spin.show()
            self.time_check.show()

        self.draw()
        self.connect()


    def connect(self):
        '''
        This routine will link to the io manager class
        from the core.
        '''
        self.foil_spin.valueChanged.connect(self.draw)
        self.time_spin.valueChanged.connect(self.draw)
        self.echo_drop.currentIndexChanged.connect(self.draw)
        self.foil_check.stateChanged.connect(self.draw)
        self.time_check.stateChanged.connect(self.draw)
        self.log_check.stateChanged.connect(self.draw)
        self.norm_check.stateChanged.connect(self.draw)

        #self.plot_widget.setMouseTracking(True)
        self.plot_widget.scene().sigMouseMoved.connect(self.mouse_moved)

        #proxy = pg.SignalProxy(self.plot_item.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_moved)


    def draw(self, stuff=None):
        '''
        '''
        data = self.import_object.file_handler.getElement(
            self.echo_drop.currentIndex())

        if self.foil_check.isChecked():
            data = np.sum(data, axis=0)
        else:
            data = data[self.foil_spin.value()]
        
        if self._mode == '4D':
            print('Something is wrong...mode = 4D')
            data = data
        elif self.time_check.isChecked():
            data = np.sum(data, axis=0)
        else:
            data = data[self.time_spin.value()]

        if self.log_check.isChecked():
            data = np.log10(data+1)

        if self.norm_check.isChecked():
            data_min = np.amin(data)
            data_max = np.amax(data)
            data = (data - data_min)/(data_max - data_min) * 10.

        if self._mode == '3D':
            x = []
            y = []
            x, y = zip(*[(i, j) for i in range(data.shape[0]) for j in range(data.shape[1])])
            x = np.array(x)
            y = np.array(y)

            heatmap, xedges, yedges = np.histogram2d(y, x, bins=[data.shape[1], data.shape[0]], weights=data.flatten())#np.flip(data.flatten()))

            colormap = pg.colormap.get('plasma')  # or 'viridis', 'thermal', etc.
            lut = colormap.getLookupTable(0.0, 1.0, 256)
            self.image_item.setImage(heatmap.T, lut=lut)
            self.image_item.setRect([xedges[0], yedges[0], xedges[-1] - xedges[0], yedges[-1] - yedges[0]])

            min_val = np.min(heatmap)
            max_val = np.max(heatmap)
            self.image_item.setLevels([min_val,max_val])

            self.colorbar.setImageItem(self.image_item)
            self.colorbar.setLevels(low=min_val,high=max_val)
            self.colorbar.setColorMap(colorMap=colormap)

    
    def mouse_moved(self, pos):
        '''
        '''
        if self.plot_item.getViewBox().sceneBoundingRect().contains(pos):
            mouse_point = self.plot_item.getViewBox().mapSceneToView(pos)
            
            x = mouse_point.x()
            y = mouse_point.y()
            self.v_line.setPos(x)
            self.h_line.setPos(y)
            
            
            img_array = self.image_item.image
            rect = self.image_item.mapRectToParent(self.image_item.boundingRect())
            if img_array is not None and rect is not None:
                px = int((x - rect.left()) / rect.width() * img_array.shape[1])
                py = int((y - rect.top()) / rect.height() * img_array.shape[0])

                if 0 <= px < img_array.shape[1] and 0 <= py < img_array.shape[0]:
                    val = img_array[px, py]  # Note: row, col = y, x
                    
                    self.xy_label.setText(f"x = {x:.0f},    y = {y:.0f},    value = {val:.0f}")
            

