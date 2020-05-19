import os
import pkg_resources
# pyinstaller --onefile --windowed ReSys.py
# pyinstaller --onedir -w --icon "D:/Projects/pyqt-math-irina/static/icon.ico" --add-data "D:/Projects/pyqt-math-irina/static;static/" ReSys.py
from PyQt5 import QtWidgets, Qt, QtGui
from PyQt5.QtCore import QFile, QTextStream
from controller import MainWindowUi
import sys

class AppContext(QtWidgets.QApplication):
    """AppContext's Main (GUI)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        file = QFile("static/css/light.css")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())


        # self.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'icon.png'))
        self.setWindowIcon(QtGui.QIcon('static/icon.ico'))
        # with open('style.css', 'r') as style:
        #     css = style.read()
        # self.setStyleSheet(css)

    def run(self):
        window = MainWindowUi(objectName='MainWindow')
        window.resize(1200, 800)
        window.show()
        return self.exec_()


if __name__ == "__main__":
    appctxt = AppContext(sys.argv)
    exit_code = appctxt.run()
    sys.exit(exit_code)