
import math


from .integral import *
from .probability import *


class Distribution:

    def __init__(self):
        pass


    def Weibull(self, t, alpha, beta):
        return ((alpha*t**(alpha-1))/beta**alpha)*math.e**(-(t/beta)**alpha)

    
    def Gamma(self, t, alpha, beta):
        return (t**(alpha-1)*math.e**-(t/beta))/(beta**alpha*Integral.GammaFunc(alpha))


    def Rayle(self, t, lmd):
        return 2*lmd*t*math.e**(-lmd*t**2)


    def Exponential(self, t, lmd):
        return lmd*math.e**(-lmd*t)


    def Normal(self, t, m0, sig0):
        return math.e**(-(t-m0)**2/(2*sig0**2))/(sig0*math.sqrt(2*math.pi)*(0.5+Integral.LaplasFunc(m0/sig0)))


    @staticmethod
    def DensityDistribution(lmdC, Pc):
        ''' Fc = lmdC*Pc '''
        return lmdC*Pc
