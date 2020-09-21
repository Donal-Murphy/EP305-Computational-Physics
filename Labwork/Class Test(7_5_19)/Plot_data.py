# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:11:01 2019

@author: Donal Murphy

Description:
"""

import numpy as np #Required for arrays
import statistics as stat # Required for calculating mean
import matplotlib.pyplot as plt # Required for plotting data

def file_read():
    """
    Reads in data from text file
    """
    file_name = "EP305_test_data.txt"
    
    # Open a file for reading
    in_file = open(file_name, 'r')
    
    # Create two empty arrays for appending later
    x_i = []
    y_i = []

    line_1 = in_file.readline() # Read in the header seperately
    headers = line_1.split()    # Split the headers
    header_1,header_2 = headers[0],headers[1] # Store the headers
    
    
    for line in in_file:
        values = line.split()   # Read data from each line in list
        x_i.append(float(values[0])) # Column 1 convert to float
        y_i.append(float(values[1])) # Column 2 convert to float
           
    in_file.close() #Close the file
    
    return x_i, y_i, header_1, header_2 #Return arrays and headers to main

def graph_data(x_data,y_data):
    """
    Plots the data on a graph using red '+' markers with no line and an x
    and y range of 0-105.
    """
    plt.plot(x_data,y_data,'r+')    # ploy data using red '+' markers
    plt.title('EP305 Test Data',fontsize = 22,color = 'r')    # graph title
    plt.xlabel('x-data',fontsize = 20)  # label x-axis, fontsize 20
    plt.ylabel('y-data',fontsize = 20)  # label y-axis, fontsize 20
    plt.axis([0,105,0,105]) # range of both axes is 0-105
    plt.show()  # print graph


def covar(array_1,array_2):
    """
    Returns the covariance of 2 arrays using the mean of each array and the
    covariance formula.
    """
    
    n = len(array_1)    # number of elements in arrays (no. in 1[] = no in 2[])
    
    # calculate the mean of each array using python statistics library
    mean_1,mean_2 = stat.mean(array_1),stat.mean(array_2) 
    
    sigma = 0   # stores the sum
    
    for i in range(n):
        # add to the sum each element of the covariance formula summation
        sigma += (array_1[i]-mean_1)*(array_2[i]-mean_2)
        
    cov = (1/n)*sigma # caclulate the covarince
    
    return cov

def correl(array_1,array_2):
    """
    Returns the coefficient of linear correlation (r) of 2 given arrays using 
    the mean of the arrays.
    """
    n = len(array_1)    # number of elements in arrays (no. in 1[] = no in 2[])
    
    # calculate the mean of each array using python statistics library    
    mean_1,mean_2 = stat.mean(array_1),stat.mean(array_2)
    
    sigma_1 = 0 # stores the summation of bracket containing xs in r-formula  
    sigma_2 = 0 # stores the summation of bracket containing ys in r-formula
    sigma_3 = 0 # stores the summation of the products in r-formula 
    
    for i in range(n):
        # calulate the summation of bracket containing xs in r-formula
        sigma_1 += (array_1[i]-mean_1)**2
        # calculate the summation of bracket containing ys in r-formula
        sigma_2 += (array_2[i]-mean_2)**2
        # calculate the summation of the products in r-formula
        sigma_3 += (array_1[i]-mean_1)*(array_2[i]-mean_2)
        
    cor = sigma_3/((sigma_1)*(sigma_2**2))**(1/2) # r-formula
    
    
    return cor

def table(col_1,col_2,title_1,title_2,covar,correl):
    """
    Prints the data in a table. 
    """
    print('\n') # leave a blank line
    
    # print headers in red
    print('\033[31m',
          '{0:>14}'.format(title_1),\
          '{0:>14}'.format(title_2),\
          '\033[0m')
    
    # print data
    for i in range(len(col_1)):
        print('{0:>14}'.format(col_1[i]),\
              '{0:>14}'.format(col_2[i]))
    print('\n')    
    print('The covariance of the data is:', covar)
    print('The coefficient of linear correlation of the data is:',\
          correl)

def main():
    """
    Uses 2 arrays x and y to retain data obtained using file_read(). 
    Passes this data to graph_data(). Retrieves the covariance and coefficient
    of linear correlation of the data using covar() and correl() respectively.
    Passes this data to table().
    """
    
    x,y,x_title,y_title = file_read() # store data and headers
    graph_data(x,y) # plot a graph of the data
    covariance =covar(x,y)  # obtain the covariance
    r = correl(x,y) # obtain the coefficient of linear correlation
    table(x,y,x_title,y_title,covariance,r) # print the data
    
ans = 'y'
while ans == 'y':
    
    # inform the user what is happening
    print('This program retrieves data from EP305_test_data.txt and plots it',\
          'on a graph.',\
          '\nIt then prints the data on a table and calulates the covariance and',\
          'coefficient of linear correlation of the data.')
    
    prompt = 'none'
    while prompt == 'none':
        prompt = input(print('\nPress any key to continue'))
    
    main()
    
    ans = input(print('\nWould you like to try again? y/n: '))
    
    
    

    