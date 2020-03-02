from PyQt5 import QtCore, QtGui, QtWidgets
from models import asr

from . import *


class RNR(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("m :"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("λ :"), 1, 0)

        self.m = QtWidgets.QLineEdit()
        self.layout.addWidget(self.m, 0, 1)

        self.lmd = QtWidgets.QLineEdit()
        self.layout.addWidget(self.lmd, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)

        self.equal.clicked.connect(self.EqualCtrl)

    def EqualCtrl(self):
        self.asr = asr.RNR(int(self.m.text()), float(self.lmd.text()), 100)

        graphLayout = QtWidgets.QHBoxLayout(self)

        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        print(self.asr.probability)
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        print(self.asr.distribution)
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")
        graphLayout.addWidget(self.graphDist)

        self.graphSysFailRate = StaticCanvas(self)
        self.graphSysFailRate.setObjectName("graphSysFailRate")
        self.graphSysFailRate.plot(self.asr.T, self.asr.system_failure_rate, "Graph for System Failure Rate")
        graphLayout.addWidget(self.graphSysFailRate)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2)
