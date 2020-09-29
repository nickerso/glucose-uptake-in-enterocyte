import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import math
import sys
import plot_func

# reload (plot_func)
import os

#caco2-600seconds
data = pd.read_csv('Caco2_600(inf).csv')
data1 = pd.read_csv('Caco2_600(Vc).csv')
data2 = pd.read_csv('Caco2_600(0.1Vc).csv')
data3 = pd.read_csv('Caco2_600(10Vc).csv')
#IEC-600seconds
data4 = pd.read_csv('IEC_600(inf).csv')
data5 = pd.read_csv('IEC_600(Vc).csv')
data6 = pd.read_csv('IEC_600(0.1Vc).csv')
data7 = pd.read_csv('IEC_600(10Vc).csv')
#caco2-300seconds
data8 = pd.read_csv('Caco2_300(inf).csv')
data9 = pd.read_csv('Caco2_300(Vc).csv')
data10 = pd.read_csv('Caco2_300(0.1Vc).csv')
data11 = pd.read_csv('Caco2_300(10Vc).csv')
#IEC-300seconds
data12 = pd.read_csv('IEC_300(inf).csv')
data13 = pd.read_csv('IEC_300(Vc).csv')
data14 = pd.read_csv('IEC_300(0.1Vc).csv')
data15 = pd.read_csv('IEC_300(10Vc).csv')

#caco2-60seconds
data16 = pd.read_csv('Caco2_60(inf).csv')
data17 = pd.read_csv('Caco2_60(Vc).csv')
data18 = pd.read_csv('Caco2_60(0.1Vc).csv')
data19 = pd.read_csv('Caco2_60(10Vc).csv')
#IEC-60seconds
data20 = pd.read_csv('IEC_60(inf).csv')
data21 = pd.read_csv('IEC_60(Vc).csv')
data22 = pd.read_csv('IEC_60(0.1Vc).csv')
data23 = pd.read_csv('IEC_60(10Vc).csv')

#caco2-30seconds
data24 = pd.read_csv('Caco2_30(inf).csv')
data25 = pd.read_csv('Caco2_30(Vc).csv')
data26 = pd.read_csv('Caco2_30(0.1Vc).csv')
data27 = pd.read_csv('Caco2_30(10Vc).csv')
#IEC-30seconds
data28 = pd.read_csv('IEC_30(inf).csv')
data29 = pd.read_csv('IEC_30(Vc).csv')
data30 = pd.read_csv('IEC_30(0.1Vc).csv')
data31 = pd.read_csv('IEC_30(10Vc).csv')

glucose_m = np.array([0, 5, 10, 25, 40, 50])

Y_values = []
data_600 = [data, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11,
            data12, data13, data14, data15, data16, data17, data18, data19,data20, data21, data22,
            data23, data24, data25, data26, data27, data28, data29, data30, data31]

for j in range(32):
    temp = []
    for i in range(6):
        Y_last = list(data_600[j][data_600[j].keys()[i]] * 1000)[-1]
        temp.append(Y_last)
    Y_values.append(temp)

# print(Y)

Y = []
for i in range(32):
    temp = []
    for j in range(6):
        temp.append(Y_values[i][j] - Y_values[i][0])
    Y.append(temp)

print(Y)

caco2__mean = []
i = 0
while i < 6:
    avg = (Y[0][i] + Y[1][i] + Y[2][i]+ Y[3][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 600s
y_600_C = caco2_mean
# Model: Caco-2, error, 600s
MSE_caco2 = []

for i in range(6):
    tempo=[]
    for j in range(4):
        v = (caco2_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_caco2.append(tempo)
# print(MSE_caco2)


MSE_caco2_600 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_caco2[i][0]+MSE_caco2[i][1]+MSE_caco2[i][2]+MSE_caco2[i][3])/4)
        MSE_caco2_600.append(MSE_values)
# print(MSE_caco2_600)

y_600_C_err = np.array(MSE_caco2_600)
# print(ymc_err_600)


#######

#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_600_C, s=0)
y_600_C_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_600_C_err, s=0)
y_600_C_err_i = interpolate.splev(xi, tck, der = 0)
########


