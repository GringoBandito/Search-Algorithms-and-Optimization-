import numpy as np
import matplotlib.pyplot as plt

def cross_entropy_f3(k):
    
    mu0 = np.ones((50)) * 2
    sigma0 = np.identity(50)
    epoch = 0
    iteration = 0
    lst = []
    yax = []
    
    while epoch < 100:
        f= 0
        for i in mu0:
            f += i**2
        
        lst.append(f)
        samplescores = []
        samplearrays = []
        for i in range(k):
            sample = np.random.multivariate_normal(mu0,sigma0)
            f_sample = 0
            for j in sample:
                f_sample += j**2
                
            samplescores.append((f_sample,i))
            samplearrays.append(sample)
            
        samplescores.sort()
        
        
        elite = []
        
        for top in range(10):
            elite.append(samplearrays[samplescores[top][1]])
        
        
        mu = np.zeros((50))
        sigma = np.zeros((50,50))
        
        for cand in elite:
           mu += cand
           
        mu = mu / 10
        
        
       
        mu0m = mu0.reshape(-1,1)
        
        
        for e in elite:
            e = e.reshape(-1,1)
            sigma += (e - mu0m) *(e-mu0m).T
        
        sigma = sigma / 10
       
        
        mu0 = mu
        sigma0 = sigma
        epoch += 1
        
        
        if epoch == 100 and iteration < 5:
            epoch = 0
            mu0 = np.ones((50)) * 2
            sigma0 = np.identity(50)
            iteration +=1
            yax.append(lst)
            lst = []
         
    
    return yax



C3= cross_entropy_f3(50)


xax = np.arange(0,100)
plt.xlabel('Epoch')
plt.ylabel('Function Value')
plt.title('F3 Cross Entropy: k=50')

for i in C3:
    plt.plot(xax,i)

plt.show()
  