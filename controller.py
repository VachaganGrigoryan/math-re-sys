
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont

import views as ui

import logging as log

from views.tools import Info

log.basicConfig(filename='text.log', filemode='w', format='%(message)s::%(levelname)s::%(asctime)s', level=log.DEBUG)
log.info("This is a controller.py file")

class MainWindowUi(QtWidgets.QMainWindow):
    """MainWindowUi's View (GUI)."""
    log.info("""MainWindowUi's Controller (GUI).""")

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags(), *args, **kwargs):
        super(MainWindowUi, self).__init__(parent=parent, flags=flags, *args, **kwargs)
        self.setupUi()


    def setupUi(self):
        self.scroll = QtWidgets.QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.generalLayout = QtWidgets.QVBoxLayout()
        self.generalLayout.setContentsMargins(20, 20, 20, 20)
        self.generalLayout.setObjectName("generalLayout")

        self.generalLayout.setAlignment(QtCore.Qt.AlignTop)
        self.centralwidget.setLayout(self.generalLayout)


        self.MainTitle = QtWidgets.QLabel()
        self.MainTitle.setObjectName("MainTitle")
        self.MainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.generalLayout.addWidget(self.MainTitle)

        self.selectedtab = QtWidgets.QWidget(self)

        self.SystemType = QtWidgets.QComboBox(self.centralwidget)
        self.SystemType.setObjectName("SystemType")
        self.SystemType.addItems(["", "", "", "", ""])
        self.generalLayout.addWidget(self.SystemType)

        self.SystemType.currentIndexChanged.connect(self._switchSystemView)

        self.scroll.setWidget(self.centralwidget)
        self.setCentralWidget(self.scroll)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 40))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.ctrl_n = QtWidgets.QAction(self)
        self.ctrl_n.setObjectName("ctrl_n")
        self.ctrl_s = QtWidgets.QAction(self)
        self.ctrl_s.setObjectName("ctrl_s")
        self.ctrl_g = QtWidgets.QAction(self)
        self.ctrl_g.setObjectName("ctrl_g")
        self.ctrl_w = QtWidgets.QAction(self)
        self.ctrl_w.setObjectName("ctrl_w")
        self.ctrl_w.triggered.connect(self.close)
        self.ctrl_a = QtWidgets.QAction(self)
        self.ctrl_a.setObjectName("ctrl_a")
        self.ctrl_a.triggered.connect(self.about)
        self.ctrl_c = QtWidgets.QAction(self)
        self.ctrl_c.setObjectName("ctrl_c")
        self.ctrl_p = QtWidgets.QAction(self)
        self.ctrl_p.setObjectName("ctrl_p")
        self.ctrl_o = QtWidgets.QAction(self)
        self.ctrl_o.setObjectName("ctrl_o")
        self.menu_1.addAction(self.ctrl_n)
        self.menu_1.addAction(self.ctrl_o)
        self.menu_1.addAction(self.ctrl_s)
        self.menu_2.addAction(self.ctrl_g)
        self.menu_2.addAction(self.ctrl_c)
        self.menu_2.addAction(self.ctrl_p)
        self.menu_3.addAction(self.ctrl_a)
        self.menu_3.addAction(self.ctrl_w)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    
    def _buildNonBackupNonRecoverable(self):
        log.info("Function _build_buildNonBackupNonRecoverable()")
        # tried = QtWidgets.QToolBox()

        self.selectedtab = QtWidgets.QTabWidget()
        self.selectedtab.addTab(ui.Consecutive(), "Հաջորդական")
        self.selectedtab.addTab(ui.Exponential(), "Ցուցչային")
        self.selectedtab.addTab(ui.Rayle(), "Ռեյլ")
        self.selectedtab.addTab(ui.Weibull(), "Վեյբուլ")
        self.selectedtab.addTab(ui.Gamma(), "Գամմա")
        self.selectedtab.addTab(ui.Normal(), "Նորմալ")

        # tried.addItem(self.selectedtab, 'Հաշվարկ')
        # tried.addItem(Info(), 'Նկարագրություն')

        self.generalLayout.addWidget(self.selectedtab)

    def _buildRNR(self):
        tabwidget = ui.RNR()
        self.selectedtab = tabwidget
        self.generalLayout.addWidget(self.selectedtab)

    
    def _buildNRR(self):
        self.selectedtab = QtWidgets.QTabWidget()
        self.selectedtab.addTab(ui.Primary(), "Հիմնական")

        self.generalLayout.addWidget(self.selectedtab)

    def _buildBackupRecoverable(self):
        self.selectedtab = QtWidgets.QTabWidget()
        self.selectedtab.addTab(ui.BackupByPermanently(), "Մշտական")
        self.selectedtab.addTab(ui.BackupByReplacement(), "Փոխարինումով")
        self.selectedtab.addTab(ui.BackupMixed(), "Խառը")

        self.generalLayout.addWidget(self.selectedtab)
    
    def _switchSystemView(self):
        # self.generalLayout.removeWidget(self.selectedtab)
        self.selectedtab.hide()
        switch = {
            0: lambda: '',
            1: self._buildNonBackupNonRecoverable,
            2: self._buildRNR,
            3: self._buildNRR,
            4: self._buildBackupRecoverable
        }
        return switch.get(self.SystemType.currentIndex())()

    def about(self):
        message = QtWidgets.QMessageBox()
        message.about(self, "Մեր մասին", """ 
        Ծրագիրը ստեղծվել է 2020 թվականին Իրինա Օհանյանի կողմից ուսումնական նկատառումներով։
        Ստեղծված ծրագիրն հիմք է հանդիսանում ավարտական աշխատանքի համար։ Ծրագիրն ավճար է և թույլատրվում 
        է օգտագործել միայն ուսումնական նպատակներով։
        Ծրագիրը ստեղծվել է Python 3 ծրագրավորման լեզվով։ Այստեղ օգտագործվել է մի շարք գրաֆիկական և 
        մաթեմատիկական գրադարաներ, ինչպիսիք են PyQt5, MathPlot, Numpy, Scipy, Math և այլն։
        
        Հեղինակային բոլոր իրավունքները պաշտպանված են և պատկանում են Իրինա Օհանյանին։
        
        Օգտվեք և հեշտացրեք ձեր աշխատանքը։
        """)
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message.button(QtWidgets.QMessageBox.Ok).setText('Text')


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Ավտոմատացված համակարգերի հուսալիություն"))

        self.MainTitle.setText(_translate("MainTitle", "ԱՎՏՈՄԱՏԱՑՎԱԾ ՀԱՄԱԿԱՐԳԵՐԻ ՀՈՒՍԱԼԻՈՒԹՅԱՆ\n ՀԱՇՎԱՐԿԻ ՃԱՐՏԱՐԱԳԻՏԱԿԱՆ ՄԵԹՈԴՆԵՐ"))

        self.SystemType.setItemText(0, _translate("MainWindow", "Ընտրել մեթոդը"))
        self.SystemType.setItemText(1, _translate("MainWindow", "Չպահուստավորված չվերականգնվող"))
        self.SystemType.setItemText(2, _translate("MainWindow", "Պահուստավորված չվերականգնվող"))
        self.SystemType.setItemText(3, _translate("MainWindow", "Չպահուստավորված վերականգնվող"))
        self.SystemType.setItemText(4, _translate("MainWindow", "Պահուստավորված վերականգնվող"))

        self.menu_1.setTitle(_translate("MainWindow", "Ֆայլ"))
        self.menu_2.setTitle(_translate("MainWindow", "Խմբագրել"))
        self.menu_3.setTitle(_translate("MainWindow", "Մեր մասին"))
        self.ctrl_n.setText(_translate("MainWindow", "Նոր"))
        self.ctrl_n.setStatusTip(_translate("MainWindow", "Սկսել նոր հաշվարկ Ctrl+N"))
        self.ctrl_n.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.ctrl_s.setText(_translate("MainWindow", "Պահպանել"))
        self.ctrl_s.setStatusTip(_translate("MainWindow", "Պահպանել հաշվարկը (MS Ecxel) Ctrl+S"))
        self.ctrl_s.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.ctrl_g.setText(_translate("MainWindow", "Գրաֆիկ (JPG)"))
        self.ctrl_g.setStatusTip(_translate("MainWindow", "Պահպանել գրաֆիկը (JPG) Ctrl+G"))
        self.ctrl_g.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.ctrl_w.setText(_translate("MainWindow", "Ելք"))
        self.ctrl_w.setStatusTip(_translate("MainWindow", "Ելք ծրագրից Ctrl+W"))
        self.ctrl_w.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.ctrl_a.setText(_translate("MainWindow", "Հեղինակ"))
        self.ctrl_a.setStatusTip(_translate("MainWindow", "Ծրագիրը ստեղծվել է ․․․ Ctrl+A"))
        self.ctrl_a.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.ctrl_c.setText(_translate("MainWindow", "Պատճենել"))
        self.ctrl_c.setStatusTip(_translate("MainWindow", "Պատճենել գրաֆիկը Ctrl+C"))
        self.ctrl_c.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.ctrl_p.setText(_translate("MainWindow", "Տպել"))
        self.ctrl_p.setStatusTip(_translate("MainWindow", "Տպել գրաֆիկը Ctrl+P"))
        self.ctrl_p.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.ctrl_o.setText(_translate("MainWindow", "Բացել"))
        self.ctrl_o.setStatusTip(_translate("MainWindow", "Բացել հին հաշվարկ Ctrl+O"))
        self.ctrl_o.setShortcut(_translate("MainWindow", "Ctrl+O"))


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
