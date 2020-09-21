# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:40:33 2019

@author: Donal Murphy

Description: Histogram example given in Laboratory 9, slide 11
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.random(100)

plt.hist(data, bins = 10)

plt.show()