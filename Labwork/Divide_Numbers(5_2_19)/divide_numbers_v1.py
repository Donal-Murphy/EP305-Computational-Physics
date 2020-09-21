# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:54:23 2019

@author: donal
"""

# main program starts here

# inform the user what is happening
print('\nThis program requires the user to enter two numbers, a and b')
print('It then divides a by b and prints the result')

# Prompt the user to enter the first number
a = float(input('please type in the first number and press enter: '))
#input() reads a string.
#Passing it to float() conversts the string to a real number

#Prompt the user to enter the second number
b = float(input('please type in the second number and press enter: '))

# do the division
div_ab = a / b

# print the results
print('\n')  # skip an extra line
print(a, ' divided by ', b , ' equals ', div_ab)