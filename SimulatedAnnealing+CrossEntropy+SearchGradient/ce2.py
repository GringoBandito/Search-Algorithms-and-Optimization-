import numpy as np
import matplotlib.pyplot as plt

def cross_entropy_f2(k):
    
    mu0 = np.ones((2)) * 2
    sigma0 = np.identity(2)
    epoch = 0
    iteration = 0
    lst = []
    yax = []
    
    while epoch < 100:
        num = 1 + np.cos(12*np.sqrt(mu0[0]**2 + mu0[1]**2))
        denom = 0.5*(mu0[0]**2 + mu0[1]**2) + 2
        f = -num/denom
        lst.append(f)
        
        samples = []
        for i in range(k):
            sample = np.random.multivariate_normal(mu0,sigma0)
            nume = 1 + np.cos(12*np.sqrt(sample[0]**2 + sample[1]**2))
            denome = 0.5*(sample[0]**2 + sample[1]**2) + 2
            f_sample = -nume/denome
            samples.append([f_sample,sample[0],sample[1]])
            
        samples.sort()
        
        
        elite = [[d[1],d[2]] for d in samples]
        
        elite = elite[0:10]
        
        
        mu = np.zeros((2))
        sigma = np.zeros((2,2))
        for i in elite:
            ob = np.array(i)
            mu += ob
        
        mu = mu /10
        
        
        for i in elite:
            ob = np.array(i)
            sigma += (ob - mu)*(ob - mu).T
            
        sigma = sigma / 10
        
        mu0 = mu
        sigma0 = sigma
        
        epoch += 1
        
        if epoch == 100 and iteration < 5:
            epoch = 0
            mu0 = np.ones((2)) * 2
            sigma0 = np.identity(2)
            iteration +=1
            yax.append(lst)
            lst = []
         
    
    return yax



C2 = cross_entropy_f2(50)


xax = np.arange(0,100)
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F2 Cross Entropy: k=50')

for i in C2:
    plt.plot(xax,i)

plt.show()
    