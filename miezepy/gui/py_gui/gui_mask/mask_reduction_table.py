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


from PyQt5 import QtWidgets, QtGui, QtCore

class ReductionTableView(QtWidgets.QTableView):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)
        self.horizontalHeader().hide()
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().hide()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self._multi_allowed = False
        self._setSelectionMode()
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

    def currentText(self):
        selected_rows = [self.model().data(item, QtCore.Qt.DisplayRole) for item in self.selectionModel().selectedRows()]
        return selected_rows[0] if len(selected_rows) > 0 else None
        
    def allTexts(self):
        return [self.model().data(item, QtCore.Qt.DisplayRole) for item in self.selectionModel().selectedRows()]

    def setCurrentIndexes(self):
        'TODO'
        print('set')
        return ''
        
    def setMultipleAllowed(self, state):
        self._multi_allowed = (state == 2)
        self._setSelectionMode()
        
    def _setSelectionMode(self):
        if self._multi_allowed:
            self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        else:
            self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
            