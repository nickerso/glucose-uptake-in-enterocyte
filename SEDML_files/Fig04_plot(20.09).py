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
ymc_600 = caco2_mean
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

ymc_err_600 = np.array(MSE_caco2_600)
# print(ymc_err_600)

#Model: IEC- 600 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[4][i] + Y[5][i] + Y[6][i]+ Y[7][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 600 s
ymi_600 = IEC_mean
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

ymi_err_600 = np.array(MSE_IEC_600)
print(ymi_err_600)

# Exp: Caco-2, 600 s
yec_600 = np.array([0,9.7,15.3,25.2,32.1,35.97])
yec_err_600 = np.array([0,1,1.5,1.5,3,3.5])
# Exp: IEC6, 600 s
yei_600 = np.array([0,6.44,9.6,13.6,15.2,15.7])
yei_err_600 = np.array([0,1.4,1.4,2,2,2])


#set up interpolation for model
xi_600 = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_600, s=0)
ymci_600 = interpolate.splev(xi_600, tck, der = 0)

#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_600, s=0)
ymc_erri_600 = interpolate.splev(xi_600, tck, der = 0)

#interpolate model data
tck = interpolate.splrep(glucose_m, ymi_600, s=0)
ymii_600 = interpolate.splev(xi_600, tck, der = 0)

#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymi_err_600, s=0)
ymi_erri_600 = interpolate.splev(xi_600, tck, der = 0)


