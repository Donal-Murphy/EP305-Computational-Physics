# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:38:55 2019

@author: Donal Murphy

Description: This program recieves 200 measurements (2 blocks) from a 
potentiometer sent by an arduino uno unit, along with their timestamps. It 
expresses the timestamps in seconds and the potentiometer values as a 
percentage of its full-scale. It then saves the results to a .txt file.
"""
import serial
from time import sleep

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

def file_write(filename,n,prt,baud):
    """
    Takes in n readings from blocks recieved from the serial port. 
    Converts the timestamp from milliseconds to seconds and the raw value to a 
    percentage of its max value. It then writes this data so a .txt file.
    """
    
    # Open a file for writing
    out_file = open(filename, 'w')
        
    with serial.Serial(port=prt, baudrate=baud, timeout=3) as myport:
        
        sleep(2)
              
        
        while (get_valid_line(myport) != 'START'):
            pass    #wait until we get the start tag
            
            for i in range(n):
                line = get_valid_line(myport)
                
                if line == 'START': # ignore any subsequent tags
                    line = myport.readline()
                
                stamp, val = [int(a) for a in line.split()]
                t_s = stamp/1e3
                p_val = (val/1023)*100
                print(t_s, ' ', p_val, file = out_file)
    # Close the file
    out_file.close()          


def main():

    file_name       = "EP305data56.txt"
    N               = 200
    serial_port     = 'COM3'
    serial_speed    = 19200
    
    file_write(file_name,N,serial_port,serial_speed)

