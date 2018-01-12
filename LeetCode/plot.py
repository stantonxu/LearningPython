import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return 100 / x + x

x1 = np.arange(1, 100, 1)

plt.figure(1)
plt.plot(x1, f(x1))