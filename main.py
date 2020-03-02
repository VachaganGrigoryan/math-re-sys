
from PyQt5 import QtWidgets
from controller import MainWindowUi
import sys

import logging as log
log.basicConfig(filename='text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)


class AppContext(QtWidgets.QApplication):
    """AppContext's Main (GUI)"""
    log.info("""AppContext's Main (GUI)""")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open('style.css', 'r') as style:
            qss = style.read()
        self.setStyleSheet(qss)

    def run(self):
        window = MainWindowUi(objectName='MainWindow')
        window.resize(550, 300)
        window.show()
        return self.exec_()


if __name__ == "__main__":
    appctxt = AppContext(sys.argv)
    exit_code = appctxt.run()
    sys.exit(exit_code)