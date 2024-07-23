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
from simpleplot.artist.artist import Artist

class DataTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data_list, col_header, row_header, *args):
        QtCore.QAbstractTableModel.__init__(self, *args)
        self.data_list = data_list
        self._base_col_header = col_header
        self._base_row_header = row_header
        self._precision = 10
        self._precision_header = 10
        self._orientataion = 'Vertical'
        self._colors = ['#d4d4d4', '#828282', '#ff837a']
        self._condense_tau = False
        self._plot_target = None
        self._color_list = [
            "#1f77b4", "#ff7f0e", "#2ca02c", 
            "#d62728", "#9467bd", "#8c564b", 
            "#e377c2", "#7f7f7f", "#bcbd22", 
            "#17becf"]
        self._manageHeaders()

    def rowCount(self, parent=None):
        if self._orientataion == 'Vertical':
            val = len(self.data_list)
        else:
            if len(self.data_list) > 0:
                val = len(self.data_list[0])
                val = val if not self._condense_tau else val - val/3
            else:
                val = 0
        
        return val

    def columnCount(self, parent=None):
        if self._orientataion == 'Horizontal':
            val =  len(self.data_list)
        else:
            if len(self.data_list) > 0:
                val = len(self.data_list[0])
                val = val if not self._condense_tau else val - val/3
            else:
                val =  0
        return val
    
    def setPlotTarget(self, target: Artist):
        self._plot_target = target
        self._plot_target.clear()
        self._plots = []
        for i in range(len(self._base_col_header)//3-1):
            plot = self._plot_target.addPlot(
                'Scatter',
                Name = self._base_col_header[i*3+1],
                x=[self.data_list[j][i*3] for j in range(len(self._base_row_header))],
                y=[self.data_list[j][i*3+1] for j in range(len(self._base_row_header))],
                error={
                    'height':None,
                    'width' : None,
                    'bottom':[float(self.data_list[j][i*3+2]) for j in range(len(self._base_row_header))],
                    'top'   :[float(self.data_list[j][i*3+2]) for j in range(len(self._base_row_header))]},
                Style=['-', 'd','r','20'],
                Color=self._color_list[i])
            self._plots.append(plot)
            
        self._plot_target.draw()

    def condenseTau(self, val):
        # We have to change the row and column count, so we get the current ant then the new
        old_row_count = self.rowCount()
        old_col_count = self.columnCount()
        self._condense_tau = val
        new_row_count = self.rowCount()
        new_col_count = self.columnCount()
        
        self._internalResize(old_row_count, old_col_count, new_row_count, new_col_count)
        self._manageHeaders()
        
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    def _manageHeaders(self):
        if self._condense_tau:
            self.col_header = [item for i, item in enumerate(self._base_col_header) if i % 3 != 0]
            self.row_header = [self.data_list[i][0] for i in range(len(self.data_list))] if len(self.data_list) > 0 else []
        else:
            self.col_header = self._base_col_header
            self.row_header = list(range(len(self.data_list)))
        
    def setPrecision(self, val):
        self._precision = val
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    def setPrecisionHeader(self, val):
        self._precision_header = val
        self.headerDataChanged.emit(QtCore.Qt.Vertical, 0, len(self.row_header))
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    def setOrientation(self, val):
        # We have to change the row and column count, so we get the current ant then the new
        old_row_count = self.rowCount()
        old_col_count = self.columnCount()
        self._orientataion = val
        new_row_count = self.rowCount()
        new_col_count = self.columnCount()
        
        self._internalResize(old_row_count, old_col_count, new_row_count, new_col_count)

        # Update the data
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
        
    def _internalResize(self, old_row_count, old_col_count, new_row_count, new_col_count):
        # handle rows
        if old_row_count < new_row_count:
            self.beginInsertRows(QtCore.QModelIndex(), old_row_count, new_row_count-1)
            self.endInsertRows()
        elif old_row_count > new_row_count:
            self.beginRemoveRows(QtCore.QModelIndex(), new_row_count, old_row_count -1)
            self.endRemoveRows()
        
        # handle columns
        if old_col_count < new_col_count:
            self.beginInsertColumns(QtCore.QModelIndex(), old_col_count, new_col_count - 1)
            self.endInsertColumns()
        elif old_col_count > new_col_count:
            self.beginRemoveColumns(QtCore.QModelIndex(), new_col_count, old_col_count - 1)
            self.endRemoveColumns()
            
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role == QtCore.Qt.DisplayRole:
            if self._orientataion == 'Vertical':
                index_mod = index.column() - index.column() // 3 if self._condense_tau else index.column()
                return round(float(self.data_list[index.row()][index_mod]), self._precision)
            else:
                index_mod = index.row() - index.row() // 3 if self._condense_tau else index.row()
                return round(float(self.data_list[index.column()][index_mod]), self._precision)
        elif role == QtCore.Qt.BackgroundRole:
            if self._orientataion == 'Vertical':
                modulator = index.column() % 2 + 1 if self._condense_tau else index.column() % 3
                return QtCore.QVariant(QtGui.QColor(self._colors[modulator]))
            else:
                modulator = index.row() % 2 + 1 if self._condense_tau else index.row() % 3
                return QtCore.QVariant(QtGui.QColor(self._colors[modulator]))
    
    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if self._orientataion == 'Vertical':
                return self.col_header[col]
            else:
                return round(float(self.row_header[col]), self._precision_header) if self._condense_tau else self.row_header[col]
            
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            if self._orientataion == 'Horizontal':
                return self.col_header[col]
            else:
                return round(float(self.row_header[col]), self._precision_header) if self._condense_tau else self.row_header[col]
            
        elif orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.BackgroundRole and self._orientataion == 'Vertical':
            modulator = col % 2 + 1 if self._condense_tau else col % 3
            return QtCore.QVariant(QtGui.QColor(self._colors[modulator]))
        
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.BackgroundRole and self._orientataion == 'Horizontal':
            modulator = col % 2 + 1 if self._condense_tau else col % 3
            return QtCore.QVariant(QtGui.QColor(self._colors[modulator]))
        else:
            return None