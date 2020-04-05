
import logging as log

log.basicConfig(filename='../text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)
log.info("This is a backup_mixed.py file")

from .non_backup_non_recoverable import *
from .non_backup_recoverable import *
from .backup_recoverable import *

from .RNR import RNR
from views.backup_recoverable.backup_mixed import BackupMixed

# __all__: object = ['NRR', 'RNR', 'MixedReserved', 'ReservedByPermanently', 'ReservedByReplacement']
