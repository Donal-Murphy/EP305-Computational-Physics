# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:49:59 2019

@author: Donal Murphy

Description: This program uses the data from sunspots.txt to calculate the 
mean, median, mode and standard deviation of the sunspot data from 1749 to
2010. 

NOTE: This program includes many user defined functions of identical purpose
      to functions included in some python libraries, but i wanted to try
      coding them myself. A comparison of the two is given in the output.
      
"""

import numpy as np       #Needed for many standard functions
import matplotlib.pyplot as plt    #Needed for plotting
import statistics as stat    #Needed for statistical functions

def py_stats(data):
    """
    Uses python statistics library to calculate accurate statistical values
    for the mean, median, mode and standard deviation of the data array 
    provided.
    """
    py_mean = stat.mean(data)       #Calculates the mean
    py_median = stat.median(data)   #Calculates the median
    py_mode = stat.mode(data)       #Calculates the mode
    py_sd = stat.stdev(data)        #Calculates the standard deiation
    
    return py_mean, py_median, py_mode, py_sd

def usr_mean(data):
    """
    User defined function that calculates and returns the mean of the data 
    array provided.
    """
    data_mean = sum(data)/len(data) #Calculates the mean
    
    return data_mean

def usr_median(data):
    """
    User defined function that calculates and returns the median of the data 
    array provided.
    """
    data.sort()     #Sort the data in ascending order
    
    #For even number of entries
    if (len(data)%2==0):
        a = len(data)/2
        b = (len(data)+1)/2
        data_median = data[int((a+b)/2)] #Calculates the median
    
    #For odd number of entries
    else:
        data_median = data[int((len(data)+1)/2)] #Calculates the median
        
    return data_median

def usr_mode(data):
    """
    User defined function that calculates and returns the mode of the data 
    array provided.
    """
    n=0             #Value being searched for through array 
    count_max = 0   #Holds the number of occurences
    my_mode = 0     #Reports the value with the most occurences
    
    while (n<=max(data)):
        count = 0
        
        for i in range(0,len(data)):
        #checks for n in each element
            if (data[i] == n):
                count += 1 #Increase count for every occurence of n
        
        if count > count_max:
            count_max = count
            my_mode = n
        
        n += 0.1 #Increment n
    
    return my_mode

def usr_sd(data,mean):
    """
    User defined function that calculates and returns the standard deviaton 
    of the data array and mean provided .
    """
    
    sigma_1 = sum((data-mean)**2)      
    sigma_2 = len(data)
    s_d = (sigma_1/sigma_2)**(1/2) #Calculates the standard deiation
    
    return s_d

def error(py_ans,my_ans):
    """
    User defined function that calculates the % error in the user defined 
    function result by comparing it with the python function result.
    """
    if py_ans == 0: #Prevents dividing by zero
        error = 0
    else:
        error = (abs(py_ans-my_ans)/py_ans)*100 #Calculates the % error
    
    return error

def create_array(txt_file):
    """
    User defined function that reads in two columns of data from a .txt file 
    and converts them to arrays.
    """
    data = np.loadtxt(txt_file,float) #Read in data from file as float
    col_1 = data[:,0] #Creates array from first column of data
    col_2 = data[:,1] #Creates array from second column of data
    
    return col_1,col_2

def main():   
    """
    Requests filename from user.Calls on py_stats(), usr_mean(), usr_median(), 
    usr_mode(), usr_sd(), error() and prints the results to a table. 
    It then plots the data on a histogram.
    """
    valid = None
    
    #Search for filename matching user input filename
    while (valid == None):
    
        txt_file = str(input('Please enter the name of the data file ' \
                             'followed by the file extention' \
                             '(e.g. sunspots.txt): '))
        
        try:
            month_array,freq_array = create_array(txt_file)
        
        except:
            print('\033[31m'"\nERROR: filename '" + txt_file + \
                  "' could not be found"'\033[0m')
            
        else:
            print('\nPlease wait...')
            valid = 1
    
    #Call on functions to calculate results
    py_mean, py_median, py_mode, py_sd = py_stats(freq_array)
    my_mean = usr_mean(freq_array)
    my_median = usr_median(freq_array)
    my_mode = usr_mode(freq_array)
    my_sd = usr_sd(freq_array,my_mean)
    
    #Print table headers
    print('\n', \
          '\033[31m''{0:>20}'.format(' '), \
          '{0:>18}'.format('Python Function'), \
          '{0:>18}'.format('My Function'), \
          '{0:>18}'.format('% Error'),'\033[0m')
    
    #Print table entries    
    print('\033[34m''{0:>20}'.format('Mean:'),'\033[0m', \
          '{0:>18.1f}'.format(py_mean), \
          '{0:>18.1f}'.format(my_mean), \
          '{0:>18.1g}'.format(error(py_mean,my_mean)))
    print('\033[34m''{0:>20}'.format('Median:'),'\033[0m', \
          '{0:>18.1f}'.format(py_median), \
          '{0:>18.1f}'.format(my_median), \
          '{0:>18.1g}'.format(error(py_median,my_median)))
    print('\033[34m''{0:>20}'.format('Mode:'),'\033[0m', \
          '{0:>18.1f}'.format(py_mode), \
          '{0:>18.1f}'.format(my_mode), \
          '{0:>18.1f}'.format(error(py_mode,my_mode)))
    print('\033[34m''{0:>20}'.format('Standard Deviation:'),'\033[0m', \
          '{0:>18.1f}'.format(py_sd), \
          '{0:>18.1f}'.format(my_sd), \
          '{0:>18.1g}'.format(error(py_sd,my_sd)))
    
    #Plot histogram
    plt.hist(freq_array,bins=40)
    plt.title('Sunspot Distribution (1749-2010)',fontsize=18,color='r')
    plt.xlabel('Sunspots/Month', fontsize = 14)
    plt.ylabel('Frequency', fontsize = 14)
    plt.grid(True)
    plt.show()

#Inform the user what is happening and wait for input 
ans = None

while ans == None:
    print('\033[31m''\nThis program takes two columns of data from a .txt ', \
          'file and calculates the mean median mode and standard deviation ', \
          'using user defined functions and python statistics library', \
          'functions. It then prints the data on a histogram.','\033[0m')
    print('\n')
    print("Press 'Enter' to continue...")
    
    ans = input()
    
main()

    