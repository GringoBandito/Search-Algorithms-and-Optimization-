import numpy as np
import matplotlib.pyplot as plt

def search_gradient(k):
    '''f(x,y) = x**2+y**2'''
    
    mu0 = np.ones((2)) * 2
    sigma0 = np.identity(2)
    epoch = 0 
    iteration = 0
    eta = 0.01
    yax = []
    lst = []
    
    while epoch < 1000:
        
        samplevalues = []
        samplevectors = []
        for i in range(k):
            sample = np.random.multivariate_normal(mu0,sigma0)
            fitness = sample[0]**2 + sample[1]**2
            samplevalues.append(fitness)
            samplevectors.append(sample)
        
        gradmu = np.zeros((2,1))
        gradsigma = np.zeros((2,2))
        mu0m = mu0.reshape(-1,1)
        
        for j in range(len(samplevalues)):
            svec = samplevectors[j].reshape(-1,1)
            gradmu += np.dot(np.linalg.inv(sigma0),(svec- mu0m)) * samplevalues[j]
            gradsigma += samplevalues[j]*(-0.5*np.linalg.inv(sigma0) + .5*np.linalg.inv(sigma0)*(svec - mu0m)* (svec - mu0m).T *np.linalg.inv(sigma0))
            
        gradmu = 1/k
        gradsigma = 1/k
        
        mu0 -= eta * gradmu
        sigma0 -= eta * gradsigma
        
        
        epoch += 1
        lst.append(sum(samplevalues)/len(samplevalues))
        
        if epoch == 1000 and iteration < 5:
            mu0 = np.ones((2)) * 2
            sigma0 = np.identity(2)
            epoch = 0 
            yax.append(lst)
            lst = []
            iteration += 1
            
            
    return yax


S1 = search_gradient(10)


xax = np.arange(0,1000)
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F1 Search Gradient: k=50')

for i in S1:
    plt.plot(xax,i)

plt.show()
  
        