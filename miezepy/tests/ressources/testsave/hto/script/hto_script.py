##--IMPORT--##
'''
#############################################
The environement is initialised automatically
and then the data is loaded within the core
as defined.

Here we recommend to set the name pointing 
to the environement and minor manipulations
on the data if necessary.
#############################################
'''
environnement = self.env

environnement.current_data.metadata_class.addMetadata('Source format', value = "ToF files", logical_type = 'str')
environnement.current_data.metadata_class.addMetadata('Measurement type', value = "MIEZE", logical_type = 'float')
environnement.current_data.metadata_class.addMetadata('Wavelength error', value = 0.117 , logical_type = 'float')
environnement.current_data.metadata_class.addMetadata('Distance error', value = 0.0005 , logical_type = 'float')

environnement.current_data.metadata_class.addMetadata('R_1', value = 9. , logical_type = 'float', unit = 'm')
environnement.current_data.metadata_class.addMetadata('R_2', value = 5. , logical_type = 'float', unit = 'm')
environnement.current_data.metadata_class.addMetadata('L_1', value = 1200 , logical_type = 'float', unit = 'm')
environnement.current_data.metadata_class.addMetadata('L_2', value = 3500 , logical_type = 'float', unit = 'm')
environnement.current_data.metadata_class.addMetadata('Wavelength in', value = 6. , logical_type = 'float', unit = 'A')
environnement.current_data.metadata_class.addMetadata('Pixel size', value = 1.5625 , logical_type = 'float', unit = 'mum')
environnement.current_data.metadata_class.addMetadata('Qy', value = 0.035 , logical_type = 'float', unit = '-')
environnement.current_data.metadata_class.addMetadata('Selected foils', value = '[1,1,1,1,1,1,1,1]' , logical_type = 'int_array', unit = '-')

print(environnement.current_data)

##--IMPORT--##
##--FIT-PARA--##
#  -*- coding: utf-8 -*-
'''
#############################################
Here we set the overall fit parameters as well
as proceeding through the phase corrections. 
#############################################
'''
environnement = self.env

#Set the foils (edit in GUI)
foils_in_echo = []
foils_in_echo.append([1, 1, 1, 1, 1, 1, 0, 0])
foils_in_echo.append([1, 1, 1, 1, 1, 1, 0, 0])
foils_in_echo.append([1, 1, 1, 1, 1, 1, 0, 0])

#Set the selected (edit in GUI)
Selected = []

#Set the time channels to use(edit in GUI)
TimeChannels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Set the background (edit in GUI)
Background = None

#Set the reference (edit in GUI)
Reference = ['ref',0]

#Instrument (edit in GUI)
instrument = 'Reseda'

#Detector(edit in GUI)
detector = 14032019

#Use the high exposure setting (edit in GUI)
exposure = False

#Use the foil summation methodology
sum_foils = False


environnement.fit.set_parameter( name = 'Select',        value = Selected     )
environnement.fit.set_parameter( name = 'Reference',     value = Reference    )
environnement.fit.set_parameter( name = 'Background',    value = Background   )
environnement.fit.set_parameter( name = 'foils_in_echo', value = foils_in_echo)
environnement.fit.set_parameter( name = 'processors',    value = 1)
environnement.fit.set_parameter( name = 'exposure',      value = exposure)
environnement.fit.set_parameter( name = 'time_channels', value = TimeChannels)
environnement.fit.set_parameter( name = 'sum_foils',     value = sum_foils)
environnement.instrument.setDetector(instrument, detector)

##--FIT-PARA--##
##--PHASE--##
#  -*- coding: utf-8 -*-
'''
#############################################
Here we set the overall fit parameters as well
as proceeding through the phase corrections. 
#############################################
'''
environnement = self.env

environnement.mask.setMask('None')
print(environnement.mask)

environnement.process.calculateEcho()
environnement.process.calcShift()

##--PHASE--##
##--REDUCTION--##
'''
#############################################
In this script we will effectively reduce the
data. Essential to this is the selection of
the mask that will be used to reduce.

environment.process.calculate_ref_contrast()
-> will evaluate the contrast of the 
reference.

environment.process.calculate_contrast()
-> will evaluate the contrast of selected 
measurements.

It is possible to edit missfit results as 
seen with the set_result command
#############################################
'''
environment = self.env

environment.mask.setMask('')
print(environment.mask)

# environment.results.set_result( 
#          name = 'Reference contrast calculation', 
#          position = ['Contrast_ref',0.36585973199337996], 
#          value = 0.73)

# environment.results.set_result(
#          name = 'Reference contrast calculation', 
#          position = ['Contrast_ref_error',0.36585973199337996], 
#          value = 0.0035)


environment.process.calcContrastRef()
environment.process.calcContrastMain()

##--REDUCTION--##
##--POST--##
'''
#############################################
This is the post process script. it is free
to the user for editing. The reduction result
is grabbed from the environnement through :
result = environment.get_result(name = 'Contrast fit')

it is possible to import matplotlib or other
libraries and to perform further 
investigations. It is also possible to save 
any output to a given path. 
#############################################
'''
environment = self.env

# -> possibility to dump the log to file
# environment.fit.log.dump_to_file('result.txt')

#grab he result
result = environment.get_result(name = 'Contrast fit')

############################################
#Matplotlib plot of the result
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.constants as co
from matplotlib.colors import Colormap, LogNorm
from matplotlib.cm import get_cmap
fig = plt.figure(figsize=(16,5))
ax  = fig.add_subplot(1,2,1)
ax.set_xscale('log')
ax1 = fig.add_subplot(1,2,2)

############################################
#cycle over the echo fit results
index = 0
for T in result['Select']:
    x        = result['Parameters'][T]['x']
    y        = result['Parameters'][T]['y']
    y_error  = result['Parameters'][T]['y_error']

    ax.errorbar(
        x, 
        y+1.2-index*0.2,
        y_error, 
        fmt='o', 
        label='$T=%.2f\,K$' %T)
    x = np.linspace(0.01,3,1000)
    ax.plot(x, result['Curve'][T]+1.2-index*0.2)
    index += 1

ax1.errorbar(
    result['Select'],
    result['Gamma'],
    result['Gamma_error'],
    fmt='o', label='Franz\' quasielastic')

############################################
#evemtually save to file
#plt.savefig('result.pdf')

##--POST--##
