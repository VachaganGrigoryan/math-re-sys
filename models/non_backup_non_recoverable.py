import numpy
import math
from functools import reduce
from .integral import Integral

import logging as log

from .math_errors import MathErrors

log.basicConfig(filename='text.log', filemode='w', format='%(levelname)s::%(message)s::%(asctime)s', level=log.DEBUG)
log.info("This is a non_backup_non_recoverable.py file")
numpy.seterr(divide='ignore', invalid='ignore')


class System:

    def __init__(self, t: int, dt: int) -> object:
        self._T = list(range(0, t + 1, dt))
        self._probability = [self.P(t) for t in self.T]
        self._distribution = [self.D(t) for t in self.T]
        self._failure_rate = [numpy.divide(d, p) for p, d in zip(self.probability, self.distribution)]

    @property
    def T(self):
        return self._T

    @property
    def probability(self):
        return self._probability

    @property
    def distribution(self):
        return self._distribution

    @property
    def failure_rate(self):
        return self._failure_rate

    def P(self, t: int) -> float:
        pass

    def D(self, t: int) -> float:
        pass


@MathErrors
class Weibull(System):

    def __init__(self, alpha, beta, t=5000, dt=100):
        self._alpha = alpha
        self._beta = beta
        System.__init__(self, t, dt)

    def P(self, t):
        return math.e ** (-(t / self._beta) ** self._alpha)

    def D(self, t):
        return ((self._alpha * t ** (self._alpha - 1)) / self._beta ** self._alpha) * math.e ** (
            -(t / self._beta) ** self._alpha)


@MathErrors
class Gamma(System):

    def __init__(self, alpha, beta, t=5000, dt=100):
        self._alpha = alpha
        self._beta = beta
        System.__init__(self, t, dt)

    def P(self, t):
        return 1 - (Integral.GammaFunc(self._alpha, 0, t / self._beta) / Integral.GammaFunc(self._alpha))

    def D(self, t):
        return (t ** (self._alpha - 1) * math.e ** -(t / self._beta)) / (
                self._beta ** self._alpha * Integral.GammaFunc(self._alpha))


@MathErrors
class Rayle(System):

    def __init__(self, lmd, t=5000, dt=100):
        self._lmd = lmd
        System.__init__(self, t, dt)

    def P(self, t):
        return math.e ** (-self._lmd * t ** 2)

    def D(self, t):
        return 2 * self._lmd * t * math.e ** (-self._lmd * t ** 2)


# @MathErrors
class Exponential(System):

    def __init__(self, lmd, t=5000, dt=100):
        self._lmd = lmd
        System.__init__(self, t, dt)

    def P(self, t):
        return math.e ** (-self._lmd * t)

    def D(self, t):
        return self._lmd * math.e ** (-self._lmd * t)


@MathErrors
class Normal(System):

    def __init__(self, m0, sig0, t=5000, dt=100):
        self._m0 = m0
        self._sig0 = sig0
        System.__init__(self, t, dt)

    def P(self, t):
        return (0.5 - Integral.LaplasFunc((t - self._m0) / self._sig0)) / (
                0.5 + Integral.LaplasFunc(self._m0 / self._sig0))

    def D(self, t):
        return math.e ** (-(t - self._m0) ** 2 / (2 * self._sig0 ** 2)) / (
                self._sig0 * math.sqrt(2 * math.pi) * (0.5 + Integral.LaplasFunc(self._m0 / self._sig0)))


class Consecutive(System):

    def __init__(self, lmds: list, t=1000, dt=100):
        self._lmds = lmds
        self._lmdFR = sum(self._lmds)
        self._Tc = 1 / self._lmdFR
        System.__init__(self, t, dt)

    @property
    def AverageUptime(self):
        return self._Tc

    def P(self, t):
        return math.e ** (-self._lmdFR * t)

    def D(self, t):
        return self._lmdFR * math.e ** (-self._lmdFR * t)



############################# END ##############################

# TODO ALL the code in belowe to need move in other file


def FailureFreeProbability(probs):
    ''' Pc = P1*P2*...*Pn '''
    return reduce(lambda p, nt: p * nt, probs)


def FailureRateSys(lmds=[]):
    ''' lmdC = sum all lmd's '''
    return sum(lmds)


def FailureRate(Pij, Dij):
    ''' lmd = f[i,j]/p[i,j] '''
    return Dij / Pij


def AverageUptime(lmdC):
    ''' Tc = 1 / lmdC '''
    return 1 / lmdC


def DensityDistribution(lmdC, Pc):
    ''' Fc = lmdC*Pc '''
    return lmdC * Pc
