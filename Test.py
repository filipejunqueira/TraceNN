import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from scipy.interpolate import UnivariateSpline


def open_trace_files(fname,lenght):

    with open(fname, 'r') as f:
        content = f.readlines()
        prefixes = ('#')
        for word in content[:]:
            if word.startswith(prefixes):
                content.remove(word)

        content = ''.join(content)
        content = content.split()
        '''
        #NEED TO INTERPOLATE DATA WHERE THE VALUE IS NOT 1000

            old_indices = np.arange(0,len(a))
            new_length = 1000
            new_indices = np.linspace(0,len(a)-1,new_length)
            spl = UnivariateSpline(old_indices,a,k=3,s=0)
            new_array = spl(new_indices)
        '''
        localsize = int(float(len(content))/2)
        localdatax = np.zeros(localsize)
        localdatay = np.zeros(localsize)
        new_localdatax = np.zeros(lenght)
        new_localdatay = np.zeros(lenght)

        for i in range(0,localsize):
            localdatax[i] = float(content[2*i])
            localdatay[i] = float(content[2*i+1])

    #print(localdatax)
    #print(localdatay)


    return localdatax, localdatay

ncurves = 1
npoints = 100
raw_data = np.zeros((2*ncurves,npoints))

fname = 'Test.txt'

data_local = open_trace_files(fname,1000)
print(str(len(data_local[0])) + ' is the file size\n\n')
print(str(len(data_local[1])) + ' is the file size\n\n')

raw_data[0] = data_local[0] #0 means x
raw_data[1] = data_local[1] #1 means y

print(raw_data)
print(len(raw_data))

print('\n This is the end \n')



'''
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

'''

'''

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

'''
