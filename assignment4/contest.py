import numpy as np
import time
import sys
from Integrators.numba_integrator import integrate_numba_midpoint

a = 1e-20
b = 1e7

N = 300000000

s = "1.0/np.pi*"
l_f_e = []

# Generating each function following the pattern
for i,n in  enumerate([1,3,5,7,9,11,13,15]):
    s += "np.sin(x/%g)/(x/%g)*" %(n,n)
    l_f_e.append(s[:-1])

l_f_e.append("1.0/np.pi*np.sin(x)/x*np.sin(x/4)/(x/4)*np.sin(x/4)/(x/4)*np.sin(x/7)/(x/7)*np.sin(x/7)/(x/7)*\
np.sin(x/9)/(x/9)*np.sin(x/9)/(x/9)")

for e in l_f_e[2:]:
    # Here we run each func
    print("Function to be integrated: \n", e)
    func = eval("lambda x: %s" %e)

    t_start = time.clock()
    integral = integrate_numba_midpoint(func, a, b, N)
    t_stop = time.clock()

    print('Integral: ', integral)
    print("Computation time: %.3f \n" % (t_stop - t_start))
