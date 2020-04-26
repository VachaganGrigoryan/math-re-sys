from scipy.integrate import quad
import numpy
import math


class Integral:

    def __init__(self):
        pass

    @staticmethod
    def GammaFunc(alpha, start=0, stop=numpy.Inf):
        """ Gamma integral """
        return quad(lambda x, alpha: x ** (alpha - 1) * math.e ** (-x), start, stop, args=(alpha))[0]

    @staticmethod
    def LaplasFunc(t):
        """ Laplas integral """
        return (1 / math.sqrt(2 * math.pi)) * quad(lambda x: math.e ** (-(x ** 2 / 2)), 0, t)[0]
