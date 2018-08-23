import numpy as np
import matplotlib.pyplot as plt
import scipy.signal


def downsample(y,downsampling):

    x = np.arange(len(y))
    downsampling = 10
    #scipy.signal.decimate(x, q, n=None, ftype='iir', axis=-1, zero_phase=True)

    Cut_y = scipy.signal.decimate(y, downsampling, n=None, ftype='iir', axis=-1, zero_phase=True)
    Cut_x = np.arange(len(Cut_y))

    print('\n Downsizing from ' + str(len(y)) + ' to ' + str(len(Cut_y)))

    return Cut_x, Cut_y

'''
    plt.figure(figsize=(7,3))
    plt.subplot(121)
    plt.plot(x,y)
    plt.subplot(122)
    plt.plot(Cut_x,Cut_y)
    plt.show()
'''
