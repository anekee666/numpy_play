import numpy as np
A = np.array([1,2,3])
for e in A:
  print(e)
print(A + np.array([4])) #array([5, 6, 7])
print(A + np.array([4,5,6])) #array([5, 7, 9])
print(2 * A) #array([2, 4, 6])
print(A**2) #array([1, 4, 9])
print(np.sqrt(A))
print(np.log(A))
print(np.exp(A))
print(np.tanh(A))
# by the way, this works with Numpy too
A = np.arange(10)
print(A)
print(A[A % 2 == 0])