# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:12:10 2019

@author: Donal Murphy

Description: This program estimates the length of a semicircle.
"""

# This program divides the semicircle into n straight line segments and sums 
# these lengths to give an estimate of the actual length. For increasing values
# values of n, the estimate forms an asymptote that converges to the actual 
# value. This program inreases n by a factor of two until the difference 
# between the current estimate and the previous etimate are sufficienty small.  
#-----------------------------------------------------------------------------#
def f(x):
    # Evaluates f at x (i.e. evaluates y)
    return (1-(x**2))**(1/2)

def new_length(x,dx):
    # Calls function f() to calculate the length of each segment
    return ((((x+dx)-x)**2)+((f(x+dx)-f(x))**2))**(1/2)
#-----------------------------------------------------------------------------#

# Print the titles
print('\033[31m''{0:>18}'.format('n'), ' | ', \
      '{0:>18}'.format('length'), ' | ', \
      '{0:>18}'.format('length difference'),'\033[0m')

# Initialise variables outside while loop
n = 1           #number of intervals
c1_length = 0   #stores the previous length

# Loops until the desired length difference value is achieved
while True:

    # Initialise variables
    x_1, x_2 = -1, 1    # Start and end points
    dx = (x_2-x_1)/n    # change in x
    c2_length = 0       #stores current length
    
    #for a number of intervals, n, calcuates the length of each segment and the
    #sum total
    for i in range(0,n):
        
        x = x_1 + i*dx  #increases x in increments i*dx
        c2_length = c2_length + new_length(x, dx) #calls on function new_length
        
    diff = c2_length-c1_length #calculates the difference in lengths
    c1_length = c2_length #stores current length for next iteration
      
    #print the results 
    print('{0:>18}'.format(n), ' | ', \
          '{0:>18.7f}'.format(c2_length), ' | ', \
          '{0:>18.7f}'.format(diff))
    
    # Number of intervals increase by a factor of two, this is sufficiently
    # large to estimate quickly, not so large that there are too few results to
    # see the convergence
    n*=10

    
    #break out of the loop when the desired error is achieved
    if (diff < 1e-6):
        break