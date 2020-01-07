
from matplotlib import pyplot as plt

from auto_system_reliability.probability import Probability as P
from auto_system_reliability.distribution import Distribution as F



T = list(range(0,4000,100))

exp = [P().Weibull(t, 2, 1800) for t in T]

plt.plot(T, exp)
plt.show()