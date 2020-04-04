from models import Exponential


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