caco2__mean = []
i = 0
while i < 6:
    avg = (Y[8][i] + Y[9][i] + Y[10][i]+ Y[11][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 300s
y_300_C = caco2_mean
# Model: Caco-2, error, 300s
MSE_caco2 = []

for i in range(6):
    tempo=[]
    for j in range(8,12):
        v = (caco2_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_caco2.append(tempo)
# print(MSE_caco2)


MSE_caco2_300 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_caco2[i][0]+MSE_caco2[i][1]+MSE_caco2[i][2]+MSE_caco2[i][3])/4)
        MSE_caco2_300.append(MSE_values)
# print(MSE_caco2_300)

y_300_C_err = np.array(MSE_caco2_300)
# print(ymc_err_300)

#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_300_C, s=0)
y_300_C_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_300_C_err, s=0)
y_300_C_err_i = interpolate.splev(xi, tck, der = 0)

#######

caco2__mean = []
i = 0
while i < 6:
    avg = (Y[16][i] + Y[17][i] + Y[18][i]+ Y[19][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 60s
y_60_C = caco2_mean
# Model: Caco-2, error, 60s
MSE_caco2 = []

for i in range(6):
    tempo=[]
    for j in range(16,20):
        v = (caco2_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_caco2.append(tempo)
# print(MSE_caco2)


MSE_caco2_60 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_caco2[i][0]+MSE_caco2[i][1]+MSE_caco2[i][2]+MSE_caco2[i][3])/4)
        MSE_caco2_60.append(MSE_values)
# print(MSE_caco2_60)

y_60_C_err = np.array(MSE_caco2_60)
# print(ymc_err_60)

#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_60_C, s=0)
y_60_C_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_60_C_err, s=0)
y_60_C_err_i = interpolate.splev(xi, tck, der = 0)
#######

caco2__mean = []
i = 0
while i < 6:
    avg = (Y[24][i] + Y[25][i] + Y[26][i]+ Y[27][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 30s
y_30_C = caco2_mean
# Model: Caco-2, error, 30s
MSE_caco2 = []

for i in range(6):
    tempo=[]
    for j in range(24,28):
        v = (caco2_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_caco2.append(tempo)
# print(MSE_caco2)


MSE_caco2_30 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_caco2[i][0]+MSE_caco2[i][1]+MSE_caco2[i][2]+MSE_caco2[i][3])/4)
        MSE_caco2_30.append(MSE_values)
# print(MSE_caco2_30)

y_30_C_err = np.array(MSE_caco2_30)
# print(ymc_err_30)
#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_30_C, s=0)
y_30_C_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_30_C_err, s=0)
y_30_C_err_i = interpolate.splev(xi, tck, der = 0)
#######
plt.figure(figsize=(6,8))
plt.clf()
plt.subplot(211)
plt.axis([0, 50, 0, 50])
#~ fig1 = plt.errorbar(x, yec, yerr=yec_err,fmt='ko', capsize=5, label="Caco2 expt")
#~ fig1 = plt.errorbar(x, yei, yerr=yei_err,fmt='go', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi, y_30_C_i-y_30_C_err_i, y_30_C_i+y_30_C_err_i, color='orange', alpha=0.5, label = '30 Seconds')
fig1 = plt.fill_between(xi, y_60_C_i-y_60_C_err_i, y_60_C_i+y_60_C_err_i, color='r', alpha=0.5, label = '60 Seconds')
fig1 = plt.fill_between(xi, y_300_C_i-y_300_C_err_i, y_300_C_i+y_300_C_err_i, color='g', alpha=0.5, label = '300 Seconds')
fig1 = plt.fill_between(xi, y_600_C_i-y_600_C_err_i, y_600_C_i+y_600_C_err_i, color='b', alpha=0.5, label = '600 Seconds')

fig1 = plt.xlabel('Apical glucose Concentration(mM)', fontsize=10)
fig1 = plt.ylabel('Intracellular glucose Concentration(mM))', fontsize=10)
plt.legend(loc='upper left')

textstr = 'CaCO2'

#~ ax.hist(x, 50)
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
plt.text(25, 48, textstr,  fontsize=12,
        verticalalignment='top', bbox=props)

#######

#Model: IEC- 600 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[4][i] + Y[5][i] + Y[6][i]+ Y[7][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 600 s
y_600_I = IEC_mean
# print(ymi_600)
# Model: IEC, error, 600s
MSE_IEC = []
for i in range(6):
    tempo=[]
    for j in range(4,8):
        v = (IEC_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_IEC.append(tempo)
# print(MSE_IEC)


MSE_IEC_600 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_IEC[i][0]+MSE_IEC[i][1]+MSE_IEC[i][2]+MSE_IEC[i][3])/4)
        MSE_IEC_600.append(MSE_values)
