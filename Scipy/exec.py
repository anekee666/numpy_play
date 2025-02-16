from PIL import Image
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
im = Image.open('lena.jpg')
gray = np.mean(im, axis=2)
Hx=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
print(Hx)
Hy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
from scipy.signal import convolve2d
Gx= convolve2d(gray, Hx)
Gy= convolve2d(gray, Hy)
G=np.sqrt(Gx**2+Gy**2)
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(G, cmap='gray')
plt.show()