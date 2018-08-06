import csv
import numpy as np


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
        Flag = False
        for Flag is False
        if int(float(len(content))) < 1000:

            content = content

            else
                Flag = True
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
