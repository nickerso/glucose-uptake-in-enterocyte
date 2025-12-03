# To reproduce the data needed for Figure 3 in associated Physiome paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: %run Fig03.py
#

import opencor as opencor

AE1_Cl = {}
# load the reference model - Thorsen
simulation = opencor.open_simulation("https://models.physiomeproject.org/workspace/572/rawfile/9214300ef1fdffa8db3115b2c18612da7f302d3c/Composite%20Model%20(Afshar%20vsThorsen).sedml")

# reset everything in case we are running interactively and have existing results
simulation.reset(True)

# run to steady-state
# for i in range(0, 1):
simulation.run()

# clear the results
simulation.clear_results()
# set the ending time
simulation.data().set_ending_point(300)
# and run the steady-state simulation
simulation.run()
for i in range(1):
    ds = simulation.results().data_store()
    AE1_Cl[i] = ds.voi_and_variables()["AE1/J_AE1_Cl"].values()

outfile = open("J_Cl.csv", 'w')
cols = []

for key, item in AE1_Cl.items():
    outfile.write(str(key) + ",")
    cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
#######

NHE3_Na = {}

simulation.run()
for i in range(1):
    ds = simulation.results().data_store()
    NHE3_Na[i] = ds.voi_and_variables()["NHE3/J_NHE3_Na"].values()



outfile = open("J_Na.csv", 'w')
cols = []

for key, item in NHE3_Na.items():
    outfile.write(str(key) + ",")
    cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

#######

CFTR = {}
simulation.run()
for i in range(1):
    ds = simulation.results().data_store()
    CFTR[i] = ds.voi_and_variables()["CFTR/J_CFTR"].values()

outfile = open("J_CFTR.csv", 'w')
cols = []

for key, item in CFTR.items():
    outfile.write(str(key) + ",")
    cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
########

ENaC = {}

simulation.run()
for i in range(1):
    ds = simulation.results().data_store()
    ENaC[i] = ds.voi_and_variables()["ENaC/J_ENaC"].values()



outfile = open("J_ENaC.csv", 'w')
cols = []

for key, item in ENaC.items():
    outfile.write(str(key) + ",")
    cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
#######

simulation = opencor.open_simulation("https://models.physiomeproject.org/workspace/5b8/rawfile/9228fb82a5fbade44d3e54d903710377759ffa77/Composite%20Model(Thorsen).sedml")

# reset everything in case we are running interactively and have existing results
simulation.reset(True)

# run to steady-state
# for i in range(0, 1):
simulation.run()

# clear the results
simulation.clear_results()
# set the ending time
simulation.data().set_ending_point(300)
# and run the steady-state simulation
simulation.run()

Cl_Dif = {}

for i in range(1):
    ds = simulation.results().data_store()
    Cl_Dif[i] = abs(ds.voi_and_variables()["Apical_Diffusion/J_D_Cl"].values())

outfile = open("J_Dif_Cl.csv", 'w')
cols = []

for key, item in Cl_Dif.items():
    outfile.write(str(key) + ",")
    cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()
#######

Na_Dif = {}

simulation.run()
for i in range(1):
    ds = simulation.results().data_store()
    Na_Dif[i] = abs(ds.voi_and_variables()["Apical_Diffusion/J_D_Na"].values())



outfile = open("J_Dif_Na.csv", 'w')
cols = []

for key, item in Na_Dif.items():
    outfile.write(str(key) + ",")
    cols.append(item)
outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

