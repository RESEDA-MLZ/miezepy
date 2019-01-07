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

#############################
#import general components
import numpy as np
import copy

from .mask_shape    import MaskShape
from .linear_comp   import LinearComposition


class RadialComposition(LinearComposition):
    
    def __init__(self):
        '''
        This is the grid mode of the element. 
        Note that this composition can only 
        be set to close gaps if the subelement
        is of rectangular shape.
        '''
        LinearComposition.__init__(self)
        self.initialize()

    def initialize(self):
        '''
        This routine will edit the inherited 
        dictionary of parameters.
        '''
        self.parameters['type']         = 'radial composition'
        self.parameters['child type']   = 'square'
        self.parameters['horizontal']   = 1
        self.parameters['vertical']     = 1
        self.parameters['angle_range']  = [0, 360]
        self.parameters['radius_range'] = [30, 60]
        self.parameters['close gap']    = True
        self.parameters['increment']    = True
        
        self.children = []

        self.setChildType(self.parameters['child type'])

    def setDirectly(self, parameters):
        '''
        The mask generator favours the direct
        input of the values onto the mask
        and will therefore send it to the mask
        element to be anaged.
        '''

        test = [
            self.parameters['position']     == parameters[1],
            self.parameters['horizontal']   == parameters[2],
            self.parameters['vertical']     == parameters[3],
            self.parameters['angle_range']  == parameters[4],
            self.parameters['radius_range'] == parameters[5],
            self.parameters['close gap']    == parameters[6],
            self.parameters['increment']    == parameters[7]]

        if not all(test):
            self.parameters['position']     = list(parameters[1])
            self.parameters['horizontal']   = int(parameters[2])
            self.parameters['vertical']     = int(parameters[3])
            self.parameters['angle_range']  = list(parameters[4])
            self.parameters['radius_range'] = list(parameters[5])
            self.parameters['close gap']    = bool(parameters[6])
            self.parameters['increment']    = bool(parameters[7])
            self.parameters['processed']    = False

    def setup(self):
        '''
        Setup the grid with the elements within
        '''
        t = np.deg2rad(np.linspace(
            self.parameters['angle_range'][0],
            self.parameters['angle_range'][1],
            num = self.parameters['horizontal']))

        r = np.linspace(
            self.parameters['radius_range'][0],
            self.parameters['radius_range'][1],
            num = self.parameters['vertical'])

        rr, tt = np.meshgrid(r, t)
        
        edges = []
        angles = []

        for i in range(tt.shape[0]):
            for j in range(tt.shape[1]):
                edges.append([
                    rr[i,j] * np.cos(tt[i,j]) + self.parameters['position'][0], 
                    rr[i,j] * np.sin(tt[i,j]) + self.parameters['position'][1]])

                angles.append(tt[i,j])

        for i in range(len(edges)):
            edges[i] = self.rotatePoint(
                self.parameters['position'],
                edges[i],
                self.parameters['angle'])

        self.children = []

        for i, edge in enumerate(edges):
            element = copy.deepcopy(self.template)

            # if self.parameters['child type'] == 'square':
            #     if self.parameters['close gap']: 
            #         element.parameters['width']  = (x[1] - x[0])
            #         element.parameters['height'] = (y[1] - y[0])

            element.move(absolute = edge)
            element.rotate(relative = self.parameters['angle'])
            element.rotate(relative = np.rad2deg(angles[i]))

            self.children.append(element)


if __name__ == '__main__':
    
    import matplotlib.pyplot as plt

    comp = RadialComposition()
    comp.parameters['horizontal']   = 6
    comp.parameters['vertical']     = 2
    comp.parameters['angle']        = 45
    comp.parameters['increment']    = False
    comp.setChildType('arc')
    comp.move(absolute = [100,100])
    comp.template.parameters['angle_range']     = (-90, 90)
    comp.template.parameters['radius_range']    = (10, 13)
    comp.generate(250,250)
    buff = np.array(comp.mask)
    comp.setChildType('square')
    comp.generate(250,250)
    buff_2 = np.array(comp.mask)
    comp.parameters['angle']  = 0
    comp.setChildType('triangle')
    comp.generate(250,250)
    plt.pcolormesh(comp.mask + buff + buff_2)
    plt.show()
