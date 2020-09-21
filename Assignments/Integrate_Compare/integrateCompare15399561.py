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
def integrateTrap(a,b,n):
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
    return analytical(a,b)-integrateTrap(a,b,n) # Calls analytical() and integrateTrap()

"""
Applies Simpson's 1\3rd rule to the desired function f()
"""
def integrateSimpson(a,b,n):
    
    # Initialise variables
    h = (b-a)/(n)           # Width
    area_1 = (h/3)*(f(a))   # First area
    area_f = (h/3)*(f(b))   # Final area
    total_odd =0.0          # Stores the sum of areas for odd n
    total_even = 0.0        # Stores the sum of areas for even n
    x = a + h
    
    # Calculate the area of odd and even indexed areas according to Simpson's
    for i in range(2,n+1):
    
        if i % 2 == 0:
            total_even += (h/3)*(4*f(x))  # Calls f()
            x += h
        else:
            total_odd += (h/3)*(2*f(x))   # Calls f()
            x += h
        
    return area_1 + area_f + total_odd + total_even # Return sum total area

"""
Calculates the error in the Simpson estimate by comparing it
with the analytical answer 
"""
def simp_error(a,b,n):
    return analytical(a,b)-integrateSimpson(a,b,n) # Calls analytical(), integrateSimpson()

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
    title_4 = 'Simp Estimate'
    title_5 = 'Simp Error'
    
    # Print analytical result and table titles 
    print('\nThe analytical answer = ',analytical(a,b))
    print('\nThe estimate of the integral between the limits [',a,' ',b,']',\
          'are: ')
    print('\n\033[31m''{0:>21}'.format(title_1), \
          '{0:>15}'.format(title_2), \
          '{0:>15}'.format(title_3), \
          '{0:>15}'.format(title_4), \
          '{0:>15}'.format(title_5),'\033[0m')
    
    error =1 # Dummy Value
    
    # Iterates over n by a factor of 2 until a good estimate is found
    while (error>1e-10):         
        
        
        print('{0:>21}'.format(n), \
              '{0:>15.10f}'.format(integrateTrap(a,b,n)),\
              '{0:>15.10f}'.format(trap_error(a,b,n)), \
              '{0:>15.10f}'.format(integrateSimpson(a,b,n)), \
              '{0:>15.10f}'.format(simp_error(a,b,n)))
        
        error = abs(simp_error(a,b,n))
        n *= 2
    
# Inform the user what is happening
print("\nThis program estimates the integral of the function sin(x)", \
      "in the interval [a,b] using both the trapezoidal rule and", \
      "Simpson's 1/3 rule" )
cont = 'y'

while (cont == 'y'):
    main()
    cont = input('Would you like to try again? y/n: ')