import numpy as np

print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(10 * np.ones((2, 3)))
print(np.eye(3))

print(np.random.random())
print(np.random.random((2, 3)))
print(np.random.randn(2, 3))

R = np.random.randn(10000)
print(R.mean())
print(np.mean(R))
print(R.var())
print(R.std())


R = np.random.randn(10000, 3)
print(R.mean(axis=0))
print(R.mean(axis=1).shape)
print(np.cov(R).shape)
print(np.cov(R.T))
print(np.cov(R, rowvar=False))
print(np.random.randint(0, 10, size=(3, 3)))
print(np.random.choice((0,1,2), size=(3, 3),replace=True,p=[0.1, 0.6, 0.3]))