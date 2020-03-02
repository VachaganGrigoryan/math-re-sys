
import logging as log

log.basicConfig(filename='../text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)
log.info("This is a RR.py file")

from graph import StaticCanvas

from .weibull import Weibull
from .gamma import Gamma
from .rayle import Rayle
from .exponential import Exponential
from .normal import Normal
from .NRR import NRR
from .RNR import RNR
from .RR import RR

__all__: object = ['Weibull', 'Gamma', 'Rayle', 'Exponential', 'Normal', 'StaticCanvas']