# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:23:47 2019

@author: Donal Murphy

Description: This program takes 100 average temperature readings from and
arduino unit using an LM35 sensor and plots the readings on a graph. 
"""

import serial # needed to take data from serial port
import numpy as np # needed for arrays
import matplotlib.pyplot as plt # needed to plot graphs
from time import sleep # needed for delay before initiating data reading
            
def get_data(prt,bps,N):
    """
    Recieves data from the device and assigns each value to an element 
    in an array of size N. Also creates an array for time in 
    """
    
    data = np.empty(N, dtype=float) # empty array to take values
    sleep(2) # wait 2 ms
    
    with serial.Serial(port=prt, baudrate=bps, timeout=2) as myport:
        
        # decode as ASCII and strip NL eetc.
        #line = myport.readline().decode(encoding='ASCII').strip()
        
        for i in range(N):
            # add value to data array if line is valid
            try:
                line = myport.readline()
                data[i] = float(line)
            
            # ignore errors
            except:
                i -= 1
                pass
        
        return data

def plot_data(x,y):
    """
    Plots arrays of data y[] against x[] on a line graph.
    """
    plt.plot(x,y, 'r--')
    plt.xlabel('time (ms)', fontsize = 18)
    plt.ylabel('Degrees Celsius', fontsize = 18)
    plt.axis([0,100,22,23])
    plt.show()

def main():
    
    prt = 'COM4' # port number
    bps = 38400 # baudrate
    N = 100     # number of samples
    
    t_ms = np.arange(0.0,N) # array of time in milliseconds
    data = get_data(prt,bps,N) # array of temperature readings in degrees C
    plot_data(t_ms,data)

main()

        