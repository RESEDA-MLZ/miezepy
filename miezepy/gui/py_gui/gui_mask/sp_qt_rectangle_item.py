#  -*- coding: utf-8 -*-
# *****************************************************************************
# This class was copied from the "simpleplot" library (ploting/graph_items/rectangle_item.py)
#                   and from the "simpleplot" library (ploting/graph_items/rectangle_view.py)
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

from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np

#from ...pyqtgraph                   import pyqtgraph as pg
#from ...pyqtgraph.pyqtgraph         import opengl as gl

from .sp_qt_graph_item import GraphItem
#from simpleplot.ploting.graph_items.rectangle_view import RectangleView
from .sp_qt_graph_item import GraphView

class RectangleView(GraphView):
    '''
    This item will be the graph item that is
    put an managed on its own
    '''

    def __init__(self, **opts):
        '''

        '''
        super().__init__(**opts)

        self._parameters['dimensions'] = [1.,1.]
        self._parameters['positions'] = [2.,2.]
        self._parameters['angle'] = 0.
        self._parameters['brush'] = QtGui.QBrush()
        self._parameters['pen'] = QtGui.QPen()
        self._parameters['Z'] = 0
        self._parameters['movable'] = False

    def setData(self, **kwargs):
        '''
        Set the data for display
        '''
        self._parameters.update(kwargs)
        super().render()

    def paint(self, p, *args):
        '''
        override the paint method
        '''
        super().inPainter(p, *args)

        rect = QtCore.QRectF(
            - self._parameters['dimensions'][0]/2., 
            - self._parameters['dimensions'][1]/2., 
            self._parameters['dimensions'][0], self._parameters['dimensions'][1])
        
        p.drawRect(rect)

        super().outPainter(p, *args)

    def boundingRect(self):
        return  QtCore.QRectF(
            self._parameters['positions'][0] - self._parameters['dimensions'][0]/2. 
            - self._parameters['pen'].widthF()*2, 
            self._parameters['positions'][1] - self._parameters['dimensions'][1]/2. 
            - self._parameters['pen'].widthF()*2,
            self._parameters['dimensions'][0] + self._parameters['pen'].widthF()*4., 
            self._parameters['dimensions'][1] + self._parameters['pen'].widthF()*4.)

    def shape(self):
        '''
        Override the shape method
        '''
        path = QtGui.QPainterPath()
        path.addRect(QtCore.QRectF(
            self._parameters['positions'][0] - self._parameters['dimensions'][0]/2., 
            self._parameters['positions'][1] - self._parameters['dimensions'][1]/2., 
            self._parameters['dimensions'][0], self._parameters['dimensions'][1]))
        return path

class RectangleItem(GraphItem):
    '''
    This item will be the graph item that is
    put an managed on its own
    '''
    def __init__(self,*args, **kwargs):
        '''
        Arrows can be initialized with any keyword arguments accepted by 
        the setStyle() method.
        '''
        super().__init__(*args, **kwargs)
        
        self.initializeMain(**kwargs)
        self.initialize(**kwargs)
        #self.initializeVisual2D(**kwargs)
        #self.initializeVisual3D(**kwargs)

    def initialize(self, **kwargs):
        '''
        This class will be the scatter plots. 
        The arguments are given as kwargs 
        '''
        self.addParameter(
            'Dimensions', [20.,20.],
            names  = ['x','y'],
            tags   = ['2D', '3D'],
            method = self.refresh)
        self.addParameter(
            'Subdivisions', [1,1],
            names  = ['x','y'],
            tags   = ['2D', '3D'],
            method = self.resetSubdivision)
        #self.addParameter(
        #    'Subdivision dimensions', [True, 2.,2.],
        #    names  = ['Fill', 'x','y'],
        #    tags   = ['2D', '3D'],
        #    method = self.setVisual)

    def setVisual(self):
        '''
        Set the visual of the given shape element
        '''
        if not hasattr(self, 'draw_items'):
            self.resetSubdivision()
            return
        if len(self.draw_items) != self['Subdivisions'][0] or len(self.draw_items[0]) != self['Subdivisions'][1]:
            self.resetSubdivision()
            return
            
        parameters = {
            'angle' : self['Angle'], 
            'pen' : super().getPen(),
            'brush' : super().getBrush(),
            'Z' : self['Z'],
            'movable' : self['Movable'],
            'positions':[],
            'dimensions':[]}

        for i in range(self['Subdivisions'][0]):
            for j in range(self['Subdivisions'][1]):
                pos = [
                    -self['Dimensions'][0]/2.+(i+0.5)*self['Dimensions'][0]
                    /self['Subdivisions'][0],
                    -self['Dimensions'][1]/2.+(j+0.5)*self['Dimensions'][1]
                    /self['Subdivisions'][1]]

                norm = np.sqrt(pos[0]**2+pos[1]**2)
                if norm == 0.:
                    parameters['positions'] = [
                        self['Position'][0],
                        self['Position'][1]]
                else:
                    angle = np.arccos(pos[0]/norm)/np.pi*180.
                    if np.arcsin(pos[1]/norm) < 0:
                        angle = -angle 

                    parameters['positions'] = [
                        norm*np.cos((self['Angle']+angle)*np.pi/180.)+self['Position'][0],
                        norm*np.sin((self['Angle']+angle)*np.pi/180.)+self['Position'][1]]
                        
                if self['Subdivision dimensions'][0]:
                    parameters['dimensions'] = [
                        self['Dimensions'][0]/self['Subdivisions'][0],
                        self['Dimensions'][1]/self['Subdivisions'][1]]
                else:
                    parameters['dimensions'] = [
                        self['Subdivision dimensions'][1],
                        self['Subdivision dimensions'][2]]  

                self.draw_items[i][j].setData(**dict(parameters))

    def draw(self, target_surface = None):
        '''
        Draw the objects.
        '''
        self.removeItems()
        self._mode = '2D'
        if not target_surface == None:
            self.default_target = target_surface.draw_surface.vb
            self.setCurrentTags(['2D'])
            
        if self['Visible']:
            self.draw_items = []
            for i in range(self['Subdivisions'][0]):
                temp = []
                for j in range(self['Subdivisions'][1]):
                    item = RectangleView()
                    temp.append(item)
                    self.default_target.addItem(item)
                    item.moved.connect(self.handleMove)
                self.draw_items.append(temp)
            self.setVisual()

    def drawGL(self, target_view = None):
        '''
        Draw the objects.
        '''
        self._mode = '3D'
        if not target_view == None:
            self.default_target = target_view
            self.setCurrentTags(['3D'])

        if self['Visible']:
            self.draw_items = []
            self.default_target.addItem(self.draw_items[-1])

