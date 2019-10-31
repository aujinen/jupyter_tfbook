###
# Execute with Python 2.7 with numpy
# Convert "ORENIST.data" of Python 2.7 to "ORENIST3p2b.data" of Python 3.6 binary data
# Since conversion depends on the environment, trial and error are likely to be required.
# The following program is a successful conversion process on windows10.
# By H.Nishiyama
# 2018/07/16
###
import numpy as np
import pickle
file = open('ORENIST.data', 'r')
images, labels = pickle.load(file)
file.close()
file = open('ORENIST3p2b.data', 'wb')
pickle.dump([images,labels],file,protocol=2)
file.close()
