# To reproduce the data needed for Figure 3 in associated Physiome paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: %run Fig03.py
#

import opencor as opencor
# import numpy as np

Na_m = [0.13, 0.1275, 0.125]
Cl_m = [0.131, 0.1285, 0.126]
glucose_m = [0.0, 0.005, 0.01]

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

# cache results for plotting
outfile = open("Fig04.csv", 'w')
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

