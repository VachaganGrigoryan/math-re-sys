import numpy
import math
from functools import reduce
from .integral import Integral

import logging as log

log.basicConfig(filename='text.log', filemode='w', format='%(levelname)s::%(message)s::%(asctime)s', level=log.DEBUG)
log.info("This is a non_recoverable_non_backup.py file")
numpy.seterr(divide='ignore', invalid='ignore')

class MathErrors:

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        try:
            return self.cls(*args, **kwargs)
        except:
            return None


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


@MathErrors
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


############################# END ##############################

# TODO ALL the code in belowe to need move in other file

class RNR:

    def __init__(self, m, lmd, t=100):
        self.m = m
        self.lmd = lmd
        self.T = list(range(0, t, 5))

    @property
    def probability(self):
        return [1 - (1 - Exponential.P(self.lmd, t)) ** (self.m + 1) for t in self.T]

    @property
    def distribution(self):
        return [((self.m + 1) * Exponential.D(self.lmd, t) ** self.m) * (1 - Exponential.P(self.lmd, t)) ** self.m for t
                in self.T]

    @property
    def system_failure_rate(self):
        return [d / p for p, d in zip(self.probability, self.distribution)]

    # @property
    # def func1(self):
    #     pass

    # @property
    # def func2(self):
    #     pass

    # @property
    # def func3(self):
    #     pass

    # @property
    # def func4(self):
    #     pass


class NRR:

    def __init__(self, lmd, myu, t):
        self.lmd = lmd
        self.myu = myu
        self.lmdC = sum(lmd)
        self.myuC = myu[0]
        self.T = list(range(0, t, 2))

    def IntensityOfFailure(self, t):
        return self.myuC / (self.lmdC + self.myuC) + self.lmdC * math.e ** (-(self.lmdC + self.myuC) * t) / (
                self.lmdC + self.myuC)

    # def IntensityOfRecovery(self):

    # pass
    @property
    def FunctionAvailability(self):
        ''' Kg(t) = myu/(lmdC+myu) + lmdC/(lmdC+myu) '''
        return [self.IntensityOfFailure(t) for t in self.T]

    def CoefficientAvailability(self):
        ''' Kg = T/(T+Tv) '''
        return 1 / (1 + sum(lmd / myu for lmd, myu in zip(self.lmd, self.myu)))

    # @staticmethod
    def TimeBetweenFailures(self):
        ''' T = 1/lmd '''
        return 1 / self.lmdC

    # @staticmethod
    def AverageTimeOfSystemRecovery(self):
        ''' Tv = sum(lmd[i]/myu[i])/lmdC '''
        return sum(lmd / myu for lmd, myu in zip(self.lmd, self.myu)) / self.lmdC


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
