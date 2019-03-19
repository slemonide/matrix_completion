# -*- coding: utf-8 -*-

import numpy as np
from matrix_completion import svt_solve, calc_unobserved_rmse

U = np.random.randn(20, 5)
V = np.random.randn(15, 5)
R = np.random.randn(20, 15) + np.dot(U, V.T)

mask = np.round(np.random.rand(20, 15))
R_hat = svt_solve(R, mask)

print("RMSE:", calc_unobserved_rmse(U, V, R_hat, mask))