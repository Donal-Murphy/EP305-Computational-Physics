# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:31:47 2019

Converts input in degres Celsius to degrees Fahrenheit

@author: Donal Murphy
"""
# prog to allow the user to enter a temperature in Celsius
#converts it to Fahrenheit and Kelvin
#and prints out the results

# inform the user what is happening
print('\nThis program converts degrees centigrade to degrees Fahrenheit')
print('Then it prints the results.')

# get input
celsius = float(input('Enter the temperature in degrees centigrade: '))

# convert to Fahrenheit
fahr = (9/5)* celsius + 32.0

title1 = 'degrees centigrade'
title2 = 'degrees Fahrenheit'
print('\n') # skip a line

# print the results in formatted output
print('{0:@<20}'.format(title1), \
      '{0:^7}'.format(':'), \
      '{0:>25}'.format(title2))
      # alpha is the fill character
     
print('{0:$<20.2f}'.format(celsius), \
      '{0:^7}'.format('='), \
      '{0:>25.4e}'.format(fahr))
      # dollar is fill character