#  -*- coding: utf-8 -*-
# *****************************************************************************
#
# This class was copied from the "simpleplot" library (models/widget_constructors.py)
# url = "https://github.com/AlexanderSchober/simpleplot_qt/archive/refs/heads/master.zip"
#
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

from PyQt5 import QtCore, QtWidgets

class comboBoxConstructor:
    def __init__(self, parent = None, keyword = None, choice_keyword = None): 
        '''
        '''
        self.manager = parent
        self.keyword = keyword
        self.choice_keyword = choice_keyword

    def create(self,parent, value = None, index = None):
        '''
        '''
        self._index = QtCore.QModelIndex(index)
        editor = QtWidgets.QComboBox(parent)

        if not self.choice_keyword == None:
            editor.addItems(self.manager.kwargs[self.choice_keyword])
        else:
            editor.addItems(self.manager.kwargs['choices'])

        
        return editor

    def updateInternals(self, value):
        '''
        '''
        if not self.keyword == None:
            self.manager.kwargs[self.keyword] = value
        else:
            self.manager._value = value

        self.manager._model.dataChanged.emit(
            self.manager.index(),
            self.manager.index())

        if 'method' in self.manager.kwargs.keys():
            self.manager.kwargs['method']()

        self.manager.parent().setString()

    def setEditorData(self, editor):
        if not self.keyword == None:
            if not self.choice_keyword == None:
                editor.setCurrentIndex(
                    self.manager.kwargs[self.choice_keyword].index(
                        self.manager.kwargs[self.keyword]))
            else:
                editor.setCurrentIndex(
                    self.manager.kwargs['choices'].index(
                        self.manager.kwargs[self.keyword]))
        else:
            if not self.choice_keyword == None:
                editor.setCurrentIndex(
                    self.manager.kwargs[self.choice_keyword].index(
                        self.manager._value))
            else:
                editor.setCurrentIndex(
                    self.manager.kwargs['choices'].index(
                        self.manager._value))

        editor.currentTextChanged.connect(self.updateInternals)

    def retrieveData(self, editor):
        return editor.currentText()
    

class spinBoxConstructor:

    def __init__(self, parent = None): 
        self.manager = parent

    def create(self,parent, value = None, index = None):
        self._index = QtCore.QModelIndex(index)
        item = QtWidgets.QSpinBox(parent)
        
        if 'min' in self.manager.kwargs.keys():
            item.setMinimum(self.manager.kwargs['min'])
        else:
            item.setMinimum(-1000)
        if 'max' in self.manager.kwargs.keys():
            item.setMaximum(self.manager.kwargs['max'])
        else:
            item.setMaximum(1000)

        item.valueChanged.connect(self.updateInternals)
        return item

    def updateInternals(self, value):
        '''
        '''
        self.manager._value = value
        self.manager._model.dataChanged.emit(
            self.manager.index(),
            self.manager.index())

        if 'method' in self.manager.kwargs.keys():
            self.manager.kwargs['method']()

        self.manager.parent().setString()

    def setEditorData(self, editor):
        editor.setValue(self.manager._value)

    def retrieveData(self, editor):
        return editor.value()

class doubleSpinBoxConstructor:

    def __init__(self, parent = None): 
        self.manager = parent

    def create(self,parent, value = None, index = None):
        self._index = QtCore.QModelIndex(index)
        #item = SpinBox(parent)
        item = QtWidgets.QDoubleSpinBox(parent)

        if 'min' in self.manager.kwargs.keys():
            item.setMinimum(self.manager.kwargs['min'])
        else:
            item.setMinimum(-1000.)
        if 'max' in self.manager.kwargs.keys():
            item.setMaximum(self.manager.kwargs['max'])
        else:
            item.setMaximum(1000.)

        if 'step' in self.manager.kwargs.keys():
            item.setSingleStep(self.manager.kwargs['step'])
        else:
            item.setSingleStep(1.)

        item.valueChanged.connect(self.updateInternals)
        return item

    def updateInternals(self, value):
        '''
        '''
        self.manager._value = value
        self.manager._model.dataChanged.emit(
            self.manager.index(),
            self.manager.index())

        if 'method' in self.manager.kwargs.keys():
            self.manager.kwargs['method']()

        self.manager.parent().setString()

    def setEditorData(self, editor):
        editor.setValue(self.manager._value)

    def retrieveData(self, editor):
        return editor.value()
    
