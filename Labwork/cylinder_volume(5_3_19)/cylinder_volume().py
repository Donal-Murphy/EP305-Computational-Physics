# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:11:37 2019

@author: Donal Murphy

Description: returns the volume of a cylinder given its radius and height
"""
#this program calculates the volume of a cylinder given the radius
#and length of the cylinder

import numpy as np    #needed for pi

#-----------------------------------------------------------------------------#
#define the function cylinder vol()
def cylinder_vol(r_value, h_value):
    return (np.pi*r_value*r_value*h_value)
#-----------------------------------------------------------------------------#
    
#main program starts here
    
#inform the user what is happening
print('\nThis programme calcuates the volume of a cylinder of radius, r, \
and height, h.    \
\nIt uses a USER DEFINED function')

ans = 'Y' #use the program at least once
while ans == 'Y':
    #prompt the user for the radius
    c_radius = float(input('\nEnter the radius of the cylinder in meters \
                           (e.g., 2.1) : '))
    #and height
    c_height = float(input('Enter the height of the cylinder in meters \
                           (e.g., 3.4) : '))
    
    #call the function cylinder_vol
    c_volume = cylinder_vol(c_radius, c_height)
    
    #output the results
    print('\nThe volume of the cylinder is ', \
          '{0:10.3f}'.format(c_volume), 'meters\xb3')
    
    ans = input('\nDo you want to try another cylinder? (Y/N) ')