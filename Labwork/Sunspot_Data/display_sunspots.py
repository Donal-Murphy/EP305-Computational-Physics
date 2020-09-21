# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:00:55 2019

@author: Donal Murphy

Description: This program plots the cycle of sunspots from 1750 to 2010.
"""

import numpy as np       #Needed for many standard functions
import matplotlib.pyplot as plt    #Needed for plotting

data = np.loadtxt( "sunspots.txt",float)
x = data[:,0]
y = data[:,1]

xyr = 1749 + (x/12)

plt.scatter(xyr,y,s=10,marker=2,linewidths=1)
plt.xlabel("year")
plt.ylabel("sunspot number")
plt.xlim(1950,max(xyr))
plt.ylim(-5,max(y))
plt.show()
