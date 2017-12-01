from numpy import *
import time

def integrate_numpy(f, a, b, N):

	x = linspace(a, b, N+1)
	f_arr = zeros(N+1)
	dx = x[1]-x[0]
	f_arr[:] = f(x[:])

	Sum = sum(dx*f_arr[:-1])

	return Sum

def integrate_numpy_midpoint(f, a, b, N):

	x = linspace(a, b, N+1)
	f_arr = zeros(N+1)
	dx = x[1]-x[0]
	f_arr[:] = f(x[:] +0.5*dx)

	Sum = sum(dx*f_arr[:-1])

	return Sum

def time_numpy():
	t_start = time.clock()
	integral = integrate_numpy(lambda x : x*x, 0, 1, 150000000)
	t_stop = time.clock()
	print("Computation time: %.3f s" % (t_stop - t_start))

if __name__ == "__main__":
	time_numpy()
