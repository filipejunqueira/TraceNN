import csv
import numpy as np

#fnameString = 'D:\PhD\Code\TraceNN\Data\default_2017Jul24-185510_STM-STM_AtomManipulation--'
#restString = '_1-I(r).txt'
#for i in range (3,893):
#    fname = fnameString + str(i) + restString


def open_trace_files(fname):
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
