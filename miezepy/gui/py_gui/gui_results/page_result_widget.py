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
        self.error_bars_list = []
        self.error_bars_logX_list = []        
        self.error_bars_logY_list = []
        self.error_bars_logXY_list = []        
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

        self.process_check_grid_x.toggled.connect(lambda checked, checkbox=self.process_check_grid_x: self.setGridX(checkbox, checked))
        self.process_check_grid_y.toggled.connect(lambda checked, checkbox=self.process_check_grid_y: self.setGridY(checkbox, checked))  

        self.process_check_crosshairs.toggled.connect(lambda checked, checkbox=self.process_check_crosshairs: self.setCrosshairs(checkbox, checked))      

        self.process_check_log_x.toggled.connect(lambda checked, checkbox=self.process_check_log_x: self.setLogX(checkbox, checked))
        self.process_check_log_y.toggled.connect(lambda checked, checkbox=self.process_check_log_y: self.setLogY(checkbox, checked))
        self.plot_widget.getPlotItem().ctrl.logXCheck.stateChanged.connect(lambda state: self.process_check_log_x.setChecked(state == QtCore.Qt.Checked))
        self.plot_widget.getPlotItem().ctrl.logYCheck.stateChanged.connect(lambda state: self.process_check_log_y.setChecked(state == QtCore.Qt.Checked))

        self.add_errorbars.toggled.connect(lambda checked, checkbox=self.add_errorbars: self.setErrorBars(checkbox, checked))        
        self.process_check_log_x.toggled.connect(lambda checked, checkbox=self.add_errorbars: self.setErrorBars(checkbox, checked))
        self.process_check_log_y.toggled.connect(lambda checked, checkbox=self.add_errorbars: self.setErrorBars(checkbox, checked))

        self.func1.toggled.connect(lambda checked, checkbox=self.func1: self.func_checkbox_toggled(checkbox, checked))
        self.func2.toggled.connect(lambda checked, checkbox=self.func2: self.func_checkbox_toggled(checkbox, checked))
        self.func3.toggled.connect(lambda checked, checkbox=self.func3: self.func_checkbox_toggled(checkbox, checked))
        self.func4.toggled.connect(lambda checked, checkbox=self.func4: self.func_checkbox_toggled(checkbox, checked))

        self.plot_widget.setMouseTracking(True)
        self.plot_widget.scene().sigMouseMoved.connect(self.mouse_moved)

    def refresh_dataset(self):
        '''
        Refresh the dictionary of environments to 
        take into account. 
        '''
        self.clean_checkbox_list()

        names = [env.name for env in self.env_handler.env_array]
        #self.scroll_widget.setMinimumWidth(self.scroll_area.width() + 20)  

        for name in names:
            target  = self.env_handler.getEnv(name)
            result  = target.results.getLastResult(name = 'Contrast fit')
            if not result is None:
                self.add_env_label(name)
                
                for ds in result['Parameters'].keys():
                    new_key = name+'__'+ds
                    self.results_to_plot.setdefault(new_key,{})['x'] = result['Parameters'][ds]['x']
                    self.results_to_plot.setdefault(new_key,{})['y'] = result['Parameters'][ds]['y']
                    self.results_to_plot.setdefault(new_key,{})['y_error'] = result['Parameters'][ds]['y_error']
                    self.results_to_plot.setdefault(new_key,{})['to_plot'] = 'False'

                    #['Exp', 'StrExp', 'StrExp_Elast', 'StrExp_InElast']
                    if (result['Reference'] is None or ds not in result['Reference']) and (result['BG'] is None or ds not in result['BG']):
                        self.results_to_plot.setdefault(new_key,{})[self.func1.objectName()+'__x'] = result['Curve Axis']['Exp'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func1.objectName()+'__y'] = result['Curve']['Exp'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func2.objectName()+'__x'] = result['Curve Axis']['StrExp'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func2.objectName()+'__y'] = result['Curve']['StrExp'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func3.objectName()+'__x'] = result['Curve Axis']['StrExp_Elast'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func3.objectName()+'__y'] = result['Curve']['StrExp_Elast'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func4.objectName()+'__x'] = result['Curve Axis']['StrExp_InElast'][ds]
                        self.results_to_plot.setdefault(new_key,{})[self.func4.objectName()+'__y'] = result['Curve']['StrExp_InElast'][ds]

                        self.results_to_plot.setdefault(new_key,{})[self.func1.objectName()+'__to_plot'] = 'False'
                        self.results_to_plot.setdefault(new_key,{})[self.func2.objectName()+'__to_plot'] = 'False'
                        self.results_to_plot.setdefault(new_key,{})[self.func3.objectName()+'__to_plot'] = 'False'  
                        self.results_to_plot.setdefault(new_key,{})[self.func4.objectName()+'__to_plot'] = 'False'                 

                    self.add_env_checkbox(name, ds)

        self.verticalLayout_411.addStretch(1)

        self.func1.setChecked(False)
        self.func2.setChecked(False)
        self.func3.setChecked(False)
        self.func4.setChecked(False)


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
        self.verticalLayout_411.addWidget(env_label)
        env_label.setText(QtCore.QCoreApplication.translate("result_widget", name))
        env_label.adjustSize() 

        self.adjust_scroll_size(env_label.width(),self.scroll_widget.width())

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
        env_checkbox.setObjectName(envname+"__"+cboxname) 
        env_checkbox.setStyleSheet("QCheckBox { padding-left: 40px; }")
        self.verticalLayout_411.addWidget(env_checkbox)
        env_checkbox.setText(QtCore.QCoreApplication.translate("result_widget", cboxname))
        env_checkbox.adjustSize()

        self.adjust_scroll_size(env_checkbox.width(),self.scroll_widget.width())

        self.env_checkbox_list.append(env_checkbox)

        env_checkbox.toggled.connect(lambda checked, checkbox=env_checkbox: self.env_checkbox_toggled(checkbox, checked))

    def adjust_scroll_size(self,item_width, scroll_width):
        if item_width+150 >= scroll_width:
            self.scroll_widget.setMinimumWidth(item_width+150)
            self.scroll_widget.adjustSize()

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

        if self.verticalLayout_411 is not None:
            while self.verticalLayout_411.count():  
                item = self.verticalLayout_411.takeAt(0)  
                widget = item.widget()
                
                if isinstance(widget, QtWidgets.QCheckBox): 
                    widget.toggled.disconnect()

                if widget is not None:
                    widget.deleteLater()  
                else:
                    self.verticalLayout_411.removeItem(item)  

        self.env_checkbox_list.clear()


    def plot_selected(self):
        self.plot_widget.clear()
        self.plot_widget.getPlotItem().enableAutoRange('xy', True)
        self.error_bars_list.clear()
        self.error_bars_logX_list.clear()
        self.error_bars_logY_list.clear()
        self.error_bars_logXY_list.clear()
        
        self.legend = self.plot_widget.getPlotItem().addLegend(offset=(-10, 10), labelTextColor='black', pen=pg.mkPen(color='black'))

        for i, key in enumerate(self.results_to_plot.keys()):
            if self.results_to_plot[key]['to_plot']==True :
                x = self.results_to_plot[key]['x']
                y = self.results_to_plot[key]['y']
                y_errors = self.results_to_plot[key]['y_error']
                color = plt.cm.hsv(1 - ((i/6) - i//6) )
                rgb = tuple(int(c * 255) for c in color[:3])  
                self.plot_widget.plot(x, y, symbol='o', symbolSize=8, symbolBrush=rgb, pen=None, name=key.split('__')[1]) 

                # calculate errorbars
                error_bars = pg.ErrorBarItem(x=x, y=y,  top=y_errors, bottom=y_errors, beam=0.02, pen=rgb)
                self.error_bars_list.append(error_bars)

                error_bars = pg.ErrorBarItem(x=np.log10(x), y=y,  top=y_errors, bottom=y_errors, beam=0.05, pen=rgb)
                self.error_bars_logX_list.append(error_bars)

                y_err_t = np.log10(y + y_errors) - np.log10(y)
                y_err_b = np.log10(y) - np.log10(y - y_errors)
                error_bars = pg.ErrorBarItem(x=x, y=np.log10(y),  top=y_err_t, bottom=y_err_b, beam=0.02, pen=rgb)
                self.error_bars_logY_list.append(error_bars)

                error_bars = pg.ErrorBarItem(x=np.log10(x), y=np.log10(y),  top=y_err_t, bottom=y_err_b, beam=0.05, pen=rgb)
                self.error_bars_logXY_list.append(error_bars)                    


                # plot fit functions 
                if self.func1.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func1.objectName()+'__to_plot']==True :
                        try:
                            x_func1 = self.results_to_plot[key][self.func1.objectName()+'__x']
                            y_func1 = self.results_to_plot[key][self.func1.objectName()+'__y']
                            func1_leg = self.plot_widget.plot(x_func1, y_func1, pen=pg.mkPen(color=rgb, width=2))
                            if i==0:
                                self.legend.addItem(func1_leg, 'Exp.')
                        except:
                           pass

                if self.func2.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func2.objectName()+'__to_plot']==True :
                        try:
                            x_func2 = self.results_to_plot[key][self.func2.objectName()+'__x']
                            y_func2 = self.results_to_plot[key][self.func2.objectName()+'__y']
                            func2_leg = self.plot_widget.plot(x_func2, y_func2, pen=pg.mkPen(color=rgb, width=2, style=QtCore.Qt.DashLine))     
                            if i==0:
                                self.legend.addItem(func2_leg, 'Stretched exp.')
                        except:
                            pass

                if self.func3.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func3.objectName()+'__to_plot']==True :
                        try:
                            x_func3 = self.results_to_plot[key][self.func3.objectName()+'__x']
                            y_func3 = self.results_to_plot[key][self.func3.objectName()+'__y']
                            func3_leg = self.plot_widget.plot(x_func3, y_func3, pen=pg.mkPen(color=rgb, width=2, style=QtCore.Qt.DotLine))
                            if i==0:
                                self.legend.addItem(func3_leg, 'Str. exp. +El. BGRD')
                        except:
                            pass

                if self.func4.objectName()+'__to_plot' in self.results_to_plot[key].keys():
                    if self.results_to_plot[key][self.func4.objectName()+'__to_plot']==True :
                        try:
                            x_func4 = self.results_to_plot[key][self.func4.objectName()+'__x']
                            y_func4 = self.results_to_plot[key][self.func4.objectName()+'__y']
                            func4_leg = self.plot_widget.plot(x_func4, y_func4, pen=pg.mkPen(color=rgb, width=2, style=QtCore.Qt.DashDotLine))
                            if i==0:
                                self.legend.addItem(func4_leg, 'Str. exp. +INS')
                        except:
                            pass

        self.setErrorBars(self.add_errorbars, self.add_errorbars.isChecked())
        self.setCrosshairs(self.process_check_crosshairs, self.process_check_crosshairs.isChecked())
        


    def mouse_moved(self, evt):
        '''
        '''
        mouse_point = self.plot_widget.getPlotItem().vb.mapSceneToView(evt)
        x = mouse_point.x()
        y = mouse_point.y()

        self.v_line.setPos(x)
        self.h_line.setPos(y)

        if self.plot_widget.getPlotItem().ctrl.logXCheck.isChecked():
            x = 10 ** x 

        self.xy_label.setText(f"x = {x:.4e},    y = {y:.2f}")

    def setErrorBars(self, checkbox, checked):
        '''
        '''
        self.removeErrorBars()
        if self.add_errorbars.isChecked(): 
            if not self.process_check_log_x.isChecked() and not self.process_check_log_y.isChecked():
                try:
                    for err_b in self.error_bars_list:
                        self.plot_widget.addItem(err_b)
                except:
                    pass
            elif self.process_check_log_x.isChecked() and not self.process_check_log_y.isChecked():
                try:
                    for err_b in self.error_bars_logX_list:
                        self.plot_widget.addItem(err_b)
                except:
                    pass
            elif not self.process_check_log_x.isChecked() and self.process_check_log_y.isChecked():
                try:
                    for err_b in self.error_bars_logY_list:
                        self.plot_widget.addItem(err_b)
                except:
                    pass
            elif self.process_check_log_x.isChecked() and self.process_check_log_y.isChecked():
                try:
                    for err_b in self.error_bars_logXY_list:
                        self.plot_widget.addItem(err_b)
                except:
                    pass        

    def removeErrorBars(self):
        ''''''
        try:
            for err_b in self.error_bars_list:
                self.plot_widget.removeItem(err_b)
            for err_b in self.error_bars_logX_list:
                self.plot_widget.removeItem(err_b)
            for err_b in self.error_bars_logY_list:
                self.plot_widget.removeItem(err_b)
            for err_b in self.error_bars_logXY_list:
                self.plot_widget.removeItem(err_b)
        except:
            pass


    def setCrosshairs(self, checkbox, checked):
        ''''''
        if checked: 
            self.removeCrosshairs()
            self.plot_widget.addItem(self.v_line, ignoreBounds=True)
            self.plot_widget.addItem(self.h_line, ignoreBounds=True)
        else: 
            self.removeCrosshairs()
    
    def removeCrosshairs(self):
        ''''''
        self.plot_widget.removeItem(self.v_line)
        self.plot_widget.removeItem(self.h_line)

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
        if not env_handler == None:
            self.env_handler = env_handler
        

