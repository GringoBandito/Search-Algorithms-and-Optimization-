import numpy as np
import matplotlib.pyplot as plt

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

def search_gradient2(k):
    '''f(x) = x1^2 + x2^2 + x3^3...'''
    
    mu0 = np.ones((50)) * 2
    sigma0 = np.identity(50)
    epoch = 0 
    iteration = 0
    eta = 0.01
    yax = []
    lst = []
    
    while epoch < 100:
        
        samplevalues = []
        samplevectors = []
        for i in range(k):
            sample = np.random.multivariate_normal(mu0,sigma0)
            
            f_sample = 0
            for i in sample:
                f_sample += i
                samplevalues.append(f_sample)
                samplevectors.append(sample)
        
        gradmu = np.zeros((50,1))
        gradsigma = np.zeros((50,50))
        mu0m = mu0.reshape(-1,1)
        
        for j in range(len(samplevalues)):
            svec = samplevectors[j].reshape(-1,1)
            gradmu += np.dot(np.linalg.inv(sigma0),(svec- mu0m)) * samplevalues[j]
            gradsigma += samplevalues[j]*(-0.5*np.linalg.inv(sigma0) + .5*np.linalg.inv(sigma0)*(svec - mu0m)* (svec - mu0m).T *np.linalg.inv(sigma0))
            
        gradmu = 1/k
        gradsigma = 1/k
        
        mu0 -= eta * gradmu
        sigma0 -= eta * gradsigma 
        
        if not is_pos_def(sigma0):
            sigma0 = np.identity(50)
        
        epoch += 1
        lst.append(sum(samplevalues)/len(samplevalues))
        
        if epoch == 100 and iteration < 5:
            mu0 = np.ones((50)) * 2
            sigma0 = np.identity(50)
            epoch = 0 
            yax.append(lst)
            lst = []
            iteration += 1
            print(iteration)
                
            
    return yax


S3 = search_gradient2(50)


xax = np.arange(0,100)
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F3 Search Gradient: k=50')

for i in S3:
    plt.plot(xax,i)

plt.show()
  
