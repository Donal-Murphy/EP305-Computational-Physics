# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:28:13 2019

@author: Donal Murphy

Description: This program evaluates the legnth of a semicircle over various
intervals
"""
import numpy as np
#-----------------------------------------------------------------------------#
def f(x):
    # Evaluates f at x
    return (1-(x**2))**(1/2)

def new_length(x,dx):
    # Calls function f()
    return ((((x+dx)-x)**2)+((f(x+dx)-f(x))**2))**(1/2)
#-----------------------------------------------------------------------------#

# Print the titles
print('\033[31m''{0:>18}'.format('n'), ' | ', \
      '{0:>18}'.format('length'), ' | ', \
      '{0:>18}'.format('error'),'\033[0m')

# Initialise variable n, the mnumber of intervals
n = 1

# Loops until the desired error value is achieved
while True:

    # Initialise variables
    x_1, x_2 = -1, 1    # Start and end points
    dx = (x_2-x_1)/n    # change in x
    c_length = 0       
    
    #for a number of intervals, n, calcuates the length of each segment and the
    #sum total
    for i in range(0,n):
        
        x = x_1 + i*dx
        
        c_length = c_length + new_length(x, dx)
        c_error = np.pi - c_length
    
    #print the results
    print('{0:>18}'.format(n), ' | ', \
          '{0:>18.7f}'.format(c_length), ' | ', \
          '{0:>18.7f}'.format(c_error))
    # Number of intervals increase by a factor of two
    n*=2
    
    #break out of the loop when the desired error is achieved
    if c_error < 1e-6:
        break