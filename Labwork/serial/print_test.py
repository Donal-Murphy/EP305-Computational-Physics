# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:14:54 2019

@author: Donal Murphy

Description:
"""

import serial
with serial.Serial('COM4', baudrate=115200, timeout=2) as myport:
    print(myport.baudrate)
    print(myport.is_open)