# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:52:08 2019

@author: Donal Murphy

Description: This program takes raw potentiometer values from an arduino unit
and converts them to a percentage of the maximum value. It first waits for a
'START' tag before taking N samples along with their timestamps, which are 
converted to seconds. It then saves th results to a .txt file.

"""
import numpy as np
import serial # required for receiving data from serial port
from time import sleep # required for setting delays

def get_valid_line(port):
    """
    Get one valid line from the serial port, ignoring any erroneous data
    """
    while True:
        try:
            # note in the case of serial port overflow some characters left in 
            # it decode will then throw an exception
            return port.readline().decode(encoding='ASCII').strip()
        
        except:
            pass # ignore the exception and try again with the next line
            
def get_data(N,port_name,port_speed):
   """
   Recieves a fixed number of data samples from the serial port. Converts 
   timestamp to seconds and expresses the raw input value as a percentage of 
   its maximum value (1023). Returns the time and percentage values as arrays
   t[] and percent[] respectively.
   """
   t        =   np.zeros(N)  # array for timestamps   
   percent  =   np.zeros(N)  # array for percentage values
   
   # get data from serial port
   with serial.Serial(port=port_name,baudrate=port_speed,timeout=2) as myport:
        
        sleep(2)    # allow arduino to reset itself
        
        while (get_valid_line(myport) != 'START'):
            pass    # wait until start tag is received
        
        # retrieve data
        for i in range(N):
            
            line = get_valid_line(myport)   # check for valid line
            
            if line == 'START': # ignore any subsequent tags
                line = myport.readline()
            
            stamp, val = [int(a) for a in line.split()] # seperate data
            t[i] = stamp/1e3 # convert to seconds
            percent[i] = (val/1023)*100 # convert to percentage of max 
        
   return t,percent 
            
def file_write(t,percent):
    """
    Writes the data to a .txt file
    """  
    
    file_name = "EP305data56.txt"
    
    # Open a file for writing
    out_file = open(file_name, 'w')
    
    # print headers
    print('{0:<10}'.format('Time(s)'),\
          '{0:<10}'.format('Output (%)'), file = out_file)
    
    # Write the values to the file
    #(fixed decimal point notation with 5 decimal places)
    for i in range (len(percent)):
        print('{0:<10.5f}'.format(t[i]),\
              '{0:<10.5f}'.format(percent[i]), file = out_file)
    
    # Close the file
    out_file.close()

def main():
    """
    Main function. Holds serial port settings and calls on get_data() and 
    file_write().
    """
    N           = 200       # number of samples
    port_name   = 'COM4'    # serial port name
    port_speed  = 19200     # serial port speed/ baudrate (bits per second)
    
    t,percent = get_data(N,port_name,port_speed) # get data
    file_write(t,percent)   # write data to file
main()