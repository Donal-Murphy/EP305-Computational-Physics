# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:39:20 2019

@author: donal

Description:
    A program to add two numbers entered by the user 
"""

# main program starts here

# inform the user what is happening
print('\nThis program requires the user to enter two numbers, a and b')
print('It then forms the sum and prints the result')

# Prompt the user to enter the first number
a = float(input('please type in the first number and press enter: '))
#input() reads a string.
#Passing it to float() conversts the string to a real number

#Prompt the user to enter the second number
b = float(input('please type in the second number and press enter: '))

# do the addition
sum_ab = a + b

# print the results
print('\n')  # skip an extra line
print(a, ' plus ', b , ' equals ', sum_ab)