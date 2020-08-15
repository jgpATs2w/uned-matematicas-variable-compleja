import numpy as np
import matplotlib.pyplot as plt

def z(n):
  t = np.linspace(-np.pi, np.pi, 1000)
  c = 0.25 * n
  for n in range(1,n+1):
      c = c - (-1) ** n * np.exp(1j * n * t) / (2 * n)
  return c.view('(2,)float').T

plt.plot( *z(2), *z(3), *z(4), *z(5), *z(6), '-', lw=3 )
plt.axis('scaled')
plt.show()