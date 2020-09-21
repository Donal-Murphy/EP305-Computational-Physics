# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:01:17 2019

Converts wavelength to frequency, energy in joules, energy to electron volts

@author: donal
"""

# inform the user what is happening
print('\nThis program converts photon wavelength entered by the user ' \
      'to frequency (Hz), energy in joules and energy in eV')

# get input (wavelength in nanometers)
wavelength_nm = float(input('Enter the wavelength in nanometers: '))

# wavelength in meters
wavelength_m = wavelength_nm*1e-9

#constants needed for calculations
c = 2.99792458e+8    #speed of light (m/s)
h = 6.6260693e-34   #Plank's conastant 
e = 1.60217653e-19   #definition of the electron volt (J)

# calculate frequency (Hz)
f = c/wavelength_m

# calculate energy (J)
En_J = h*f

# calculate energy (J)
E_eV = En_J/e

# titles
title1 = 'w/l (nm)'
title2 = 'Frequency (Hz)'
title3 = 'energy (J)'
title4 = 'energy (eV)'
print('\n') # skip a line

# print results in formatted output
print('{0:>10}'.format(title1), \
      '{0:>15}'.format(title2), \
      '{0:>11}'.format(title3), \
      '{0:>12}'.format(title4))

print('{0:>10.1f}'.format(wavelength_nm), \
      '{0:>15.2e}'.format(f), \
      '{0:>11.3e}'.format(En_J), \
      '{0:>12.4f}'.format(E_eV))