plt.figure(figsize=(12,12))
plt.subplot(224)
plt.axis([0, 52, 0, 50])
fig1 = plt.errorbar(glucose_m, yec_600, yerr=yec_err_600,fmt='ko', capsize=5, label="Caco2 expt")
fig1 = plt.errorbar(glucose_m, yei_600, yerr=yei_err_600,fmt='ks', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_600, ymci_600-ymc_erri_600, ymci_600+ymc_erri_600, alpha=0.5, label="Caco2 model")
fig1 = plt.fill_between(xi_600, ymii_600-ymi_erri_600, ymii_600+ymi_erri_600, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
fig1 = plt.ylabel('Intracellular glucose (mM)', fontsize=14)
plt.title('D')
plt.legend(loc='best')
#
plt.subplots_adjust(wspace=0.3, hspace=0.3)

#######

caco2__mean = []
i = 0
while i < 6:
    avg = (Y[8][i] + Y[9][i] + Y[10][i]+ Y[11][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 300s
ymc_300 = caco2_mean
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

ymc_err_300 = np.array(MSE_caco2_300)
# print(ymc_err_300)

#Model: IEC- 300 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[12][i] + Y[13][i] + Y[14][i]+ Y[15][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 300 s
ymi_300 = IEC_mean
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

ymi_err_300 = np.array(MSE_IEC_300)
print(ymi_err_300)

# Exp: Caco-2, 300 s
yec_300 = np.array([0,9.84,14.9,21.3,25.2,27.5])
yec_err_300 = np.array([0,1,1.5,3,4,5])
# Exp: IEC6, 300 s
yei_300 = np.array([0,4,6.1,8.4,9.5,9.89])
yei_err_300 = np.array([0,1.4,1.4,2,2,2.5])


#set up interpolation for model
xi_300 = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_300, s=0)
ymci_300 = interpolate.splev(xi_300, tck, der = 0)

#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_300, s=0)
ymc_erri_300 = interpolate.splev(xi_300, tck, der = 0)

#interpolate model data
tck = interpolate.splrep(glucose_m, ymi_300, s=0)
ymii_300 = interpolate.splev(xi_300, tck, der = 0)

#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymi_err_300, s=0)
ymi_erri_300 = interpolate.splev(xi_300, tck, der = 0)

plt.subplot(223)
plt.axis([0, 52, 0, 50])
fig1 = plt.errorbar(glucose_m, yec_300, yerr=yec_err_300,fmt='ko', capsize=5, label="Caco2 expt")
fig1 = plt.errorbar(glucose_m, yei_300, yerr=yei_err_300,fmt='ks', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_300, ymci_300-ymc_erri_300, ymci_300+ymc_erri_300, alpha=0.5, label="Caco2 model")
fig1 = plt.fill_between(xi_300, ymii_300-ymi_erri_300, ymii_300+ymi_erri_300, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
fig1 = plt.ylabel('Intracellular glucose (mM)', fontsize=14)
plt.title('C')
plt.legend(loc='upper left')
#######

caco2__mean = []
i = 0
while i < 6:
    avg = (Y[16][i] + Y[17][i] + Y[18][i]+ Y[19][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 60s
ymc_60 = caco2_mean
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

ymc_err_60 = np.array(MSE_caco2_60)
# print(ymc_err_60)

#Model: IEC- 60 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[20][i] + Y[21][i] + Y[22][i]+ Y[23][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 60 s
ymi_60 = IEC_mean
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

ymi_err_60 = np.array(MSE_IEC_60)
print(ymi_err_60)

# Exp: Caco-2, 60 s
yec_60 = np.array([0,7.65,11.13,13.9,15.2,15.9])
yec_err_60 = np.array([0,0.4,0.7,0.7,0.7,0.7])
# Exp: IEC6, 60 s
yei_60 = np.array([0,1.2,1.8,2.4,2.66,2.76])
yei_err_60 = np.array([0,0.4,0.7,0.7,0.7,0.7])


#set up interpolation for model
xi_60 = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_60, s=0)
ymci_60 = interpolate.splev(xi_60, tck, der = 0)

#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_60, s=0)
ymc_erri_60 = interpolate.splev(xi_60, tck, der = 0)

#interpolate model data
tck = interpolate.splrep(glucose_m, ymi_60, s=0)
ymii_60 = interpolate.splev(xi_60, tck, der = 0)

#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymi_err_60, s=0)
ymi_erri_60 = interpolate.splev(xi_60, tck, der = 0)

plt.subplot(222)
plt.axis([0, 52, 0,30])
fig1 = plt.errorbar(glucose_m, yec_60, yerr=yec_err_60,fmt='ko', capsize=5, label="Caco2 expt")
fig1 = plt.errorbar(glucose_m, yei_60, yerr=yei_err_60,fmt='ks', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_60, ymci_60-ymc_erri_60, ymci_60+ymc_erri_60, alpha=0.5, label="Caco2 model")
fig1 = plt.fill_between(xi_60, ymii_60-ymi_erri_60, ymii_60+ymi_erri_60, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
fig1 = plt.ylabel('Intracellular glucose (mM)', fontsize=14)
plt.title('B')
plt.legend(loc='upper left')
#######

caco2__mean = []
i = 0
while i < 6:
    avg = (Y[24][i] + Y[25][i] + Y[26][i]+ Y[27][i])/4
    caco2__mean.append(avg)
    i += 1

caco2_mean = np.array(caco2__mean)


# Model: Caco-2, 30s
ymc_30 = caco2_mean
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

ymc_err_30 = np.array(MSE_caco2_30)
# print(ymc_err_30)

#Model: IEC- 30 sec
IEC__mean = []
i = 0
while i < 6:
    avg = (Y[28][i] + Y[29][i] + Y[30][i]+ Y[31][i])/4
    IEC__mean.append(avg)
    i += 1

IEC_mean = np.array(IEC__mean)

# Model: IEC6, 30 s
ymi_30 = IEC_mean
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

ymi_err_30 = np.array(MSE_IEC_30)
print(ymi_err_30)

# Exp: Caco-2, 30 s
yec_30 = np.array([0,6.07, 9.2, 10.9,11.8, 12.1])
yec_err_30 = np.array([0,0.4,0.7,0.7,0.7,0.7])

# Exp: IEC6, 30 s
yei_30 = np.array([0,0.59, 0.91, 1.38, 1.51, 1.55])
yei_err_30 = np.array([0,0.4,0.7,0.7,0.7,0.7])

#set up interpolation for model
xi_30 = np.linspace(0,50,100)
#interpolate model data
tck = interpolate.splrep(glucose_m, ymc_30, s=0)
ymci_30 = interpolate.splev(xi_30, tck, der = 0)
#interpolate model error bar
tck = interpolate.splrep(glucose_m, ymc_err_30, s=0)
ymc_erri_30 = interpolate.splev(xi_30, tck, der = 0)

tck = interpolate.splrep(glucose_m, ymi_30, s=0)
ymii_30 = interpolate.splev(xi_30, tck, der = 0)
tck = interpolate.splrep(glucose_m, ymi_err_30, s=0)
ymi_erri_30 = interpolate.splev(xi_30, tck, der = 0)




#plt.clf()

plt.subplot(221)
plt.axis([0, 52, 0, 30])
fig1 = plt.errorbar(glucose_m, yec_30, yerr=yec_err_30,fmt='ko', capsize=5, label="Caco2 expt")
fig1 = plt.errorbar(glucose_m, yei_30, yerr=yei_err_30,fmt='ks', capsize=5, label="IEC6 expt")
fig1 = plt.fill_between(xi_30, ymci_30-ymc_erri_30, ymci_30+ymc_erri_30, alpha=0.5, label="Caco2 model")
fig1 = plt.fill_between(xi_30, ymii_30-ymi_erri_30, ymii_30+ymi_erri_30, alpha=0.5, label="IEC6 model")
fig1 = plt.xlabel('Apical glucose (mM)', fontsize=14)
fig1 = plt.ylabel('Intracellular glucose (mM)', fontsize=14)
plt.title('A')
plt.legend(loc='upper left')

#######
plt.show()








