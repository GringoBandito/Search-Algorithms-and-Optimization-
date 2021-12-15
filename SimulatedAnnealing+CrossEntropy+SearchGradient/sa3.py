import numpy as np
import matplotlib.pyplot as plt


def simulated_annealing_f3(temp):
    
    yax = []
    iterations = 0
    epoch = 1
    x0 = np.ones((50))*2
    lst = []
    
    while epoch < 1001:
        f0 = 0
        for i in x0:
            f0 += i**2
        
        lst.append(f0)
        
        x = x0 + np.random.normal(size=(50))
        f = 0
        for j in x:
            f += j ** 2
            
        
        
        if f < f0:
            x0 = x
            epoch += 1
            
        
        if f >= f0:
            e = (f0 - f)
            t = temp/epoch
            beta = np.exp(e/t)
            
            samp = np.random.uniform(0,1)
            
            if samp < beta:
                x0 = x
                epoch += 1
            
            else:
                epoch +=1
    
        if epoch == 1001 and iterations < 5:
            iterations +=1
            epoch = 1
            yax.append(lst)
            lst = []
            x0 = np.ones((50))*2
       
    
    return yax

an1 = simulated_annealing_f3(1000)
xax = np.arange(0,1000)
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F3 Simulated Annealing: T=1000')

for i in an1:
    plt.plot(xax,i)

plt.show()
