from PyQt5 import QtWidgets, QtCore
from models import non_recoverable_non_backup
from views.tools import Info, Graph, TableView


class Rayle(QtWidgets.QToolBox):

    def __init__(self, parent=None, *args, **kwargs):
        super(Rayle, self).__init__(parent=parent, *args, **kwargs)

        self.addItem(QtWidgets.QWidget(), 'Հաշվարկ')
        self.addItem(Info(), 'Նկարագրություն')
        self.widget(0).setLayout(QtWidgets.QGridLayout())

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Մուտքային տվյալներ"), 0, 0)
        inputW = QtWidgets.QWidget()
        self.widget(0).layout().addWidget(inputW, 1, 0)
        form = QtWidgets.QFormLayout(inputW)

        self.lmd = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("λ :"), self.lmd)

        self.t = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("t :"), self.t)

        self.dt = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("dt :"), self.dt)

        equal = QtWidgets.QPushButton("Հաշվել")
        form.addWidget(equal)

        equal.clicked.connect(self.EqualCtrl)
        form.setAlignment(QtCore.Qt.AlignTop)

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Համառոտ նկարագրություն"), 0, 1)
        self.widget(0).layout().addWidget(Info(), 1, 1)

    def EqualCtrl(self):
        try:
            lmd = float(self.lmd.text())
            t = int(self.t.text())
            dt = int(self.dt.text())
            if lmd<=0 or t<1 or dt<1:
                raise ValueError
        except:
            return

        calc = non_recoverable_non_backup.Rayle(lmd, t, dt)

        table = TableView(self, len(calc.T), 3, ["t", "Pₕ(t)", "fₕ(t)"], calc.T, calc.probability, calc.distribution)

        graphProb = Graph(self)
        graphProb.plot(calc.T, calc.probability, "Անխափան աշխատանքի  հավանականություն", "t", "$P_c(t)$")

        graphDist = Graph(self)
        graphDist.plot(calc.T, calc.distribution, "Մինչև  համակարգի  խափանումը ընկած\n ժամանակահատվածի բաշխման խտություն", "t", "$f_c(t)$")

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Ելքային տվյալներ"), 2, 0, 1, 2)
        self.widget(0).layout().addWidget(table, 3, 0, 2, 1)
        self.widget(0).layout().addWidget(graphProb, 3, 1)
        self.widget(0).layout().addWidget(graphDist, 4, 1)

