from Integrators.integrator import *
from Integrators.numpy_integrator import *
from Integrators.numba_integrator import *
from Integrators.cython_integrator import *
import numpy as np
import time

methods = [integrate, integrate_midpoint, integrate_numpy, integrate_numpy_midpoint, \
            integrate_numba, integrate_numba_midpoint, integrate_cython, integrate_cython_midpoint]

a = 0
b = np.pi

f = lambda x: np.sin(x)
tol = 1e-10

for method in methods:
    N = 0
    error = 10000
    t_start = time.clock()
    while error > tol:
        N += 1000
        integral = method(f, a, b, N)
        error = abs(integral - 2)
    t_stop = time.clock()

    print('Required N for %s method: %i || time: %.3f s' % (method.__name__, N, t_stop-t_start))
