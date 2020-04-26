import numpy
import math
from const.integral import Integral

numpy.seterr(divide='ignore', invalid='ignore')


class SystemProperty:

    def __init__(self) -> object:
        self._probability = None
        self._distribution = None
        self._failure_rate = None

    @property
    def probability(self):
        return self._probability

    @property
    def distribution(self):
        return self._distribution

    @property
    def failure_rate(self):
        return self._failure_rate


class Method:

    class Weibull:

        @staticmethod
        def P(alpha, beta, t):
            return math.e ** (-(t / beta) ** alpha)

        @staticmethod
        def D(alpha, beta, t):
            return ((alpha * t ** (alpha - 1)) / beta ** alpha) * math.e ** (
                -(t / beta) ** alpha)


    class Gamma:

        @staticmethod
        def P(alpha, beta, t):
            return 1 - (Integral.GammaFunc(alpha, 0, t / beta) / Integral.GammaFunc(alpha))

        @staticmethod
        def D(alpha, beta, t):
            return (t ** (alpha - 1) * math.e ** -(t / beta)) / (
                    beta ** alpha * Integral.GammaFunc(alpha))


    class Rayle:

        @staticmethod
        def P(lmd, t):
            return math.e ** (-lmd * t ** 2)

        @staticmethod
        def D(lmd, t):
            return 2 * lmd * t * math.e ** (-lmd * t ** 2)


    class Exponential:

        @staticmethod
        def P(lmd, t):
            return math.e ** (-lmd * t)

        @staticmethod
        def D(lmd, t):
            return lmd * math.e ** (-lmd * t)


    class Normal:

        @staticmethod
        def P(m0, sig0, t):
            return (0.5 - Integral.LaplasFunc((t - m0) / sig0)) / (
                    0.5 + Integral.LaplasFunc(m0 / sig0))

        @staticmethod
        def D(m0, sig0, t):
            return math.e ** (-(t - m0) ** 2 / (2 * sig0 ** 2)) / (
                    sig0 * math.sqrt(2 * math.pi) * (0.5 + Integral.LaplasFunc(m0 / sig0)))


