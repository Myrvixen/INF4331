import matplotlib.pylab as plt
from numpy import *
import time

def integrate(f, a, b, N):

	dx = (b-a)/N
	Sum = 0
	for i in range(N):
		Sum += dx*f(a + i*dx)

	return Sum

def integrate_midpoint(f, a, b, N):

	dx = (b-a)/N
	Sum = 0
	for i in range(N):
		Sum += dx*f(a + (i + 0.5)*dx)

	return Sum

def plot_error_of_squared_function():

	f = lambda x: x**2

	a = 0;  b = 1

	N = range(10, 20000, 10) # The different N-values to be computed
	error = zeros(len(N))

	int_exact = 1.0/3

	for i in range(len(N)):
		integral = integrate(f, a, b, N[i])
		error[i] = abs(integral - int_exact)

	plt.plot(N, error)
	plt.xlabel('N')
	plt.ylabel('Err(N)')
	plt.title('Numerical error of integration of f(x) = x^2')
	plt.show()

def time_integrator():
	t_start = time.clock()
	integral = integrate(lambda x : x*x, 0, 1, 150000000)
	t_stop = time.clock()
	print("Computation time: %.3f s" % (t_stop - t_start))

if __name__ == "__main__":
	plot_error_of_squared_function()
	time_integrator()
