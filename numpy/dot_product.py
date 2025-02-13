import numpy as np
#a⋅b=aTb=∑d=1Dadbd
a = np.array([1,2])
b = np.array([3,4])


#option 1
dot = 0
for e, f in zip(a, b):
  dot += e*f
print(dot)


# option 2 use integer index
dot = 0
for i in range(len(a)):
  dot += a[i] * b[i]
print(dot)

#option 3 
#a * b -->array([3, 8])
print(np.sum(a * b)) #same as (a * b).sum()

#option 4
print(np.dot(a, b)) # same as  a.dot(b) , b.dot(a)

#option 5
print(a @ b)

amag = np.sqrt((a * a).sum())
print(amag)
amag2 = np.linalg.norm(amag)
print(amag2)
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cosangle)