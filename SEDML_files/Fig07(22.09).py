# To reproduce the data needed for Figure 4 in associated Physiome paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: %run Fig05.py
#

import opencor as opencor
# import numpy as np

Na_m = [0.13, 0.1275, 0.125, 0.1175, 0.11, 0.105]
Cl_m = [0.131, 0.1285, 0.126, 0.1185, 0.111, 0.106]
glucose_m = [0.0, 0.005, 0.01, 0.025, 0.04, 0.05]
#######

#Glucose flux
glucose_flux = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.states()["Basolateral_concentrations/glucose_s"] = 0.001
    # data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_flux[glu_m] = abs(ds.voi_and_variables()["GLUT2/J_GLUT"].values())
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("J_GLUT.csv", 'w')
cols = []
for key, item in glucose_flux.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
#######
#Glucose flux n_SGLT*3
glucose_flux = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.states()["Basolateral_concentrations/glucose_s"] = 0.001
    data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    # data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_flux[glu_m] = abs(ds.voi_and_variables()["GLUT2/J_GLUT"].values())
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("J_GLUT_n_SGLT.csv", 'w')
cols = []
for key, item in glucose_flux.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
#######
#Glucose flux n_GLUT*3
glucose_flux = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.states()["Basolateral_concentrations/glucose_s"] = 0.001
    data.constants()["A_GLUT2/n_GLUT"] = 126e7
    data.constants()["GLUT2/n_GLUT"] = 42e7
    # data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    # data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_flux[glu_m] = abs(ds.voi_and_variables()["GLUT2/J_GLUT"].values())
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("J_GLUT_n_GLUT.csv", 'w')
cols = []
for key, item in glucose_flux.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

#######
#Glucose flux n_GLUT*3
glucose_flux = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.states()["Basolateral_concentrations/glucose_s"] = 0.001
    data.constants()["A_GLUT2/n_GLUT"] = 126e7
    data.constants()["GLUT2/n_GLUT"] = 42e7
    data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    # data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_flux[glu_m] = ds.voi_and_variables()["GLUT2/J_GLUT"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("J_GLUT_n_GLUT_SGLT.csv", 'w')
cols = []
for key, item in glucose_flux.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()