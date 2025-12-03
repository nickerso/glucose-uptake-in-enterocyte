import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import plot_func
# reload (plot_func)
import os
#~ root = 'D:/Nima/ABI/Python'
data_t = pd.read_csv('Fig03-thorsen.csv')
data_t
data_a = pd.read_csv('Fig03-afshar.csv')
X_name = 'parameters/time'
#~ X1_name = 'X2'
#~ X2_name = 'X3'
#~ X3_name = 'X3'
# y_name = 'pH_int'

# Afshar model
y1_name = 'Apical_voltage/v_mc'
y2_name = 'Basol_voltage/v_sc'
y3_name = 'Cell_concentration/glucose_i'
y4_name = 'Cell_concentration/Na_i'
y5_name = 'Cell_concentration/K_i'
y6_name = 'Cell_concentration/Cl_i'
y7_name = 'Apical_concentrations/glucose_m'
y15_name = 'Paracellular_voltage/v_ms'

# Thorsen model
y8_name = 'Apical_voltage/v_mc'
y9_name = 'Basol_voltage/v_sc'
y10_name = 'Cell_concentration/glucose_i'
y11_name = 'Cell_concentration/Na_i'
y12_name = 'Cell_concentration/K_i'
y13_name = 'Cell_concentration/Cl_i'
y14_name = 'Paracellular_voltage/v_ms'

#~ y7_name = 'glucose_m(Thorsen)'
#~ y8_name = 'v_mc(Thorsen)'
#~ y9_name = 'v_sc(Thorsen)'
#~ y10_name = 'glucose_i(Thorsen)'
#~ y11_name = 'sodium_i(Thorsen)'
#~ y12_name = 'potassium_i(Thorsen)'
#~ y13_name = 'chloride_i(Thorsen)'



X = data_a[X_name]
#~ X1 = data[X1_name]
#~ X2 = data[X2_name]
#~ X3 = data[X3_name]
#~ data.set_index(X,inplace=True)
# Y = data[y_name]
Y1 = data_a[y1_name] / data_t[y8_name].iat[-1]
Y2 = data_a[y2_name] / data_t[y9_name].iat[-1]
Y3 = data_a[y3_name] / data_t[y10_name].iat[-1]
Y4 = data_a[y4_name] / data_t[y11_name].iat[-1]
Y5 = data_a[y5_name] / data_t[y12_name].iat[-1]
Y6 = data_a[y6_name] / data_t[y13_name].iat[-1]
Y7 = data_t[y7_name] * 1000.0
Y8 = data_t[y8_name] / data_t[y8_name].iat[-1]
Y9 = data_t[y9_name] / data_t[y9_name].iat[-1]
Y10 = data_t[y10_name] / data_t[y10_name].iat[-1]
Y11 = data_t[y11_name] / data_t[y11_name].iat[-1]
Y12 = data_t[y12_name] / data_t[y12_name].iat[-1]
Y13 = data_t[y13_name] / data_t[y13_name].iat[-1]
Y14 = data_t[y14_name] / data_t[y14_name].iat[-1]
Y15 = data_a[y15_name] / data_t[y14_name].iat[-1]



plt.figure(figsize=(14,14))

x, y = plot_func.smooth_func(X,Y1,3,1,kind='linear')
plt.subplot(422)
plt.plot(x, y, 'navy',linestyle='-',  label = 'Apical Voltage-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y8,3,1,kind='linear')
plt.subplot(422)
plt.plot(x, y, 'navy', linestyle='--',  label = 'Apical Voltage-Thorsen Model', linewidth= 3)

plt.grid()
plt.xlim(0, 600)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)')
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Membrane Potential(mV)', fontsize=12)
# plt.title('B')
plt.legend(loc = 'best', fontsize=12)

x, y = plot_func.smooth_func(X,Y15,3,1,kind='linear')
plt.subplot(424)
plt.plot(x, y, 'navy',linestyle='-',  label = 'Transepithelial potential-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y14,3,1,kind='linear')
plt.subplot(424)
plt.plot(x, y, 'navy', linestyle='--',  label = 'Transepithelial potential-Thorsen Model', linewidth= 3)

plt.grid()
plt.xlim(0, 600)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)', fontsize= 12)
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Membrane Potential(mV)', fontsize= 12)
# plt.title('D')
plt.legend(loc = 'best', fontsize=12)


