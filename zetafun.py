# plotting zeta function on complex plane


# [zeta function impl]
from itertools import count, islice

def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


def zeta(s, t=100):
    if s == 1: return complex("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


# [correct data with numpy]
import numpy

x = numpy.arange(-3, 3, 0.1)
y = numpy.arange(-30, 30, 1)
X, Y = numpy.meshgrid(x, y)

@numpy.vectorize
def z(real, imag):
    r = zeta(real + imag * 1j).real
    return min(max(-10, r), 10)

Z = z(X, Y)
#print(Z)


# [plot with matplotlib]
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm

fig = pyplot.figure()
ax = fig.gca(projection="3d")
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-10, 10)


pyplot.show()