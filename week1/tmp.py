# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:04:41 2019

@author: root
"""

import numpy as np
import matplotlib.pyplot as plt

b = np.random.randn(1, 5)
M = np.random.randn(5, 5)
[Q,R] = np.linalg.qr(M)

