# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:19:15 2019

@author: root
"""

import numpy as np
import matplotlib.pyplot as plt

# Matrix is of the form:
# a b
# c d

NUM_SAMPLES = 10000

A = []
B = []
C = []
D = []

for i in range(NUM_SAMPLES):
    # pick a random matrix
    M = np.random.randn(2, 2)
    
    # make sure |s1| + |s2| <= 1
    M = M/np.linalg.norm(np.linalg.svd(M)[1],ord=1)
    
    A.append(M[0,0])
    B.append(M[0,1])
    C.append(M[1,0])
    D.append(M[1,1])

#plt.plot(A, C, '*')

      # A     B     C     D
fig, ((ax11, ax12, ax13, ax14),
      (ax21, ax22, ax23, ax24),
      (ax31, ax32, ax33, ax34),
      (ax41, ax42, ax43, ax44)) = plt.subplots(4, 4, sharex='col', sharey='row')

# First row
ax11.plot(A, A, '*')
ax11.set_title("A")
ax11.set_ylabel("A")

ax12.plot(A, B, '*')
ax12.set_title("B")

ax13.plot(A, C, '*')
ax13.set_title("C")

ax14.plot(A, D, '*')
ax14.set_title("D")

# Second row
ax21.plot(B, A, '*')
ax21.set_ylabel("B")
ax22.plot(B, B, '*')
ax23.plot(B, C, '*')
ax24.plot(B, D, '*')

# Third row
ax31.plot(C, A, '*')
ax31.set_ylabel("C")
ax32.plot(C, B, '*')
ax33.plot(C, C, '*')
ax34.plot(C, D, '*')

# Fourth row
ax41.plot(D, A, '*')
ax41.set_ylabel("B")
ax42.plot(D, B, '*')
ax43.plot(D, C, '*')
ax44.plot(D, D, '*')