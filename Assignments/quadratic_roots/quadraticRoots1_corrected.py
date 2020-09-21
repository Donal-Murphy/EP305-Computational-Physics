# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:23:35 2019

@author: Donal Murphy
Python ver3.7, Spyder v3.3.3
*******************************************************************************
NOTE: I recently had to reinstall Anaconda and thus I am running a more up
to date version of spyder. As a result, I think that it handles imaginary
numbers differently as it calculates imaginary roots without any dedicated
code.
******************************************************************************* 

Description: returns the roots to a quadratic equation
"""

#this program calculates the roots of a quadratic of the form:
#Ax^2 + Bx + C = 0

#inform the user what is happening
print('\nThis program calculates the roots of a quadratic of the form \
      Ax\xb2+Bx+C=0 \
      \nIt uses 2 USER DEFINED functions.')
#-----------------------------------------------------------------------------#
#define the two root functions
def root_1(a_value,b_value,c_value):
    #positive -b formula
    return((-b_value + (b_value**2 - 4*a_value*c_value)**(1/2))) / (2*a_value)
    
def root_2(a_value,b_value,c_value):
    #negative -b formula
    return((-b_value - (b_value**2 - 4*a_value*c_value)**(1/2))) / (2*a_value)
#-----------------------------------------------------------------------------#
    
ans = 'Y' #use the program at least once
while ans == 'Y':
    #prompt the user for the coefficients
    A = float(input('\nEnter the first coefficient, A (e.g. 2.0): '))
    B = float(input('\nEnter the second coefficient, B (e.g. 2.0): '))
    C = float(input('\nEnter the third coefficient, C (e.g. 2.0): '))
    
    #call the functions root_1() and root_2()
    r_1 = root_1(A,B,C)
    r_2 = root_2(A,B,C)
    
    #output the results
    print('\nThe roots of the quadratic are:', \
          '{0:.3f}'.format(r_1), ' and ', '{0:.3f}'.format(r_2))
    
    ans = input('\nDo you want to try another quadratic? (Y/N) ')
    
if ans == 'N':
    print('\nEnd.')