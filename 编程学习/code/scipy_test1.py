import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as spi  # 插值专用函数
import scipy.integrate as sci  # 积分专用函数
import scipy.optimize as spo  # 优化专用函数

f = lambda x, y: np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2

from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(8, 4))
ax = Axes3D(fig)

surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
