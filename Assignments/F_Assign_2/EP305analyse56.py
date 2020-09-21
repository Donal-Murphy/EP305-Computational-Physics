# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:48:05 2019

@author: Donal Murphy

Description: This program takes percentage values and timestaps from a .txt
file.
It calculates the mean, median, mode and standard deviation of the data from 
the sensor.  
It calculates the number of sensor readings thatare in the lowest 4%, 4-8%, 
8-12%,...92-96%, and the upper 4% of the data stored.
It then determines the times at which the minimum and maximum occur.
It plots a graph of % value against time and prints a summary of all results.  
"""
import numpy as np # Required for arrays
import statistics as stat # required for mean, median, mode, standard deviation 
import matplotlib.pyplot as plt    # required for plotting

def file_read(file_name):
    """
    Reads in data from text file
    """
    
    # Open a file for reading
    in_file = open(file_name, 'r')
    
    # Create two empty arrays for appending later
    time = []
    percent = []

    in_file.readline() # Read in the header seperately
    
    
    for line in in_file:
        values = line.split()   # Read data from each line in list
        time.append(float(values[0])) # Column 1 convert to float
        percent.append(float(values[1])) # Column 2 convert to float
           
    in_file.close() #Close the file
    
    return time, percent

def get_stats(data):
    """
    Returns the mean, median, mode and standard deviation of the data array
    provided.
    """
    data_mean = stat.mean(data)       #Calculates the mean
    data_median = stat.median(data)   #Calculates the median
    data_mode = stat.mode(data)       #Calculates the mode
    data_sd = stat.stdev(data)        #Calculates the standard deiation
    
    return data_mean, data_median, data_mode, data_sd

def sort_data(data):
    """
    Sorts the data into ranges of 4% (Lowest 0-4%,4-8% etc) of the data array
    provided and counts the number of values in that range. 
    It then prints the results.
    """
    percent_range = 0.04*(max(data)-min(data)) # 4% of the range of data
    p_lower = min(data) # start the lower range at zero
    
    
    # print headers in red
    print('\033[31m\n')
    print('{0:<12}'.format('Percentile'),\
          '{0:<9}'.format('Frequency\033[0m'))
    
    # count the number of values in every 4% range
    for n in range(25):
        
        count = 0 # stores the number of occurences in each range
        p_upper = p_lower + percent_range # upper range is + 4% of lower range
        
        # search through every element in array
        for i in range(len(data)):
            
            # check 0-4% including 0
            if (n == 0) and (data[i]<=p_upper):
                count += 1 # if i in range, count +1
            
            # check all other ranges up tp 100% (upper range inclusive)
            elif (p_lower<data[i]) and (data[i] <= p_upper):
                count += 1# if i in range count +1
            
        p_lower += percent_range # increase lower range by 4%
        # print results
        print('{0:.<15}'.format(str(4*n)+'-'+str((n+1)*4)+'%'),\
              '{0:<6}'.format(count)) 
    
def min_max(data,time):
    """
    Returns the minimum and maximum values of the data provied, as well as the
    time in which they occur.
    """
    
    min_val = min(data) # get the min value
    min_index = np.argmin(data) # get index at which min occurs
    min_time = time[min_index]   # get time at which min occurs
    
    max_val = max(data) # get the max value
    max_index = np.argmax(data)  # get index at which max occurs
    max_time = time[max_index]   # get time at which max occurs
    
    return min_val, min_time, max_val, max_time

def plot_data(x,y,mean,median,mode,sd):
    """
    Plots a graph of y against x along with statistical data.
    """
    plt.plot(x,y, 'r', label = '')  # plot data, red line
    plt.title('Potentiometer Readings',fontsize = 20, color = 'b') #graph title
    plt.xlabel('Time (s)', fontsize = 14)   # x-axis title
    plt.ylabel('Potentiometer Output (%)', fontsize = 14)  # y-axis title
    plt.axis([0,max(x),0,100]) #range of x- and y-axes
    # print stat data
    plt.text(3.5,78,
             'mean = '+str('{0:.1f}'.format(mean))\
             +'\nMedian = '+str('{0:.1f}'.format(median))\
             + '\nMode = '+str('{0:.1f}'.format(mode))\
             +'\nS.D. = '+str('{0:.1f}'.format(sd)))
    plt.show()  # print graph
    
def main():

    input('This program graphs values obtained from and arduino unit and'\
          'obtains statistical data on the recorded values.'\
          '\n\nPress Enter to continue...')
    
    time,percent = file_read("EP305data56.txt") # retrieve data from .txt file
    mean,median,mode,sd = get_stats(percent)    # retrieve statistical data
    plot_data(time,percent,mean,median,mode,sd) # plot graph
    sort_data(percent)
    min_val, min_time, max_val, max_time = min_max(percent,time)

    
    print('\033[31m\nSummary of Statistical Data:\033[0m',\
          '\nMean = '+str('{0:.5f}'.format(mean)),\
          '\nMedian = '+str('{0:.5f}'.format(mode)),\
          '\nMode = '+str('{0:.5f}'.format(mode)),\
          '\nStandard Deviation = '+str('{0:.5f}'.format(sd)))
    print('\n')
    print('The minimum value was '+str(min_val)+'% which occured at '\
          +str(min_time)+'seconds.',\
          'The maximum value was '+str(max_val)+'% which occured at '\
          +str(max_time)+'seconds.')
    print('\nWould you like to try again? y/n: ')


while True:
    main()
    ans = input()
    if ans =='n':
        break
    elif ans == 'y':
        pass
    else:
        print('\nNot a valid answer. Please run the program again.')
        break
        
print('END')