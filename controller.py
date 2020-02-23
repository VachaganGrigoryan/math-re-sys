from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

import view as ui


import logging as log
log.basicConfig(filename='text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)
log.info("This is a controller.py file")

class MainWindowUi(QtWidgets.QMainWindow):
    """MainWindowUi's View (GUI)."""

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(MainWindowUi, self).__init__(parent=parent, flags=flags)
        
        self.setupUi()


    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.generalLayout = QtWidgets.QVBoxLayout()
        self.generalLayout.setContentsMargins(20, 20, 20, 20)
        self.generalLayout.setObjectName("generalLayout")

        self.generalLayout.setAlignment(QtCore.Qt.AlignTop)
        self.centralwidget.setLayout(self.generalLayout)

        self.selectedtab = QtWidgets.QWidget(self)
        
        # self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.formLayoutWidget.setGeometry(QtCore.QRect(0, 120, 611, 261))
        # self.formLayoutWidget.setObjectName("formLayoutWidget")

        # self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout.setObjectName("gridLayout")

        # self.ok = QtWidgets.QPushButton(self.formLayoutWidget)
        # self.ok.setObjectName("ok")
        # self.gridLayout.addWidget(self.ok, 2, 0, 1, 1)
        # self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        # self.lineEdit.setObjectName("lineEdit")
        # self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.sysType = QtWidgets.QComboBox(self.centralwidget)
        # self.sysType.setGeometry(QtCore.QRect(20, 20, 520, 40))
        self.sysType.setObjectName("sysType")
        self.sysType.addItems(["","","","",""])
        self.generalLayout.addWidget(self.sysType)
        self.sysType.currentIndexChanged.connect(lambda: self._switchUi(self.sysType.currentIndex()))

        # self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        # self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItems(["","","","",""])
        # self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        
        # self.comboBox.currentIndexChanged.connect(lambda: self._switchUi(self.comboBox.currentIndex()))


        # self.graph = StaticCanvas(self.centralwidget)
        # # self.graph.setGeometry(QtCore.QRect(610, 0, 411, 261))
        # self.graph.setObjectName("graph")
        # self.graph.plot(T, exp, "Graph for Probability")
        # self.graph.plot(T, gamma, "Graph for Probability")
        # self.generalLayout.addWidget(self.graph)

        # self.console = QtWidgets.QLabel(self.centralwidget)
        # self.console.setGeometry(QtCore.QRect(0, 290, 89, 28))
        # self.console.setText("Console")
        # self.console.setObjectName("console")
        # self.generalLayout.addWidget(self.console)


        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 40))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(self)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(self)
        self.action_2.setObjectName("action_2")
        self.action_JPG = QtWidgets.QAction(self)
        self.action_JPG.setObjectName("action_JPG")
        self.action_3 = QtWidgets.QAction(self)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(self)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(self)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(self)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(self)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_JPG)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # self.ok.clicked.connect(self._ok)

    
    def _buildNRNR(self):
        log.info("Function _buildNRNR()")
        tabwidget = QtWidgets.QTabWidget()
        tabwidget.addTab(ui.Weibull(), "Weibull")
        tabwidget.addTab(ui.Gamma(), "Gamma")
        tabwidget.addTab(ui.Rayle(), "Rayle")
        tabwidget.addTab(ui.Exponential(), "Exponential")
        tabwidget.addTab(ui.Normal(), "Normal")
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # font.setPointSize(19)
        tabwidget.setFont(QFont("Times", 15, QFont.Bold))
        self.selectedtab = tabwidget
        self.generalLayout.addWidget(self.selectedtab)


    def _buildRNR(self):
        log.info("Function _buildRNR()")
        tabwidget = ui.RNR()     
        self.selectedtab = tabwidget
        self.generalLayout.addWidget(self.selectedtab)

    
    def _buildNRR(self):
        log.info("Function _buildNRR()")
        tabwidget = ui.NRR()     
        self.selectedtab = tabwidget
        self.generalLayout.addWidget(self.selectedtab)
        

    def _buildRR(self):
        print("Any Ui 4")
        tabwidget = ui.RR()     
        self.selectedtab = tabwidget
        self.generalLayout.addWidget(self.selectedtab)
    
    def _switchUi(self, i):
        print(i)
        # self.generalLayout.removeWidget(self.selectedtab)
        self.selectedtab.hide()
        switch = {
            0: lambda: '',
            1: self._buildNRNR,
            2: self._buildRNR,
            3: self._buildNRR,
            4: self._buildRR
        }
        return switch.get(i)()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Ավտոմատացված համակարգերի հուսալիություն"))
        # self.ok.setText(_translate("MainWindow", "Առաջ"))
        

        # self.comboBox.setItemText(1, _translate("MainWindow", "Ենթահամակարգ"))
        # self.comboBox.setItemText(2, _translate("MainWindow", "Հաջորդական"))
        # self.comboBox.setItemText(3, _translate("MainWindow", "Մշտական"))
        # self.comboBox.setItemText(4, _translate("MainWindow", "Փոխարինումով"))

        self.sysType.setItemText(0, _translate("MainWindow", "Ընտրել համակարգը"))
        self.sysType.setItemText(1, _translate("MainWindow", "Չպահուստավորված չվերականգնվող"))
        self.sysType.setItemText(2, _translate("MainWindow", "Պահուստավորված չվերականգնվող"))
        self.sysType.setItemText(3, _translate("MainWindow", "Չպահուստավորված վերականգնվող"))
        self.sysType.setItemText(4, _translate("MainWindow", "Պահուստավորված վերականգնվող"))

        
       
        
        self.menu.setTitle(_translate("MainWindow", "Ֆայլ"))
        self.menu_2.setTitle(_translate("MainWindow", "Խմբագրել"))
        self.menu_3.setTitle(_translate("MainWindow", "Մեր մասին"))
        self.action.setText(_translate("MainWindow", "Նոր"))
        self.action.setStatusTip(_translate("MainWindow", "Սկսել նոր հաշվարկ Ctrl+N"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_2.setText(_translate("MainWindow", "Պահպանել"))
        self.action_2.setStatusTip(_translate("MainWindow", "Պահպանել հաշվարկը (MS Ecxel) Ctrl+S"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_JPG.setText(_translate("MainWindow", "Գրաֆիկ (JPG)"))
        self.action_JPG.setStatusTip(_translate("MainWindow", "Պահպանել գրաֆիկը (JPG) Ctrl+G"))
        self.action_JPG.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.action_3.setText(_translate("MainWindow", "Ելք"))
        self.action_3.setStatusTip(_translate("MainWindow", "Ելք ծրագրից Ctrl+W"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_4.setText(_translate("MainWindow", "Հեղինակ"))
        self.action_4.setStatusTip(_translate("MainWindow", "Ծրագիրը ստեղծվել է ․․․ Ctrl+A"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_5.setText(_translate("MainWindow", "Պատճենել"))
        self.action_5.setStatusTip(_translate("MainWindow", "Պատճենել գրաֆիկը Ctrl+C"))
        self.action_5.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_6.setText(_translate("MainWindow", "Տպել"))
        self.action_6.setStatusTip(_translate("MainWindow", "Տպել գրաֆիկը Ctrl+P"))
        self.action_6.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_7.setText(_translate("MainWindow", "Բացել"))
        self.action_7.setStatusTip(_translate("MainWindow", "Բացել հին հաշվարկ Ctrl+O"))
        self.action_7.setShortcut(_translate("MainWindow", "Ctrl+O"))


class RootEqualCtrl:    
    """RootEqual's Controller."""
    def __init__(self, prob, dist, view):
        """Controller initializer."""
        self._prob = prob
        self._dist = dist
        self._view = view
        # Connect signals and slots
        self._connectSignals()
    
    
    def _ok(self):
        print("ok")
    
    
    def _connectSignals(self):
        """Connect signals and slots."""
        print("Connect")

        # self._view.ok.clicked.connect(self._ok)
