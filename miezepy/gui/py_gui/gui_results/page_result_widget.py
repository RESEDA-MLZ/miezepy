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
import pyqtgraph as pg
import matplotlib.pyplot as plt


#private dependencies
from ...qt_gui.main_result_ui   import Ui_result_widget
from ..gui_common.dialog        import dialog 
#from .result_list_handler       import ResultHandlerUI
#from .drag_drop_trees           import ResultTree, PlotTree

#private plotting library
#from simpleplot.canvas.multi_canvas import MultiCanvasItem

class PageResultWidget(Ui_result_widget):
    
    def __init__(self, stack, parent):
        
        Ui_result_widget.__init__(self)
        self.parent         = parent
        self.stack          = stack
        self.local_widget   = QtWidgets.QWidget() 
        self.env_handler    = None
        self._setup()
        self._connect()
        
    def _setup(self):
        '''
        This is the initial setup method that will 
        build the layout and introduce the graphics
        area.
        '''
        self.setupUi(self.local_widget)
        self.env_checkbox_list = []
        self.results_to_plot = {}
        log_x = self.plot_widget.getPlotItem().getAxis('bottom').logMode
        log_y = self.plot_widget.getPlotItem().getAxis('left').logMode
        if log_x:
            self.process_check_log_x.setChecked(True)
        if log_y:
            self.process_check_log_y.setChecked(True)

    def _connect(self):
        '''
        Connect all Qt slots to their respective methods.
        '''
        self.process_refresh_button.clicked.connect(self.refresh_dataset)
        self.plotitems_button.clicked.connect(self.plot_selected)            

        self.process_check_log_x.toggled.connect(lambda checked, checkbox=self.process_check_log_x: self.setLogX(checkbox, checked))
        self.process_check_log_y.toggled.connect(lambda checked, checkbox=self.process_check_log_y: self.setLogY(checkbox, checked))
        self.process_check_grid_x.toggled.connect(lambda checked, checkbox=self.process_check_grid_x: self.setGridX(checkbox, checked))
        self.process_check_grid_y.toggled.connect(lambda checked, checkbox=self.process_check_grid_y: self.setGridY(checkbox, checked))

        self.func1.toggled.connect(lambda checked, checkbox=self.func1: self.func_checkbox_toggled(checkbox, checked))
        self.func2.toggled.connect(lambda checked, checkbox=self.func2: self.func_checkbox_toggled(checkbox, checked))
        self.func3.toggled.connect(lambda checked, checkbox=self.func3: self.func_checkbox_toggled(checkbox, checked))


    def refresh_dataset(self):
        '''
        Refresh the dictionary of environments to 
        take into account. 
        '''
        # first clean what was there before
        self.clean_checkbox_list()

        names = [env.name for env in self.env_handler.env_array]

        for name in names:
            target  = self.env_handler.getEnv(name)
            result  = target.results.getLastResult(name = 'Contrast fit')
            if not result is None:
                self.add_env_label(name)
                
                for ds in result['Parameters'].keys():
                    self.results_to_plot.setdefault(name+'__'+ds,{})['x'] = result['Parameters'][ds]['x']
                    self.results_to_plot.setdefault(name+'__'+ds,{})['y'] = result['Parameters'][ds]['y']
                    self.results_to_plot.setdefault(name+'__'+ds,{})['y_error'] = result['Parameters'][ds]['y_error']
                    self.results_to_plot.setdefault(name+'__'+ds,{})['to_plot'] = 'False'

                    if (result['Reference'] is None or ds not in result['Reference']) and (result['BG'] is None or ds not in result['BG']):
                        self.results_to_plot.setdefault(name+'__'+ds,{})[self.func1.objectName()+'__x'] = result['Curve Axis'][ds]
                        self.results_to_plot.setdefault(name+'__'+ds,{})[self.func1.objectName()+'__y'] = result['Curve'][ds]
                        #self.results_to_plot.setdefault(name+'__'+ds,{})['x_func2'] = 
                        #self.results_to_plot.setdefault(name+'__'+ds,{})['y_func2'] = 
                        #self.results_to_plot.setdefault(name+'__'+ds,{})['x_func3'] = 
                        #self.results_to_plot.setdefault(name+'__'+ds,{})['y_func3'] = 

                        self.results_to_plot.setdefault(name+'__'+ds,{})[self.func1.objectName()+'__to_plot'] = 'False'
                        self.results_to_plot.setdefault(name+'__'+ds,{})[self.func2.objectName()+'__to_plot'] = 'False'
                        self.results_to_plot.setdefault(name+'__'+ds,{})[self.func3.objectName()+'__to_plot'] = 'False'                   

                    self.add_env_checkbox(name, ds)

        self.verticalLayout_41.addStretch(1)

    def add_env_label(self, name):
        '''
        comment
        '''
        env_label = QtWidgets.QLabel(self.data_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(env_label.sizePolicy().hasHeightForWidth())
        env_label.setSizePolicy(sizePolicy)
        env_label.setObjectName("env_label"+name)
        self.verticalLayout_41.addWidget(env_label)
        env_label.setText(QtCore.QCoreApplication.translate("result_widget", name))

        #self.env_label_list.append(env_label)

    def add_env_checkbox(self, envname, cboxname):
        '''
        comment
        '''
        env_checkbox = QtWidgets.QCheckBox(self.data_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(env_checkbox.sizePolicy().hasHeightForWidth())
        env_checkbox.setSizePolicy(sizePolicy)
        env_checkbox.setMinimumSize(QtCore.QSize(75, 0))
        env_checkbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        env_checkbox.setObjectName(envname+"__"+cboxname) # before changing name of the checkbox, remember that it is related to the results_to_plot
        env_checkbox.setStyleSheet("QCheckBox { padding-left: 40px; }")
        self.verticalLayout_41.addWidget(env_checkbox)
        env_checkbox.setText(QtCore.QCoreApplication.translate("result_widget", cboxname))

        self.env_checkbox_list.append(env_checkbox)

        env_checkbox.toggled.connect(lambda checked, checkbox=env_checkbox: self.env_checkbox_toggled(checkbox, checked))

    def env_checkbox_toggled(self, checkbox, checked):
        """ Slot to handle checkbox state change. """
        self.results_to_plot[checkbox.objectName()]['to_plot'] = checked

    def func_checkbox_toggled(self, checkbox, checked):
        """ Slot to handle checkbox state change. """
        k = checkbox.objectName()+'__to_plot'
        for key in self.results_to_plot.keys():
            if key in self.results_to_plot and k in self.results_to_plot[key]:
                self.results_to_plot[key][k] = checked

    def clean_checkbox_list(self):
        '''
        '''
        self.results_to_plot.clear()

        if self.verticalLayout_41 is not None:
            while self.verticalLayout_41.count():  # Loop through items in layout
                item = self.verticalLayout_41.takeAt(0)  # Take item from layout
                widget = item.widget()
                
                if isinstance(widget, QtWidgets.QCheckBox): 
                    widget.toggled.disconnect()

                if widget is not None:
                    widget.deleteLater()  # Delete widget safely
                else:
                    self.verticalLayout_41.removeItem(item)  # This removes stretches and empty spaces

        self.env_checkbox_list.clear()

    def plot_selected(self):
        self.plot_widget.clear()

        for i, key in enumerate(self.results_to_plot.keys()):
            if self.results_to_plot[key]['to_plot']==True :
                x = self.results_to_plot[key]['x']
                y = self.results_to_plot[key]['y']
                y_err = self.results_to_plot[key]['y_error']
                color = plt.cm.hsv(1 - ((i/6) - i//6) )
                rgb = tuple(int(c * 255) for c in color[:3])  # Convert to RGB
                self.plot_widget.plot(x, y, symbol='o', symbolSize=8, symbolBrush=rgb, pen=None) #pg.mkPen(color=rgb, width=3))
                #error_bars = pg.ErrorBarItem(x=x, y=y, height=y_err, beam=0.2, pen=rgb)
                #self.plot_widget.addItem(error_bars)
                
                if self.func1.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func1.objectName()+'__to_plot']==True :
                        try:
                            x_func1 = self.results_to_plot[key][self.func1.objectName()+'__x']
                            y_func1 = self.results_to_plot[key][self.func1.objectName()+'__y']
                            self.plot_widget.plot(x_func1, y_func1, pen=pg.mkPen(color=rgb, width=3))
                        except:
                           pass

                if self.func2.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func2.objectName()+'__to_plot']==True :
                        try:
                            x_func2 = self.results_to_plot[key][self.func2.objectName()+'__x']
                            y_func2 = self.results_to_plot[key][self.func2.objectName()+'__y']
                            self.plot_widget.plot(x_func2, y_func2, pg.mkPen(color=rgb, width=3, style=QtCore.Qt.DashLine))     
                        except:
                            pass

                if self.func3.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func3.objectName()+'__to_plot']==True :
                        try:
                            x_func3 = self.results_to_plot[key][self.func3.objectName()+'__x']
                            y_func3 = self.results_to_plot[key][self.func3.objectName()+'__y']
                            self.plot_widget.plot(x_func3, y_func3, pg.mkPen(color=rgb, width=3, style=QtCore.Qt.DotLine))
                        except:
                            pass

    def setLogX(self, checkbox, checked):
        '''
        '''
        if checked: 
            self.plot_widget.setLogMode(x=True)
        else: 
            self.plot_widget.setLogMode(x=False)

    def setLogY(self, checkbox, checked):
        '''
        '''   
        if checked: 
            self.plot_widget.setLogMode(y=True)
        else: 
            self.plot_widget.setLogMode(y=False)

    def setGridX(self, checkbox, checked):
        '''
        '''
        if checked: 
            self.plot_widget.showGrid(x=True, alpha=0.5)
        else:
            self.plot_widget.showGrid(x=False)

    def setGridY(self, checkbox, checked):
        '''
        '''
        if checked: 
            self.plot_widget.showGrid(y=True, alpha=0.5)
        else:
            self.plot_widget.showGrid(y=False)


    def link(self, env_handler = None):
        '''
        Link the GUI to the environment that will be  read and
        taken care of.
        '''
        print('link in page result widget, env_handler = ', env_handler) #to del
        if not env_handler == None:
            self.env_handler = env_handler
        

