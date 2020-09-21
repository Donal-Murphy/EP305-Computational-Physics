# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:28:58 2019

@author: Donal Murphy

Description:
"""

import numpy as np
import serial
from time import sleep

N = 10 # numberof samples
data = np.empty(N, dtype=int) # empty array to take values

with serial.Serial('COM4', baudrate=115200, timeout=2) as myport:
    
    sleep(2) # need this to allow arduino to reset itself after a serial change
    
    # format string to encode as ASCII
    message = '{}\n'.format(N).encode(encoding='ascii')
    myport.write(message)   # send to arduino
    
    for i in range(N):      # read response one line at a time
        message = myport.readline() # read raw line
        
        # decode as ASCII and strip NL eetc.
        line = message.decode(encoding='ascii').strip()
        data[i] = int(line)

print(len(data), data)