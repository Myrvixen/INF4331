import sympy as sym
from itertools import zip_longest

class Polynomial:

    def __init__(self, Coefficients):
        """coefficients should be a list of numbers with
        the i-th element being the coefficient a_i."""

        self.Coefficients = Coefficients
        self.N = len(Coefficients)


    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        deg = None

        for i in range(self.N):
            if self.Coefficients[self.N-i-1] != 0:
                deg = self.N - i -1
                break

        if deg == None:
            return -1
        else:
            return deg

    def coefficients(self):
        """Return the list of coefficients.

        The i-th element of the list should be a_i, meaning that the last
        element of the list is the coefficient of the highest degree term."""

        return self.Coefficients

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        Sum = 0
        for i in range(self.N):
            Sum += self.Coefficients[i]*x**i

        return Sum


    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""


        if type(p) == int:
            p = [p]
        else:
            p = p.Coefficients

        p_new = [x + y for x, y in zip_longest(self.Coefficients, p, fillvalue=0)]

        return Polynomial(p_new)
        

    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        if type(p) == int:
            p = [p]
        else:
            p = p.Coefficients

        p_new = [x - y for x, y in zip_longest(self.Coefficients, p, fillvalue=0)]

        return Polynomial(p_new)
        

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        if type(c) != int:
            print("c must be of type int.")
            raise ArithmeticError

        p_new = [c*self.Coefficients[i] for i in range(self.N)]

        return Polynomial(p_new)


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        p_new = [self.Coefficients[i]*c for i in range(self.N)]

        return Polynomial(p_new)

    def __repr__(self):
        """Return a nice string representation of polynomial.

        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """

        x = sym.symbols('x')

        #sym.simplify will remove eventual terms with 0 as coefficient
        p_sym = self.Coefficients[0]
        for i in range(1, self.N):
            p_sym = sym.simplify(p_sym + self.Coefficients[i]*x**i)

        return str(p_sym)

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

        '''Simply enough to check that these two string are the same, as __repr__
        will remove any terms with 0 as coefficient'''
        if str(self) == str(p):
            return True
        else:
            return False



def sample_usage():
    
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))


    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )

    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))

#sample_usage()
