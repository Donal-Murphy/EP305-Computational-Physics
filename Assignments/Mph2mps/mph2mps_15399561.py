# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:21:31 2019

Assignment 2

This program converts miles per hour to metres per second

@author: Donal Murphy
"""

# Informs the user what is happening
print('\nThis program converts miles per hour entered by the user ' \
      'to metres per second.')
print('It then prints the result.')

# Get user input
mph = float(input('Please enter a speed in miles per hour: '))

# Convertion Constants
mtr_mile = 1609.344   #metres in a mile
scnd_hr = 3600      #seconds in an hour

# Calculate the conversion
mps = (mph*mtr_mile)/scnd_hr

# Skip a line
print('\n')

# Print results in formatted output
print('Here is your conversion:')

print('{0:<20}'.format(str('{0:<0.3f}'.format(mph)) + ' mph'), \
      '=', \
      '{0:<20}'.format(str('{0:<0.3f}'.format(mps)) + ' m/s'))

print('{0:>25}'.format(str('{0:<0.5E}'.format(mph)) + ' mph'), \
      '=', \
      '{0:>25}'.format(str('{0:<0.5E}'.format(mps)) + ' m/s'))




