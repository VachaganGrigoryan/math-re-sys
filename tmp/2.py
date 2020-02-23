from scipy.integrate import quad
import numpy as np
import math
from functools import reduce
from matplotlib import pyplot as plt

def main():
    ''' Mshtakan yndhanur pahustavorum '''
    m = int(input("M = "))
    lmd = float(input("lambda = "))
    
    T = list(range(0, int(input("Enter T = "))+1, 5))
    Ph = [1-(1-math.e**(-lmd*t))**(m+1) for t in T]
    Fh = [(m+1)*lmd*math.e**(-lmd*t)*(1-math.e**(-lmd*t))**m for t in T]
    LMDh = [f/p for p, f in zip(Ph, Fh)]

    plt.plot(T, Ph)
    plt.show()
    plt.plot(T, Fh)
    plt.plot(T, LMDh)
    plt.show()


def main2():
    lmd = float(input("Enter lmd : "))
    alpha = int(input("Enter alpha : "))
    beta = int(input("Enter beta : "))
    T = list(range(0, int(input("Enter T = "))+1, 100))

    Phw = [math.e**(-(t/beta)**alpha) for t in T]
    Phe = [math.e**(-lmd*t) for t in T]

    plt.plot(T, Phw)
    plt.plot(T, Phe)
    plt.show()

if __name__ == "__main__":
    main()