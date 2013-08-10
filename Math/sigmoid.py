import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(-60, 60, 1000)

sigma = 1/(1+np.e**-z)

plt.figure(figsize=(8,3))
plt.plot(z, sigma)
plt.ylabel('Sigmoid(x)')
plt.savefig('sigma.png')
