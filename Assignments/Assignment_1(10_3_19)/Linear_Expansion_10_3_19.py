#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:17:55 2019

@author: Donal Murphy [15399561]

Description: This program calculates the linear expansion and % expansion of a 
steel rod.
"""

#-----------------------------------------------------------------------------#
# This is a modified range function that allows floats to be iterated for a 
# range of values
def mod_range(start,end,increment):
    while start < end:
        yield start
        start += increment

# Function for linear expansion
def linear_exp(temp):
    return alpha*(temp-temp_i)*length_i     # Returns the change in length
#-----------------------------------------------------------------------------#

ans = 'y'   # Ensures the program runs at least once

# Initialise constants required for calculation     
alpha = 11.7e-6 # Coefficient of linear expansion
temp_i = 0.0        # Initial temperature (in degrees Celsius)
length_i =  23.0  # Initial length (in metres, @ initial temperature)

# Create titles for table
title_1 = 'Temperature (C)'
title_2 = 'Expansion (m)'
title_3 = '% Expansion (%)'
 
# Inform the user what is happening
print('\nThis program calculates the linear expansion of a steel rod of '\
      'initial length 23m at 0 degrees Celsius for a range of ' \
      'temperatures between a and b (where a,b also in degrees Celsius).')

def main():
    
# request user input for temperature ranges
    while True:
        
        a = float(input('\nPlease enter a temperature in degrees Celsius ' \
                        '(10e5 <= a <= 10e6): '))
        # Check if input a in range
        if ((a>=10e5) and (a<=10e6)):
            break
        # Print error message if a not in range
        else:
            print('\033[31m\n\aError: value outside range\033[0m')
            
    while True:
        
        b = float(input('\nPlease enter a temperature in degrees Celsius ' \
                        '(10e5 <= b <= 10e6): '))
        
        # Check if input b in range
        if ((b>=10e5) and (b<=10e6)):
            break
        # Print error message if b not in range
        else:
            print('\033[31m\n\aError: value outside range\033[0m')

# Set minimum and maximum range
    if a > b:
        min_range = b
        max_range = a
        
    else:
        min_range = a
        max_range = b
    
# Print titles (right justified, fill character: 'f', field seperator: '|')
    print('\n\033[0;34;47m', \
          '{0:f>20}'.format(title_1), \
          ' | ', \
          '{0:f>20}'.format(title_2), \
          ' | ', \
          '{0:f>20}'.format(title_3), \
          '\033[0;30;0m')
# Run mod_range() within ranges in step size of 10e5         
    for i in mod_range(min_range,max_range,10e5):
        
        # Print results (Scientific format, 4 decimal places)
        print('\033[0;37;44m', \
              '{0:f>20.4e}'.format(i), \
              ' | ', \
              '{0:f>20.4e}'.format(linear_exp(i)), \
              ' | ', \
              '{0:f>20.4e}'.format((linear_exp(i)/length_i)*100), \
              '\033[0;30;0m')


# Run main() while user requests it
while ans == 'y':
    main()
    ans = input('Would you like to try again? (y/n): ')

# End program when user requests it
if ans == 'n':
    print('\nEnd')