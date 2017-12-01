import time
from numba import jit

def integrate_numba(f, a, b, N):

	# Makes the input function "parseable"
	f_jit = jit("f8(f8)", nopython = True)(f)

	@jit("f8(f8, f8, i8)", nopython=True)
	def call(a, b, N):

		dx = (b-a)/N
		Sum = 0
		for i in range(N):
			Sum += dx*f_jit(a+i*dx)

		return Sum

	return call(a,b,N)

def integrate_numba_midpoint(f, a, b, N):

	f_jit = jit("f8(f8)", nopython = True)(f)

	@jit("f8(f8, f8, i8)", nopython=True)
	def call(a, b, N):

		dx = (b-a)/N
		Sum = 0
		for i in range(N):
			Sum += dx*f_jit(a+(i + 0.5)*dx)

		return Sum

	return call(a,b,N)

def time_numba():
	t_start = time.clock()
	integral = integrate_numba(lambda x: x*x, 0, 1, 150000000)
	t_stop = time.clock()
	print("Computation time: %.3f s" % (t_stop - t_start))

if __name__ == "__main__":
	time_numba()
