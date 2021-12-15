import numpy as np
import matplotlib.pyplot as plt


def simulated_annealing_f2(temp):
    
    yax = []
    iterations = 0
    epoch = 1
    x10 = 2
    x20 = 2
    lst = []
    
    while epoch < 101:
        
        num0 = 1 + np.cos(12*np.sqrt(x10**2 + x20**2))
        den0 = 0.5*(x10**2 + x20**2) + 2
        f0 = -num0 / den0
        lst.append(f0)
        
        x1 = x10 + np.random.normal()
        x2 = x20 + np.random.normal()
        
        num = 1 + np.cos(12*np.sqrt(x1**2 + x2**2))
        den = 0.5*(x1**2 + x2**2) + 2
        f = -num / den
        
        if f < f0:
            x10 = x1
            x20 = x2 
            epoch += 1
            
        
        if f >= f0:
            e = (f0 - f)
            t = temp/epoch
            beta = np.exp(e/t)
            
            samp = np.random.uniform(0,1)
            
            if samp < beta:
                x10 = x1
                x20 = x2
                epoch += 1
            
            else:
                epoch +=1
    
        if epoch == 101 and iterations < 5:
            iterations +=1
            epoch = 1
            yax.append(lst)
            lst = []
            x10 = 2
            x20 = 2
       
    
    return yax

an1 = simulated_annealing_f2(1000)
xax = np.arange(0,100)
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F2 Simulated Annealing: T=10')

for i in an1:
    plt.plot(xax,i)

plt.show()

           