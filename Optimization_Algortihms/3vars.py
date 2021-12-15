from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import random
 
# Creating dataset
x = np.outer(np.linspace(-1, 1, 32), np.ones(32))

y = np.zeros((32,32))

for i in range(32):
    for j in range(32):
        y[i][j] = random.uniform(-1 * (1/math.sqrt(5)) * math.sqrt(1-x[i][j]**2),(1/math.sqrt(5)) * math.sqrt(1-x[i][j]**2) )


z = np.zeros((32,32))

for i in range(32):
    for j in range(32):
        z[i][j] = -1* math.sqrt(-x[i][j]**2 - 5*(y[i][j]**2) + 1)/math.sqrt(3)
    
# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating plot
ax.plot_surface(x, y, z)
 
# show plot
plt.show()

