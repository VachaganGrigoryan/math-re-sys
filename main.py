
from PyQt5 import QtWidgets
from controller import MainWindowUi, RootEqualCtrl
import sys

import logging as log
log.basicConfig(filename='text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)
log.info("This is a main.py file")

if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    log.info("")
    ui = MainWindowUi()
    ui.show()

    # RootEqualCtrl(prob=P, dist=F, view=ui)
    
    sys.exit(app.exec_())
