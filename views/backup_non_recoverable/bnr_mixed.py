from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialogButtonBox, QVBoxLayout, QToolBar, QAction, QRadioButton, QButtonGroup, QLabel, \
    QLineEdit, QPushButton, QWidget, QScrollArea, QHBoxLayout, QDialog, QComboBox, QCheckBox


class BNRMixed(QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(BNRMixed, self).__init__(parent=parent, flags=flags)
        self.setLayout(QVBoxLayout())
        self.addSystem = QPushButton('Ավելացնել')
        self.layout().addWidget(self.addSystem)
        # toolBar = QToolBar(self)
        # add = QAction('Ավելացնել', self)
        # add.triggered.connect(self.CreateCtrl)
        # toolBar.addAction(add)
        # self.layout().addWidget(toolBar)

        self.scroll = QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.Systems = QWidget()
        self.Systems.setLayout(QHBoxLayout())
        self.scroll.setWidget(self.Systems)
        self.layout().addWidget(self.scroll)

        self.addSystem.clicked.connect(self.CreateCtrl)

        self.layout().setAlignment(QtCore.Qt.AlignTop)

    def CreateCtrl(self, s):
        dlg = AddSystem(self)
        dlg.exec_()

    def RemoveCtrl(self):
        self.Systems.layout().removeWidget(self.sender().parent())
        self.sender().setParent(None)

class AddSystem(QDialog):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(AddSystem, self).__init__(parent=parent, flags=flags)
        self.setWindowTitle("Ավելացնել համակարգ")
        self.setLayout(QVBoxLayout())

        self.setupContent()

        btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btnBox.accepted.connect(self.accept)
        btnBox.rejected.connect(self.reject)
        btnBox.button(QDialogButtonBox.Ok).setText("Ստեղծել")
        btnBox.button(QDialogButtonBox.Cancel).setText("Չեղարկել")
        self.layout().addWidget(btnBox)

    def setupContent(self):
        self.Content = QWidget(self)
        self.layout().addWidget(self.Content)
        self.FormLayout = QtWidgets.QFormLayout()
        self.Content.setLayout(self.FormLayout)

        self.system = QComboBox()
        self.system.addItem("Ցուցչային")
        self.system.addItem("Վեյբուլ")
        # self.system.currentIndexChanged.connect(self.systemChanged)

        self.SysType = [
            (QRadioButton('Չպահուստավորված', objectName='0'), QRadioButton('Պահուստավորված', objectName='1')),
        ]
        self.btnGroupOne = QButtonGroup(self)
        self.btnGroupOne.addButton(self.SysType[0][0])
        self.btnGroupOne.addButton(self.SysType[0][1])
        self.btnGroupOne.buttonClicked.connect(self.onClickedTypeOne)

        self.FormLayout.addRow(QLabel("Համակարգի տեսակը"), self.system)
        self.FormLayout.addRow(self.SysType[0][0], self.SysType[0][1])

    def onClickedTypeOne(self, btn):
        if int(btn.objectName()):
            self.SysType.append((QRadioButton('Մշտական', objectName='0'), QRadioButton('Փոխարինումով', objectName='1')))
            self.btnGroupTwo = QButtonGroup(self)
            self.btnGroupTwo.addButton(self.SysType[1][0])
            self.btnGroupTwo.addButton(self.SysType[1][1])
            self.FormLayout.addRow(self.SysType[1][0], self.SysType[1][1])
            
            self.SysType.append((QRadioButton('Ըստ տարրերի', objectName='0'), QRadioButton('Ընդհանուր', objectName='1')))
            self.btnGroupThree = QButtonGroup(self)
            self.btnGroupThree.addButton(self.SysType[2][0])
            self.btnGroupThree.addButton(self.SysType[2][1])
            self.btnGroupThree.buttonClicked.connect(self.onClickedTypeThree)
            self.FormLayout.addRow(self.SysType[2][0], self.SysType[2][1])
            self.isSame = QCheckBox('Պահուստավորված տարերի \nարժեքները նունական են')
            self.FormLayout.addWidget(self.isSame)
            self.col = QLineEdit()
            self.FormLayout.addRow(QLabel("Պահուստավորված տարերի քանակ (m)"), self.col)
        else:
            self.SysType = self.SysType[:1]
            for i in range(4, self.FormLayout.count(), 2):
                self.FormLayout.removeRow(2)

    def onClickedTypeThree(self, btn):
        if int(btn.objectName()):
            self.row = QLineEdit()
            self.row.setText('2')
            self.FormLayout.addRow(QLabel("Համակարգի տարերի քանակ (n)"), self.row)
        else:
            self.FormLayout.removeRow(6)

    def systemChanged(self):
        switch = {
            0: self.exponential,
            1: self.weibull
        }
        return switch.get(self.system.currentIndex())()

    def exponential(self):
        pass

    def weibull(self):
        pass

    def accept(self) -> None:
        System = QWidget(self)
        self.parent().Systems.layout().addWidget(System)
        form = QtWidgets.QFormLayout()
        System.setLayout(form)

        toolBar = QToolBar(System)
        remove = QAction('Ջնջել', System)
        remove.triggered.connect(self.parent().RemoveCtrl)
        toolBar.addAction(remove)
        # edit = QAction('Խմբագրել', System)
        # toolBar.addAction(edit)
        form.addWidget(toolBar)

        SysConfig = {
            'system': self.system.currentIndex(),
            'col': 0,
            'row': 1,
            'typeOne' : [self.btnGroupOne.checkedId()]
        }
        print(SysConfig)

        self.close()


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())