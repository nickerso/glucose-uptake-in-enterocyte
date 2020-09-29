# To reproduce the data needed for Figure 2 in associated Physiome paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: %run Fig02.py
#

import opencor as opencor

simulation = opencor.open_simulation("Fig02.sedml")

# reset everything in case we are running interactively and have existing results
simulation.reset(True)

# run to steady-state
for i in range(0, 10):
    simulation.run()

# clear the results
simulation.clear_results()

# and run the steady-state simulation
simulation.run()