# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:47:26 2019

@author: Donal Murphy

Description: Calculates the values of the sine and cosine functions at n
equal intervals between 0 and 2*pi (inclusive).
"""

#import numpy for trig functions
import numpy as np

#inform the user what is happening
print('\nThis program calculates sine and cosine between 0 and 2*Pi '\
      'in an equal number of intervals entered by the user.')

# declare and initialize constant end points
x_0, x_1 = 0.0, 2.0*np.pi

# get the number intervals from the user
n = int(input('Enter the number of intervals, n (e.g., 12): '))

# set the step size
deltaX = ((x_1-x_0)/n)

# put a header on the table of values
title1, title2, title3, title4 = 'x(rad)', 'x(degrees)', 'sin(x)', 'cos(x)'

print('\n{0:>8}'.format(title1), \
      '{0:>12}'.format(title2), \
      '{0:>16}'.format(title3), \
      '{0:>16}'.format(title4))

# evaluate and print the values of the function in a for loop
for i in range(1,n+1):
    x = x_0 + i*deltaX
    
    print('{0:>8.3f}'.format(x), \
          '{0:>12.3f}'.format(np.degrees(x)), \
          '{0:>16.3f}'.format(np.sin(x)), \
          '{0:>16.3f}'.format(np.cos(x)))






