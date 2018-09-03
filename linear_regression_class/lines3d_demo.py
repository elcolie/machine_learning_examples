import math

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.linspace(-50, 50, 100)
y = np.linspace(-50, 50, 100)
z = lambda x, y : (x ** 2) + np.power(y, 4)
ax.plot(x, y, z(x,y), label='parametric curve')
ax.legend()

plt.show()
