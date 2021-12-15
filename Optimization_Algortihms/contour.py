import numpy as np
import matplotlib.pyplot as plot
import pylab


xpoints = []
ypoints = []

for i in range(-10,10):
    xpoints.append(i)
    ypoints.append(i)
    

zpoints = np.ndarray((20,20))

for i in range(0,len(xpoints)):
    for j in range(0,len(ypoints)):
        zpoints[i][j] = xpoints[i]**2 - 3*ypoints[j]**2
        

print(xpoints)
print(ypoints)
print(zpoints)


pylab.xlim([-10,10])
pylab.ylim([-10,10])

plot.title("Contour plot X^2 - 3Y^2")
plot.xlabel("X")
plot.ylabel("Y")

contours = plot.contour(xpoints, ypoints, zpoints)

plot.clabel(contours, inline=1, fontsize=10)

plot.show()

