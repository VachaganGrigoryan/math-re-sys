# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diplom1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class RootEqualUi(QMainWindow):
    """RootEqual's View (GUI)."""
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(RootEqualUi, self).__init__(parent=parent, flags=flags)
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("My App Title") 
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 311, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.ok = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        
        self.graph = QtWidgets.QWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(380, 0, 331, 221))
        self.graph.setObjectName("graph")
        self.console = QtWidgets.QLabel(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(0, 290, 89, 28))
        self.console.setText("")
        self.console.setObjectName("console")

        self.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 40))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ok.setText(_translate("MainWindow", "Առաջ"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ենթահամակարգ"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Հաջորդական"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Մշտական"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Փոխարինումով"))




class RootEqualCtrl:    
    """RootEqual's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = RootEqualUi()
    ui.show()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
