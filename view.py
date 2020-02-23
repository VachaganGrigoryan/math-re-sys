
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

from graph import StaticCanvas
from auto_system_reliability import asr

import math

import logging as log
log.basicConfig(filename='text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)
log.info("This is a view.py file")

class Weibull(QtWidgets.QWidget): # , asr.Weibull
    def __init__(self):
        super().__init__()

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

        # asr.Weibull.super(self, int(self.alpha.text()), int(self.beta.text()))
        self.equal.clicked.connect(self.EqualCtrl)

    def EqualCtrl(self):
        # self.T = list(range(0,5000,100))

        # self.prob = [P().Weibull(t, int(self.alpha.text()), int(self.beta.text())) for t in self.T]
        # self.dist = [F().Weibull(t, int(self.alpha.text()), int(self.beta.text())) for t in self.T]
        
        self.asr = asr.Weibull(int(self.alpha.text()), int(self.beta.text()), 5000)


        graphLayout = QtWidgets.QHBoxLayout(self)
        
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)


        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")

        graphLayout.addWidget(self.graphDist)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2) 


class Gamma(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
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

    def EqualCtrl(self):
        # self.T = list(range(0,5000,100))

        # self.prob = [P().Gamma(t, int(self.alpha.text()), int(self.beta.text())) for t in self.T]
        # self.dist = [F().Gamma(t, int(self.alpha.text()), int(self.beta.text())) for t in self.T]
        
        self.asr = asr.Gamma(int(self.alpha.text()), int(self.beta.text()), 5000)


        graphLayout = QtWidgets.QHBoxLayout(self)
        
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)


        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")

        graphLayout.addWidget(self.graphDist)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2) 



class Rayle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("λ :"), 0, 0)
        # self.layout.addWidget(QtWidgets.QLabel("β :"), 1, 0)

        self.lmd = QtWidgets.QLineEdit()
        self.layout.addWidget(self.lmd, 0, 1)

        # self.beta = QtWidgets.QLineEdit()
        # self.layout.addWidget(self.beta, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)

        self.equal.clicked.connect(self.EqualCtrl)

    def EqualCtrl(self):
        # self.T = list(range(0,5000,100))

        # self.prob = [P().Rayle(t, float(self.lmd.text())) for t in self.T]
        # self.dist = [F().Rayle(t, float(self.lmd.text())) for t in self.T]
        
        self.asr = asr.Rayle(float(self.lmd.text()), 5000)


        graphLayout = QtWidgets.QHBoxLayout(self)
        
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)


        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")

        graphLayout.addWidget(self.graphDist)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2) 



class Exponential(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("λ :"), 0, 0)
        # self.layout.addWidget(QtWidgets.QLabel("β :"), 1, 0)

        self.lmd = QtWidgets.QLineEdit()
        self.layout.addWidget(self.lmd, 0, 1)

        # self.beta = QtWidgets.QLineEdit()
        # self.layout.addWidget(self.beta, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)

        self.equal.clicked.connect(self.EqualCtrl)


    def EqualCtrl(self):
        # self.T = list(range(0,5000,100))

        # self.prob = [P().Exponential(t, float(self.lmd.text())) for t in self.T]
        # self.dist = [F().Exponential(t, float(self.lmd.text())) for t in self.T]
        
        self.asr = asr.Exponential(float(self.lmd.text()), 5000)


        graphLayout = QtWidgets.QHBoxLayout(self)
        
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)


        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")

        graphLayout.addWidget(self.graphDist)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2) 


class Normal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("m˳ :"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("Ϭ˳ :"), 1, 0)

        self.m0 = QtWidgets.QLineEdit()
        self.layout.addWidget(self.m0, 0, 1)

        self.sig0 = QtWidgets.QLineEdit()
        self.layout.addWidget(self.sig0, 1, 1)

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, 2, 1)

        self.setLayout(self.layout)

        self.equal.clicked.connect(self.EqualCtrl)


    def EqualCtrl(self):
        # self.T = list(range(0,5000,100))

        # self.prob = [P().Normal(t, float(self.m0.text()), float(self.sig0.text())) for t in self.T]
        # self.dist = [F().Normal(t, float(self.m0.text()), float(self.sig0.text())) for t in self.T]
        
        self.asr = asr.Normal(int(self.m0.text()), int(self.sig0.text()), 5000)


        graphLayout = QtWidgets.QHBoxLayout(self)
        
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)


        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")

        graphLayout.addWidget(self.graphDist)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2)




