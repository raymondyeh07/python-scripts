import numpy as np
import sys 

nmodules = float(sys.argv[1])
width = 40.
pricem2 = 30.

sizes = np.array([82., 38.])
module = np.array([3, 6])
nelems = module*nmodules

surf = np.sum(nelems * sizes) * width  * 1e-4
price = surf*pricem2

print 'width', width
print 'tailles', sizes
print 'nelems', nelems 
print 'surface', surf, 'price', price

