from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QRegExpValidator, QValidator, QIntValidator
from PyQt5.QtWidgets import QDialogButtonBox, QVBoxLayout, QToolBar, QAction, QRadioButton, QButtonGroup, QLabel, \
    QLineEdit, QPushButton, QWidget, QScrollArea, QHBoxLayout, QDialog, QComboBox, QCheckBox, QFormLayout, QGroupBox


class BNRMixed(QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(BNRMixed, self).__init__(parent=parent, flags=flags)
        self.setLayout(QVBoxLayout())
        # self.addSystem = QPushButton('Ավելացնել')
        # self.addSystem.clicked.connect(self.CreateCtrl)
        # self.layout().addWidget(self.addSystem)
        toolBar = QToolBar(self)
        add = QAction('Ավելացնել', self)
        add.triggered.connect(self.CreateCtrl)
        toolBar.addAction(add)
        self.calc = QAction('Հաշվել', self)
        self.calc.triggered.connect(self.EqualCtrl)
        self.calc.setEnabled(False)
        toolBar.addAction(self.calc)
        toolBar.addSeparator()
        self.layout().addWidget(toolBar)



        self.scroll = QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.Systems, self.SystemList = QWidget(), []
        self.Systems.setLayout(QHBoxLayout())
        self.scroll.setWidget(self.Systems)
        self.layout().addWidget(self.scroll)
        self.error = QtWidgets.QLabel("Մուտքագրել համապատասխան տվյալները", objectName='error')
        self.layout().addWidget(self.error)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        tBox = QGroupBox()
        vbox = QHBoxLayout()
        vbox.addWidget(QLabel("t: "))
        self.Systems.t = QLineEdit()
        vbox.addWidget(self.Systems.t)
        vbox.addWidget(QLabel("dt: "))
        self.Systems.dt = QLineEdit()
        vbox.addWidget(self.Systems.dt)
        tBox.setLayout(vbox)
        toolBar.addWidget(tBox)

    @pyqtSlot()
    def CreateCtrl(self):
        dlg = AddSystem(self)
        dlg.exec_()

    @pyqtSlot()
    def RemoveCtrl(self):
        print(self.Systems.layout().count())
        elem = self.sender().parent()
        self.SystemList.remove(elem)
        elem.deleteLater()
        # self.Systems.layout().removeWidget(elem)
        # deleteItemsOfLayout(elem.layout())
        print(self.SystemList)
        if len(self.SystemList) == 0:
            self.calc.setEnabled(False)

    @pyqtSlot()
    def EqualCtrl(self):
        try:
            valueList = []
            for system in self.SystemList:
                tmp = system.SysConfig
                tmp['values'] = [[float(row.text()) for row in col] for col in system.lmds]
                tmp['time'] = [int(self.Systems.t.text()), int(self.Systems.dt.text())]
                valueList.append(tmp)
        except:
            self.error.setText("Մուտքային տվյալները սխալ են")
            self.error.show()
            return


        self.error.hide()
        print(valueList)

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
        self.FormLayout = QFormLayout()
        self.Content.setLayout(self.FormLayout)

        self.error = QtWidgets.QLabel("Մուտքագրել համապատասխան տվյալները", objectName='error')
        self.FormLayout.addWidget(self.error)

        self.sys = QComboBox()
        self.sys.addItem("Ցուցչային")
        # self.sys.addItem("Վեյբուլ")
        # self.system.currentIndexChanged.connect(self.systemChanged)

        self.sysType = [
            (QRadioButton('Չպահուստավորված', objectName='0'), QRadioButton('Պահուստավորված', objectName='1')),
        ]
        self.btnGroupOne = QButtonGroup(self)
        self.btnGroupOne.addButton(self.sysType[0][0])
        self.btnGroupOne.addButton(self.sysType[0][1])
        self.sysType[0][0].setChecked(True)
        self.groupOne = True
        self.btnGroupOne.buttonClicked.connect(self.onClickedTypeOne)

        self.FormLayout.addRow(QLabel("Համակարգի տեսակը"), self.sys)
        self.FormLayout.addRow(self.sysType[0][0], self.sysType[0][1])

    def onClickedTypeOne(self, btn):
        if btn.objectName() == '1' and self.groupOne:
            self.groupOne = False
            self.sysType.append((QRadioButton('Փոխարինումով', objectName='0'), QRadioButton('Մշտական', objectName='1')))
            self.btnGroupTwo = QButtonGroup(self)
            self.btnGroupTwo.addButton(self.sysType[1][0])
            self.btnGroupTwo.addButton(self.sysType[1][1])
            self.sysType[1][1].setChecked(True)
            self.FormLayout.addRow(self.sysType[1][0], self.sysType[1][1])
            
            self.sysType.append((QRadioButton('Ըստ տարրերի', objectName='0'), QRadioButton('Ընդհանուր', objectName='1')))
            self.btnGroupThree = QButtonGroup(self)
            self.btnGroupThree.addButton(self.sysType[2][0])
            self.btnGroupThree.addButton(self.sysType[2][1])
            self.sysType[2][0].setChecked(True)
            self.groupThree = True
            self.btnGroupThree.buttonClicked.connect(self.onClickedTypeThree)
            self.FormLayout.addRow(self.sysType[2][0], self.sysType[2][1])
            self.isSame = QCheckBox('Արժեքները նույնն են')
            self.FormLayout.addWidget(self.isSame)

            self.row = QLineEdit()
            self.row.setPlaceholderText('1 կամ ավելի')
            regexp = QtCore.QRegExp('^([1-9]\\d{0,1})$')
            validator = QRegExpValidator(regexp) # QIntValidator(1, 15)
            self.row.setValidator(validator)
            self.row.textChanged.connect(self.check_state)
            self.row.textChanged.emit(self.row.text())

            self.FormLayout.addRow(QLabel("Պահուստավորված տարերի քանակ (m)"), self.row)
        elif btn.objectName() == '0' and not self.groupOne:
            self.groupOne = True
            self.sysType = self.sysType[:1]
            for i in range(5, self.FormLayout.count(), 2):
                self.FormLayout.removeRow(3)

    def onClickedTypeThree(self, btn):
        if btn.objectName() == '1' and self.groupThree:
            self.groupThree = False
            self.col = QLineEdit()
            self.col.setPlaceholderText('2 կամ ավելի')
            regexp = QtCore.QRegExp('^([2-9]\\d{0,1})$')
            validator = QRegExpValidator(regexp)  # QIntValidator(1, 15)
            self.col.setValidator(validator)
            self.col.textChanged.connect(self.check_state)
            self.col.textChanged.emit(self.row.text())

            self.FormLayout.addRow(QLabel("Համակարգի տարերի քանակ (n)"), self.col)
        elif btn.objectName() == '0' and not self.groupThree:
            self.groupThree = True
            self.FormLayout.removeRow(7)

    def CreateSystem(self):
        switch = {
            0: self.exponential,
            1: self.weibull
        }
        return switch.get(self.System.SysConfig['system'][0])()

    def exponential(self):
        grid = QHBoxLayout()
        wdg = QWidget()
        wdg.setLayout(grid)

        if self.System.SysConfig['isSame'][0]:
            rows = 0
        else:
            rows = self.System.SysConfig["row"]

        self.System.lmds = []
        for col in range(self.System.SysConfig["col"]):
            f, w = QFormLayout(), QWidget()
            w.setLayout(f)
            grid.addWidget(w)
            self.System.lmds.append([])
            for row in range(rows+1):
                self.System.lmds[col].append(QLineEdit())
                f.addRow(QLabel(f"λ[{row}][{col}]:"), self.System.lmds[col][row])

        self.System.layout().addWidget(wdg)



    def weibull(self):
        pass

    @pyqtSlot()
    def accept(self) -> None:
        try:
            isOne = int(self.btnGroupOne.checkedButton().objectName())
            if isOne:
                isTwo = int(self.btnGroupTwo.checkedButton().objectName())
                isThree = int(self.btnGroupThree.checkedButton().objectName())
                row = int(self.row.text())
                if isThree:
                    col = int(self.col.text())
        except:
            self.error.setText("Մուտքային տվյալները սխալ են")
            self.error.show()
            return

        self.error.hide()

        self.System = QWidget()
        self.parent().Systems.layout().addWidget(self.System)
        self.parent().SystemList.append(self.System)

        form = QtWidgets.QFormLayout()
        self.System.setLayout(form)

        toolBar = QToolBar(self.System)
        remove = QAction('Ջնջել', self.System)
        remove.triggered.connect(self.parent().RemoveCtrl)
        toolBar.addAction(remove)
        # edit = QAction('Խմբագրել', self.System)
        # toolBar.addAction(edit)
        form.addWidget(toolBar)

        self.System.SysConfig = {
            'system': [self.sys.currentIndex(), self.sys.currentText()],
            'row': row if isOne else 0,
            'col': col if isOne and isThree else 1,
            'typeOne': [isOne, self.btnGroupOne.checkedButton().text()],
            'typeTwo': [isTwo, self.btnGroupTwo.checkedButton().text()] if isOne else None,
            'typeThree': [isThree, self.btnGroupThree.checkedButton().text()] if isOne else None,
            'isSame': [self.isSame.isChecked(), self.isSame.text()] if isOne else [None],
        }

        print(self.System.SysConfig)

        form.addWidget(QLabel(f'{self.System.SysConfig["system"][1]} համակարգ'))
        typeText = f'{self.System.SysConfig["typeOne"][1]}/{self.System.SysConfig["row"]}'
        if self.System.SysConfig["typeOne"][0]:
            typeText += f'\n{self.System.SysConfig["typeThree"][1]}/{self.System.SysConfig["col"]}' \
                        f'\n{self.System.SysConfig["typeTwo"][1]}'
            if self.System.SysConfig["isSame"][0]:
                typeText += f'\n{self.System.SysConfig["isSame"][1]}'
        form.addWidget(QLabel(typeText))

        self.CreateSystem()

        # print(self.parent().SystemList)

        self.parent().calc.setEnabled(True)
        self.close()

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())