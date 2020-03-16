from PyQt5 import QtWidgets, QtCore
from models import non_recoverable_non_backup
from .graph import StaticCanvas
from .table import CreateTable

class Weibull(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(Weibull, self).__init__(parent=parent, *args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("α :"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("β :"), 1, 0)
        self.layout.addWidget(QtWidgets.QLabel("t :"), 0, 2)
        self.layout.addWidget(QtWidgets.QLabel("dt :"), 1, 2)

        self.alpha = QtWidgets.QLineEdit()
        self.layout.addWidget(self.alpha, 0, 1)

        self.beta = QtWidgets.QLineEdit()
        self.layout.addWidget(self.beta, 1, 1)

        self.t = QtWidgets.QLineEdit()
        self.layout.addWidget(self.t, 0, 3)

        self.dt = QtWidgets.QLineEdit()
        self.layout.addWidget(self.dt, 1, 3)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 2)

        self.setLayout(self.layout)
        self.equal.clicked.connect(self.EqualCtrl)

        self.layout.setAlignment(QtCore.Qt.AlignTop)

    def EqualCtrl(self):

        try:
            alpha = int(self.alpha.text())
            beta = int(self.beta.text())
            t = int(self.t.text())
            dt = int(self.dt.text())
            if alpha<=0 or beta<=0 or t<1 or dt<1:
                raise ValueError
        except:
            return

        self.asr = non_recoverable_non_backup.Weibull(alpha, beta, t, dt)
        graphLayout = QtWidgets.QVBoxLayout(self)
        graphLayout.setObjectName("graph")
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")
        graphLayout.addWidget(self.graphDist)

        # self.createTable()

        self.tableWidget = CreateTable(self, t//dt, 3, ["Time", "Probability", "Distribution"], self.asr.T, self.asr.probability, self.asr.distribution)

        tableLayout = QtWidgets.QHBoxLayout()
        tableLayout.addLayout(graphLayout)
        tableLayout.addWidget(self.tableWidget)

        self.layout.addLayout(tableLayout, 3, 0, 3, 4)
