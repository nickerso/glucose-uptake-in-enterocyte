import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math
import sys
import plot_func

# reload (plot_func)
import os

#caco2-600seconds-with apical GLUT2
data = pd.read_csv('panel_A(inf).csv')
data1 = pd.read_csv('panel_A(Vc).csv')
data2 = pd.read_csv('panel_A(0.1Vc).csv')
data3 = pd.read_csv('panel_A(10Vc).csv')
#caco2-600seconds-without apical GLUT2
data4 = pd.read_csv('panel_B(inf).csv')
data5 = pd.read_csv('panel_B(Vc).csv')
data6 = pd.read_csv('panel_B(0.1Vc).csv')
data7 = pd.read_csv('panel_B(10Vc).csv')
#caco2-600seconds-without apical GLUT2, n_SGLT*2
data8 = pd.read_csv('panel_C(inf).csv')
data9 = pd.read_csv('panel_C(Vc).csv')
data10 = pd.read_csv('panel_C(0.1Vc).csv')
data11 = pd.read_csv('panel_C(10Vc).csv')
#caco2-600seconds-without apical GLUT2, n_SGLT*3
data12 = pd.read_csv('panel_D(inf).csv')
data13 = pd.read_csv('panel_D(Vc).csv')
data14 = pd.read_csv('panel_D(0.1Vc).csv')
data15 = pd.read_csv('panel_D(10Vc).csv')

glucose_m = np.array([0, 5, 10, 25, 40, 50])

Y_values = []
data_600 = [data, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11,
            data12, data13, data14, data15]

for j in range(16):
    temp = []
    for i in range(6):
        Y_last = list(data_600[j][data_600[j].keys()[i]] * 1000)[-1]
        temp.append(Y_last)
    Y_values.append(temp)

# print(Y)

Y = []
for i in range(16):
    temp = []
    for j in range(6):
        temp.append(Y_values[i][j] - Y_values[i][0])
    Y.append(temp)

print(Y)


mean_value = []
i = 0
while i < 6:
    avg = (Y[0][i] + Y[1][i] + Y[2][i]+ Y[3][i])/4
    mean_value.append(avg)
    i += 1



# Model:
ymc = mean_value
# Model error:
MSE = []

for i in range(6):
    tempo=[]
    for j in range(4):
        v = (mean_value[i]-Y[j][i])**2
        tempo.append(v)
    MSE.append(tempo)



MSE_A = []
for i in range(6):
        MSE_A.append(math.sqrt((MSE[i][0]+MSE[i][1]+MSE[i][2]+MSE[i][3])/4))



ymc_err = np.array(MSE_A)



# Exp(with apical glut2):
yec = np.array([0,9.2,14.8,25.2,32.1,35.97])
yec_err = np.array([0,1.2,1.2,0.9,1.2,2.0])
# # Exp: IEC6, 600 s
# yei_600 = np.array([0,6.44,9.6,13.6,15.2,15.7])
# yei_err_600 = np.array([0,1.4,1.4,2,2,2])


#set up interpolation for model
xi = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc, s=0)
ymci = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err, s=0)
ymc_erri = interpolate.splev(xi, tck, der = 0)


plt.figure(figsize=(12,12))
plt.subplot(221)
plt.axis([0, 51, 0, 50])
fig1 = plt.errorbar(glucose_m, yec, yerr=yec_err,fmt='ko', capsize=5, label="Caco2 expt")
#~ fig1 = plt.errorbar(x, yei, yerr=yei_err,fmt='go', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi, ymci-ymc_erri, ymci+ymc_erri, alpha=0.5, label="model with Apical GLUT2")
#~ fig1 = plt.fill_between(xi, ymii-ymi_erri, ymii+ymi_erri, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
plt.tick_params(axis='both', labelsize=12)
fig1 = plt.ylabel('Intracellular glucose (M)', fontsize=14)
plt.title('A')
plt.legend(loc='upper left', fontsize=12)
plt.subplots_adjust(wspace=0.3, hspace=0.3)

#######
#without apical GLUT2

mean_value = []
i = 0
while i < 6:
    avg = (Y[4][i] + Y[5][i] + Y[6][i]+ Y[7][i])/4
    mean_value.append(avg)
    i += 1



# Model:
ymc_B = mean_value
# Model error:
MSE = []

for i in range(6):
    tempo=[]
    for j in range(4,8):
        v = (mean_value[i]-Y[j][i])**2
        tempo.append(v)
    MSE.append(tempo)



MSE_B = []
for i in range(6):
        MSE_B.append(math.sqrt((MSE[i][0]+MSE[i][1]+MSE[i][2]+MSE[i][3])/4))



ymc_err_B = np.array(MSE_B)




# Exp:
yec_B = np.array([0,9.7,15.3,25.2,32.1,35.97])
yec_err_B = np.array([0,1,1,0.9,1.2,2.0])

