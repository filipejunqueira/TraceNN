import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from numpy import random
from Load_Manip_Trace import raw_data, classification

################  Fucking-Chuck-Norris-Fast-FFT   #############################
#Now we are going to create a Fourier Transform :-) we love fourier transforms

Nsignal = 1000
tsize = 1000

t = np.linspace(0, 2*np.pi, tsize, endpoint=True)
