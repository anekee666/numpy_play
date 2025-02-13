import numpy as np

A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
print(np.linalg.solve(A, b))
# don't do this
print(np.linalg.inv(A).dot(b))