from PyQt5 import QtWidgets, QtCore
from models import Normal as NormalModel
from views.tools import Info, Graph, TableView


class Normal(QtWidgets.QToolBox):

    def __init__(self, parent=None, *args, **kwargs):
        super(Normal, self).__init__(parent=parent, *args, **kwargs)

        self.addItem(QtWidgets.QWidget(), 'Հաշվարկ')
        # self.addItem(Info(), 'Նկարագրություն')
        self.widget(0).setLayout(QtWidgets.QGridLayout())

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Մուտքային տվյալներ"), 0, 0)
        inputW = QtWidgets.QWidget()
        self.widget(0).layout().addWidget(inputW, 1, 0)
        form = QtWidgets.QFormLayout(inputW)

        self.m0 = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("m˳ :"), self.m0)

        self.sig0 = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("Ϭ˳ :"), self.sig0)

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

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Համառոտ նկարագրություն"), 0, 1)
        self.widget(0).layout().addWidget(Info('normal_short.html'), 1, 1)

    def EqualCtrl(self):
        #ToDo Refactoring Try block and creating Decorator for value checking
        try:
            m0 = int(self.m0.text())
            sig0 = int(self.sig0.text())
            t = int(self.t.text())
            dt = int(self.dt.text())
            if m0<=0 or sig0<=0 or t<1 or dt<1:
                raise ValueError
        except ValueError:
            self.error.setText("Մուտքային տվյալները սխալ են")
            self.error.show()
            return

        calc = NormalModel(m0, sig0, t, dt)

        if calc is None:
            self.error.setText("Հաշվարկային սխալ (0֊ի բաժանում), \nխնդրում ենք ճշգրտել մուտքային տվյալները․")
            self.error.show()
            return

        self.error.hide()

        #ToDo Refactoring this block and creating optimal DRY code for all Methods
        table = TableView(self, len(calc.T), 3, ["t", "Pₕ(t)", "fₕ(t)"], calc.T, calc.probability, calc.distribution)

        graphProb = Graph(self)
        graphProb.plot(calc.T, calc.probability, "Անխափան աշխատանքի  հավանականություն", "t", "$P_c(t)$")

        graphDist = Graph(self)
        graphDist.plot(calc.T, calc.distribution,
                       "Մինչև  համակարգի  խափանումը ընկած\n ժամանակահատվածի բաշխման խտություն", "t", "$f_c(t)$")

        graphRate = Graph(self)
        graphRate.plot(calc.T, calc.failure_rate, "Համակարգի խափանման ինտեսիվություն", "t", "$\lambda_c(t)$")

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Ելքային տվյալներ"), 2, 0, 1, 2)
        self.widget(0).layout().addWidget(table, 3, 0, 2, 1)
        self.widget(0).layout().addWidget(graphProb, 3, 1)
        self.widget(0).layout().addWidget(graphDist, 4, 1)
        self.widget(0).layout().addWidget(graphRate, 5, 1)

