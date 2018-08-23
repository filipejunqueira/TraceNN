import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Load_Manip_Trace import raw_data, classification
from Histrogram_Function import downsample
from sklearn.preprocessing import MinMaxScaler
import os


def fft_trace(t,s):

    ################  Fucking-Chuck-Norris-Fast-FFT   #############################
    #Now we are going to create a Fourier Transform :-) we love fourier transforms

    tsize = len(s)

    ################  Fucking-Chuck-Norris-Fast-FFT   #############################
    #Now we are going to create a Fourier Transform of variable s
    Y = np.fft.fft(s)
    fft_size = int(len(Y)/2 + 1)

    #Now we need to adjust the frequency and the Amplitude axis
    #Stating with the Frequency Axix (x-Axis)

    dt = t[1] - t[0]
    fa = 1.0/dt # scan frequency
    #print(len(Y))
    #print('dt=%.5fs (Sample Time)' % dt)
    #print('fa=%.2fHz (Frequency)' % fa)

    #Building Nyquist-Shannon-Frequency from the Nyquist-Shannon Sampling Theorem

    X = np.linspace(0, fa/2, fft_size, endpoint=True)

    # Correcting Wrong Amplitude Spectrum because of Leakage Effect
    # We need a window function to get a periodic signal from real data
    # you could use np.hanning, np.hamming or np.blackman for instance

    hann = np.hanning(len(s))
    Yhann = np.fft.fft(hann*s)

    Y_FFT = 2.0*np.abs(Yhann[:fft_size])/fft_size


    return X, Y_FFT

#storing all the fft_data on a list:

fft_data0 = []
fft_data1 = []
fft_data2 = []

fft_data0.clear()
fft_data1.clear()
fft_data2.clear()

flag = True
CurveTest = 'y'
N = len(classification)

for i in range(0,N):

    if classification[i][1] == 0.0:
        x,y = fft_trace(raw_data[2*i],raw_data[2*i+1])
        #fft_data0.append(classification[i][0])
        fft_data0.append(x)
        fft_data0.append(y)
    if classification[i][1] == 1.0:
        x,y = fft_trace(raw_data[2*i],raw_data[2*i+1])
        #fft_data1.append(classification[i][0])
        fft_data1.append(x)
        fft_data1.append(y)
    if classification[i][1] == 2.0:
        x,y = fft_trace(raw_data[2*i],raw_data[2*i+1])
        #fft_data2.append(classification[i][0])
        fft_data2.append(x)
        fft_data2.append(y)
    if all([classification[i][1] != 0, classification[i][1] != 1,classification[i][1] != 2]):
        print('curve ' + str(i) + ' - MISSING DATA - ERROR\n\n')
        print(i)

        # Create Curves:

    if flag == True:
        CurveTest = input("Do you want to create images with the FFT of every curve (y/n)? ")

    if CurveTest == 'y':
        if i%1==0:
            print('Progress: '+"%d%%" %(100*i/len(classification)) + ' || Picture ' + str(i) + ' created' , end="\r", flush=True)
        if i == len(classification)-1:
            print('100% all '+ str(len(classification)) + ' Pictures were created')

        #Creating figures
        plt.figure(figsize=(7,3))
        plt.subplot(121)
        plt.plot(raw_data[2*i],raw_data[2*i+1])
        plt.title('Manipulation Curve')
        plt.xlabel('Distance ($nm$)')
        plt.ylabel('I-Amplitude ($nA$)')

        plt.subplot(122)
        plt.plot(x,y)
        plt.title('FFT')
        plt.xlabel('Frequency ($Hz$)')
        plt.ylabel('Amplitude ($Unit$)')
        plt.ylim(-max(y)/100,max(y)/12)
        plt.xlim(max(x)/20,max(x))
        # Save figures of FFT In folder

        plt.tight_layout()
        plt.savefig('Output_Data\\FFT\\FFT'+str(i+3) + '.png',bbox_inches='tight', dpi=150, transparent=True)
        plt.close()

    if CurveTest == 'n' and flag == True:
        print('ok then... \n')
        print('--------------------------------------------------------------------------------------------------\n')
    flag = False

print('Added ' + str(N) + ' FFT curves to variables fft_data0,fft_data1 and fft_data2\n')

print('FFT sucessfuly calculated')

print('\n######################################################################################################## \n')


size_data0 = len(fft_data0)
size_data1 = len(fft_data1)
size_data2 = len(fft_data2)

#print(str(len(fft_data0)//3) + ' with classification 0 (no manipulation event)')
#print(str(len(fft_data1)//3) + ' with classification 1 (manipulation event detected)')
#print(str(len(fft_data2)//3) + ' with classification 2 (Curve not classified)')


# DAQUI PRA BAIXO EU NAO TENHO CERTEZA SE FUNCIONA AINDA!!!!

# Gabiarra pra nao transformar todos os dados que eu tenho em 1000
# f =  dados com 500 pontos usados pra simular dados

f0= [x for x in fft_data0 if len(x)==101]
f1 = [x for x in fft_data1 if len(x)==101]

# g = dados com pra testar a rede neural
g0 = [x for x in fft_data0 if len(x)==501]
g1 = [x for x in fft_data1 if len(x)==501]

print(len(f0)/2)
print(len(f1)/2)

print(len(g0)/2)
print(len(g1)/2)

print('---####################################################---')

###### Histogram #####
# Will have 4 histograms (0,1 and 0,2)

hf0 = np.zeros(101)
hf1 = np.zeros(101)

for i in range(len(f0)//2):
    hf0 = np.add(f0[2*i+1],hf0)

hf0 = hf0/101*10000000000
xxx = np.arange(101)

# ------------------------------------------------

for i in range(len(f1)//2):
    hf1 = np.add(f1[2*i+1],hf1)

hf1 = (hf1/101)*10000000000
xx = np.arange(101)

plt.figure(figsize=(7,3))
plt.subplot(121)

plt.plot(xxx,hf0)
plt.title('FFT')
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Counts')
plt.ylim(0,1.5)

plt.subplot(122)
plt.plot(xx,hf1)
plt.title('FFT')
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Counts')
plt.ylim(0,1.5)
plt.tight_layout()
plt.show()

# To do a histogram I need to sum all the Ys together and divide by the number of
# if they all have the same size it should be easy
# Could do it normalized and non normalized
