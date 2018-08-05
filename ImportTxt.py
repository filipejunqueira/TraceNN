import csv
import numpy as np

fnameString = 'D:\PhD\Code\TraceNN\Data\default_2017Jul24-185510_STM-STM_AtomManipulation--'
restString = '_1-I(r).txt'

ncurves = 889
npoints = 1000
raw_data = np.zeros((3,3))
fname = 'Test.txt'

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

    #print(localdatax)
    #print(localdatay)

    return localdatax, localdatay

data_local = open_trace_files(fname)
raw_data[0] = data_local[0]
raw_data[1] = data_local[1]


print('\n',raw_data)

print('\n This is the end of the function \n')

print(raw_data[1])

#for i in range (3,893):
#    filename = fnameString + str(i) + restString
#    open_trace_files(filename)
#    raw_data[:,2*i+1] = localdatax[i]
#    raw_data[:,2*i+1] = localdatay[i]
