from PyQt5 import QtWidgets, QtCore
from models import Consecutive as ConsecutiveModel
from views.tools import Info, Graph, TableView


class Consecutive(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(Consecutive, self).__init__(parent=parent, *args, **kwargs)

        # self.addItem(QtWidgets.QWidget(), 'Հաշվարկ')
        # self.addItem(Info(), 'Նկարագրություն')
        self.setLayout(QtWidgets.QGridLayout())

        self.layout().addWidget(QtWidgets.QLabel("Մուտքային տվյալներ"), 0, 0)
        inputW = QtWidgets.QWidget()
        self.layout().addWidget(inputW, 1, 0)
        self.form = QtWidgets.QFormLayout(inputW)

        self.count = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("N :"), self.count)

        create = QtWidgets.QPushButton("Ստեղծել")
        self.form.addWidget(create)

        create.clicked.connect(self.CreateCtrl)
        self.form.setAlignment(QtCore.Qt.AlignTop)

        self.layout().addWidget(QtWidgets.QLabel("Համառոտ նկարագրություն"), 0, 1)
        self.layout().addWidget(Info('consecutive_short.html'), 1, 1)

    def CreateCtrl(self):

        try:
            count = int(self.count.text())
        except:
            return

        deleteItemsOfLayout(self.form)

        self.lmds = []
        for i in range(count):
            self.lmds.append(QtWidgets.QLineEdit())
            self.form.addRow(QtWidgets.QLabel(f"λ[{i+1}] :"), self.lmds[i])

        self.t = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("t :"), self.t)

        self.dt = QtWidgets.QLineEdit()
        self.form.addRow(QtWidgets.QLabel("dt :"), self.dt)

        self.error = QtWidgets.QLabel("Մուտքագրել համապատասխան տվյալները", objectName='error')
        self.form.addWidget(self.error)

        equal = QtWidgets.QPushButton("Հաշվել")
        self.form.addWidget(equal)

        equal.clicked.connect(self.EqualCtrl)

    def EqualCtrl(self):
        try:
            lmds = map(lambda lmd: float(lmd.text()), self.lmds)
            t = int(self.t.text())
            dt = int(self.dt.text())
            if t<1 or dt<1:
                raise ValueError
        except:
            self.error.setText("Մուտքային տվյալները սխալ են")
            self.error.show()
            return
        calc = ConsecutiveModel(lmds, t, dt)

        if calc is None:
            self.error.setText("Հաշվարկային սխալ (0֊ի բաժանում),\nխնդրում ենք ճշգրտել մուտքային տվյալները․")
            self.error.show()
            return

        self.error.hide()

        table = TableView(self, len(calc.T), 4, ["t", "Pₕ(t)", "fₕ(t)", "λₕ(t)"], calc.T, calc.probability,
                          calc.distribution, calc.failure_rate)
        graphProb = Graph(self)
        graphProb.plot(calc.T, calc.probability, "Անխափան աշխատանքի  հավանականության\n կախումը ժամանակից", "t", "$P_c(t)$")

        graphDist = Graph(self)
        graphDist.plot(calc.T, calc.distribution, "Մինչև  համակարգի  խափանումը ընկած\n ժամանակահատվածի բաշխման խտություն", "t", "$f_c(t)$")

        # graphRate = Graph(self)
        # graphRate.plot(calc.T, calc.failure_rate, "Համակարգի խափանման ինտեսիվություն", "t", "$\lambda_c(t)$")
        content = f'''{{%16 :; T_h%}}={"%.2f" % calc.AverageUptime} <br>
                    {{%16 :; \lambda_h%}}={calc._lmdFR}'''

        self.layout().addWidget(QtWidgets.QLabel("Ելքային տվյալներ"), 2, 0, 1, 2)
        self.layout().addWidget(table, 3, 0)
        self.layout().addWidget(Info(content=content), 4, 0)
        self.layout().addWidget(graphProb, 3, 1)
        self.layout().addWidget(graphDist, 4, 1)
        # self.layout().addWidget(graphRate, 5, 1)


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())