x, y = plot_func.smooth_func(X,Y2,3,1,kind='linear')
plt.subplot(423)
plt.plot(x, y, 'navy' ,linestyle='-',  label = 'Basolateral Voltage-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y9,3,1,kind='linear')
plt.subplot(423)
plt.plot(x, y, 'navy', linestyle='--',  label = 'Basolateral Voltage-Thorsen Model', linewidth= 3)
plt.grid()
plt.xlim(0, 600)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)', fontsize= 12)
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Membrane Potential(mV)', fontsize= 12)
# plt.title('C')
plt.legend(loc = 'best', fontsize=12)
x, y = plot_func.smooth_func(X,Y3,3,1,kind='linear')
plt.subplot(428)
plt.plot(x, y, 'navy',linestyle='-',  label = 'Glucose-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y10,3,1,kind='linear')
plt.subplot(428)
plt.plot(x, y, 'navy',linestyle='--',  label = 'Glucose-Thorsen Model', linewidth= 3)
plt.grid()
plt.xlim(0, 600)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)', fontsize= 12)
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Interacellular Concentration(mM)', fontsize= 12)
# plt.title('H')
plt.legend(loc = 'best', fontsize=12)
x, y = plot_func.smooth_func(X,Y4,3,1,kind='linear')
plt.subplot(425)
plt.plot(x, y, 'navy', linestyle='-', label = 'Sodium-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y11,3,1,kind='linear')
plt.subplot(425)
plt.plot(x, y, 'navy', linestyle='--', label = 'Sodium-Thorsen Model', linewidth= 3)
plt.grid()
plt.xlim(0, 600)
# plt.ylim(1, 1.25)
plt.xlabel ('time(s)', fontsize= 12)
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Interacellular Concentration(mM)', fontsize= 12)
# plt.title('E')
plt.legend(loc = 'best', fontsize=12)
x, y = plot_func.smooth_func(X,Y5,3,1,kind='linear')
plt.subplot(426)
plt.plot(x, y, 'navy',linestyle='-',  label = 'Potassium-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y12,3,1,kind='linear')
plt.subplot(426)
plt.plot(x, y, 'navy',linestyle='--',  label = 'Potassium-Thorsen Model', linewidth= 3)
plt.grid()
plt.xlim(0, 600)
plt.ylim(0.92, 1.04)
plt.xlabel ('time(s)', fontsize= 12)
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Interacellular Concentration(mM)', fontsize= 12)
# plt.title('F')
plt.legend(loc = 'best', fontsize=12)

x, y = plot_func.smooth_func(X,Y6,3,1,kind='linear')
plt.subplot(427)
plt.plot(x, y, 'navy',linestyle='-',  label = 'Chloride-Current Model', linewidth= 3)
x, y = plot_func.smooth_func(X,Y13,3,1,kind='linear')
plt.subplot(427)
plt.plot(x, y, 'navy',linestyle='--',  label = 'Chloride-Thorsen Model', linewidth= 3)
plt.grid()
plt.xlim(0, 600)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)', fontsize= 12)
plt.tick_params(axis='both', labelsize=12)
plt.ylabel ('Interacellular Concentration(mM)', fontsize= 12)
# plt.title('G')
plt.legend(loc = 'best', fontsize=12)

#~ x, y = plot_func.smooth_func(X,Y,3,1,kind='linear')
#~ plt.subplot(427)
#~ plt.plot(x, y, 'k', linestyle='-', label = 'pH')
#~
#~ plt.grid()
#~ plt.xlim(0, 1000)
#~ plt.ylim(0.0, 0.2)
#~ plt.xlabel ('time(s)')
#~ plt.ylabel ('Intracellular_pH')
#~ plt.title('G')
#~ plt.legend(loc = 'best')

x, y = plot_func.smooth_func(X,Y7,3,1,kind='linear')
plt.subplot(421)
plt.plot(x, y, 'navy',  label = 'Apical glucose stimulus', linewidth= 3)
#~ x, y = plot_func.smooth_func(X,Y14,3,1,kind='linear')
#~ plt.subplot(427)
#~ plt.plot(x, y, 'k', linestyle='--', label = 'Paracellular Membrane Potential-Exp')
plt.grid()
plt.xlim(0, 600)
plt.tick_params(axis='both', labelsize=12)
plt.ylim(0.0, 25)
plt.xlabel ('time(s)', fontsize= 12)
plt.ylabel ('Lumen Concentration(mM)', fontsize= 12)
# plt.title('A')
plt.legend(loc = 'best', fontsize=12)



#~ legend = ax.legend(loc='upper center', shadow=True)
#~ frame = legend.get_frame()
#~ frame.set_facecolor('0.90')
# Set the fontsize
#~ for label in legend.get_texts():
    #~ label.set_fontsize('small')
#~
#~ for label in legend.get_lines():
    #~ label.set_linewidth(1.5)  # the legend line width

#~ plt.xlim(0, 50)
#~ plt.ylim(0, 0.1)
#~ plt.xlabel ('')
#~ plt.ylabel ('')
#~ plt.title('Results')
#~ plt.xticks(np.arange(min(x), max(x)+1, 50))
#~ plt.legend(loc = 'best', fontsize='medium')
#~ plt.grid()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.savefig('fig03.png')
plt.show()
#~ plt.legend(loc=0)
