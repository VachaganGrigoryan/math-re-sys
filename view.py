
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

from graph import StaticCanvas
from auto_system_reliability import asr


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



class NRR(QtWidgets.QWidget):
    log.info("Class NRR")
    def __init__(self):
        super().__init__()
        log.info("NRR init")

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("N :"), 0, 0)

        self.n = QtWidgets.QLineEdit()
        self.layout.addWidget(self.n, 0, 1)

        self.create = QtWidgets.QPushButton("Ստեղծել")
        self.layout.addWidget(self.create, 0, 2)

        self.setLayout(self.layout)

        self.create.clicked.connect(self.CreateCtrl)

    def CreateCtrl(self):
        log.info(f"Create Ctrl NRR(n={self.n})")
        n = int(self.n.text())
               
        # self.layout = QtWidgets.QGridLayout()
        
        self.lmd = []
        self.myu = []            

        for i in range(n):
            self.lmd.append(QtWidgets.QLineEdit())
            self.myu.append(QtWidgets.QLineEdit())
            self.layout.addWidget(QtWidgets.QLabel(f"λ{i} :"), i, 0)
            self.layout.addWidget(self.lmd[i-1], i, 1)
            self.layout.addWidget(QtWidgets.QLabel(f"μ{i} :"), i, 2)
            self.layout.addWidget(self.myu[i-1], i, 3)
                
        self.equal = QtWidgets.QPushButton("Հաշվել")
        self.layout.addWidget(self.equal, n+1, 0, n+1, 4)
        
        self.equal.clicked.connect(self.EqualCtrl)


    def EqualCtrl(self):

        lmd = map(lambda lmd: lmd.text(), self.lmd)
        myu = map(lambda myu: myu.text(), self.myu)
        print(list(lmd), list(myu))
