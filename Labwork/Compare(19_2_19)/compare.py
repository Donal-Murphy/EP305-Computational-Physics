# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:31:53 2019

this program compares two positive integers and informs the user 
whether on value is greater than, less than or equal two the entered values

@author: donal
"""
#inform the user what is happening
print('\nThis program comapres two positive integers entered by the user',\
      ' x and y.')
print('It then informs the user whether x is greater than, less than or',\
      'equal to y')

#get user inputs
x = int(input('Please enter a positive integer for x: '))
y = int(input('Please enter a positive integer for y: '))

print('\n') #skip a line

#compare the two values
if (x<y):
    print(x, 'is less than', y) #print if x is less than y
    
elif (x>y):
    print(x, 'is greater than', y) #print if x is greater than y
    
else:
    print(x, 'is equal to' , y) # otherwise they are equal