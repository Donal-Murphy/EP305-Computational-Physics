# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:24:07 2019

@author: Donal Murphy

Description:
"""

import serial
from time import sleep

with serial.Serial('COM4', baudrate=115200, timeout=2) as myport:
    sleep(2) # need this to allow arduino to reset itself after a serial change
    myport.write(b'10\n')
    for i in range(10):
        print(myport.readline())