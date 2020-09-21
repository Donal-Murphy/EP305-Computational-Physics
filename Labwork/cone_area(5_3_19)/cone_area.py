# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:04:56 2019

@author: Donal Murphy

Description: returns the surface area of a cone given its height and radius
"""

#this program calculates the surface area of a cone given the radius and height

import numpy as np    #needed for pi

#-----------------------------------------------------------------------------#
#define the function cone_area()
def cone_area(r_value, h_value):
    #slant legth = sqrt(r**2 + h**2)
    return (np.pi*r_value*((r_value**2 + h_value**2)**(1/2)) +np.pi*r_value**2)
#-----------------------------------------------------------------------------#
    
#main program starts here
    
#inform the user what is happening
print('\nThis programme calcuates the surface area of a cone of radius, r, \
and height, h.    \
\nIt uses a USER DEFINED function')

ans = 'Y' #use the program at least once
while ans == 'Y':
    #prompt the user for the radius
    c_radius = float(input('\nEnter the radius of the cone in meters \
                           (e.g., 2.1) : '))
    #and height
    c_height = float(input('Enter the height of the cone in meters \
                           (e.g., 3.4) : '))
    
    #call the function cylinder_vol
    c_area = cone_area(c_radius, c_height)
    
    #output the results
    print('\nThe surface area of the cone is', \
          '{0:10.3f}'.format(c_area), 'meters\xb2')
    
    ans = input('\nDo you want to try another cone? (Y/N) ')