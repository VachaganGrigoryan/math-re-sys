from PyQt5 import QtWidgets
from models import non_recoverable_non_backup
from views.graph import StaticCanvas

class NRR(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(NRR, self).__init__(parent=parent, *args, **kwargs)

        self.horizontalLayout = QtWidgets.QVBoxLayout(self)
        self.MainLayout = QtWidgets.QGridLayout()

        self.PropertyLayout = QtWidgets.QGridLayout()
        self.PropertyLayout.addWidget(QtWidgets.QLabel(f"λ :"), 0, 0)
        self.PropertyLayout.addWidget(QtWidgets.QLineEdit(), 1, 0)

        self.PropertyLayout.addWidget(QtWidgets.QLabel(f"μ :"), 0, 1)
        self.PropertyLayout.addWidget(QtWidgets.QLineEdit(), 1, 1)

        self.pb_addRow = QtWidgets.QPushButton("Ավելացնել")

        self.PropertyLayout.addWidget(self.pb_addRow, 1, 2)

        self.MainLayout.addLayout(self.PropertyLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.MainLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.MainLayout)

        self.pb_addRow.clicked.connect(self.addRow)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.horizontalLayout.addWidget(self.equal)

        self.equal.clicked.connect(self.EqualCtrl)

    def addRow(self):
        rows = self.PropertyLayout.rowCount()
        print(rows)
        columns = self.PropertyLayout.columnCount()
        for column in range(columns):
            layout = self.PropertyLayout.itemAtPosition(rows - 1, column)
            if layout is not None:
                widget = layout.widget()
                if isinstance(widget, QtWidgets.QPushButton):
                    widget.setText('Հեռացնել %d' % (rows - 1))
                    widget.clicked.disconnect(self.addRow)
                    widget.clicked.connect(self.removeRow)
                else:
                    widget.setEnabled(False)

        self.PropertyLayout.addWidget(QtWidgets.QLineEdit(), rows, 0)
        self.PropertyLayout.addWidget(QtWidgets.QLineEdit(), rows, 1)

        widget = QtWidgets.QPushButton('Ավելացնել')
        widget.clicked.connect(self.addRow)
        self.PropertyLayout.addWidget(widget, rows, columns - 1, 1, 1)

    def removeRow(self):
        index = self.PropertyLayout.indexOf(self.sender())
        row = self.PropertyLayout.getItemPosition(index)[0]

        for column in range(self.PropertyLayout.columnCount()):
            layout = self.PropertyLayout.itemAtPosition(row, column)
            if layout is not None:
                print(layout)
                layout.widget().deleteLater()
                self.PropertyLayout.removeItem(layout)

    def EqualCtrl(self):
        print("Equal")
        rows = self.PropertyLayout.rowCount()

        lmd = [float(self.PropertyLayout.itemAtPosition(row, 0).widget().text() or 0) for row in range(1, rows) if
               self.PropertyLayout.itemAtPosition(row, 0)]
        myu = [float(self.PropertyLayout.itemAtPosition(row, 1).widget().text() or 0) for row in range(1, rows) if
               self.PropertyLayout.itemAtPosition(row, 1)]
        print(lmd, myu)

        self.asr = non_recoverable_non_backup.NRR(lmd, myu, 40)

        graphLayout = QtWidgets.QHBoxLayout(self)
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.FunctionAvailability, "Graph for Function Availability")
        graphLayout.addWidget(self.graphProb)

        self.MainLayout.addLayout(graphLayout, 3, 0, 3, 2)

