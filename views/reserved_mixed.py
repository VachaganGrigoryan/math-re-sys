import math

from PyQt5 import QtCore, QtWidgets

from models.recoverable_backup import *


class MixedReserved(QtWidgets.QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(MixedReserved, self).__init__(parent=parent, flags=flags)
        self.MainLayout = QtWidgets.QVBoxLayout(self)
        # self.MainLayout.addWidget(System(self))

        self.scroll = QtWidgets.QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.System = System(self)
        self.scroll.setWidget(self.System)
        self.MainLayout.addWidget(self.scroll)



        equal = QtWidgets.QPushButton('Հաշվել', objectName='equal')
        self.MainLayout.addWidget(equal)
        equal.clicked.connect(self.EqualCtrl)

        self.setLayout(self.MainLayout)


        self.MainLayout.setAlignment(QtCore.Qt.AlignTop)


    def EqualCtrl(self):

        values = MixedReserved.getValues(self.System)

        print(values)

    @staticmethod
    def getValues(system):
        # system = self.System
        print(system)
        rows = system.MainLayout.rowCount()
        cols = system.MainLayout.columnCount()
        print(rows, cols)
        if rows is 1: return

        ls = []
        for row in range(1, rows):
            for col in range(0, cols):
                elm = system.MainLayout.itemAtPosition(row, col)
                print(elm)
                if elm:
                    widget = elm.widget()
                    print(widget)
                    if widget.sysType.currentIndex():
                        print(widget.System)
                        ls.append(RR.getValues(widget.System))
                    else:
                        ls.append((float(widget.grid.itemAtPosition(0, 1).widget().text() or 0), float(widget.grid.itemAtPosition(1, 1).widget().text() or 0)))
        #
        # [RR.getValues(system.MainLayout.itemAtPosition(row, col).widget().System) if system.MainLayout.itemAtPosition(row, col).widget().sysType.currentIndex() else (system.MainLayout.itemAtPosition(row, col).widget().grid.itemAtPosition(0, 1).widget().text(), system.MainLayout.itemAtPosition(row, col).widget().grid.itemAtPosition(1, 1).widget().text())  for row in range(1, rows) for col in range(0, cols) if system.MainLayout.itemAtPosition(row, col)]
        #
        sys_dict = {
            'type': [system.type1.currentIndex(), system.type2.currentIndex()],
            'value': ls
        }

        return sys_dict


class System(QtWidgets.QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(System, self).__init__(parent=parent, flags=flags)

        self.MainLayout = QtWidgets.QGridLayout()

        self.MainLayout.addWidget(QtWidgets.QLabel('N = '), 0, 0)
        self.MainLayout.addWidget(QtWidgets.QLineEdit(objectName='count'), 0, 1)
        create = QtWidgets.QPushButton('Ստեղծել', objectName='create')
        self.MainLayout.addWidget(create, 0, 2)
        create.clicked.connect(self.CreateCtrl)

        self.setLayout(self.MainLayout)
        self.MainLayout.setAlignment(QtCore.Qt.AlignTop)

    def CreateCtrl(self):

        try:
            count = self.findChild(QtWidgets.QLineEdit, "count")
            k = int(count.text())
        except:
            return

        deleteItemsOfLayout(self.MainLayout)

        self.type1 = QtWidgets.QComboBox(self)
        self.type1.addItems(["Ըստ տարրերի", "Ընդհանուր"])
        self.MainLayout.addWidget(self.type1, 0, 0)
        self.type2 = QtWidgets.QComboBox(self)
        self.type2.addItems(["Մշտական", "Փոխարինումով"])
        self.MainLayout.addWidget(self.type2, 0, 1)

        n = math.ceil(math.sqrt(k))
        print(n)
        for i in range(1, n+1):
            for j in range(n):
                self.MainLayout.addWidget(Element(), i, j)
                if k == (i-1)*n+j+1:
                    break
            else:
                continue
            break


class Element(QtWidgets.QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(Element, self).__init__(parent=parent, flags=flags)
        self.MainLayout = QtWidgets.QVBoxLayout(self)
        self.sysType = QtWidgets.QComboBox(self)
        self.grid = QtWidgets.QGridLayout()
        self.setupUi()

        self.MainLayout.setAlignment(QtCore.Qt.AlignTop)

    def setupUi(self):
        self.setLayout(self.MainLayout)
        self.sysType.addItems(["Տարր", "Համակարգ"])
        self.sysType.currentIndexChanged.connect(self.sysTypechange)
        self.MainLayout.addWidget(self.sysType)
        self.sysTypechange(0)

    def sysTypechange(self, i):
        print(i)

        if not i:
            deleteItemsOfLayout(self.grid)
            self.MainLayout.addLayout(self.grid)
            self.grid.addWidget(QtWidgets.QLabel(f"λ :"), 0, 0)
            self.grid.addWidget(QtWidgets.QLineEdit(), 0, 1)

            self.grid.addWidget(QtWidgets.QLabel(f"μ :"), 1, 0)
            self.grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
        else:
            deleteItemsOfLayout(self.grid)
            self.System = System()
            self.grid.addWidget(self.System)




def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())