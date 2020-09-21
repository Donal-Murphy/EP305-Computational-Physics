# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:56:47 2019

@author: donal

This is a program that squares two positive integers x and y entered by the user 
and prints them to the screen
"""

# main program starts here

# inform the user what is happening
print('\nThis program requires the user to enter two positive integers, x and y.')
print('It then squares the two numbers and prints the result')

# Prompt the user to enter the first number
x = int(input('Please type in the first positive integer, x, and press enter: '))
#input() reads a string.
#Passing it to float() converts the string to a real number

#Prompt the user to enter the second number
y = int(input('Please type in the second positive integer, y, and press enter: '))

# square both numbers
x_squared,y_squared = x**2, y**2

# print the results
print('\n')  # skip an extra line
print(x, 'squared is', x_squared, 'and', y, 'squared is', y_squared)