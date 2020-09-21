# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:21:12 2019

@author: Donal Murphy

Description: Plots sin(x) from 0 to 2pi
"""

import numpy as np       
import matplotlib.pyplot as plt

n = 0.001
x = np.arange(0,2*np.pi,n)
y = np.sin(x)
y_0 = x-x

plt.plot(x,y, 'r--', label = 'sin(x)')
plt.plot(x,y_0,'k')
plt.xlabel('x', fontsize = 18)
plt.ylabel('f(x)', fontsize = 18)
plt.axis([0,2*np.pi,-1.2,1.2])
plt.legend()
plt.show()

