from PyQt5 import QtWidgets, QtCore
from models import asr
from .graph import StaticCanvas
from .table import CreateTable

class Weibull(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(Weibull, self).__init__(parent=parent, *args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("α :"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("β :"), 1, 0)

        self.alpha = QtWidgets.QLineEdit()
        self.layout.addWidget(self.alpha, 0, 1)

        self.beta = QtWidgets.QLineEdit()
        self.layout.addWidget(self.beta, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)
        self.equal.clicked.connect(self.EqualCtrl)

        self.layout.setAlignment(QtCore.Qt.AlignTop)

    def EqualCtrl(self):
        self.asr = asr.Weibull(int(self.alpha.text()), int(self.beta.text()), 5000)

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

        self.tableWidget = CreateTable(self, 50, 3, ["Time", "Probability", "Distribution"], self.asr.T, self.asr.probability, self.asr.distribution)

        tableLayout = QtWidgets.QHBoxLayout()
        tableLayout.addLayout(graphLayout)
        tableLayout.addWidget(self.tableWidget)

        self.layout.addLayout(tableLayout, 3, 0, 3, 2)

    # def createTable(self):
    #     # Create table
    #     self.tableWidget = QtWidgets.QTableWidget()
    #     self.tableWidget.setRowCount(50)
    #     self.tableWidget.setColumnCount(3)
    #     for i, t, p, d in zip(range(50), self.asr.T, self.asr.probability, self.asr.distribution):
    #         print(i, t, p, d)
    #         self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem('%d' % t))
    #         self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem('%.5f' % p))
    #         self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem('%.5f' % d))
        # self.tableWidget.move(0, 0)

        # table selection change
        # self.tableWidget.doubleClicked.connect(self.on_click)


# def deleteItemsOfLayout(layout):
#     if layout is not None:
#         while layout.count():
#             item = layout.takeAt(0)
#             widget = item.widget()
#             if widget is not None:
#                 widget.setParent(None)
#             else:
#                 deleteItemsOfLayout(item.layout())