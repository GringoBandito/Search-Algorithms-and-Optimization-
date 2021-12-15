import numpy as np
import matplotlib.pyplot as plt


X = np.array([[1,2,3],[1,2,3],[-1,2,-1]])
Y = np.array([[-1,3,1], [1,-3,1],[0,1,2]])



def grad_descent(x,y,alpha,iterations):
    
    count = 0
    a = np.random.rand(3,3)
    b = np.random.rand(3,1)
    xaxis = []
    yaxis = []
    
    while count < iterations:
            
        loss = 0
        for i in range(3):
            loss += (np.linalg.norm(np.matmul(a,x[i])+ b - y[i]) ** 2)
        
        yaxis.append(loss)
        xaxis.append(count)
        
        dat1 = np.reshape(x[0],(3,1))
        dat2 = np.reshape(x[1],(3,1))
        dat3 = np.reshape(x[2],(3,1))
        dep1 = np.reshape(y[0],(3,1))
        dep2 = np.reshape(y[1],(3,1))
        dep3 = np.reshape(y[2],(3,1))
        
        grada = 2 * ( np.matmul(np.matmul(a,dat1) + b - dep1,np.transpose(dat1)) + np.matmul(np.matmul(a,dat2) + b - dep2,np.transpose(dat2)) + np.matmul(np.matmul(a,dat3) + b - dep3,np.transpose(dat3)))
        gradb = 2 * (np.matmul(a,dat1) + b - dep1 + np.matmul(a,dat2) + b - dep2 + np.matmul(a,dat3) + b - dep3)
        
        
        a = a - alpha * grada
        b = b - alpha * gradb
    
        
        count += 1
        
               
    
    return grada,gradb,a,b,yaxis,xaxis

        
gradienta,gradientb,aa,bb,loss,xax = grad_descent(X,Y,.01,30)

plt.title("Question 4: L(A,B)")
plt.xlabel("Iteration")
plt.ylabel("Loss Value")
plt.plot(xax,loss, color = 'red')
plt.show()
