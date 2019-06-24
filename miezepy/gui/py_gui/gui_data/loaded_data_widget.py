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

import operator
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys
import os

from ...qt_gui.loaded_data_ui import Ui_dataset_widget

class LoadedDataWidget(Ui_dataset_widget,QtCore.QObject):
    '''
    This class will manage the raw import 
    machinery. the UI is inherited through 
    Ui_main_window from the Qt designer anf then
    converted through pyuic5
    '''

    def __init__(self, data_handler, parent = None):
        QtCore.QObject.__init__(self)
        Ui_dataset_widget.__init__(self)

        self.parent = parent
        self.item   = QtWidgets.QListWidgetItem(parent)
        self.widget = QtWidgets.QWidget()

        self.setupUi(self.widget)
        self.meta_table.resizeColumnsToContents()
        self.data_handler = data_handler
        self.initialize()

        self.parent.setItemWidget(self.item, self.widget)
        self.item.setSizeHint(self.widget.size())

    def initialize(self):
        '''
        set all the fields after initializing the gui
        '''
        try:
            self.disconnect()
        except:
            pass

        self.para_input.setText(self.data_handler.parameter)
        self.meas_input.setValue(int(self.data_handler.meas))
        self.ref_radio.setChecked(self.data_handler.reference)
        self.back_radio.setChecked(self.data_handler.background)

        self.connect()

    def setMeta(self,val_dict, file_list):
        '''
        Process an array of values to set the 
        parameters in the design
        '''
        new_val_dict = dict(val_dict)
        try:
            del new_val_dict['Parameter']
        except:
            pass
        try:
            del new_val_dict['Measurement']
        except:
            pass
        self.setTable(new_val_dict, file_list)

    def clearTable(self):
        '''
        Clears the table content and makes it ready 
        for new entries
        '''
        pass

    def setTable(self,val_dict, file_list):
        '''
        Put the elements into the table widget
        '''
        data_list = [[val_dict[key][i] for key in val_dict.keys()] for i in range(len(file_list))]
        self.header = [key for key in val_dict.keys()]
        self.model = MyTableModel(
            None,
            data_list, 
            self.header, 
            file_list)

        self.meta_table.setModel(self.model)

    def eventFilter(self, in_object, event):
        '''
        The event filter to manage clicks on all 
        '''
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.item.setSelected(True)
        return in_object.eventFilter(in_object, event)

    def connect(self):
        '''
        connect
        '''
        self.para_input.textChanged.connect(self.getValues)
        self.meas_input.valueChanged.connect(self.getValues)
        self.ref_radio.toggled.connect(self.getValues)
        self.back_radio.toggled.connect(self.getValues)

        self.para_input.installEventFilter(self)
        self.meas_input.installEventFilter(self)
        self.ref_radio.installEventFilter(self)
        self.back_radio.installEventFilter(self)
        self.vis_button.installEventFilter(self)
        self.meta_table.installEventFilter(self)


    def disconnect(self):
        '''
        disconnect
        '''
        self.para_input.textChanged.disconnect(self.getValues)
        self.meas_input.valueChanged.disconnect(self.getValues)
        self.ref_radio.toggled.disconnect(self.getValues)
        self.back_radio.toggled.disconnect(self.getValues)

        # self.para_input.selectionChanged.disconnect(self.setSelected)
        # self.meas_input.clicked.disconnect(self.setSelected)
        # self.ref_radio.clicked.disconnect(self.setSelected)
        # self.back_radio.clicked.disconnect(self.setSelected)
        # self.vis_button.clicked.disconnect(self.setSelected)
        # self.meta_table.clicked.disconnect(self.setSelected)


    def getValues(self, index = None):
        '''
        initialize the widget and set the stage
        '''
        self.data_handler.parameter = self.para_input.text()
        self.data_handler.meas      = str(self.meas_input.value())
        self.data_handler.reference = self.ref_radio.isChecked()
        self.data_handler.background= self.back_radio.isChecked()


#https://stackoverflow.com/questions/19411101/pyside-qtableview-example
class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mylist, col_header,row_header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.col_header = col_header
        self.row_header = row_header

    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        if len(self.mylist) > 0:
            return len(self.mylist[0])
        else:
            return 0
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.col_header[col]
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return self.row_header[col]
        else:
            return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))


                
        
