import math

from models.math_errors import MathErrors


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

    def __str__(self):
        return f'Kg(t)[{self.availability}]\nT[{self.T}]'

@MathErrors
class Primary(System):

    def __init__(self, lmd_s: list, myu: float, t: int = 40, dt: int = 2):
        self._failure_intensity = sum(lmd_s)
        self._recovery_intensity = myu
        self._Tg = 1/self.failure_intensity
        self._Tv = 1/self.recovery_intensity
        self._availability_factor = self._Tg/(self._Tg+self._Tv)
        System.__init__(self, t, dt)

    @property
    def failure_intensity(self):
        return self._failure_intensity

    @property
    def recovery_intensity(self):
        return self._recovery_intensity

    @property
    def Tg(self):
        return self._Tg

    @property
    def Tv(self):
        return self._Tv

    @property
    def availability_factor(self):
        return self._availability_factor

    def A(self, t):
        sumfr = self.failure_intensity + self.recovery_intensity
        return self.recovery_intensity / sumfr + self.failure_intensity * math.e ** (-sumfr * t) / sumfr


@MathErrors
class Primary2(System):

    def __init__(self, lmd_s: list, myu_s: list, t: int = 40, dt: int = 2):
        _failure_recovery_ = sum(lmd/myu for lmd, myu in zip(lmd_s, myu_s))

        self._failure_intensity = sum(lmd_s)
        self._recovery_intensity = self._failure_intensity/_failure_recovery_

        self._Tg = 1/self.failure_intensity
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
    def Tg(self):
        return self._Tg

    @property
    def Tv(self):
        return self._Tv

    @property
    def availability_factor(self):
        return self._availability_factor

    def A(self, t):
        sumfr = self.failure_intensity + self.recovery_intensity
        return self.recovery_intensity / sumfr + self.failure_intensity * math.e ** (-sumfr * t) / sumfr

    def __str__(self):
        return f'''
                _failure_intensity : {self.failure_intensity}\n
                _recovery_intensity : {self.recovery_intensity}\n
                _availability_factor : {self.availability_factor}\n
                _Tg : {self.Tg}\n
                _Tv : {self.Tv}\n
                Kg(t)[{self.availability}]\n
                T[{self.T}]
                '''


if __name__ == '__main__':

    lmd_s = [0.0003, 0.0002, 0.0009, 0.0006, 0.0004, 0.0003, 0.0005, 0.0007]
    myu_s = [0.5, 0.2, 0.1, 0.4, 0.9, 0.7, 0.6, 0.8]

    calc = Primary2(lmd_s, myu_s, 40, 4)
