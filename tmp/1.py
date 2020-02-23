from scipy.integrate import quad
import numpy as np
import math
from functools import reduce
from matplotlib import pyplot as plt

''' Integralneri hashvark ''' 

def gamma_func(x, alpha):
    ''' Gamma function for integral  '''
    return x**(alpha-1)*math.e**(-x)


def g(alpha, start=0, stop=np.Inf):
    ''' Gamma integral '''
    return quad(gamma_func, start, stop, args=(alpha))[0]


def laplas_func(x):
    ''' Laplas function for integral '''
    return math.e**(-(x**2/2))


def fi0(t):
    ''' Laplas integral '''
    return (1/math.sqrt(2*math.pi))*quad(laplas_func, 0, t)[0]


''' //////////////////////// '''

def W(alpha, beta):
    return [beta*g(1+1/alpha), beta*math.sqrt(g(1+2/alpha)-g(1+1/alpha)**2)]


def G(alpha, beta):
    return [alpha*beta, math.sqrt(alpha)*beta]


def R(lmd):
    return [math.sqrt(math.pi/(4*lmd)), math.sqrt((4-math.pi)/(4*lmd))]


def EXP(lmd):
    return [1/lmd, 1/lmd]


def TN(m0, sig0):
    k = math.e**(-m0**2/(2*sig0**2))/(math.sqrt(2*math.pi)*(0.5+fi0(m0/sig0)))
    return [m0+k*sig0, sig0*math.sqrt(1+k*(m0/sig0)-k**2)]

'''  Bashxumneri hamar  '''

def P1(t, alpha, beta):
    return math.e**(-(t/beta)**alpha)


def P2(t, alpha, beta):
    return 1-(g(alpha, 0, t/beta)/g(alpha))


def P3(t, lmd):
    return math.e**(-lmd*t**2)


def P4(t, lmd):
    return math.e**(-lmd*t)


def P5(t, m0, sig0):
    return (0.5-fi0((t-m0)/sig0))/(0.5+fi0(m0/sig0))


def main():

    w_alpha, w_beta = int(input("Function(W)\n\tEnter alpha : ")), int(input("\tEnter beta : "))
    g_alpha, g_beta = int(input("Function(G)\n\tEnter alpha : ")), int(input("\tEnter beta : "))
    r_lmd = float(input("Function(R)\n\tEnter lambda : "))
    exp_lmd = float(input("Function(EXP)\n\tEnter lambda : "))
    m0, sig0 = int(input("Function(TH)\n\tEnter m[0] : ")), int(input("\tEnter sigma[0] : "))
    t = int(input("Enter t : "))


    # arr_func = {
    #     1: W(w_alpha, w_beta),
    #     2: G(g_alpha, g_beta),
    #     3: R(r_lmd),
    #     4: EXP(exp_lmd),
    #     5: TN(m0, sig0)
    # }

    # for item in arr_func.items():
    #     print(item)


    T = list(range(0,t+1,100))

    dist_P = { 'T':T, 'P1':[P1(t, w_alpha, w_beta) for t in T], 'P2':[P2(t, g_alpha, g_beta) for t in T], 'P3':[P3(t, r_lmd) for t in T], 'P4':[P4(t, exp_lmd) for t in T], 'P5':[P5(t, m0, sig0) for t in T]}
    
    dist_P['Ph'] = []
    all_P = list(dist_P.values())
    for val in zip(all_P[1], all_P[2], all_P[3], all_P[4], all_P[5]):
        dist_P['Ph'].append(reduce(lambda a, b: a*b, val))
   

    for item in list(dist_P.values())[1:]:
        plt.plot(T, item)
    plt.show()

if __name__ == "__main__":
    main()