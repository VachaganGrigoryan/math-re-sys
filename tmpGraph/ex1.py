from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
import sys


class ExampleWindow(QMainWindow):

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(ExampleWindow, self).__init__(parent=parent, flags=flags)
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("My App Title")
        self.initUI()

    def initUI(self):

        self.generalLayout = QHBoxLayout(self)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)


        self.label = QLabel("#1 : ")
        self.generalLayout.addWidget(self.label)
        
        self.n = QLineEdit()
        self.n.setPlaceholderText("n = ")
        
        self.generalLayout.addWidget(self.n)

        self.btn = QPushButton()
        self.btn.setText("Հաշվել")

        self.generalLayout.addWidget(self.btn)

        self.btn.clicked.connect(self.clickedEqual)

    def clickedEqual(self):
        self.label.setText(self.n.text())


def window():

    app = QApplication(sys.argv)
    win = ExampleWindow()
    
    win.show()
    sys.exit(app.exec_())

window()

