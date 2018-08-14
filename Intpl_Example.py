import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np


def open_trace_files(fname,new_length):

    with open(fname, 'r') as f:
        content = f.readlines()
        prefixes = ('#')
        for word in content[:]:
            if word.startswith(prefixes):
                content.remove(word)

        content = ''.join(content)
        content = content.split()

        localsize = int(float(len(content))/2)
        localdatax = np.zeros(localsize)
        localdatay = np.zeros(localsize)

        for i in range(0,localsize):
            localdatax[i] = float(content[2*i])
            localdatay[i] = float(content[2*i+1])


        return localdatax, localdatay



points = 1000
fname = 'Test.txt'

data_local = open_trace_files(fname,points)
data_local2 = open_trace_files('Test2.txt',points)
data_local3 = open_trace_files('Test3.txt',points)

x,y = data_local
x2,y2 = data_local2
x3,y3 = data_local3

x = np.arange(0,len(y))
new_length = 1000
new_indices = np.linspace(0,len(y)-1,new_length)
spl = UnivariateSpline(x,y,k=3,s=0)
new_array = spl(new_indices)


plt.plot(x2, y2, 'b', ms=5)
plt.figure()
plt.plot(x3, y3, 'b', ms=5)

plt.figure()

plt.plot(x, y, 'ro', ms=5)
plt.plot(new_indices,new_array, 'g', ms=5)
plt.show()


#spl.set_smoothing_factor(0.5)
#plt.plot(xs, spl(xs), 'b', lw=3)
