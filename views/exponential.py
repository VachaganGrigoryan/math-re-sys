from PyQt5 import QtCore, QtGui, QtWidgets
from models import asr

from . import *

class Exponential(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("λ :"), 0, 0)
        # self.layout.addWidget(QtWidgets.QLabel("β :"), 1, 0)

        self.lmd = QtWidgets.QLineEdit()
        self.layout.addWidget(self.lmd, 0, 1)

        # self.beta = QtWidgets.QLineEdit()
        # self.layout.addWidget(self.beta, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)

        self.equal.clicked.connect(self.EqualCtrl)

    def EqualCtrl(self):
        self.asr = asr.Exponential(float(self.lmd.text()), 5000)

        graphLayout = QtWidgets.QHBoxLayout(self)

        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")

        graphLayout.addWidget(self.graphDist)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2)
