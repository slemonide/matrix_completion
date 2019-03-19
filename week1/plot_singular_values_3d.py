# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:57:27 2019

@author: Danil
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

s1 = np.array([0, 1,  0, -1, 0])
s2 = np.array([1, 0, -1,  0, 1])
t0  = np.array([1, 1,  1,  1, 1])

NUM = 50

T1  = [] # first singular value
T2  = [] # second singular value
ANG = [] # angle

for theta in np.linspace(-np.pi/4,np.pi/4,NUM):

    det = np.sqrt((s2-s1)**2 + 1 + 2*np.cos(2*theta)*(s2-s1))
    t1 = 1/2*(s1 + s2 - 1 + det)
    t2 = 1/2*(s1 + s2 - 1 - det)
    a = t0*theta
    
    T1.append(t1)
    T2.append(t2)
    ANG.append(a)



ax.plot_wireframe(np.array(T1), np.array(T2), np.array(ANG))
ax.set_xlabel("t1", fontsize=20)
ax.set_ylabel("t2", fontsize=20)
ax.set_zlabel("angle", fontsize=20)
plt.title("Descent cone for symmetric matrices", fontsize=20)