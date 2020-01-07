# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageshow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    index = 0
    path = '../../Kapan/Garnik/CS50/Week3/Recover/'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, -10, 741, 541))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(f"{Ui_MainWindow.path}{'%03d' % Ui_MainWindow.index}.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(-10, -10, 41, 541))
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(770, -10, 31, 541))
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 40))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.prev.clicked.connect(self._prev)
        self.next.clicked.connect(self._next)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prev.setText(_translate("MainWindow", "prev"))
        # self.prev.setShortcut(_translate("MainWindow", "prev"))
        self.next.setText(_translate("MainWindow", "next"))
        # self.next.setShortcut(_translate("MainWindow", "next"))


    def _next(self):
        if Ui_MainWindow.index != 49:
            Ui_MainWindow.index += 1
        self.label.setPixmap(QtGui.QPixmap(f"{Ui_MainWindow.path}{'%03d' % Ui_MainWindow.index}.jpg"))
    

    def _prev(self):
        if Ui_MainWindow.index != 0:
            Ui_MainWindow.index -= 1
        self.label.setPixmap(QtGui.QPixmap(f"{Ui_MainWindow.path}{'%03d' % Ui_MainWindow.index}.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
