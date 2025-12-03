import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math
import sys
import plot_func

# reload (plot_func)
import os

#glucose flux
data = pd.read_csv('J_GlUT.csv')
#glucose flux/SGLT*3
data1 = pd.read_csv('J_GLUT_n_SGLT.csv')
#glucose flux/GLUT*3
data2 = pd.read_csv('J_GLUT_n_GLUT.csv')
#glucose flux/SGLT*3,GLUT*3
data3 = pd.read_csv('J_GLUT_n_GLUT_SGLT.csv')


glucose_m = np.array([5, 10, 25, 40, 50])

Y = []
data_flux = [data, data1, data2, data3]

for j in range(4):
    temp = []
    for i in range(6):
        Y_last = list(data_flux[j][data_flux[j].keys()[i]] *36e8)[-1]
        temp.append(Y_last)
    Y.append(temp)

print(Y)

Y_normalised = []
for i in range(1,4):
    temp = []
    for j in range(1,6):
        Y_normal = Y[i][j]/Y[0][j]
        temp.append(Y_normal)
    Y_normalised.append(temp)

print(Y_normalised)


# plt.clf()
# ~ plt.subplot(221)
plt.figure(figsize=(12,8))
plt.axis([5, 50, 0.8, 4])

fig1 = plt.plot(glucose_m, Y_normalised[0], color='g', alpha=1, label="n_SGLT1*3", linewidth=2)
fig1 = plt.plot(glucose_m, Y_normalised[1], color='b', alpha=1, label="n_GLUT2*3", linewidth=2)
fig1 = plt.plot(glucose_m, Y_normalised[2], color='r',alpha=1, label="n_SGLT1&n_GLUT2*3", linewidth=2)

fig1 = plt.xlabel('Apical glucose Concentration (mM)', fontsize=20)
plt.tick_params(axis='both', labelsize=14)
fig1 = plt.ylabel('Normalized S.S Basolateral Glucose Flux (Pmole/hr)', fontsize=20)

plt.legend(loc='upper left',fontsize=14)

plt.show()


#
#
#
#
#
