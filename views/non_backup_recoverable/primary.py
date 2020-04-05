from PyQt5 import QtWidgets, QtCore
from models import Primary as PrimaryModel, Primary2 as PrimaryModel2
from views.tools import Info, Graph, TableView

class Primary(QtWidgets.QToolBox):

    def __init__(self, parent=None, *args, **kwargs):
        super(Primary, self).__init__(parent=parent, *args, **kwargs)

        self.addItem(QtWidgets.QWidget(), 'Հաշվարկ')
        # self.addItem(Info(), 'Նկարագրություն')
        self.widget(0).setLayout(QtWidgets.QGridLayout())

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Մուտքային տվյալներ"), 0, 0)
        self.mainWidget = QtWidgets.QWidget()
        self.widget(0).layout().addWidget(self.mainWidget, 1, 0)
        self.mainWidget.setLayout(QtWidgets.QGridLayout())

        inputW = QtWidgets.QWidget()
        self.mainWidget.layout().addWidget(inputW)
        form = QtWidgets.QFormLayout(inputW)

        self.count = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel("N :"), self.count)
        self.isSame = QtWidgets.QCheckBox('Էլեմենտների վերականգման ուժգնությունը միանման է')
        form.addWidget(self.isSame)

        create = QtWidgets.QPushButton("Ստեղծել")
        form.addWidget(create)

        create.clicked.connect(self.CreateCtrl)
        form.setAlignment(QtCore.Qt.AlignTop)
        self.mainWidget.layout().setAlignment(QtCore.Qt.AlignTop)

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Համառոտ նկարագրություն"), 0, 1)
        self.widget(0).layout().addWidget(Info(), 1, 1)

    def CreateCtrl(self):

        try:
            count = int(self.count.text())
            self.isSame = self.isSame.isChecked()
        except:
            return

        deleteItemsOfLayout(self.mainWidget.layout())

        input1 = QtWidgets.QWidget()
        input2 = QtWidgets.QWidget()
        form1 = QtWidgets.QFormLayout(input1)
        form2 = QtWidgets.QFormLayout(input2)
        self.mainWidget.layout().addWidget(input1, 0, 0)
        self.mainWidget.layout().addWidget(input2, 0, 1)

        self.lmds = []
        self.myus = []
        for i in range(count):
            self.lmds.append(QtWidgets.QLineEdit())
            form1.addRow(QtWidgets.QLabel(f"λ[{i+1}] :"), self.lmds[i])
            if not self.isSame:
                self.myus.append(QtWidgets.QLineEdit())
                form2.addRow(QtWidgets.QLabel(f"μ[{i+1}] :"), self.myus[i])

        if self.isSame:
            self.myu = QtWidgets.QLineEdit()
            form1.addRow(QtWidgets.QLabel("μ :"), self.myu)


        self.t = QtWidgets.QLineEdit()
        form1.addRow(QtWidgets.QLabel("t :"), self.t)

        self.dt = QtWidgets.QLineEdit()
        form1.addRow(QtWidgets.QLabel("dt :"), self.dt)

        self.error = QtWidgets.QLabel("Մուտքագրել համապատասխան տվյալները", objectName='error')
        self.error.hide()
        self.mainWidget.layout().addWidget(self.error, 1, 0, 1, 2)

        equal = QtWidgets.QPushButton("Հաշվել")
        self.mainWidget.layout().addWidget(equal, 2, 0, 1, 2)

        equal.clicked.connect(self.EqualCtrl)


    def EqualCtrl(self):

        try:
            lmd = list(map(lambda lmd: float(lmd.text()), self.lmds))
            if self.isSame: myu = float(self.myu.text())
            else: myu = list(map(lambda myu: float(myu.text()), self.myus))
            t = int(self.t.text())
            dt = int(self.dt.text())
            if t<1 or dt<1:
                raise ValueError
        except:
            self.error.setText("Մուտքային տվյալները սխալ են")
            self.error.show()
            return

        if self.isSame:
            calc = PrimaryModel(lmd, myu, t, dt)
        else:
            calc = PrimaryModel2(lmd, myu, t, dt)

        if calc is None:
            self.error.setText("Հաշվարկային սխալ (0֊ի բաժանում), \nխնդրում ենք ճշգրտել մուտքային տվյալները․")
            self.error.show()
            return

        self.error.hide()

        table = TableView(self, len(calc.T), 2, ["t", "Kₕ(t)"], calc.T, calc.availability)

        graphAvailable = Graph(self)
        graphAvailable.plot(calc.T, calc.availability, "Անխափան աշխատանքի  հավանականություն", "t", "$K_g(t)$")

        self.widget(0).layout().addWidget(QtWidgets.QLabel("Ելքային տվյալներ"), 2, 0, 1, 2)
        self.widget(0).layout().addWidget(table, 3, 0, 2, 1)
        self.widget(0).layout().addWidget(graphAvailable, 3, 1)


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())