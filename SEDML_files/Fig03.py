# To reproduce the data needed for Figure 3 in associated Physiome paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: %run Fig03.py
#

import opencor as opencor

# load the reference model - Thorsen
simulation = opencor.open_simulation("https://models.physiomeproject.org/workspace/5b8/rawfile/9228fb82a5fbade44d3e54d903710377759ffa77/Composite%20Model(Thorsen).sedml")

# reset everything in case we are running interactively and have existing results
simulation.reset(True)

# run to steady-state
for i in range(0, 1):
    simulation.run()

# clear the results
simulation.clear_results()
# set the ending time
simulation.data().set_ending_point(600)
# and run the steady-state simulation
simulation.run()

# cache the reference results
ds = simulation.results().data_store()
variables = ds.voi_and_variables()
outfile = open("Fig03-thorsen.csv", 'w')
cols = []
for key, item in variables.items():
    outfile.write(key + ",")
    cols.append(list(item.values()))

outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()

# load the current model
simulation = opencor.open_simulation("Fig02.sedml")

# reset everything in case we are running interactively and have existing results
simulation.reset(True)

# run to steady-state
for i in range(0, 1):
    simulation.run()

# clear the results
simulation.clear_results()
# and run the steady-state simulation
simulation.run()

# cache the reference results
ds = simulation.results().data_store()
variables = ds.voi_and_variables()
outfile = open("Fig03-afshar.csv", 'w')
cols = []
for key, item in variables.items():
    outfile.write(key + ",")
    cols.append(list(item.values()))

outfile.write("\n")

for i in range(0, len(cols[0])):
    for j in range(0, len(cols)):
        outfile.write(str(cols[j][i]) + ",")
    outfile.write("\n")
outfile.close()