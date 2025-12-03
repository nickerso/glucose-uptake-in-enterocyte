import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math
import sys
import plot_func



data = pd.read_csv('J_Cl.csv')
data1 = pd.read_csv('J_Na.csv')
data2 = pd.read_csv('J_CFTR.csv')
data3 = pd.read_csv('J_ENaC.csv')
data4 = pd.read_csv('J_Dif_Cl.csv')
data5 = pd.read_csv('J_Dif_Na.csv')

X = np.arange(300)
# print(X)

Y = []
data_flux = [data, data1, data2, data3, data4, data5]

for i in range(6):
    Y_last = list(data_flux[i][data_flux[i].keys()[0]])
    Y.append(Y_last)
#
# print(Y)

Y_Cl_Na = []
for i in range(300):
    Y_Cl_Na.append(Y[0][i]/Y[1][i])

Y_CFTR_Cl = []
for i in range(300):
    Y_CFTR_Cl.append(Y[2][i]/Y[4][i])

Y_ENaC_Na = []
for i in range(300):
    Y_ENaC_Na.append(Y[3][i] / Y[5][i])
# print(Y_Cl_Na)

# print(data_flux)
#
# for i in range(2):
#     Y_last = list(data.keys()[i])
#     Y.append(Y_last)
#
# print(Y)

#reported proportion in the paper
Y_Thorsen = np.arange(300)
Y_Thorsen.fill(1)
print(Y_Thorsen)

# a = np.empty(10)
# a.fill(7)
# print(a)

plt.figure(figsize=(10,10))
plt.subplot(211)

x, y = plot_func.smooth_func(X,Y_Cl_Na,3,1,kind='linear')
# plt.subplot(211)
plt.plot(x, y, linestyle='--', color ='navy', markevery=1,  linewidth=3.0, label = 'AE1/NHE3 ratio(Current model)')

x, y = plot_func.smooth_func(X,Y_Thorsen,3,1,kind='linear')

plt.plot(x, y, linestyle='-', color ='navy', markevery=1,  linewidth=3.0, label = 'Cl/Na Co-transporter ratio(Thorsen model)''AE1/NHE3 ratio(Current model)')

plt.grid()
plt.xlim(0, 300)
plt.ylim(-0.1, 10)
plt.ylabel ('Flux Ratio',fontsize=16)
plt.tick_params(axis='both', labelsize= 12)
plt.xlabel ('time(s)',fontsize=16)
# plt.title('A' ,fontsize=20)
plt.legend(loc = 'best',fontsize=14)
# plt.show()
#
x, y = plot_func.smooth_func(X,Y_CFTR_Cl,3,1,kind='linear')
plt.subplot(212)
plt.plot(x, y, linestyle='-', color ='navy', markevery=1,  linewidth=3.0, label = 'CFTR flux/Cl Diffusion')

x, y = plot_func.smooth_func(X,Y_ENaC_Na,3,1,kind='linear')

plt.plot(x, y, linestyle='--', color ='navy', markevery=1,  linewidth=3.0, label = 'ENaC flux/Na Diffusion')


plt.grid()
plt.xlim(0, 300)
plt.ylim(-0.1, 8)
plt.ylabel ('Flux Ratio',fontsize=16)
plt.tick_params(axis='both', labelsize=12)
plt.xlabel ('time(s)',fontsize=16)
# plt.title('B' ,fontsize=20)
plt.legend(loc = 'best',fontsize=14)
plt.show()
#
#
#
# plt.subplots_adjust(bottom=0.5, right=0.8, top=1)
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
#
# #plt.savefig('Y:/Graphs/plot(30).png')
# plt.savefig('C:/Nima/ABI/Physiome Journal/Final Modular Version/Python codes/python_codes/fig08.png')
# plt.show()
# #~ plt.legend(loc=0)


