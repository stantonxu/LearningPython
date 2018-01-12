from mpl_toolkits import mplot3d

import numpy as np 
import matplotlib.pyplot as plt 

def f(x1, x2):
    return 100 / x1 + x1 / x2 + x2

x1 = np.linspace(1, 100, 2000)
x2 = np.linspace(1, 100, 2000)

X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X1, X2, Y, 500, cmap='binary')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.show()
