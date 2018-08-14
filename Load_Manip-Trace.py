import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from numpy import random
from ImportTxt import open_trace_files

fnameString = 'C:\\Users\\filip\\Documents\\Projects\\TraceNN\\Data\\default_2017Jul24-185510_STM-STM_AtomManipulation--'
restString = '_1-I(r).txt'

ncurves = 889
npoints = 1000


raw_data = []
raw_data.clear

for i in range(3,ncurves + 3):
    fname = fnameString + str(i) + restString
    print('Adding ' + fname)

    data_local = open_trace_files(fname,npoints)

    #print(str(len(data_local[0])) + ' File is ' +str(i))
    #print(str(len(data_local[1])) + ' File is ' +str(i))

    raw_data.append(data_local[0]) #0 means x
    raw_data.append(data_local[1]) #1 means y


print('\n ######################################################################################################## \n')
print(len(raw_data))
print(raw_data[1])
print('\n\nThis is the end \n')

#2nd LOOP
#NEW array
#Copies all the valid (y,x) values (either manipulation or not)

#load .cvc to manipulation_value

#3rd LOOP
#Avarage all data into new array


#4th LOOP
#FFT of the avaraged array with manipulation, and with non manipulation

#call FFT function from other file

#PLOT THE TWO GRAPHS
