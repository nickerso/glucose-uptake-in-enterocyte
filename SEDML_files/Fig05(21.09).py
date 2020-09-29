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

#Caco2-600 with apical GLUT2
glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_A(inf).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)
# data.constants()["Basolateral_concentrations/theta"] = 1

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()
    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()

# cache results for plotting
outfile = open("panel_A(Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)
# data.constants()["Basolateral_concentrations/theta"] = 1

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()
    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 10
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()

# cache results for plotting
outfile = open("panel_A(10Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)
# data.constants()["Basolateral_concentrations/theta"] = 1

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()
    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 0.1
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()

# cache results for plotting
outfile = open("panel_A(0.1Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
######
#Caco2-600 without apical GLUT2
glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 0
    data.constants()["Cell_concentration/theta_26"] = 0  #Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_B(inf).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 1
    data.constants()["Cell_concentration/theta_26"] = 0  #Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_B(Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 10
    data.constants()["Cell_concentration/theta_26"] = 0  #Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_B(10Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 0.1
    data.constants()["Cell_concentration/theta_26"] = 0  #Apical GLUT2 is turned off
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_B(0.1Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
######
#Caco2-600 without apical GLUT2, n_SGLT*2


glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 0
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 8e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_C(inf).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)
# data.constants()["Basolateral_concentrations/theta"] = 1

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 1
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 8e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()

# cache results for plotting
outfile = open("panel_C(Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)
# data.constants()["Basolateral_concentrations/theta"] = 1

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()
    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 10
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 8e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()

# cache results for plotting
outfile = open("panel_C(10Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)
# data.constants()["Basolateral_concentrations/theta"] = 1

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 0.1
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 8e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()

# cache results for plotting
outfile = open("panel_C(0.1Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

######
#Caco2-600 without apical GLUT2, n_SGLT*3
glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 0
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_D(inf).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 1
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_D(Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 10
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_D(10Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

glucose_i = {}

simulation = opencor.open_simulation("test.sedml")
data = simulation.data()
data.set_ending_point(600)

for i, glu_m in enumerate(glucose_m):
    # reset everything in case we are running interactively and have existing results
    simulation.reset(True)
    simulation.clear_results()

    data.constants()["Basolateral_concentrations/theta"] = 1
    data.constants()["Basolateral_concentrations/m"] = 0.1
    data.constants()["Cell_concentration/theta_26"] = 0  # Apical GLUT2 is turned off
    data.constants()["phenomonological_constants/n_SGLT"] = 12e7
    data.constants()["Apical_concentrations/Na_m"] = Na_m[i]
    data.constants()["Apical_concentrations/Cl_m"] = Cl_m[i]
    data.constants()["Apical_concentrations/glucose_m"] = glu_m
    simulation.run()
    ds = simulation.results().data_store()
    glucose_i[glu_m] = ds.voi_and_variables()["Cell_concentration/glucose_i"].values()
    # print((glucose_i))
    # for key, value in glucose_i.items():
    #     print(key, value)

# cache results for plotting
outfile = open("panel_D(0.1Vc).csv", 'w')
cols = []
for key, item in glucose_i.items():
     outfile.write(str(key) + ",")
     cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

#######
