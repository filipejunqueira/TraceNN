import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array

seed = 14
#np.random.seed(seed)
Nsignal = 1000
tsize = 1000
#Generating a Synthetic Signal
# linspace creates a lineared spaced vector (goes from 0 to 2pi in 1000 points)
t = np.linspace(0, 2*np.pi, tsize, endpoint=True)
A = 100.0 # Amplitude in Unit
fo = 1
#s is now a vector of 1000 points since t has 1000 points

print(len(t))

bigdata = np.zeros((tsize,Nsignal))
print(bigdata)


for x in range(0,Nsignal):
    wrandom = 2*np.pi*fo*np.random.uniform(0,1)
    theta_random = np.random.uniform(0,2*np.pi)
    Arandom = A*np.random.uniform(0,1)
    s = Arandom*np.sin(wrandom*t + theta_random) # Signal

    for i in range(0,tsize):
        bigdata[i,x] = s[i]


#plotting

ylim = np.amax(bigdata)
plt.figure()
plt.subplot(121)
plt.plot(t,bigdata[:,0])
plt.title('Example')
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.ylim(-1.2*ylim, 1.2*ylim)

plt.subplot(122)
plt.plot(t,bigdata[:,1])
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Amplitude ($Unit$)')
plt.ylim(-1.2*ylim, 1.2*ylim)

plt.tight_layout()

plt.savefig('FFTExample.png',bbox_inches='tight', dpi=500, transparent=True)
plt.show()
