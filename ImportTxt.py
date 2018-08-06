import csv
import numpy as np
from scipy.interpolate import UnivariateSpline


def open_trace_files(fname):

    with open(fname, 'r') as f:
        content = f.readlines()
        prefixes = ('#')
        for word in content[:]:
            if word.startswith(prefixes):
                content.remove(word)

        content = ''.join(content)
        content = content.split()

"""
    #NEED TO INTERPOLATE DATA WHERE  THE VALUE IS NOT 1000
        old_indices = np.arange(0,len(a))
        new_length = 11
        new_indices = np.linspace(0,len(a)-1,new_length)
        spl = UnivariateSpline(old_indices,a,k=3,s=0)
        new_array = spl(new_indices)


"""

        localsize = int(float(len(content))/2)
        localdatax = np.zeros(localsize)
        localdatay = np.zeros(localsize)

        for i in range(0,localsize):
            localdatax[i] = float(content[2*i])
            localdatay[i] = float(content[2*i+1])

    #print(localdatax)
    #print(localdatay)




    return localdatax, localdatay
