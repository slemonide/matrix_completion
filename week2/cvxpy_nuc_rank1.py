#!/usr/bin/env python3

#print("test")

from cvxpy import *
import numpy as np

n = 4
unknowns = 5
rank = 1

#mu = 0.001

U = np.random.randn(n, rank)
V = np.random.randn(n, rank)

original = np.dot(U, V.T)

print(original)

mask = np.array([0] * unknowns + [1] * (n*n - unknowns))
np.random.shuffle(mask)
mask = np.reshape(mask, [n, n])
mask = np.ma.make_mask(mask)

print(mask)

A = original
X = Variable(shape=A.shape)
#objective = Minimize(mu * norm(X, "nuc") + sum_squares(multiply(mask, X-A)))
objective = Minimize(norm(X, "nuc"))
constraints = [X[mask] == A]

#problem = Problem(objective, [])
problem = Problem(objective, constraints)
problem.solve(solver=SCS)

solution = X.value

print("solution\n",solution)

print("solution - original\n",solution - original)

print('\n')
print(np.linalg.norm(solution - original))
