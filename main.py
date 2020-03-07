import pkg_resources
# pyinstaller --onefile --windowed main.py
from PyQt5 import QtWidgets, Qt
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
            css = style.read()
        self.setStyleSheet(css)

    def run(self):
        window = MainWindowUi(objectName='MainWindow')
        window.resize(910, 600)
        window.show()
        return self.exec_()


if __name__ == "__main__":
    appctxt = AppContext(sys.argv)
    exit_code = appctxt.run()
    sys.exit(exit_code)