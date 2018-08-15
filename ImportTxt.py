import csv
import numpy as np

#This function adds collums of the Txt to two variables called localdatax and localdatay which are returned


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
