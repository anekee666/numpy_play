from PIL import Image
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
im = Image.open('lena.jpg')
gray = np.mean(im, axis=2)
x = np.linspace(-6, 6, 50)
fx = norm.pdf(x, loc=0, scale=1)
plt.plot(x, fx)
plt.show()
filt = np.outer(fx, fx)
plt.imshow(filt, cmap='gray')
plt.show()
from scipy.signal import convolve2d
out = convolve2d(gray, filt)
plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(out, cmap='gray')
plt.show()