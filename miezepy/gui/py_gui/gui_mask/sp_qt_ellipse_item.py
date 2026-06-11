#  -*- coding: utf-8 -*-
# *****************************************************************************
# This class was copied from the "simpleplot" library (ploting/graph_items/ellipse_item.py)
#                   and from the "simpleplot" library (ploting/graph_items/ellipse_view.py)
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

from PyQt5 import QtGui, QtCore

from .sp_qt_graph_item import GraphItem
from .sp_qt_graph_item import GraphView

class EllipseView(GraphView):
    '''
    This item will be the graph item that is
    put an managed on its own
    '''

    def __init__(self, **opts):
        '''

        '''
        super().__init__(**opts)

        self._parameters['diameters'] = [1.,1.]
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

        p.drawEllipse(
            QtCore.QPointF(0.,0.), 
            self._parameters['diameters'][0], self._parameters['diameters'][1])

        super().outPainter(p, *args)

    def boundingRect(self):
        return  QtCore.QRectF(
            self._parameters['positions'][0] - self._parameters['diameters'][0] 
            - self._parameters['pen'].widthF()*2, 
            self._parameters['positions'][1] - self._parameters['diameters'][1] 
            - self._parameters['pen'].widthF()*2,
            self._parameters['diameters'][0]*2 + self._parameters['pen'].widthF()*4., 
            self._parameters['diameters'][1]*2 + self._parameters['pen'].widthF()*4.)

    def shape(self):
        '''
        Override the shape method
        '''
        path = QtGui.QPainterPath()
        path.addEllipse(
            self._parameters['positions'][0], self._parameters['positions'][1], 
            self._parameters['diameters'][0], self._parameters['diameters'][1])
        return path


class EllipseItem(GraphItem):
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
        self.initializeVisual2D(**kwargs)
        self.initializeVisual3D(**kwargs)
        self._mode = '2D'

    def initialize(self, **kwargs):
        '''
        This class will be the scatter plots. 
        The arguments are given as kwargs 
        '''
        self.addParameter(
            'Diameters', [2.,2.],
            names  = ['x','y'],
            tags   = ['2D', '3D'],
            method = self.refresh)

    def setVisual(self):
        '''
        Set the visual of the given shape element
        '''
        self.draw_items[-1].setData(
            positions = self['Position'][:-1], 
            diameters = self['Diameters'],
            angle = self['Angle'], 
            pen = super().getPen(),
            brush = super().getBrush(),
            Z = self['Z'],
            movable = self['Movable'])

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
            self.draw_items = [EllipseView()]
            self.default_target.addItem(self.draw_items[0])
            self.draw_items[0].moved.connect(self.handleMove)
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
