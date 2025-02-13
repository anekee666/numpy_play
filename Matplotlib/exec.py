import numpy as np
import matplotlib.pyplot as plt

X = 2*np.random.random((1000, 2))-1
Y = (X[:, 0] > 0) ^ (X[:, 1] > 0)  # True (1) if one is positive, one is negative
# Plot with two colors
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="bwr")  # Blue for 0, Red for 1
plt.colorbar(label="XOR Output")
plt.axhline(0, color="black", linewidth=0.5)  # Draw x-axis
plt.axvline(0, color="black", linewidth=0.5)  # Draw y-axis
plt.title("XOR Function Visualization")
plt.show()