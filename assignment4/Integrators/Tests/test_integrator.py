import sys
sys.path.append("..")  # Fetches the directory the current subdirectory is a part of
from integrator import integrate
from numpy_integrator import integrate_numpy

def test_integral_of_constant_function():

	f = lambda x: 2

	a = 0;  b = 1
	N1 = 10 ; N2 = 1000

	tol = 1e-10

	integral1 = integrate(f, a, b, N1)
	integral2 = integrate(f, a, b, N2)
	integral1_numpy = integrate_numpy(f, a, b, N1)
	integral2_numpy = integrate_numpy(f, a, b, N2)

	assert abs(integral1 - 2) < tol
	assert abs(integral2 - 2) < tol
	assert abs(integral1_numpy - 2) < tol
	assert abs(integral2_numpy - 2) < tol



def test_integral_of_linear_function():

	f = lambda x: 2*x

	a = 0;  b = 1

	N1 = 10 ; N2 = 1000
	tol = 1e-10

	integral1 = integrate(f, a, b, N1)
	integral2 = integrate(f, a, b, N2)
	integral1_numpy = integrate_numpy(f, a, b, N1)
	integral2_numpy = integrate_numpy(f, a, b, N2)

	assert abs(integral1 - 1) < 1.0/N1 + tol
	assert abs(integral2 - 1) < 1.0/N2 + tol
	assert abs(integral1_numpy - 1) < 1.0/N1 + tol
	assert abs(integral2_numpy - 1) < 1.0/N2 + tol


if __name__ == '__main__':
	test_integral_of_constant_function()
	test_integral_of_linear_function()
