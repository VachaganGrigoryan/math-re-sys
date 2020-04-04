import math
from functools import reduce


class RecoverableBackup:

    def __init__(self):
        self._systems = []

    @property
    def systems(self):
        return self._systems
    
    @systems.deleter
    def systems(self):
        self._systems = []

    def add(self, system):
        self._systems.append(system)

    def remove(self, system):
        self._systems.remove(system)



    
class RRSystem:
    
    def __init__(self, lmd, myu, _function):
        self.lmd = lmd
        self.myu = myu
        self._function = eval(f'{_function}(self)')

    def all_by_replacement(self): # Ընդհանուր փոխարինումով
        return 

    def all_by_permanent(self): # Ընդհանուր մշտական
        pass

    def еlement_by_replacement(self): # Ըստ տարրերի փոխարինումով
        pass
    
    def еlement_by_permanent(self): # Ըստ տարրերի մշտական
        pass


class ReservedAndBackuped:

    def __init__(self, m, r, lmd, myu):
        self.m = m
        self.r = r
        self.lmd = lmd
        self.myu = myu
        self.createVar()

    def createVar(self):
        self.rs = list(range(1, self.r + 1))
        self.lmds = [i * self.lmd for i in range(self.m+1, 0, -1)]
        self.myus = [i * self.myu if i<=self.r else self.r*self.myu for i in range(1, self.m+2)]
        self.rhos = [[self.rho(lmd, myu) for lmd in self.lmds] for myu in self.myus]
        self.gammas = [[self.gamma(lmd, myu) for lmd in self.lmds] for myu in self.myus]

        # self.rhos = [self.rho(lmd, myu) for lmd, myu in zip(self.lmds, self.myus)]
        # self.gammas = [self.gamma(lmd, myu) for lmd, myu in zip(self.lmds, self.myus)]

    @staticmethod
    def rho(lmd, myu):
        return lmd / myu

    @staticmethod
    def gamma(lmd, myu):
        return myu / lmd


class ReservedByPermanently(ReservedAndBackuped):

    def __init__(self, m, r, lmd, myu):
        super(ReservedByPermanently, self).__init__(m, r, lmd, myu)

    @property
    def ReadinessFunction(self):
        return [sum(gammas[i]**i/math.factorial(i) for i in range(1, self.m+1))/sum(gammas[i]**i/math.factorial(i) for i in range(self.m+1)) for gammas in self.gammas]
        # return [1-((rho**(self.m+1))/((1+rho)**(self.m+1))) for rho in self.rhos]
        # return [(1+sum(rhos[1:-1]))/(1+sum(rhos[1:])) for rhos in self.rhos]

    @property
    def T(self):
        return [sum(gammas[i]*math.factorial(self.m)/math.factorial(self.m-i) for i in range(self.m))/self.lmd for gammas in self.gammas]
        # return [((self.m+1)*rho**(self.m+1)-rho**(self.m+1))/(self.lmd*(self.m+1)*rho**self.m) for rho in self.rhos]
        # return [(1+sum(rhos[1:-1]))/reduce(lambda p, next: p*next, [self.lmd]+rhos[1:-1]) for rhos in self.rhos]

    @property
    def Tv(self):
        return [1/myu for myu in self.myus]

    # @property
    # def T1(self):
    #     return [1+sum() for gamma in self.gammas]



class ReservedByReplacement(ReservedAndBackuped):

    def __init__(self, m, r, lmd, myu):
        super(ReservedByReplacement, self).__init__(m, r, lmd, myu)

    @property
    def ReadinessFunction(self):
        return [sum(rhos[i] ** i / math.factorial(i) for i in range(self.m)) / sum(rhos[i] ** i / math.factorial(i) for i in range(self.m + 1)) for rhos in self.rhos]
        # return [(1+sum(rhos[1:-1]))/(1+sum(rhos[1:])) for rhos in self.rhos]

    @property
    def T(self):
        return [sum(gammas[i] * math.factorial(self.m) / math.factorial(self.m - i) for i in range(self.m)) / self.lmd for gammas in self.gammas]
        # return [(1+sum(rhos[1:-1]))/reduce(lambda p, next: p*next, [self.lmd]+rhos[1:-1]) for rhos in self.rhos]

    @property
    def Tv(self):
        return [1 /((self.m+1)*myu) for myu in self.myus]

