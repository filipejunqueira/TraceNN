from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt


a = [2,6,4,5,9]

old_indices = np.arange(0,len(a))
new_length = 11
new_indices = np.linspace(0,len(a)-1,new_length)
spl = UnivariateSpline(old_indices,a,k=3,s=0)
new_array = spl(new_indices)



plt.plot(new_indices,new_array, 'g', lw=3)
plt.plot(old_indices,a, 'r', lw=3)

plt.show()
