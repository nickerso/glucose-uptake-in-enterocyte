import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math
import sys
import plot_func

# reload (plot_func)
import os

#glucose flux/SGLT
data = pd.read_csv('J_Gl_SGLT.csv')
#glucose flux/GLUT
data1 = pd.read_csv('J_Gl_GLUT.csv')


glucose_m = np.array([0, 5, 10, 25, 40, 50])

Y = []
data_flux = [data, data1]

for j in range(2):
    temp = []
    for i in range(6):
        Y_last = list(data_flux[j][data_flux[j].keys()[i]] *36e8)[-1]
        temp.append(Y_last)
    Y.append(temp)

for i in range(2):
    Y[i][0] = 0


print(Y)

x, y = plot_func.smooth_func(glucose_m,Y[0],91,1,kind='linear')
#~ plt.subplot(212)
plt.plot(x, y, 'k' ,linestyle='-',  label = 'SGLT1 Flux',linewidth=3)

x, y = plot_func.smooth_func(glucose_m,Y[1],51,1,kind='linear')
#~ plt.subplot(212)
plt.plot(x, y, 'k', linestyle='--',  label = 'GLUT2 Flux',linewidth=3)


Y_total = []
for i in range(6):
    Y_value = Y[0][i] + Y[1][i]
    Y_total.append(Y_value)

x, y = plot_func.smooth_func(glucose_m,Y_total,91,1,kind='linear')
#~ plt.subplot(212)
plt.plot(x, y, 'k', linestyle=':',  label = 'GLUT2 Flux',linewidth=3)

plt.grid()
plt.xlim(0, 50)
plt.ylim(0, 1)
plt.ylabel ('Glucose flux(Pmole/h)',fontsize=16)
plt.xlabel ('Extracellular Glucose Concentration(mM)',fontsize=16)
#~ plt.title('b)' ,fontsize=22)
plt.legend(loc = 'best',fontsize=12)

plt.show()


#
#
#
#
#
