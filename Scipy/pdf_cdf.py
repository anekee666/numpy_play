import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
x = np.linspace(-6, 6, 1000)
fx = norm.pdf(x, loc=0, scale=1)
plt.plot(x, fx)
plt.show()
Fx = norm.cdf(x, loc=0, scale=1)
plt.plot(x, Fx)
plt.show()
logfx = norm.logpdf(x, loc=0, scale=1)
plt.plot(x, logfx)
plt.show()