#set up interpolation for model
xi_B = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_B, s=0)
ymci_B = interpolate.splev(xi_B, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_B, s=0)
ymc_erri_B = interpolate.splev(xi_B, tck, der = 0)

plt.subplot(222)
plt.axis([0, 51, 0, 50])
fig1 = plt.errorbar(glucose_m, yec_B, yerr=yec_err_B,fmt='ko', capsize=5, label="expt")
#~ fig1 = plt.errorbar(x_60, yei_60, yerr=yei_err_60,fmt='go', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_B, ymci_B-ymc_erri_B, ymci_B+ymc_erri_B, alpha=0.5, label="model without Apical GLUT2")
#~ fig1 = plt.fill_between(xi, ymii_60-ymi_erri_60, ymii_60+ymi_erri_60, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
plt.tick_params(axis='both', labelsize=12)
fig1 = plt.ylabel('Intracellular glucose (M)', fontsize=14)
plt.title('B')
plt.legend(loc='upper left', fontsize=12)
#######

#without apical GLUT2, n_SGLT*2

mean_value = []
i = 0
while i < 6:
    avg = (Y[8][i] + Y[9][i] + Y[10][i]+ Y[11][i])/4
    mean_value.append(avg)
    i += 1



# Model:
ymc_C = mean_value
# Model error:
MSE = []

for i in range(6):
    tempo=[]
    for j in range(8,12):
        v = (mean_value[i]-Y[j][i])**2
        tempo.append(v)
    MSE.append(tempo)



MSE_C = []
for i in range(6):
        MSE_C.append(math.sqrt((MSE[i][0]+MSE[i][1]+MSE[i][2]+MSE[i][3])/4))



ymc_err_C = np.array(MSE_C)

# Exp:
yec_C = np.array([0,9.7,15.3,25.2,32.1,35.97])
yec_err_C = np.array([0,1,1,0.9,1.2,2.0])

#set up interpolation for model
xi_C = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_C, s=0)
ymci_C = interpolate.splev(xi_C, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_C, s=0)
ymc_erri_C = interpolate.splev(xi_C, tck, der = 0)

plt.subplot(223)
plt.axis([0, 51, 0, 50])
fig1 = plt.errorbar(glucose_m, yec_C, yerr=yec_err_C,fmt='ko', capsize=5, label="expt")
#~ fig1 = plt.errorbar(x_300, yei_300, yerr=yei_err_300,fmt='go', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_C, ymci_C-ymc_erri_C, ymci_C+ymc_erri_C, alpha=0.5, label="without Apical_GLUT2 n_SGLT1*2")
#~ fig1 = plt.fill_between(xi, ymii_300-ymi_erri_300, ymii_300+ymi_erri_300, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
plt.tick_params(axis='both', labelsize=12)
fig1 = plt.ylabel('Intracellular glucose (M)', fontsize=14)
plt.title('C')
plt.legend(loc='upper left', fontsize=12)
#######


#without apical GLUT2, n_SGLT*3

mean_value = []
i = 0
while i < 6:
    avg = (Y[12][i] + Y[13][i] + Y[14][i]+ Y[15][i])/4
    mean_value.append(avg)
    i += 1



# Model:
ymc_D = mean_value
# Model error:
MSE = []

for i in range(6):
    tempo=[]
    for j in range(12,16):
        v = (mean_value[i]-Y[j][i])**2
        tempo.append(v)
    MSE.append(tempo)



MSE_D = []
for i in range(6):
        MSE_D.append(math.sqrt((MSE[i][0]+MSE[i][1]+MSE[i][2]+MSE[i][3])/4))



ymc_err_D = np.array(MSE_D)

# Exp:
yec_D = np.array([0,9.7,15.3,25.2,32.1,35.97])
yec_err_D = np.array([0,1,1,0.9,1.2,2.0])

#set up interpolation for model
xi_D = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_D, s=0)
ymci_D = interpolate.splev(xi_D, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_D, s=0)
ymc_erri_D = interpolate.splev(xi_D, tck, der = 0)

plt.subplot(224)
plt.axis([0, 51, 0, 50])
fig1 = plt.errorbar(glucose_m, yec_D, yerr=yec_err_D, fmt='ko', capsize=5, label="expt")
#~ fig1 = plt.errorbar(x_600, yei_600, yerr=yei_err_600,fmt='go', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_D, ymci_D-ymc_erri_D, ymci_D+ymc_erri_D, alpha=0.5, label="model Apical_GLUT2 n_SGLT1*3")
#~ fig1 = plt.fill_between(xi, ymii_600-ymi_erri_600, ymii_600+ymi_erri_600, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
plt.tick_params(axis='both', labelsize=12)
fig1 = plt.ylabel('Intracellular glucose (M)', fontsize=14)
plt.title('D')
plt.legend(loc='upper left', fontsize=12)
#######
plt.show()







