import numpy as np
import matplotlib.pyplot as plt


xx = np.array([2,2])



def grad_desc(x0,alpha,iterations):
    
    count = 0
    xaxis = []
    yaxis = []
    xaxis2 = []
    yaxis2 = []
    grad0 = []
    grad1 = []
    
    while count < iterations:
        
        grad = np.array([2*x0[0] - x0[1], 6*x0[1]-x0[0]])
        x0 = x0 - alpha*grad
        f = x0[0]**2-x0[0]*x0[1] + 3*x0[1]**2 + 5
        
        xaxis.append(count+1)
        yaxis.append(f)
        xaxis2.append(x0[0])
        yaxis2.append(x0[1])
        grad0.append(grad[0])
        grad1.append(grad[1])
        count += 1
    
    return x0,xaxis,yaxis,xaxis2, yaxis2, grad0,grad1
        
    
#print(grad_desc(xx,.3,10))

def exact_line(x0, iterations):
    
    count = 0
    xaxis = []
    xaxis2 = []
    yaxis = []
    yaxis2 = []
    grad0 = []
    grad1 = []
    
    
    while count < iterations:
        
        grad = np.array([2*x0[0] - x0[1], 6*x0[1]-x0[0]])
        num = 2*x0[0]*grad[0] + grad[0]*grad[1] + 6*x0[1]*grad[1]
        denom = 2*(grad[0]**2) + 6*(grad[1]**2)
        alpha = num/denom
        
        x0 = x0 - alpha * grad
        f = x0[0]**2-x0[0]*x0[1] + 3*x0[1]**2 + 5
        
        xaxis.append(count+1)
        yaxis.append(f)
        xaxis2.append(x0[0])
        yaxis2.append(x0[1])
        grad0.append(grad[0])
        grad1.append(grad[1])
        count += 1
    
    return x0,xaxis,yaxis,xaxis2, yaxis2, grad0,grad1


def newton_search(x0,iterations):
    
    count = 0
    xaxis = []
    xaxis2 = []
    yaxis = []
    yaxis2 = []
    grad0 = []
    grad1 = []
    
    while count < iterations:
        
        grad = np.array([2*x0[0] - x0[1], 6*x0[1]-x0[0]])
        hessian = np.array([[2,-1], [-1,6]])
        hessian = np.linalg.inv(hessian)
        
        x0 = x0 - np.matmul(hessian,grad)
        
        f = x0[0]**2-x0[0]*x0[1] + 3*x0[1]**2 + 5
        
        xaxis.append(count+1)
        xaxis2.append(x0[0])
        yaxis.append(f)
        yaxis2.append(x0[1])
        grad0.append(grad[0])
        grad1.append(grad[1])
        count += 1
    
    return x0,xaxis,yaxis,xaxis2, yaxis2, grad0,grad1

vec_max, xax, yax1, xax1, yax2,grad0,grad1 = newton_search(xx,10)


plt.title("Newton Direction")
plt.xlabel("Iteration")
plt.ylabel("Function Value")
plt.plot(xax,yax1, color = 'red')
plt.show()

plt.title("Newton Direction Coordinate Pairs")
plt.xlabel("X-Value")
plt.ylabel("Y-Value")
plt.axis('equal')
plt.scatter(xax1,yax2, color = 'red')
plt.quiver(xax1,yax2,grad0,grad1, color='blue')
plt.show()