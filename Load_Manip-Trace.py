import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from numpy import random


#Create array that stores all the curves (goes from 3 to 891)
#Therefore the number collums should be 0 to 2*890 (from 3 to 891 + 1 ),
#Last collum is dedicated to the value (manipulation or not)
#0 = y0, 1 = x0, 2 = y1, 3 = x1 ....

ncurves = 889
npoints = 1000

raw_data = np.zeros( (2*ncurves+1), npoints )

#1st LOOP
#Reads all the files and loads the array:
#Reads each file one at a time.

for j in range(0,ncurves)
    #load all the files to variables x,y
    for i in range(0,npoints):
        raw_data[i,2*j]     =   y[i]
        raw_data[i,2*j+1]   =   x[i]

print(raw_data)

#2nd LOOP
#NEW array
#Copies all the valid (y,x) values (either manipulation or not)


manipulation_value = np.zeros(npoints)

#load .cvc to manipulation_value

for i in range(0,npoints)
    raw_data[i,2*ncurves+1] = manipulation_value[i]


#3rd LOOP
#Avarage all data into new array

Average_data = np.zeros(2, npoints)

for i in range(0,ncurves)
    for j in range(0,points)
        Average_data[i,j] = np.average(rawdata[i,j]) # indices not corret just yet


#4th LOOP
#FFT of the avaraged array with manipulation, and with non manipulation

#call FFT function from other file

#PLOT THE TWO GRAPHS

call plot the GRAPHS
