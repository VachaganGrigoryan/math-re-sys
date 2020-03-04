from PyQt5 import QtWidgets, QtCore
from models import asr
from views.graph import StaticCanvas
from views.table import CreateTable


class Normal(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(Normal, self).__init__(parent=parent, *args, **kwargs)

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("m˳ :"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("Ϭ˳ :"), 1, 0)

        self.m0 = QtWidgets.QLineEdit()
        self.layout.addWidget(self.m0, 0, 1)

        self.sig0 = QtWidgets.QLineEdit()
        self.layout.addWidget(self.sig0, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)

        self.equal.clicked.connect(self.EqualCtrl)

        self.layout.setAlignment(QtCore.Qt.AlignTop)

    def EqualCtrl(self):
        self.asr = asr.Normal(int(self.m0.text()), int(self.sig0.text()), 5000)

        graphLayout = QtWidgets.QVBoxLayout(self)
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")
        graphLayout.addWidget(self.graphDist)

        tableLayout = QtWidgets.QHBoxLayout()
        self.tableWidget = CreateTable(self, 50, 3, ["Time", "Probability", "Distribution"], self.asr.T, self.asr.probability, self.asr.distribution)

        tableLayout.addLayout(graphLayout)
        tableLayout.addWidget(self.tableWidget)

        self.layout.addLayout(tableLayout, 3, 0, 3, 2)

