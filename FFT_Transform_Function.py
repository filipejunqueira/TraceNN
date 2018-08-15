import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from numpy import random
from Load_Manip_Trace import raw_data, classification

################  Fucking-Chuck-Norris-Fast-FFT   #############################
#Now we are going to create a Fourier Transform :-) we love fourier transforms

s = raw_data[5]
t = raw_data[4]

tsize = len(s)

################  Fucking-Chuck-Norris-Fast-FFT   #############################
#Now we are going to create a Fourier Transform of variable s
Y = np.fft.fft(s)
print(len(Y))
fft_size = int(len(Y)/2 + 1)

#Now we need to adjust the frequency and the Amplitude axis
#Stating with the Frequency Axix (x-Axis)

dt = t[1] - t[0]
fa = 1.0/dt # scan frequency
print('dt=%.5fs (Sample Time)' % dt)
print('fa=%.2fHz (Frequency)' % fa)

#Building Nyquist-Shannon-Frequency from the Nyquist-Shannon Sampling Theorem

X = np.linspace(0, fa/2, fft_size, endpoint=True)

# Correcting Wrong Amplitude Spectrum because of Leakage Effect
# We need a window function to get a periodic signal from real data
# you could use np.hanning, np.hamming or np.blackman for instance

hann = np.hanning(len(s))
Yhann = np.fft.fft(hann*s)

Y_FFT = 2.0*np.abs(Yhann[:fft_size])/fft_size
print(max(Y_FFT))

plt.figure(figsize=(7,3))
plt.subplot(121)
plt.plot(t,s)
plt.title('Manipulation Curve')
#plt.ylim(np.min(s)*3, np.max(s)*3)
plt.xlabel('Distance ($nm$)')
plt.ylabel('I-Amplitude ($nA$)')

plt.subplot(122)
plt.plot(X, 2.0*np.abs(Yhann[:fft_size])/fft_size)
plt.title('FFT')
#plt.xlim(0.5,5)
#plt.ylim(0,1200)
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Amplitude ($Unit$)')

plt.tight_layout()

plt.savefig('FFT.png',bbox_inches='tight', dpi=150, transparent=True)
plt.show()
