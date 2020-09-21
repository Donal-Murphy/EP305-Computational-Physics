# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:28:04 2019

This program converts degrees centigrade to fahrenheit and comments on the
temperature.
It terminates if the user enters a neative number or a number over 100.

@author: Donal Murphy
"""
#inform the user what is happening
print('This program accepts a temperature in degrees centigrade entered' \
      'by the user.')
print('It then prints this temperature in Fahrenheit and makes a comment.')
print('This program will terminate if the user enters a temperature outside' \
      'the range 0-100.')

celsius = 0.0 # initialize the temperature variable

# repeat the program so long as the temperature is between 1-100 C
while ((celsius >= 0.0) and (celsius <= 100.0) ):
    
    # get user input
    celsius = float(input('\nPlease enter a temperature in' \
                          'degrees centigrade: '))
    
    # convert the temperature
    fahr = (9.0/5.0)* celsius + 32.0
    
    # print the result
    print('\n') # empty line
    print(celsius, 'degrees centigrade =', fahr, 'degrees Fahrenheit.')
    
    # if temperature is between 32-100C print message in red
    if((celsius > 32.0) and (celsius < 100.0)):
        print('\033[31mThe temperature is rather warm.\033[0m')
    
    # if temperature is between 0C and 59F print msg in blue   
    elif((fahr <= 59.0) and (celsius > 0.0)):
        print( '\033[34mThe temperature is quite cool.\033[0m')
    
    # otherwise print message in green    
    else:
        print('\033[32mThe temperature is comfortable.\033[0m')

# terminate the program if temperature is outside 0-100C        
else:
    print('\n')
    print(celsius, 'is outside this programs temperature range.' \
          '\nThis program will now terminate.')
    