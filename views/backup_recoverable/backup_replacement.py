from PyQt5 import QtWidgets, QtCore
from models import backup_recoverable
from views.tools.graph import Graph
from views.tools.table import TableView

class BackupByReplacement(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(BackupByReplacement, self).__init__(parent=parent, *args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("m :"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("r :"), 1, 0)
        self.layout.addWidget(QtWidgets.QLabel("λ :"), 0, 2)
        self.layout.addWidget(QtWidgets.QLabel("μ :"), 1, 2)

        self.m = QtWidgets.QLineEdit()
        self.layout.addWidget(self.m, 0, 1)

        self.r = QtWidgets.QLineEdit()
        self.layout.addWidget(self.r, 1, 1)

        self.lmd = QtWidgets.QLineEdit()
        self.layout.addWidget(self.lmd, 0, 3)

        self.myu = QtWidgets.QLineEdit()
        self.layout.addWidget(self.myu, 1, 3)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 2)

        self.setLayout(self.layout)
        self.equal.clicked.connect(self.EqualCtrl)

        self.layout.setAlignment(QtCore.Qt.AlignTop)

    def EqualCtrl(self):

        try:
            m = int(self.m.text())
            r = int(self.r.text())
            lmd = float(self.lmd.text())
            myu = float(self.myu.text())
            if m<=0 or r<=0 or lmd<=0 or myu<=0:
                raise ValueError
        except:
            return


        self.asr = backup_recoverable.ReservedByReplacement(m, r, lmd, myu)
        graphLayout = QtWidgets.QVBoxLayout(self)
        graphLayout.setObjectName("graph")
        self.graphProb = Graph(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(list(range(m+1)), self.asr.ReadinessFunction, "Graph for Readiness Function")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = Graph(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(list(range(m+1)), self.asr.T, "Graph for Time")
        graphLayout.addWidget(self.graphDist)

        # self.createTable()
        self.tableWidget = TableView(self, m + 1, 4, ["r", "Kг", "T", "Tв"], self.asr.rs, self.asr.ReadinessFunction, self.asr.T, self.asr.Tv)

        tableLayout = QtWidgets.QHBoxLayout()
        tableLayout.addLayout(graphLayout)
        tableLayout.addWidget(self.tableWidget)

        self.layout.addLayout(tableLayout, 3, 0, 3, 4)
