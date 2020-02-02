import math
from functools import reduce
from .integral import *


import logging as log
log.basicConfig(filename='text.log', filemode='w', format='%(levelname)s::%(message)s::%(asctime)s', level=log.DEBUG)
log.info("This is a asr.py file")

class Weibull:

    def __init__(self, alpha, beta, t=5000):
        self.alpha = alpha
        self.beta = beta
        self.t = t
        self.T = list(range(0, t, 100))
    

    @property
    def probability(self):
        return [self.P(self.alpha, self.beta, t) for t in self.T]
    

    @property
    def distribution(self):
        return [self.D(self.alpha, self.beta, t) for t in self.T]

 
    @staticmethod
    def P(alpha, beta, t):
        return math.e**(-(t/beta)**alpha)


    @staticmethod
    def D(alpha, beta, t):
        return ((alpha*t**(alpha-1))/beta**alpha)*math.e**(-(t/beta)**alpha)


class Gamma:

    def __init__(self, alpha, beta, t=5000):
        self.alpha = alpha
        self.beta = beta
        self.t = t
        self.T = list(range(0,t,100))
    

    @property
    def probability(self):
        return [self.P(self.alpha, self.beta, t) for t in self.T]
    

    @property
    def distribution(self):
        return [self.D(self.alpha, self.beta, t) for t in self.T]

 
    @staticmethod
    def P(alpha, beta, t):
        return 1-(Integral.GammaFunc(alpha, 0, t/beta)/Integral.GammaFunc(alpha))


    @staticmethod
    def D(alpha, beta, t):
        return (t**(alpha-1)*math.e**-(t/beta))/(beta**alpha*Integral.GammaFunc(alpha))
    


class Rayle:

    def __init__(self, lmd, t=5000):
        self.lmd = lmd
        self.t = t
        self.T = list(range(0,t,100))
    

    @property
    def probability(self):
        return [self.P(self.lmd, t) for t in self.T]
    

    @property
    def distribution(self):
        return [self.D(self.lmd, t) for t in self.T]

 
    @staticmethod
    def P(lmd, t):
        return math.e**(-lmd*t**2)


    @staticmethod
    def D(lmd, t):
        return 2*lmd*t*math.e**(-lmd*t**2)



class Exponential:

    def __init__(self, lmd, t=5000):
        self.lmd = lmd
        self.t = t
        self.T = list(range(0,t,100))
    

    @property
    def probability(self):
        return [self.P(self.lmd, t) for t in self.T]
    

    @property
    def distribution(self):
        return [self.D(self.lmd, t) for t in self.T]

 
    @staticmethod
    def P(lmd, t):
        return math.e**(-lmd*t)


    @staticmethod
    def D(lmd, t):
        return lmd*math.e**(-lmd*t)



class Normal:

    def __init__(self, m0, sig0, t=5000):
        self.m0 = m0
        self.sig0 = sig0
        self.t = t
        self.T = list(range(0,t,100))
    

    @property
    def probability(self):
        return [self.P(self.m0, self.sig0, t) for t in self.T]
    

    @property
    def distribution(self):
        return [self.D(self.m0, self.sig0, t) for t in self.T]

 
    @staticmethod
    def P(m0, sig0, t):
        return (0.5-Integral.LaplasFunc((t-m0)/sig0))/(0.5+Integral.LaplasFunc(m0/sig0))


    @staticmethod
    def D(m0, sig0, t):
        return math.e**(-(t-m0)**2/(2*sig0**2))/(sig0*math.sqrt(2*math.pi)*(0.5+Integral.LaplasFunc(m0/sig0)))
    


class NRR:

    def __init__(self, lmd, myu):
        self.lmd = lmd
        self.myu = myu
        self.lmdC = sum(lmd)



    def IntensityOfFailure(self, t):
        return self.myu/(self.lmdC+self.myu) + self.lmdC*math.e**(-(self.lmdC+self.myu)*t)/(self.lmdC+self.myu)
    

    # def IntensityOfRecovery(self):

        # pass
    
    
    def FunctionAvailability(self):
        ''' Kg(t) = myu/(lmdC+myu) + lmdC/(lmdC+myu) '''
        return
    
    def CoefficientAvailability(self):
        ''' Kg = T/(T+Tv) '''
        return 1/(1+sum(lmd/myu for lmd, myu in zip(self.lmd, self.myu)))


    # @staticmethod
    def TimeBetweenFailures(self):
        ''' T = 1/lmd '''
        return 1/self.lmdC

    # @staticmethod
    def AverageTimeOfSystemRecovery(self):
        ''' Tv = sum(lmd[i]/myu[i])/lmdC '''
        return sum(lmd/myu for lmd, myu in zip(self.lmd, self.myu))/self.lmdC

    


def FailureFreeProbability(probs):
    ''' Pc = P1*P2*...*Pn '''
    return reduce(lambda p, nt: p*nt, probs)


def FailureRateSys(lmds=[]):
    ''' lmdC = sum all lmd's '''
    return sum(lmds)


def FailureRate(Pij, Dij):
    ''' lmd = f[i,j]/p[i,j] '''
    return Dij/Pij


def AverageUptime(lmdC):
    ''' Tc = 1 / lmdC '''
    return 1/lmdC


def DensityDistribution(lmdC, Pc):
    ''' Fc = lmdC*Pc '''
    return lmdC*Pc