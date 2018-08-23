import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
import ImportTxt

#Load_manipulation TraceNN
#Transform fft

#grab f0 and f1

# use f0 and f1 as input in a NN

#use raw data downsampled 2x (500 points) if needed and input as NN, call that r0 and r1

#grab h0 and h1 - use as input to simulate data (max 25 peaks and) do A*sin(wt)
#or just grab h0 and add random step (might be a better idea).
#generate 500 curves (250 with step and 250 without)
# add simulated curves to r0 and r1

#train neural network with r0 and r1

#Save model in \\Output_Data\\Models

#Test with 20% of data
