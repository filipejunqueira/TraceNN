import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from numpy import random

N = 100000

#Generating a Synthetic Signal
# linspace creates a lineared spaced vector (goes from 0 to 2pi in 1000 points)
t = np.linspace(0,20*2*np.pi, N, endpoint=True)
A = 1000 # Amplitude in Unit
fo = 3
#s is now a vector of 1000 points since t has 1000 points

#bigdata = np.zeros((tsize,Nsignal))
#print(bigdata)
s = A*np.sin(t*2*np.pi*fo)

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
plt.title('Time Domain Signal')
plt.ylim(np.min(s)*3, np.max(s)*3)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')

plt.subplot(122)
plt.plot(X, 2.0*np.abs(Yhann[:fft_size])/fft_size)
plt.title('Frequency Domain Signal')
plt.xlim(0,120)
plt.ylim(0,1200)
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Amplitude ($Unit$)')

plt.tight_layout()

plt.savefig('FFT.png',bbox_inches='tight', dpi=150, transparent=True)
plt.show()
