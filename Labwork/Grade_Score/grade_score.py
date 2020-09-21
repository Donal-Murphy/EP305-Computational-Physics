# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:52:04 2019

This program provides a user with a grade based on the percentage mark entered
by the user.
It then prints the result

@author: donal
"""
#inform the user what is happening
print('\nThis program accepts an exam mark (0-100%) entered by the user.')
print('It then prints the grade associated with this mark.')
print('This program will end if the user enters a mark outside the range',\
      '0-100.')

x = 0 #initialize the mark, x

while ((x >= 0) and (x <= 100)):

#get user input
    x = int(input('\nPlease enter the percentage mark recieved: '))

#assign a grade based on user input   
    if ((x >= 85) and (x <= 100)):
        print('A mark of', x, '% equals an A-grade.')
        
    if ((x >= 70) and (x < 85)):
        print('A mark of', x , '% equals a B-grade.')
        
    if ((x >= 55) and (x < 70)):
        print('A mark of', x , '% equals a C-grade.')
    
    if ((x >= 40) and (x < 55)):
        print('A mark of', x , '% equals a D-grade.')
        
    if ((x >= 0) and (x < 40)):
        print('A mark of', x , '% equals a E-grade.')
        
else:
    print(x, '% is not a valid grade. This program will now terminate.')