from polynomials import Polynomial

def test_eval():

    # Choose to test the polynomial 2x^2 + 1
    p = Polynomial([1, 0, 2])

    #Checks that x = 0, 2, 4 gives the correct results 1, 5, and 17
    assert p(0) == 1
    assert p(2) == 9
    assert p(4) == 33


def test_add():

    # Choose the test polynomials 2x^2 + 1 and 2x^2 + x
    p = Polynomial([1, 0, 2])
    q = Polynomial([0, 1, 2])

    # Checks that these add up to the polynomial 4x^2 + x + 1
    r = p + q
    p_ex = [1, 1, 4]

    assert r.coefficients() == p_ex


def test_subtract():

    # Choose the test polynomials 2x^2 + 1 and 2x^2 + x
    p = Polynomial([1, 0, 2])
    q = Polynomial([0, 1, 2])

    # Checks that the former subtracted by the latter gives the polynomial
    # -x + 1
    r = p - q
    p_ex =  [1, -1, 0]

    assert r.coefficients() == p_ex

def test_degree():

    # Testing that the degree of both of these polynomials is 2
    p = Polynomial([1, 2, 3])
    q = Polynomial([1, 2, 3, 0, 0])

    deg_ex = 2
    assert p.degree() == deg_ex
    assert q.degree() == deg_ex

def test_repr():

    # Checks that the __repr__ method gives the correct string
    p = Polynomial([1, 2, 3])

    p_string = "3*x**2 + 2*x + 1"

    assert p == p_string

def test_mul():
    ''' Checks that both __mul__ and __rmul__ gives the right result'''

    p = Polynomial([1, 2, 3])

    q = p * 3
    r = 3 * p

    p_coeff = [3, 6, 9]

    assert q.coefficients() == p_coeff
    assert r.coefficients() == p_coeff