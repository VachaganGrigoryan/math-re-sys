
import math
from functools import reduce

from .integral import *


class Probability:

    def __init__(self):
        pass


    def Weibull(self, t, alpha, beta):
        return math.e**(-(t/beta)**alpha)

    
    def Gamma(self, t, alpha, beta):
        return 1-(Integral.GammaFunc(alpha, 0, t/beta)/Integral.GammaFunc(alpha))


    def Rayle(self, t, lmd):
        return math.e**(-lmd*t**2)


    def Exponential(self, t, lmd):
        return math.e**(-lmd*t)


    def Normal(self, t, m0, sig0):
        return (0.5-Integral.LaplasFunc((t-m0)/sig0))/(0.5+Integral.LaplasFunc(m0/sig0))


    @staticmethod
    def FailureFreeProbability(probs):
        ''' Pc = P1*P2*...*Pn '''
        return reduce(lambda p, nt: p*nt, probs)

    @staticmethod
    def FailureRateSys(lmds=[]):
        ''' lmdC = sum all lmd's '''
        return sum(lmds)


    @staticmethod
    def FailureRate(Pij, Fij):
        ''' lmd = f[i,j]/p[i,j] '''
        return Fij/Pij

    @staticmethod
    def AverageUptime(lmdC):
        ''' Tc = 1 / lmdC '''
        return 1/lmdC

if __name__ == "__main__":
    pass