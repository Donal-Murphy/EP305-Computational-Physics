# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:22:33 2019

@author: Donal Murphy

Description: This program evaluates, for a positive integer n in the range 
[0,100], the sum, the exponentials, the factorials and the natural logarithm 
of the factorials of all integers from 0 to n.
"""

#import math library for exponentials, logarithms and factorials
import math

#inform the user what is happening
print('\nThis program produces a table of n, sum(n), exp(n), n! and ln(n!) '\
      'where n is an integer in the range [1,100] entered by the user.')

#request variable 'n' from user
n = int(input('Please enter a positive integer n (0<=n<=100): '))

#if n is outside range, request new n
while (n<1) or (n>100):
    print('\n\aThat is not a valid n.')
    n = int(input('Please enter a positive integer n (1<=n<=100): '))

#executes if n is in range
else:
    
    #initialize table headings
    title1 = 'n'
    title2 = 'sum(0..n)'
    title3 = 'exp(n)'
    title4 = 'n!'
    title5 = 'ln(n!)'
    
    #print table headings in red, fixed format
    print('\n\033[31m{0:>8}'.format(title1), \
          '{0:>10}'.format(title2), \
          '{0:>18}'.format(title3), \
          '{0:>20}'.format(title4), \
          '{0:>10}\033[0m'.format(title5))
    
    count = 0 #initialize a variable 'count' used for sum(0..n)
    
    for i in range(0,n+1):
        count = count + i           #sum(0..n)
        fact = math.factorial(i)    #n!
        e = math.exp(i)             #exp(n)
        ln = math.log(fact)         #ln(n!)
        
        #print table contents, fixed format
        print('{0:>8}'.format(i), \
              '{0:>10.3f}'.format(count), \
              '{0:>18.3f}'.format(e), \
              '{0:>20d}'.format(fact), \
              '{0:>10d}'.format(round(ln)))