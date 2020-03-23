from PyQt5 import QtWidgets, QtCore
from models import non_recoverable_non_backup
from views.tools.graph import Graph


class RNR(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(RNR, self).__init__(parent=parent, *args, **kwargs)

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

        self.layout.setAlignment(QtCore.Qt.AlignTop)

    def EqualCtrl(self):
        self.asr = non_recoverable_non_backup.RNR(int(self.m.text()), float(self.lmd.text()), 100)

        graphLayout = QtWidgets.QHBoxLayout(self)

        self.graphProb = Graph(self)
        self.graphProb.setObjectName("graphProb")
        print(self.asr.probability)
        self.graphProb.plot(self.asr.T, self.asr.probability, "Անխափան աշխատանքի  հավանականություն", "t", "$P_c(t)$")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = Graph(self)
        self.graphDist.setObjectName("graphDist")
        print(self.asr.distribution)
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Մինչև  համակարգի  խափանումը ընկած\n ժամանակահատվածի բաշխման խտություն", "t", "$f_c(t)$ ")
        graphLayout.addWidget(self.graphDist)

        self.graphSysFailRate = Graph(self)
        self.graphSysFailRate.setObjectName("graphSysFailRate")
        self.graphSysFailRate.plot(self.asr.T, self.asr.system_failure_rate, "Graph for System Failure Rate")
        graphLayout.addWidget(self.graphSysFailRate)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2)
