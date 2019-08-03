import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as spi  # 插值专用函数
import scipy.integrate as sci  # 积分专用函数
import scipy.optimize as spo  # 优化专用函数

x = np.linspace(-2 * np.pi, 2 * np.pi, 11)
f = lambda x: np.sin(x) + 0.5 * x
tck = spi.splrep(x, f(x), k=1)
iy = spi.splev(x, tck)
# 利用matplotlib进行可视化
plt.figure(figsize=(8, 4), dpi=80)
x_ = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
plt.plot(x_, f(x_), color='blue', linewidth=2.5, label='true value')
plt.scatter(x, iy, 30, color='red', label='interpolated value')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

xd = np.linspace(1, 3, 50)
iyd = spi.splev(xd, tck)
tck = spi.splrep(x, f(x), k=3)
iyd = spi.splev (xd, tck)
print(xd, '\n\n,iyd')
plt.figure(figsize=(8, 4), dpi=80)
plt.plot(xd, f(xd), color='blue', linewidth=2.5, label='true value')
plt.scatter(xd, iyd, 30, color='red', label='interpolated value')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