# print(MSE_IEC_600)

y_600_I_err = np.array(MSE_IEC_600)

#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_600_I, s=0)
y_600_I_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_600_I_err, s=0)
y_600_I_err_i = interpolate.splev(xi, tck, der = 0)
#######

#Model: IEC- 300 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[12][i] + Y[13][i] + Y[14][i]+ Y[15][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 300 s
y_300_I = IEC_mean
# print(ymi_300)
# Model: IEC, error, 300s
MSE_IEC = []
for i in range(6):
    tempo=[]
    for j in range(12,16):
        v = (IEC_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_IEC.append(tempo)
# print(MSE_IEC)


MSE_IEC_300 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_IEC[i][0]+MSE_IEC[i][1]+MSE_IEC[i][2]+MSE_IEC[i][3])/4)
        MSE_IEC_300.append(MSE_values)
# print(MSE_IEC_300)

y_300_I_err = np.array(MSE_IEC_300)
#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_300_I, s=0)
y_300_I_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_300_I_err, s=0)
y_300_I_err_i = interpolate.splev(xi, tck, der = 0)
#######

#Model: IEC- 60 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[20][i] + Y[21][i] + Y[22][i]+ Y[23][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 60 s
y_60_I = IEC_mean
# print(ymi_60)
# Model: IEC, error, 60s
MSE_IEC = []
for i in range(6):
    tempo=[]
    for j in range(20,24):
        v = (IEC_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_IEC.append(tempo)
# print(MSE_IEC)


MSE_IEC_60 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_IEC[i][0]+MSE_IEC[i][1]+MSE_IEC[i][2]+MSE_IEC[i][3])/4)
        MSE_IEC_60.append(MSE_values)
# print(MSE_IEC_60)

y_60_I_err = np.array(MSE_IEC_60)
#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_60_I, s=0)
y_60_I_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_60_I_err, s=0)
y_60_I_err_i = interpolate.splev(xi, tck, der = 0)
#######

#Model: IEC- 30 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[28][i] + Y[29][i] + Y[30][i]+ Y[31][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 30 s
y_30_I = IEC_mean
# print(ymi_30)
# Model: IEC, error, 30s
MSE_IEC = []
for i in range(6):
    tempo=[]
    for j in range(28,32):
        v = (IEC_mean[i]-Y[j][i])**2
        tempo.append(v)
    MSE_IEC.append(tempo)
# print(MSE_IEC)


MSE_IEC_30 = []
for i in range(6):
        MSE_values = math.sqrt((MSE_IEC[i][0]+MSE_IEC[i][1]+MSE_IEC[i][2]+MSE_IEC[i][3])/4)
        MSE_IEC_30.append(MSE_values)
# print(MSE_IEC_30)

y_30_I_err = np.array(MSE_IEC_30)

#set up interpolation for model
xi = np.linspace(0,100,50)
#interpolate model data
tck = interpolate.splrep(glucose_m, y_30_I, s=0)
y_30_I_i = interpolate.splev(xi, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, y_30_I_err, s=0)
y_30_I_err_i = interpolate.splev(xi, tck, der = 0)
#######
plt.subplot(212)
plt.axis([0, 50, 0, 30])

fig1 = plt.fill_between(xi, y_30_I_i-y_30_I_err_i, y_30_I_i+y_30_I_err_i, color='orange', alpha=0.5, label = '30 Seconds')
fig1 = plt.fill_between(xi, y_60_I_i-y_60_I_err_i, y_60_I_i+y_60_I_err_i, color='r', alpha=0.5, label = '60 Seconds')
fig1 = plt.fill_between(xi, y_300_I_i-y_300_I_err_i, y_300_I_i+y_300_I_err_i, color='g', alpha=0.5, label = '300 Seconds')
fig1 = plt.fill_between(xi, y_600_I_i-y_600_I_err_i, y_600_I_i+y_600_I_err_i, color='b', alpha=0.5, label = '600 Seconds')
fig1 = plt.xlabel('Apical glucose Concentration(mM)', fontsize=10)
fig1 = plt.ylabel('Intracellular glucose Concentration(mM))', fontsize=10)
plt.legend(loc='upper left')

textstr = 'IEC6'

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
plt.text(25, 29, textstr,  fontsize=12,
        verticalalignment='top', bbox=props)

plt.show()