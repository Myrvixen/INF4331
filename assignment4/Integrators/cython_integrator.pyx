import numpy as np
cimport numpy as np

cpdef double integrate_cython(f, double a, double b, int N):

  cdef np.ndarray[np.double_t, ndim=1] x, f_arr
  x = np.linspace(a, b, N+1, dtype=np.double)
  f_arr = np.zeros(N+1, dtype=np.double)
  f_arr[:] = f(x[:])

  cdef double dx = (b-a)/N
  cdef double Sum

  Sum = np.sum(dx*f_arr[:-1])

  return Sum

cpdef double integrate_cython_midpoint(f, double a, double b, int N):

  cdef np.ndarray[np.double_t, ndim=1] x, f_arr
  x = np.linspace(a, b, N+1, dtype=np.double)
  f_arr = np.zeros(N+1, dtype=np.double)

  cdef double dx = (b-a)/N
  cdef double Sum

  f_arr[:] = f(x[:]+0.5*dx)

  Sum = np.sum(dx*f_arr[:-1])

  return Sum
