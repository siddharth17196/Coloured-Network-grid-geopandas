#min max normalization
import numpy as np
import pickle


f = open('weights200.pkl','rb')
cgrid = pickle.load(f)
f.close()

n = cgrid.shape[0]
ma = np.max(cgrid)
mi = np.min(cgrid)
cgrid.shape
fgrid = np.zeros((n,n))		# to store normalized values

for i in range(n):
    for j in range(n):
        fgrid[i][j] = (cgrid[i][j]-mi)/(ma-mi)

f = open('norm_grid200.pkl', 'wb')		#store normalized values in a pickle file
pickle.dump(fgrid, f)
f.close()