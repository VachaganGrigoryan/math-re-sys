
from matplotlib import pyplot as plt

from auto_system_reliability.asr import NRR



T = list(range(0, 40, 2))

lmd = [0.0003, 0.0002, 0.0009, 0.0006, 0.0004, 0.0003, 0.0005, 0.0007]
myu = [0.5, 0.2, 0.1, 0.4, 0.9, 0.7, 0.6, 0.8]

nrr = NRR(lmd, myu)
# nrr.setLmd()

# nrr.setMyu(0.4)

# exp = [nrr.IntensityOfFailure(t) for t in T]

# print(exp)
print(nrr.TimeBetweenFailures())
print(nrr.AverageTimeOfSystemRecovery())
print(nrr.CoefficientAvailability())


# plt.plot(T, exp)
# plt.show()