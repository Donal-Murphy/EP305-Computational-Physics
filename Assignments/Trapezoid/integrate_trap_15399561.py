# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:13:46 2019

@author: Donal Murphy

Description: This program performs an estimate for the definite integral of 
             sin(x) using the trapezoidal method. 
"""
#-----------------------------------------------------------------------------#
# import numpy library for sine and cosine functions
import numpy as np

#-----------------------------------------------------------------------------#
"""
Function to be calculated
"""
def f(x):
    return np.sin(x)

"""
Applies the trapezoidal rule to the desired function f()
"""
def my_trap(a,b,n):
    # Initialise and calulate variables
    
    h = (b-a)/n             # Trapezoid width
    trap_1 = (h/2)*(f(a))    # Area of first trapezoid. Calls f()
    trap_f = (h/2)*(f(b))    # Area of final trapezoid. Calls f()
    total = 0.0
    x = a + h
    # Calculate the sum of all remaining trapezoids 
    while (x<b):
        total += h*f(x) # Calls f(). Stores sum of trapezoids
        x += h          #Increments x, the distance along the x axis
    
    return total + trap_1 + trap_f # Return sum total areas

"""
Calculates the error in the trapezoidal estimate by comparing it
with the analytical answer
"""
def trap_error(a,b,n):
    return analytical(a,b)-my_trap(a,b,n) # Calls analytical() and my_trap()


"""
Calculates sin(x) analytically through direct integration
"""
def analytical(a,b):
    return np.cos(a)-np.cos(b)  # Integral of sin(x) = -cos(x) 
#-----------------------------------------------------------------------------#
"""
Main program. Requests user input and prints results on a table by calling
user defined functions
"""
def main(): 
    
    # Initialise variables and request user input
    a = float(input('Enter the lower limit a (e.g., 0.0) : '))
    b = float(input('Enter the upper limit b (e.g., 1.0) : '))
    n = 2
    
    #Titles
    title_1 = 'No. of Intervals'
    title_2 = 'Trap Estimate'
    title_3 = 'Trap Error'
    
    # Print analytical result and table titles 
    print('\nThe analytical answer = ',analytical(a,b))
    print('\nThe estimate of the integral between the limits [',a,' ',b,']',\
          'are: ')
    print('\n\033[31m''{0:>21}'.format(title_1), \
          '{0:>15}'.format(title_2), \
          '{0:>15}'.format(title_3), \
          '\033[0m')
    
    error =1 # Dummy Value
    
    # Iterates over n by a factor of 2 until a good estimate is found
    while (error>1e-5):         
        
        
        print('{0:>21}'.format(n), \
              '{0:>15.10f}'.format(my_trap(a,b,n)),\
              '{0:>15.10f}'.format(trap_error(a,b,n)))
        
        error = abs(trap_error(a,b,n))
        n *= 2
    
# Inform the user what is happening
print("This program estimates the integral of the function sin(x)", \
      "in the interval [a,b] using the trapezoidal rule")
cont = 'y'

while (cont == 'y'):
    main()
    cont = input('Would you like to try again? y/n: ')