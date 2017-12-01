import cython_integrator as cy
import time

def time_cython():
    t_start = time.clock()
    integral = cy.integrate_cython(lambda x: x*x, 0, 1, 150000000)
    t_stop = time.clock()
    print("Computation time: %.3f s" % (t_stop - t_start))

if __name__ == "__main__":
    time_cython()
