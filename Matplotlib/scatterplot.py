import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(100, 2)
plt.scatter(X[:,0], X[:,1])
plt.show()

X = np.random.randn(200, 2)
X[:50] += 3
X[50:100] += 6
Y = np.zeros(200)
Y[:50] = 1
Y[50:100] = 2
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()