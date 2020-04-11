from PyQt5 import QtWidgets, QtCore
from models import Rayle as RayleModel
from views.tools import Info, Graph, TableView


class Rayle(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(Rayle, self).__init__(parent=parent, *args, **kwargs)

        # self.addItem(QtWidgets.QWidget(), 'Հաշվարկ')
        # self.addItem(Info(), 'Նկարագրություն')
        self.setLayout(QtWidgets.QGridLayout())

        self.layout().addWidget(QtWidgets.QLabel("Մուտքային տվյալներ"), 0, 0)
        inputW = QtWidgets.QWidget()
        self.layout().addWidget(inputW, 1, 0)
        form = QtWidgets.QFormLayout(inputW)

        self.lmd = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("λ :"), self.lmd)

        self.t = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("t :"), self.t)

        self.dt = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("dt :"), self.dt)

        self.error = QtWidgets.QLabel("Մուտքագրել համապատասխան տվյալները", objectName='error')
        form.addWidget(self.error)

        equal = QtWidgets.QPushButton("Հաշվել")
        form.addWidget(equal)

        equal.clicked.connect(self.EqualCtrl)
        form.setAlignment(QtCore.Qt.AlignTop)

        self.layout().addWidget(QtWidgets.QLabel("Համառոտ նկարագրություն"), 0, 1)
        self.layout().addWidget(Info('rayle_short.html'), 1, 1)

    def EqualCtrl(self):
        try:
            lmd = float(self.lmd.text())
            t = int(self.t.text())
            dt = int(self.dt.text())
            if lmd<=0 or t<1 or dt<1:
                raise ValueError
        except:
            self.error.setText("Մուտքային տվյալները սխալ են")
            self.error.show()
            return

        calc = RayleModel(lmd, t, dt)

        if calc is None:
            self.error.setText("Հաշվարկային սխալ (0֊ի բաժանում), \nխնդրում ենք ճշգրտել մուտքային տվյալները․")
            self.error.show()
            return

        self.error.hide()

        table = TableView(self, len(calc.T), 4, ["t", "Pₕ(t)", "fₕ(t)", "λₕ(t)"], calc.T, calc.probability, calc.distribution, calc.failure_rate)

        graphProb = Graph(self)
        graphProb.plot(calc.T, calc.probability, "Անխափան աշխատանքի  հավանականություն", "t", "$P_c(t)$")

        graphDist = Graph(self)
        graphDist.plot(calc.T, calc.distribution, "Մինչև  համակարգի  խափանումը ընկած\n ժամանակահատվածի բաշխման խտություն", "t", "$f_c(t)$")

        graphRate = Graph(self)
        graphRate.plot(calc.T, calc.failure_rate, "Համակարգի խափանման ինտեսիվություն", "t", "$\lambda_c(t)$")


        self.layout().addWidget(QtWidgets.QLabel("Ելքային տվյալներ"), 2, 0, 1, 2)
        self.layout().addWidget(table, 3, 0, 2, 1)
        self.layout().addWidget(graphProb, 3, 1)
        self.layout().addWidget(graphDist, 4, 1)
        self.layout().addWidget(graphRate, 5, 1)

