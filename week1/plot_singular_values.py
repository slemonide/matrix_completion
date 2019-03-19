# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:57:27 2019

@author: Danil
"""

import numpy as np
import matplotlib.pyplot as plt

s1 = np.array([0, 1, 0, -1, 0])
s2 = np.array([1, 0, -1, 0, 1])

theta = 0

det = np.sqrt((s2-s1)**2 + 1 + 2*np.cos(2*theta)*(s2-s1))
t1 = 1/2*(s1 + s2 - 1 + det)
t2 = 1/2*(s1 + s2 - 1 - det)

plt.plot(t1, t2)