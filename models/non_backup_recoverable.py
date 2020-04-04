import math

    
class System:

    def __init__(self, t: int, dt: int) -> object:
        self._T = list(range(0, t + 1, dt))
        self._availability = [self.A(t) for t in self.T]

    @property
    def T(self):
        return self._T

    @property
    def availability(self):
        return self._availability

    def A(self, t: int) -> float:
        pass


class Primary(System):

    def __init__(self, lmd_s: list, myu: float, t: int = 40, dt: int = 2):
        self._failure_intensity = sum(lmd_s)
        self._recovery_intensity = myu
        self._T = 1/self.failure_intensity
        self._Tv = 1/self.recovery_intensity
        self._availability_factor = self._T/(self._T+self._Tv)
        System.__init__(self, t, dt)

    @property
    def failure_intensity(self):
        return self._failure_intensity

    @property
    def recovery_intensity(self):
        return self._recovery_intensity

    @property
    def T(self):
        return self._T

    @property
    def Tv(self):
        return self._Tv

    @property
    def availability_factor(self):
        return self._availability_factor

    def A(self, t):
        sumfr = self.failure_intensity + self.recovery_intensity
        return self.recovery_intensity / sumfr + self.failure_intensity * math.e ** (-sumfr * t) / sumfr


class Primary2(System):

    def __init__(self, lmd_s: list, myu_s: list, t: int = 40, dt: int = 2):
        _failure_recovery_ = sum(lmd/myu for lmd, myu in zip(lmd_s, myu_s))
        self._failure_intensity = sum(lmd_s)
        self._recovery_intensity = self._failure_intensity/_failure_recovery_
        # self._recovery_intensity = sum(myu_s)
        self._T = 1/sum(self.failure_intensity)
        self._Tv = _failure_recovery_/self._failure_intensity
        self._availability_factor = 1/(1+_failure_recovery_)
        System.__init__(self, t, dt)

    @property
    def failure_intensity(self):
        return self._failure_intensity

    @property
    def recovery_intensity(self):
        return self._recovery_intensity

    @property
    def T(self):
        return self._T

    @property
    def Tv(self):
        return self._Tv

    @property
    def availability_factor(self):
        return self._availability_factor

    def A(self, t):
        sumfr = self.failure_intensity + self.recovery_intensity
        return self.recovery_intensity / sumfr + self.failure_intensity * math.e ** (-sumfr * t) / sumfr
