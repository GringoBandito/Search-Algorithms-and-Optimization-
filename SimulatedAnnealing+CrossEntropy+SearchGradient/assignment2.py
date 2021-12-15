import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

'''
def f(x,y):
    return -1 * (1 + np.cos(12*np.sqrt(x**2 + y**2)))/(0.5*(x**2 + y**2) + 2)

x = np.linspace(-5,5,30)
y = np.linspace(-5,5,30)


X,Y = np.meshgrid(x,y)
Z = f(X,Y)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='binary')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60,35)
fig


ax = plt.axes(projection ='3d')
ax.plot_surface(X,Y,Z, rstride=1,cstride=1,cmap='viridis',edgecolor='none')

ax.set_title('F2(x)')
'''


def grad_desc_f1():
    
    x1 = 2
    x2 = 2
    alpha = 0.01
    epoch = 0
    yax = []
    
    while epoch < 100:
        f = x1**2 + x2**2
        yax.append(f)
        x1 = x1 - 2 * alpha * x1
        x2 = x2 - 2 * alpha * x2
        
       
        epoch +=1
    
    return yax


l = grad_desc_f1()


plt.plot(np.arange(100),l,color='b')
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('f(x,y)= x^2 + y^2')
plt.show()


def grad_desc_f2():
    x1_0 = 2
    x2_0 = 2
    alpha = 0.01
    epoch = 0 
    yax = []
    
    while epoch < 100:
        denom = 0.5 *(x1_0**2 + x2_0**2) + 2
        num = 1 + np.cos(12*np.sqrt(x1_0**2 + x2_0 **2))
        yax.append(-1 * num/denom)
        x1 = x1_0 - alpha * (np.sin(12*np.sqrt(x1_0 **2 + x2_0**2)) * 6/np.sqrt(x1_0**2+x2_0**2) * 2*x1_0 * denom - (num * x1_0))
        x2 = x2_0 - alpha * (np.sin(12*np.sqrt(x1_0 **2 + x2_0**2)) * 6/np.sqrt(x1_0**2+x2_0**2) * 2*x2_0 * denom - (num * x1_0))
        x1 = x1/(denom**2)
        x2 = x2/ (denom**2)
        
        x1_0 = x1
        x2_0 = x2
        
        epoch += 1
    
    return yax


l2 = grad_desc_f2()


plt.plot(np.arange(100),l2,color='b')
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F2(x)')
plt.show()          
        
        
def grad_desc_f3():
    x = np.ones((50)) *2
    alpha = 0.01
    epoch = 0
    yax = []
    
    while epoch < 100:
        count = 0
        for i in x:
            count += i**2
        yax.append(count)
        
        x = x - alpha * 2 * x
        epoch+=1
    
    
    return yax

l3 = grad_desc_f3()

plt.plot(np.arange(100),l3,color='b')
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F3(x)')
plt.show()          
 
    
    
    
    
    
    
    
    
    
    