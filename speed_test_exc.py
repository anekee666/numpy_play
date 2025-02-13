## speed comparison ##
import numpy as np
from datetime import datetime

# note: you can also use %timeit
T = 100000

def slow_matrix_dot_product(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Ensure matrices are compatible for multiplication
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must match number of rows in B")

    # Initialize result matrix with zeros
    result = [[0] * cols_B for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):  # Iterate over rows of A
        for j in range(cols_B):  # Iterate over columns of B
            for k in range(cols_A):  # Iterate over elements in row A and column B
                result[i][j] += A[i][k] * B[k][j]

    return result



a = np.random.randn(2,2)
b = np.random.randn(2,2)
print(np.allclose(a.dot(b),slow_matrix_dot_product(a,b)))





t0 = datetime.now()
for t in range(T):
  slow_matrix_dot_product(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
  a.dot(b)
dt2 = datetime.now() - t0

print("dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds())