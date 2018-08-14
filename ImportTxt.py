import csv
import numpy as np
from scipy.interpolate import UnivariateSpline


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


        #Now im going to resize the value of localdatax if localsize is not new_length
        #If localsize is diferent I'll have to resize it
        #This means create a array with new lenght from localdatax and another one from localdatay
        '''
        if localsize != new_length:

            aux = np.linspace(min(localdatax), max(localdatax) , num = new_length)

            new_localdatax = np.zeros(new_length)
            new_localdatay = np.zeros(new_length)

            sply = UnivariateSpline(localdatax, localdatay)
            splx = UnivariateSpline(localdatax, localdatax)

            new_localdatay = splx()
            '''
        for i in range(0,localsize):
            localdatax[i] = float(content[2*i])
            localdatay[i] = float(content[2*i+1])


    return localdatax, localdatay


"""

    #NEED TO INTERPOLATE DATA WHERE  THE VALUE IS NOT 1000
        old_indices = np.arange(0,len(a))
        new_length = 11
        new_indices = np.linspace(0,len(a)-1,new_length)
        spl = UnivariateSpline(old_indices,a,k=3,s=0)
        new_array = spl(new_indices)

"""
