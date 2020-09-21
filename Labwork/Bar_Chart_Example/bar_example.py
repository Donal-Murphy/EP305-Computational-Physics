# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:13:49 2019

@author: Donal Murphy

Description: Example for plotting a bar chart from Laboratory 9, slide 10 
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np       
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos,performance, align='center',alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()