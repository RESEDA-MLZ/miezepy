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
from PyQt5 import QtWidgets, QtCore
import glob
import os
import csv
import json
from io import StringIO
import numpy as np
import subprocess
import sys
from send2trash import send2trash

from .checkbox_delegate import CheckBoxDelegate
from .combobox_delegate import ComboBoxDelegate
from .result_list_model import ResultListModel
from .result_file_model import ResultFileModel
from .results_data_table import DataTableModel
from .comparison_setup_model import ComparisonSetupModel
from ..gui_common.code_editor import CodeEditor, PythonHighlighter

#private plotting library
from simpleplot.canvas.multi_canvas import MultiCanvasItem
from ....core.mask_modules.generator import MaskGenerator

class ResultsTabHandler():

    def __init__(self, parent):
        self.parent = parent
        self._mask_generator = MaskGenerator()
        self._result_dict = {}
        self._current_files = {}
        self._selected_file = None
        self._data_headers = {}
        self._tab_rules = {
            'py': ['text'],
            'txt': ['text'],
            'json': ['mask', 'text'],
            'csv': ['grid', 'plot', 'text']}
        self._actions = {
            'txt': self._handleNewText,
            'json': self._handleNewMask,
            'csv': self._handleNewData,
            'py': self._handleNewScript,
        }
        
        self.color_list = [
            "#1f77b4", "#ff7f0e", "#2ca02c", 
            "#d62728", "#9467bd", "#8c564b", 
            "#e377c2", "#7f7f7f", "#bcbd22", 
            "#17becf"]
        
        self._init_ui()
        
        self._setModels()
        self._connectModels()
        self.updateResultList()
        
    def _init_ui(self):
        '''
        locally create the editors to allow custom ones. These parts
        have been engineered through the pyqt framework and then
        exported through the pyuic5 routine. Note that here we are
        simply selecting parts of it and changing the intput text editor
        '''
        self.checkbox_delegate = CheckBoxDelegate(None)
        self.combobox_delegate = ComboBoxDelegate()

        self.parent._result_tab = QtWidgets.QWidget()
        self.parent._result_tab.setStyleSheet("")
        self.parent._result_tab.setObjectName("result_tab")
        self.parent._result_tab.setStyleSheet(
            "#result_tab{background-color: rgb(179, 179, 179);}\n"
            "QGroupBox::title{color:rgb(0, 0, 0)}\n"
            "QLabel{color:rgb(0, 0, 0)}\n"
            "QTabWidget{background-color: rgb(131, 131, 131);}\n"
            "#process_tab{background-color: rgb(131, 131, 131);}\n"
            "#panel_tab{background-color: rgb(131, 131, 131);}\n"
            "#script_tab{background-color: rgb(131, 131, 131);}\n"
            "#script_tab_import{background-color: rgb(131, 131, 131);}\n"
            "#script_tab_set_fit{background-color: rgb(131, 131, 131);}\n"
            "#script_tab_phase{background-color: rgb(131, 131, 131);}\n"
            "#script_tab_reduction{background-color: rgb(131, 131, 131);}\n"
            "#tab{background-color: rgb(131, 131, 131);}")
        self.parent._result_tab_layout = QtWidgets.QHBoxLayout(self.parent._result_tab)
        self.parent._result_main_spliter = QtWidgets.QSplitter(self.parent._result_tab)
        self.parent._result_tab_layout.addWidget(self.parent._result_main_spliter)
        self.parent._results_organisation = QtWidgets.QWidget()
        self.parent._results_organisation_layout = QtWidgets.QVBoxLayout(self.parent._results_organisation)
        
        ################## The result intance section
        self.parent._results_instances_container = QtWidgets.QWidget(parent=self.parent._result_tab)
        self.parent._results_instances_container_layout = QtWidgets.QHBoxLayout(self.parent._results_instances_container)

        self.parent._results_instances_view = QtWidgets.QTableView(self.parent._results_instances_container)
        self.parent._results_instances_view.horizontalHeader().setStretchLastSection(True)
        self.parent._results_instances_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.parent._results_instances_view.setItemDelegateForColumn(0, self.checkbox_delegate)

        self.parent._results_instances_hide = QtWidgets.QToolButton(self.parent._results_instances_container)
        pixmapi = getattr(QtWidgets.QStyle, 'SP_ToolBarHorizontalExtensionButton')
        icon = self.parent._results_instances_hide.style().standardIcon(pixmapi)
        self.parent._results_instances_hide.setIcon(icon)

        self.parent._results_instances_locate = QtWidgets.QToolButton(self.parent._results_instances_container)
        pixmapi = getattr(QtWidgets.QStyle, 'SP_DirLinkIcon')
        icon = self.parent._results_instances_locate.style().standardIcon(pixmapi)
        self.parent._results_instances_locate.setIcon(icon)
        self.parent._results_instances_locate.clicked.connect(self._openResultFolder)

        self.parent._results_instances_delete = QtWidgets.QToolButton(self.parent._results_instances_container)
        pixmapi = getattr(QtWidgets.QStyle, 'SP_TrashIcon')
        icon = self.parent._results_instances_delete.style().standardIcon(pixmapi)
        self.parent._results_instances_delete.setIcon(icon)
        self.parent._results_instances_locate.clicked.connect(self._trashResult)

        self.parent._results_instances_container_side_layout = QtWidgets.QVBoxLayout()
        self.parent._results_instances_container_side_layout.addWidget(self.parent._results_instances_hide)
        self.parent._results_instances_container_side_layout.addWidget(self.parent._results_instances_locate)
        self.parent._results_instances_container_side_layout.addWidget(self.parent._results_instances_delete)
        self.parent._results_instances_container_side_layout.addStretch()

        self.parent._results_instances_container_layout.addWidget(self.parent._results_instances_view)
        self.parent._results_instances_container_layout.addLayout(self.parent._results_instances_container_side_layout)

        ################## The result data file section
        self.parent._results_files_view = QtWidgets.QListView(parent=self.parent._result_tab)
        self.parent._results_specific_tabs = QtWidgets.QTabWidget(parent=self.parent._result_tab)
        
        self.parent._results_organisation_layout.addWidget(self.parent._results_instances_container)
        self.parent._results_organisation_layout.addWidget(self.parent._results_files_view)
        self.parent._result_main_spliter.addWidget(self.parent._results_organisation)
        self.parent._result_main_spliter.addWidget(self.parent._results_specific_tabs)
        
        self.parent._results_tab_selection = QtWidgets.QTabWidget()
        self.parent._results_tab_comparison = QtWidgets.QTabWidget()
        self.parent._results_specific_tabs.addTab(self.parent._results_tab_selection, "Selection")
        self.parent._results_specific_tabs.addTab(self.parent._results_tab_comparison, "Comparison")
        
        self.parent._selection_tab_data_grid = QtWidgets.QWidget()
        self.parent._selection_tab_data_widget = QtWidgets.QWidget()
        self.parent._selection_tab_mask = QtWidgets.QWidget()
        self.parent._selection_tab_text = CodeEditor(self.parent._results_tab_selection)
        self.parent._results_tab_selection.addTab(self.parent._selection_tab_data_grid, "Data Table")
        self.parent._results_tab_selection.addTab(self.parent._selection_tab_data_widget, "Data Plot")
        self.parent._results_tab_selection.addTab(self.parent._selection_tab_mask, "Mask View")
        self.parent._results_tab_selection.addTab(self.parent._selection_tab_text, "File viewer")
        self._tab_orders = ['grid', 'plot', 'mask', 'text']
        
        self.parent._comparison_tab_setup = QtWidgets.QWidget()
        self.parent._comparison_tab_data_grid = QtWidgets.QWidget()
        self.parent._comparison_tab_data_plot = QtWidgets.QWidget()
        # self.parent._comparison_tab_mask = QtWidgets.QWidget()
        self.parent._results_tab_comparison.addTab(self.parent._comparison_tab_setup, "Setup")
        self.parent._results_tab_comparison.addTab(self.parent._comparison_tab_data_grid, "Data Table")
        self.parent._results_tab_comparison.addTab(self.parent._comparison_tab_data_plot, "Data Plot")
        # self.parent._results_tab_comparison.addTab(self.parent._comparison_tab_mask, "Mask View")
        
        self._setUpComparisonSetup()
        self._setUpDataComparisonTable()
        self._setUpPlots()
        self._setUpDataSelectionTable()
        
        self.parent.tabWidget.addTab(self.parent._result_tab, "Results")
        
    def _openResultFolder(self):
        indexes = self.parent._results_instances_view.selectionModel().selectedIndexes()
        if len(indexes) == 0:
            return

        selected_row = indexes[0].row()
        path = list(self._result_dict.keys())[selected_row]

        if sys.platform == 'darwin':
            def openFolder(path):
                subprocess.check_call(['open', '--', path])
        elif sys.platform == 'linux2':
            def openFolder(path):
                subprocess.check_call(['xdg-open', '--', path])
        elif sys.platform == 'win32':
            def openFolder(path):
                subprocess.check_call(['explorer', path])
        else:
            return

        openFolder(path)

    def _trashResult(self):
        indexes = self.parent._results_instances_view.selectionModel().selectedIndexes()
        if len(indexes) == 0:
            return

        move_to_trash = [self._result_dict.keys()[index.row()] for index in indexes]
        for path in move_to_trash:
            send2trash(path)
        
    def _setUpComparisonSetup(self):
        self._comparison_result_data_model = DataTableModel([], [], [])
        self.parent._comparison_tab_setup_table = QtWidgets.QTableView(self.parent._comparison_tab_setup)
        self.parent._comparison_tab_setup_table.setItemDelegateForColumn(0, self.checkbox_delegate)
        self.parent._comparison_tab_setup_table.setItemDelegateForColumn(1, self.combobox_delegate)
                
        self.parent._comparison_tab_contrast_radio = QtWidgets.QRadioButton("Contrast", self.parent._selection_tab_data_grid)
        self.parent._comparison_tab_raw_radio = QtWidgets.QRadioButton("Raw values", self.parent._selection_tab_data_grid)
        self.parent._comparison_tab_group = QtWidgets.QButtonGroup()
        self.parent._comparison_tab_group.addButton(self.parent._comparison_tab_contrast_radio)
        self.parent._comparison_tab_group.addButton(self.parent._comparison_tab_raw_radio)
        
        v_layout = QtWidgets.QVBoxLayout(self.parent._comparison_tab_setup)
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.parent._comparison_tab_contrast_radio)
        h_layout.addWidget(self.parent._comparison_tab_raw_radio)
        h_layout.addStretch()
        
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.parent._comparison_tab_setup_table)
        
        self.parent._comparison_tab_contrast_radio.setChecked(True)
        self.parent._comparison_tab_group.buttonClicked.connect(self._setComparisonData)
        
    def _setUpDataComparisonTable(self):
        self._comparison_result_data_model = DataTableModel([], [], [])
        self.parent._comparison_result_data_view = QtWidgets.QTableView()
        self.parent._comparison_result_data_view.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        self.parent._comparison_result_data_vert = QtWidgets.QRadioButton("Vertical", self.parent._comparison_tab_data_grid)
        self.parent._comparison_result_data_hori = QtWidgets.QRadioButton("Horizontal", self.parent._comparison_tab_data_grid)
        self.parent._comparison_result_data_dire = QtWidgets.QButtonGroup()
        self.parent._comparison_result_data_dire.addButton(self.parent._comparison_result_data_vert)
        self.parent._comparison_result_data_dire.addButton(self.parent._comparison_result_data_hori)
        
        self.parent._comparison_result_data_prec = QtWidgets.QSpinBox()
        self.parent._comparison_result_data_prec.setMinimum(1)
        self.parent._comparison_result_data_prec.setMaximum(10)
        self.parent._comparison_result_data_prec.setValue(10)
        
        self.parent._comparison_result_header_prec = QtWidgets.QSpinBox()
        self.parent._comparison_result_header_prec.setMinimum(1)
        self.parent._comparison_result_header_prec.setMaximum(10)
        self.parent._comparison_result_header_prec.setValue(10)
        self.parent._comparison_result_header_prec.setEnabled(False)
        
        self.parent._comparison_result_data_cond = QtWidgets.QCheckBox('Condense tau')
        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.parent._comparison_result_data_vert)
        h_layout.addWidget(self.parent._comparison_result_data_hori)
        h_layout.addWidget(QtWidgets.QLabel('Decimal precision:'))
        h_layout.addWidget(self.parent._comparison_result_data_prec)
        h_layout.addWidget(self.parent._comparison_result_data_cond)
        h_layout.addWidget(QtWidgets.QLabel('Header precision:'))
        h_layout.addWidget(self.parent._comparison_result_header_prec)
        h_layout.addStretch()

        v_layout = QtWidgets.QVBoxLayout(self.parent._comparison_tab_data_grid)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.parent._comparison_result_data_view)
        
        self.parent._comparison_result_data_vert.setChecked(True)
        self.parent._comparison_result_data_view.setModel(self._comparison_result_data_model)
        self.parent._comparison_result_data_prec.valueChanged.connect(self._comparison_result_data_model.setPrecision)
        self.parent._comparison_result_data_dire.buttonClicked.connect(self._directionChangedComparison)

    def _setUpPlots(self):
        self.parent._selection_tab_data_layout = QtWidgets.QVBoxLayout(self.parent._selection_tab_data_widget)
        
        self.parent._selection_tab_data_logx = QtWidgets.QCheckBox('Log x', self.parent._selection_tab_data_widget)
        self.parent._selection_tab_data_logy = QtWidgets.QCheckBox('Log y', self.parent._selection_tab_data_widget)
        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.parent._selection_tab_data_logx)
        h_layout.addWidget(self.parent._selection_tab_data_logy)
        h_layout.addStretch()
        
        self.parent._selection_tab_data_plot = QtWidgets.QWidget()
        self._data_plot_canvas = MultiCanvasItem(
            self.parent._selection_tab_data_plot,
            grid        = [[True]],
            x_ratios    = [1],
            y_ratios    = [1],
            background  = "w",
            highlightthickness = 0)
        self.ax = self._data_plot_canvas.getSubplot(0,0)
        self.ax.pointer.pointer_handler['Sticky'] = 3
        self._data_plot_canvas.canvas_nodes[0][0][0].grid_layout.setMargin(0)
        
        self.parent._selection_tab_data_layout.addLayout(h_layout)
        self.parent._selection_tab_data_layout.addWidget(self.parent._selection_tab_data_plot)
        
        self.parent._selection_tab_data_logx.clicked.connect(self._manageLogStandart)
        self.parent._selection_tab_data_logy.clicked.connect(self._manageLogStandart)
        
        # Set up the data plot canvas
        self._mask_canvas = MultiCanvasItem(
            self.parent._selection_tab_mask,
            grid        = [[True]],
            x_ratios    = [1],
            y_ratios    = [1],
            background  = "w",
            highlightthickness = 0)
        self.bx = self._mask_canvas.getSubplot(0,0)
        self.bx.pointer.pointer_handler['Sticky'] = 2
        self._mask_canvas.canvas_nodes[0][0][0].grid_layout.setMargin(0)   
        self._mask_plot_selection = self.bx.addPlot('Surface', Name='Mask area')
        self.bx.draw()
        
        # data comparinson
        self.parent._comparison_tab_plot_layout = QtWidgets.QVBoxLayout(self.parent._comparison_tab_data_plot)
        
        self.parent._comparison_tab_plot_logx = QtWidgets.QCheckBox('Log x', self.parent._comparison_tab_data_plot)
        self.parent._comparison_tab_plot_logy = QtWidgets.QCheckBox('Log y', self.parent._comparison_tab_data_plot)
        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.parent._comparison_tab_plot_logx)
        h_layout.addWidget(self.parent._comparison_tab_plot_logy)
        h_layout.addStretch()
        
        self.parent._comparison_tab_plot_plot = QtWidgets.QWidget()
        self._comparison_data_canvas = MultiCanvasItem(
            self.parent._comparison_tab_plot_plot,
            grid        = [[True]],
            x_ratios    = [1],
            y_ratios    = [1],
            background  = "w",
            highlightthickness = 0)
        self.cx = self._comparison_data_canvas.getSubplot(0,0)
        self.cx.pointer.pointer_handler['Sticky'] = 3
        self._comparison_data_canvas.canvas_nodes[0][0][0].grid_layout.setMargin(0)
        
        self.parent._comparison_tab_plot_layout.addLayout(h_layout)
        self.parent._comparison_tab_plot_layout.addWidget(self.parent._comparison_tab_plot_plot)
        
        self.parent._comparison_tab_plot_logx.clicked.connect(self._manageLogCompare)
        self.parent._comparison_tab_plot_logy.clicked.connect(self._manageLogCompare)
        
    def _setUpDataSelectionTable(self):
        self._selection_result_data_model = DataTableModel([], [], [])
        self.parent._selection_result_data_view = QtWidgets.QTableView()
        self.parent._selection_result_data_view.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        self.parent._selection_result_data_vert = QtWidgets.QRadioButton("Vertical", self.parent._selection_tab_data_grid)
        self.parent._selection_result_data_hori = QtWidgets.QRadioButton("Horizontal", self.parent._selection_tab_data_grid)
        self.parent._selection_result_data_dire = QtWidgets.QButtonGroup()
        self.parent._selection_result_data_dire.addButton(self.parent._selection_result_data_vert)
        self.parent._selection_result_data_dire.addButton(self.parent._selection_result_data_hori)
        
        self.parent._selection_result_data_prec = QtWidgets.QSpinBox()
        self.parent._selection_result_data_prec.setMinimum(1)
        self.parent._selection_result_data_prec.setMaximum(10)
        self.parent._selection_result_data_prec.setValue(10)
        
        self.parent._selection_result_header_prec = QtWidgets.QSpinBox()
        self.parent._selection_result_header_prec.setMinimum(1)
        self.parent._selection_result_header_prec.setMaximum(10)
        self.parent._selection_result_header_prec.setValue(10)
        self.parent._selection_result_header_prec.setEnabled(False)
        
        self.parent._selection_result_data_cond = QtWidgets.QCheckBox('Condense tau')
        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.parent._selection_result_data_vert)
        h_layout.addWidget(self.parent._selection_result_data_hori)
        h_layout.addWidget(QtWidgets.QLabel('Decimal precision:'))
        h_layout.addWidget(self.parent._selection_result_data_prec)
        h_layout.addWidget(self.parent._selection_result_data_cond)
        h_layout.addWidget(QtWidgets.QLabel('Header precision:'))
        h_layout.addWidget(self.parent._selection_result_header_prec)
        h_layout.addStretch()

        v_layout = QtWidgets.QVBoxLayout(self.parent._selection_tab_data_grid)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.parent._selection_result_data_view)
        
        self.parent._selection_result_data_vert.setChecked(True)
        self.parent._selection_result_data_view.setModel(self._selection_result_data_model)
        self.parent._selection_result_data_prec.valueChanged.connect(self._selection_result_data_model.setPrecision)
        self.parent._selection_result_data_dire.buttonClicked.connect(self._directionChanged)
        
    def _manageLogStandart(self, item):
        '''
        '''
        self.ax.axes.general_handler['Log'] = [
            self.parent._selection_tab_data_logx.isChecked(),
            self.parent._selection_tab_data_logy.isChecked()]
        
    def _manageLogCompare(self, item):
        '''
        '''
        self.cx.axes.general_handler['Log'] = [
            self.parent._comparison_tab_plot_logx.isChecked(),
            self.parent._comparison_tab_plot_logy.isChecked()]

    def _directionChanged(self, item):
        '''
        '''
        self._selection_result_data_model.setOrientation(item.text())

    def _directionChangedComparison(self, item):
        '''
        '''
        self._comparison_result_data_model.setOrientation(item.text())

    def _condenseChange(self, val):
        '''
        '''
        self._selection_result_data_model.condenseTau(val)
        self.parent._selection_result_header_prec.setEnabled(val > 0)
        self._selection_result_data_model.setPrecisionHeader(
            self.parent._selection_result_header_prec.value())
        
    def _condenseChangeComparison(self, val):
        '''
        '''
        self._comparison_result_data_model.condenseTau(val)
        self.parent._comparison_result_header_prec.setEnabled(val > 0)
        self._comparison_result_data_model.setPrecisionHeader(
            self.parent._comparison_result_header_prec.value())

    def _setModels(self):
        '''
        Create the different interaction models and then set them
        '''
        self._result_list_model = ResultListModel(
            self.parent._results_instances_view,
            {},
            ['compare', 'key', 'name', 'date'], [])
        self.parent._results_instances_view.setModel(self._result_list_model)
        
        self.parent._result_file_model = ResultFileModel(
            self.parent._results_files_view,
            [])
        self.parent._results_files_view.setModel(self.parent._result_file_model)
        
        self._comparison_setup_model = ComparisonSetupModel(
            self.parent._comparison_tab_setup_table,
            {},
            self._result_list_model)
        self.parent._comparison_tab_setup_table.setModel(self._comparison_setup_model)
        
    def _connectModels(self):
        '''
        Connect the data changed signals of the dfferent models !
        '''
        self.parent._results_instances_view.selectionModel().selectionChanged.connect(self._updatePresentFiles)
        self._result_list_model.edited_key.connect(self.updateMetaKeyFromTable)
        self.parent._results_files_view.selectionModel().selectionChanged.connect(self._updateSelectedFile)
        self._comparison_setup_model.dataChanged.connect(self._setComparisonData)
        self._result_list_model.dataChanged.connect(self._setComparisonData)
    
    def updateResultList(self):
        '''
        Set up the result comparison routines
        '''
        if self.parent.env is None:
            self._result_dict = {}
            return
            
        path = self.parent.env.io.path
        if not path or not os.path.exists(os.path.join(path, "results")):
            self._result_dict = {}
            return
            
        keys = [item[1] for _, item in self._result_dict.items()]
        directories = glob.glob(os.path.join(path, "results", "*/"))
            
        rows_to_insert = {}
        for key in directories:
            if key not in self._result_list_model.my_dict:
                meta_path = os.path.join(key, "meta.txt")
                if not os.path.exists(meta_path):
                    self.parent.env.io.dumpResultMeta(os.path.dirname(key))
                
                with open(meta_path, 'r') as meta_file:
                    meta_lines = meta_file.read().splitlines()
                
                if '_'.join(meta_lines[1].split('_')[2:]) in ['_'.join(item.split('_')[2:]) for item in keys]:
                    meta_lines[1] = self._updateMetaKey(meta_path, meta_lines[1], keys, meta_lines)
                    
                rows_to_insert[key] = [
                    False,
                    meta_lines[1],
                    meta_lines[0],
                    meta_lines[2],
                    glob.glob(os.path.join(key, "*/")),
                    self._getDataHeaders(key)]
                
                keys.append(meta_lines[1])
                
        self._result_list_model.insertRows(rows_to_insert)
        self._result_dict = dict(self._result_list_model.my_dict)
        self._processAvailableHeaders()
        
    def _processAvailableHeaders(self):
        '''
        grab all the headers from the item disct and create a set
        '''
        keys = set()
        for val in self._result_list_model.my_dict.values():
            keys.update(val[-1].keys())
            
        self._data_headers = {key: [] for key in keys}
        
        for key in self._result_list_model.my_dict.keys():
            for header_key in keys:
                if header_key in self._result_list_model.my_dict[key][-1]:
                    self._data_headers[header_key].append(key)
        
        self._comparison_setup_model.insertRows(self._data_headers)
        
    def _getDataHeaders(self, path: str):
        '''
        Get the header line of the data files 
        '''
        contast_path = os.path.join(path, 'contrast_result.csv')
        raw_path = os.path.join(path, 'raw_result.csv')
        if not os.path.isfile(contast_path) or not os.path.isfile(raw_path):
            return {}
        
        with open(contast_path,'r') as f:
            data_str = f.read()
            csv_io = StringIO(data_str)
            contrast_read = list(csv.reader(csv_io, lineterminator='\n'))
            contrast_header = contrast_read[0]
            contrast_data = np.array(contrast_read[1:]).transpose().astype(float)
            
        with open(raw_path,'r') as f:
            data_str = f.read()
            csv_io = StringIO(data_str)
            raw_read = list(csv.reader(csv_io, lineterminator='\n'))
            raw_header = raw_read[0]
            raw_data = np.array(raw_read[1:]).transpose().astype(float)
            
        if raw_header != contrast_header:
            raise Exception('Header data of files not equal')
            
        header_data = {}
        for i in range(1,len(contrast_header),3):
            header_data[contrast_header[i]] = {
                'contrast': [contrast_data[i-1], contrast_data[i], contrast_data[i+1]],
                'raw': [raw_data[i-1], raw_data[i], raw_data[i+1]]
            }
        
        return header_data
    
    def _setComparisonData(self, top_left=None, bot_right=None, roles=None):
        '''
        This method will grab the model datas and then build the data tree
        necessary to view the comparison
        '''
        header_data = self._comparison_setup_model.header_data
        model_data = self._comparison_setup_model.model_data
        
        data_groups = {}
        selected = 'contrast' if self.parent._comparison_tab_contrast_radio.isChecked() else 'raw'
        for key, item in model_data.items():
            if item[0]:
                data_groups[key] = [
                    [key + ' ['+self._result_list_model.getKeyRepresentationAtKey(sub_key)+']' 
                     for sub_key in header_data[key] 
                     if self._result_list_model.my_dict[sub_key][0]],
                    [self._result_list_model.my_dict[sub_key][-1][key][selected]
                     for sub_key in header_data[key] 
                     if self._result_list_model.my_dict[sub_key][0]],
                    self._comparison_setup_model.available_symbols[item[1]],
                    item[1],
                    [self.color_list[i%len(self.color_list)]
                     for i, sub_key in enumerate(header_data[key]) 
                     if self._result_list_model.my_dict[sub_key][0]]
                ]
                
        self._setComparisonPlot(data_groups)
        self._setComparisonTable(data_groups)
        
    def _setComparisonPlot(self, data_groups):
        '''
        '''
        self.cx.clear()
        for item in data_groups.values():
            for i in range(len(item[0])):
                plot = self.cx.addPlot(
                    'Scatter',
                    Name=item[0][i],
                    x=item[1][i][0],
                    y=item[1][i][1],
                    error={
                        'height':None,
                        'width' : None,
                        'bottom':item[1][i][2],
                        'top'   :item[1][i][2]},
                    Style=['-', item[2],'r',str(item[3])],
                    Color=item[4][i])
            
        self.cx.draw()
        
    def _setComparisonTable(self, data_groups):
        '''
        '''
        data = []
        headers = []
        for item in data_groups.values(): 
            for i in range(len(item[0])):
                data.append(item[1][i][0].tolist())
                data.append(item[1][i][1].tolist())
                data.append(item[1][i][2].tolist())
                
                headers.append(item[0][i])
                headers.append(item[0][i])
                headers.append(item[0][i])

        self._setUpComparisonModel(headers, np.array(data).transpose().tolist())

    def _updateMetaKey(self, path, key, keys, lines):
        lead = '_'.join(key.split('_')[:3])
        key = '_'.join(key.split('_')[3:])
        formated_keys = ['_'.join(item.split('_')[3:]) for item in keys]
        if key in formated_keys:
            if key.split('_')[-1].isnumeric():
                num = int(key.split('_')[-1])
                key = '_'.join(key.split('_')[:-1])
            else:
                num = 0
            
            while '_'.join([key, str(num)]) in formated_keys:
                num += 1
                
            lines[1] = '_'.join([lead, key, str(num)])
            
        else:
            lines[1] = '_'.join([lead, key])
            
        with open(path, 'w') as meta_file:
            meta_file.write('\n'.join(lines) + '\n')
        
        return lines[1]
    
    def updateMetaKeyFromTable(self, full_key: str, new_key: str, keys: list):
        '''
        Update the meta data from the table change
        '''
        meta_path = os.path.join(full_key, "meta.txt")
        if not os.path.exists(meta_path):
            self.parent.env.io.dumpResultMeta(os.path.dirname(full_key))
        
        with open(meta_path, 'r') as meta_file:
            meta_lines = meta_file.read().splitlines()
        
        key = self._updateMetaKey(meta_path, new_key, keys, meta_lines)
        
        # -------------
        new_full_key =  os.path.join(*(list(os.path.split(full_key)[:-1])+[key]))
        os.rename(full_key, new_full_key)
        temp = {}
        for temp_key, temp_val in self._result_list_model.my_dic.items():
            if temp_key == full_key:
                temp[new_full_key] = temp_val
                temp[new_full_key][1] = key
            else:
                temp[temp_key] = temp_val
        self._result_list_model.my_dict = temp
        # -------------
        
        self._result_dict = dict(self._result_list_model.my_dict)
        self._result_list_model.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
            
    def _updatePresentFiles(self, selection_start, selection_end):
        '''
        '''
        if len(selection_start.indexes()) == 0:
            return
        selected_row = selection_start.indexes()[0].row()
        files = glob.glob(os.path.join(list(self._result_dict.keys())[selected_row], "*"))
        self.parent._result_file_model.clear()
        self.parent._result_file_model.insertRows(files)
        
        file_names = [os.path.basename(file) for file in files]
        if self._selected_file and os.path.basename(self._selected_file) in file_names:
            self._selected_file = files[file_names.index(os.path.basename(self._selected_file))]
            self._setSelectedFile()
            
    def _updateSelectedFile(self, selection_start, selection_end):
        '''
        '''
        if len(selection_start.indexes()) == 0:
            return
        selected_row = selection_start.indexes()[0].row()
        self._selected_file = self.parent._result_file_model.my_files[selected_row]
        self._setSelectedFile()
        
    def _setSelectedFile(self):
        extension = self._selected_file.split('.')[-1]
        for i in range(len(self._tab_orders)):
            if self._tab_orders[i] not in self._tab_rules[extension]:
                self.parent._results_tab_selection.setTabVisible(i, False)
            else:
                self.parent._results_tab_selection.setTabVisible(i, True)
                self._actions[extension](self._selected_file)

    def _handleNewText(self, path):
        '''
        '''
        self.parent._selection_tab_text.highlighter = None
        with open(path, 'r') as f:
            self.parent._selection_tab_text.setPlainText(f.read())
        
    def _handleNewData(self, path):
        '''
        '''
        self.parent._selection_tab_text.highlighter = None
        with open(path, 'r') as f:
            data_str = f.read()
            self.parent._selection_tab_text.setPlainText(data_str)
            csv_io = StringIO(data_str)
            data = list(csv.reader(csv_io, lineterminator='\n'))
            header = list(data[0])
            data = data[1:]
            self._setUpModel(header, data)
            
    def _setUpModel(self, header, data):
        self._selection_result_data_model = DataTableModel(data, header, [str(i) for i in range(len(data))])
        self._selection_result_data_model.setPrecision(self.parent._selection_result_data_prec.value())
        self._selection_result_data_model.setOrientation('Vertical' if self.parent._selection_result_data_vert.isChecked() else 'Horizontal')
        self.parent._selection_result_data_prec.valueChanged.connect(self._selection_result_data_model.setPrecision)
        self.parent._selection_result_header_prec.valueChanged.connect(self._selection_result_data_model.setPrecisionHeader)
        self.parent._selection_result_data_view.setModel(self._selection_result_data_model)
        self.parent._selection_result_data_view.resizeColumnsToContents()
        self.parent._selection_result_data_cond.stateChanged.connect(self._condenseChange)
        self._selection_result_data_model.dataChanged.connect(self.parent._selection_result_data_view.resizeColumnsToContents)
        self._selection_result_data_model.setPlotTarget(self.ax)
                
    def _setUpComparisonModel(self, header, data):
        self._comparison_result_data_model = DataTableModel(data, header, [str(i) for i in range(len(data))])
        self._comparison_result_data_model.setPrecision(self.parent._comparison_result_data_prec.value())
        self._comparison_result_data_model.setOrientation('Vertical' if self.parent._comparison_result_data_vert.isChecked() else 'Horizontal')
        self.parent._comparison_result_data_prec.valueChanged.connect(self._comparison_result_data_model.setPrecision)
        self.parent._comparison_result_header_prec.valueChanged.connect(self._comparison_result_data_model.setPrecisionHeader)
        self.parent._comparison_result_data_view.setModel(self._comparison_result_data_model)
        self.parent._comparison_result_data_view.resizeColumnsToContents()
        self.parent._comparison_result_data_cond.stateChanged.connect(self._condenseChangeComparison)
        self._comparison_result_data_model.dataChanged.connect(self.parent._comparison_result_data_view.resizeColumnsToContents)

    def _handleNewMask(self, path):
        '''
        '''
        self.parent._selection_tab_text.highlighter = None
        with open(path, 'r') as f:
            self.parent._selection_tab_text.setPlainText(f.read())
            f.seek(0)
            self._mask_generator.grabMask(json.load(f))
            mask = self._mask_generator.generateMask(128, 128)
            self._mask_plot_selection.setData(
                x=np.array(
                    [i for i in range(mask.shape[0])]),
                y=np.array(
                    [i for i in range(mask.shape[1])]),
                z=mask)
        
    def _handleNewScript(self, path):
        '''
        '''
        self.parent._selection_tab_text.highlighter = self.parent._selection_tab_text.highlighter = PythonHighlighter(self.parent._selection_tab_text.document())
        with open(path, 'r') as f:
            self.parent._selection_tab_text.setPlainText(f.read())
            