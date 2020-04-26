from PyQt5 import QtWidgets, QtCore
from models import Exponential as ExponentialModel
from views.tools import Info, Graph, TableView

from const.constants import TEXT

class Exponential(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(Exponential, self).__init__(parent=parent, *args, **kwargs)

        # self.addItem(QtWidgets.QWidget(), 'Հաշվարկ')
        # self.addItem(Info(), 'Նկարագրություն')
        self.setLayout(QtWidgets.QGridLayout())

        self.layout().addWidget(QtWidgets.QLabel(TEXT.LB_INPUT_DATA), 0, 0)
        inputW = QtWidgets.QWidget()
        self.layout().addWidget(inputW, 1, 0)
        form = QtWidgets.QFormLayout(inputW)

        self.lmd = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel(TEXT.LB_LMD), self.lmd)

        self.t = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel(TEXT.LB_t), self.t)

        self.dt = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel(TEXT.LB_dt), self.dt)

        self.error = QtWidgets.QLabel(TEXT.LB_ERR_CORRECT_DATA, objectName='error')
        form.addWidget(self.error)

        equal = QtWidgets.QPushButton(TEXT.BTN_CALCULATE)
        form.addWidget(equal)

        equal.clicked.connect(self.EqualCtrl)
        form.setAlignment(QtCore.Qt.AlignTop)

        self.layout().addWidget(QtWidgets.QLabel(TEXT.LB_DESC), 0, 1)
        self.layout().addWidget(Info('exponential_short.html'), 1, 1)

    def EqualCtrl(self):
        try:
            lmd = float(self.lmd.text())
            t = int(self.t.text())
            dt = int(self.dt.text())
            if lmd<=0 or t<1 or dt<1:
                raise ValueError
        except:
            self.error.setText(TEXT.LB_ERR_WRONG_DATA)
            self.error.show()
            return

        calc = ExponentialModel(lmd, t, dt)

        if calc is None:
            self.error.setText(TEXT.LB_ERR_ZERO_DIVISION)
            self.error.show()
            return

        self.error.hide()

        table = TableView(self, len(calc.T), 4, [TEXT.TABLE_T, TEXT.TABLE_P, TEXT.TABLE_F, TEXT.TABLE_LMD], calc.T, calc.probability, calc.distribution, calc.failure_rate)

        graphProb = Graph(self)
        graphProb.plot(calc.T, calc.probability, TEXT.TITLE_PROBABILITY, TEXT.GR_T, TEXT.GR_P)

        graphDist = Graph(self)
        graphDist.plot(calc.T, calc.distribution, TEXT.TITLE_DISTRIBUTION, TEXT.GR_T, TEXT.GR_F)

        graphRate = Graph(self)
        graphRate.plot(calc.T, calc.failure_rate, TEXT.TITLE_FAILURE, TEXT.GR_T, TEXT.GR_LMD)

        self.layout().addWidget(QtWidgets.QLabel(TEXT.LB_OUTPUT_DATA), 2, 0, 1, 2)
        self.layout().addWidget(table, 3, 0, 2, 1)
        self.layout().addWidget(graphProb, 3, 1)
        self.layout().addWidget(graphDist, 4, 1)
        self.layout().addWidget(graphRate, 5, 1)

