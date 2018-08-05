import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array

#This is how you generate a Synthetic Signal
# linspace creates a lineared spaced vector (goes from 0 to 2pi in 1000 points)
t = np.linspace(0, 2*np.pi, 1000, endpoint=True)
f = 3.0 # Frequency in Hz
A = 100.0 # Amplitude in Unit

#s is now a vector of 1000 points since t has 1000 points
s = A * np.sin(2*np.pi*f*t) # Signal

plt.plot(t,s)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.show()

################  Fucking-Chuck-Norris-Fast-FFT   #############################
#Now we are going to create a Fourier Transform (of variable
Y = np.fft.fft(s)
N = len(Y)/2 + 1
N = int(N)

#Now we need to adjust the frequency and the Amplitude axis
#Stating with the Frequency Axix (x-Axis)

dt = t[1] - t[0]
fa = 1.0/dt # scan frequency
print('dt=%.5fs (Sample Time)' % dt)
print('fa=%.2fHz (Frequency)' % fa)

#Building Nyquist-Shannon-Frequency from the Nyquist-Shannon Sampling Theorem

X = np.linspace(0, fa/2, N, endpoint=True)

# Correcting Wrong Amplitude Spectrum because of Leakage Effect
# We need a window function to get a periodic signal from real data
# you could use np.hanning, np.hamming or np.blackman for instance

hann = np.hanning(len(s))
Yhann = np.fft.fft(hann*s)

plt.figure(figsize=(7,3))
plt.subplot(121)
plt.plot(t,s)
plt.title('Time Domain Signal')
plt.ylim(np.min(s)*3, np.max(s)*3)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')

plt.subplot(122)
plt.plot(X, 2.0*np.abs(Yhann[:N])/N)
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Amplitude ($Unit$)')

plt.tight_layout()

plt.savefig('FFT.png',bbox_inches='tight', dpi=150, transparent=True)
plt.show()

#importing a file -not working yet

df = pd.read_csv('Vertikale_Netzlast_2013.csv', header=6, sep=';', parse_dates=[[0, 1]], index_col=0, na_values=['n.v.'])
df.rename(columns={'Unnamed: 3': 'Load'}, inplace=True)
#interpoling df for missing data
