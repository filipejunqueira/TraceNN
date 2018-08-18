import csv
import pandas as pd
import numpy as np
from ImportTxt import open_trace_files

fnameString = 'C:\\Users\\filip\\Documents\\Projects\\TraceNN\\Data\\default_2017Jul24-185510_STM-STM_AtomManipulation--'
#fnameString = 'D:\\PhD\\Code\\TraceNN\\Data\\default_2017Jul24-185510_STM-STM_AtomManipulation--'

restString = '_1-I(r).txt'

ncurves = 889
npoints = 1000


raw_data = []
raw_data.clear

print('\n\n########################################################################################################')

for i in range(3,ncurves + 3):
    fname = fnameString + str(i) + restString

    #print('Adding ' + fname +'to position ' + str(i-3))

    data_local = open_trace_files(fname,npoints)

    #print(str(len(data_local[0])) + ' File is ' +str(i))
    #print(str(len(data_local[1])) + ' File is ' +str(i))

    raw_data.append(data_local[0]) #0 means x
    raw_data.append(data_local[1]) #1 means y

print('\nAdded ' + str(int(len(raw_data)/2)) + ' curves (x,y) to the main variable raw_data\n')

#now we need to load the cvc file (if its a manipulation trace or not)
#classification_dataframe is a variable of type data_frame (Panda variable)
#we transform that into a list because its easier to work with I think...

classification_dataframe = pd.read_csv('C:\\Users\\filip\\Documents\\Projects\\TraceNN\\Data\\Classification.csv', header =None)
#classification_dataframe = pd.read_csv('D:\\PhD\\Code\\TraceNN\\Data\\Classification.csv', header =None)

classification = classification_dataframe.values.tolist()

print('Added ' + str(len(classification)) + ' classification curves added')

print('\n######################################################################################################## \n')

print('\n                                           Files sucessfuly imported \n')
