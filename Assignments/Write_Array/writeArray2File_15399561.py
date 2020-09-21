# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:11:30 2019

@author: Donal Murphy

Description: This program reads user input data for a simple pendulum, writes 
it to a file, retrieves the data from the file and reprints it to the screen.
"""

import numpy as np #Required for arrays

def get_data():
"""
Creates arrays sp_length and sp_period of size 10 and assigns each element 
based on user input.
"""
    n = 10  #Length of arrays
    sp_length_v1 = np.empty((n)) #Empty array
    sp_period_v1 = np.empty((n)) #Empty array
    print('\n')
    
    #Assigns user input value to each element of the array
    for i in range (n):
        print('Enter \033[34mlength\033[0m [', i, '] in cm (float): ',end = '')
        sp_length_v1[i] = float(input())
        print('Enter \033[32mperiod\033[0m [', i, '] in seconds (float): ', \
              end = '')
        sp_period_v1[i] = float(input())
        
    return sp_length_v1,sp_period_v1 #Return arrays to main


def print_data(sp_length,sp_period):
"""
Prints the data to a table in python.
"""   
    # Print table headers
    print('\n{0:>15}'.format('index'), \
          '{0:>15}'.format('length (cm)'), \
          '{0:>15}'.format('period (s)'))
    
    # Print data
    for i in range (len(sp_length)):
        print('{0:>15}'.format(i), \
              '{0:>15.3f}'.format(sp_length[i]), \
              '{0:>15.3f}'.format(sp_period[i]))


def file_write(sp_length,sp_period):
"""
Writes the file to a .txt file
"""  
    
    file_name = "pendulum.txt"
    
    # Open a file for writing
    out_file = open(file_name, 'w')
    print('{0:>15}'.format('index'), \
          '{0:>15}'.format('length (cm)'), \
          '{0:>15}'.format('period (s)'), file = out_file)
    
    # Write the values to the file
    for i in range (len(sp_length)):
        print('{0:>15}'.format(i), \
              '{0:>15.3f}'.format(sp_length[i]), \
              '{0:>15.3f}'.format(sp_period[i]), file = out_file)
    
    # Close the file
    out_file.close()


def file_read():
"""
Reads in data from text file
"""
    file_name = "pendulum.txt"
    
    # Open a file for reading
    in_file = open(file_name, 'r')
    
    # Create two empty arrays for appending later
    sp_length_v2 = []
    sp_period_v2 = []

    in_file.readline() # Read in the header seperately
    
    
    for line in in_file:
        values = line.split()   # Read data from each line in list
        sp_length_v2.append(float(values[1])) # Column 2 convert to float
        sp_period_v2.append(float(values[2])) # Column 3 convert to float
           
    in_file.close() #Close the file
    
    return sp_length_v2,sp_period_v2 #Return arrays to main
    


def main():
"""
Main program. Informs the user and calls on get_data(), print_data(), 
file_write & file_read.
"""       
    print('This program reads in simple pendulum data, prints the data and ', \
          'writes it to a file before reading from the file and printing ', \
          'the retrieved data')
    
    sp_length_v1, sp_period_v1 = get_data() #Retrieve arrays from get_data  
    
    print('\nThe data \033[31mread from the keyboard\033[0m shown below:')
    print_data(sp_length_v1,sp_period_v1)   #Pass the arrays to print_data
    
    file_write(sp_length_v1,sp_period_v1)   #Pass the arrays to file_write
    sp_length_v2,sp_period_v2 = file_read() #Retrieve new arrays from file_read
    
    print('\nThe data \033[35mretrieved from the file\033[0m shown below:')
    print_data(sp_length_v2,sp_period_v2) #Pass the new arrays to priny_data
 
ans = 'y'
#Ask the user if they would like to run the program again
while ans == 'y':
    main()
    ans = input('Would you like to try again? y/n: ')


    

     
