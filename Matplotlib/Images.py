import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


im = Image.open('lena.jpg')
arr = np.array(im)
print(arr.shape)
plt.imshow(arr)
plt.show()
plt.imshow(im)
plt.show()
gray = arr.mean(axis=2)
print(gray.shape)
plt.imshow(gray)
plt.show()
plt.imshow(gray, cmap='gray')
plt.show()