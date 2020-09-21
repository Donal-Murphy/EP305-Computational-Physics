# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:46:11 2019

@author: Donal Murphy

Description:
"""

import serial
import numpy as np

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
            
N = 1000
t = np.empty(N)
data = np.empty(N)

with serial.Serial(port='COM4', baudrate=115200, timeout=2) as myport:
    
    while (get_valid_line(myport) != 'BLOCK'):
        pass    #wait until we get the start tag
        
        for i in range(N):
            line = get_valid_line(myport)
            if line == 'BLOCK': # ignore any subsequent tags
                line = myport.readline()
            stamp, val = [int(a) for a in line.split()]
            t[i] = stamp*1e6 # convert to seconds
            data[i] = 22.0*(1023-val)/val #convert the ldr raw reading