class RNR(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
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


    def EqualCtrl(self):
        self.asr = asr.RNR(int(self.m.text()), float(self.lmd.text()), 100)


        graphLayout = QtWidgets.QHBoxLayout(self)
        
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        print(self.asr.probability)
        self.graphProb.plot(self.asr.T, self.asr.probability, "Graph for Probability")
        graphLayout.addWidget(self.graphProb)

        self.graphDist = StaticCanvas(self)
        self.graphDist.setObjectName("graphDist")
        print(self.asr.distribution)
        self.graphDist.plot(self.asr.T, self.asr.distribution, "Graph for Distribution")
        graphLayout.addWidget(self.graphDist)

        self.graphSysFailRate = StaticCanvas(self)
        self.graphSysFailRate.setObjectName("graphSysFailRate")
        self.graphSysFailRate.plot(self.asr.T, self.asr.system_failure_rate, "Graph for System Failure Rate")
        graphLayout.addWidget(self.graphSysFailRate)

        self.layout.addLayout(graphLayout, 3, 0, 3, 2)



class NRR(QtWidgets.QWidget):
    log.info("Class NRR")
    def __init__(self):
        super().__init__()
        log.info("NRR init")

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
               
        self.pb_addRow.clicked.connect( self.addRow )

        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.horizontalLayout.addWidget(self.equal)
        
        self.equal.clicked.connect(self.EqualCtrl)


    def addRow( self ):
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
        # lmd = []
        # myu = []
        # for row in range(1, rows):
        #     l = self.PropertyLayout.itemAtPosition(row, 0)
        #     m = self.PropertyLayout.itemAtPosition(row, 1)
        #     if l and m:
        #         print(l.widget().text(), m.widget().text())
        #         lmd.append(float(l.widget().text() or 0))
        #         myu.append(float(m.widget().text() or 0))
        lmd = [float(self.PropertyLayout.itemAtPosition(row, 0).widget().text() or 0) for row in range(1, rows) if self.PropertyLayout.itemAtPosition(row, 0)]
        myu = [float(self.PropertyLayout.itemAtPosition(row, 1).widget().text() or 0) for row in range(1, rows) if self.PropertyLayout.itemAtPosition(row, 1)]
        print(lmd, myu)

        self.asr = asr.NRR(lmd, myu, 40)

        graphLayout = QtWidgets.QHBoxLayout(self)
        self.graphProb = StaticCanvas(self)
        self.graphProb.setObjectName("graphProb")
        self.graphProb.plot(self.asr.T, self.asr.FunctionAvailability, "Graph for Function Availability")
        graphLayout.addWidget(self.graphProb)


        self.MainLayout.addLayout(graphLayout, 3, 0, 3, 2)        



class RR(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.MainLayout = QtWidgets.QGridLayout()

        self.MainLayout.addWidget(QtWidgets.QLabel('N = '), 0, 0)
        self.MainLayout.addWidget(QtWidgets.QLineEdit(objectName='count'), 0, 1)
        create = QtWidgets.QPushButton('Ստեղծել', objectName='create')
        self.MainLayout.addWidget(create, 0, 2)
        create.clicked.connect(self.CreateCtrl)


        self.setLayout(self.MainLayout)

    def CreateCtrl(self):

        try:
            count = self.findChild(QtWidgets.QLineEdit, "count")
            k = int(count.text())
        except:
            return
        
        deleteItemsOfLayout(self.MainLayout)
        # self.MainLayout = QtWidgets.QGridLayout()
        n = math.ceil(math.sqrt(k))

        for i in range(n):
            for j in range(1, n+1):
                self.MainLayout.addWidget(System(), i, j)
                if k == i*n+j:
                    break
            else:
                continue
            break

        # self.setLayout(self.MainLayout)

class System(QtWidgets.QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi()

    def setupUi(self):
        self.MainLayout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.MainLayout)
        self.sysType = QtWidgets.QComboBox(self)
        self.sysType.addItems(["Տարր", "Համակարգ"])
        self.sysType.currentIndexChanged.connect(self.sysTypechange)
        self.MainLayout.addWidget(self.sysType)
        
        self.grid = QtWidgets.QGridLayout()
        self.sysTypechange(0)
    
    def sysTypechange(self,i):
        print(i)

        if not i: 
            deleteItemsOfLayout(self.grid)
            self.MainLayout.addLayout(self.grid)      
            self.grid.addWidget(QtWidgets.QLabel(f"λ :"), 1, 0)
            self.grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
            
            self.grid.addWidget(QtWidgets.QLabel(f"μ :"), 2, 0)
            self.grid.addWidget(QtWidgets.QLineEdit(), 2, 1)
        else:
            deleteItemsOfLayout(self.grid)
            self.grid.addWidget(RR())




def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())