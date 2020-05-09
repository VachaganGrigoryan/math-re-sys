from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QRegExpValidator, QValidator, QIntValidator
from PyQt5.QtWidgets import QDialogButtonBox, QVBoxLayout, QToolBar, QAction, QRadioButton, QButtonGroup, QLabel, \
    QLineEdit, QPushButton, QWidget, QScrollArea, QHBoxLayout, QDialog, QComboBox, QCheckBox, QFormLayout, QGroupBox, \
    QTextEdit, QGridLayout

from const.constants import TEXT
from models import BNR_mixed
from views.tools import Info


class BNRMixed(QWidget):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(BNRMixed, self).__init__(parent=parent, flags=flags)
        self.setLayout(QGridLayout())
        # self.addSystem = QPushButton('Ավելացնել')
        # self.addSystem.clicked.connect(self.CreateCtrl)
        # self.layout().addWidget(self.addSystem)
        toolBar = QToolBar(self)
        add = QAction(TEXT.BTN_ADD, self)
        add.triggered.connect(self.CreateCtrl)
        toolBar.addAction(add)
        toolBar.addSeparator()

        tBox = QGroupBox()
        vbox = QHBoxLayout()
        vbox.addWidget(QLabel(TEXT.LB_t))
        self.t = QLineEdit()
        vbox.addWidget(self.t)
        vbox.addWidget(QLabel(TEXT.LB_dt))
        self.dt = QLineEdit()
        vbox.addWidget(self.dt)
        tBox.setLayout(vbox)
        toolBar.addWidget(tBox)
        toolBar.addSeparator()

        self.calc = QAction(TEXT.BTN_CALCULATE, self)
        self.calc.triggered.connect(self.EqualCtrl)
        self.calc.setEnabled(False)
        toolBar.addAction(self.calc)
        self.layout().addWidget(toolBar, 0, 0)


        self.scroll = QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.Systems, self.SystemList = QWidget(), []
        self.Systems.setLayout(QHBoxLayout())
        self.Systems.setMinimumHeight(800)
        self.scroll.setWidget(self.Systems)
        self.layout().addWidget(self.scroll, 1, 0, 1, 2)
        self.error = QtWidgets.QLabel(TEXT.LB_ERR_CORRECT_DATA, objectName='error')
        self.layout().addWidget(self.error, 2, 0)
        self.layout().setAlignment(QtCore.Qt.AlignTop)



        self.layout().addWidget(Info("non_recoverable_backup.html"), 3, 1)


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
                valueList.append(tmp)
            time = [int(self.t.text()), int(self.dt.text())]
        except:
            self.error.setText(TEXT.LB_ERR_WRONG_DATA)
            self.error.show()
            return

        print(valueList, time)
        calc = BNR_mixed(valueList, time)
        print(calc.get_Pc)

        answers = QTextEdit()
        answers.setLayout(QHBoxLayout())
        self.layout().addWidget(answers, 3, 0)

        answers.setReadOnly(True)

        answers.insertPlainText(f'P = {"%.6G" % calc.get_Pc}')


        self.error.hide()

class AddSystem(QDialog):

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super(AddSystem, self).__init__(parent=parent, flags=flags)
        self.setWindowTitle(TEXT.DIALOG_TITLE)
        self.setLayout(QVBoxLayout())

        self.setupContent()

        btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btnBox.accepted.connect(self.accept)
        btnBox.rejected.connect(self.reject)
        btnBox.button(QDialogButtonBox.Ok).setText(TEXT.BTN_CREATE)
        btnBox.button(QDialogButtonBox.Cancel).setText(TEXT.BTN_CANCEL)
        self.layout().addWidget(btnBox)

    def setupContent(self):
        self.Content = QWidget(self)
        self.layout().addWidget(self.Content)
        self.FormLayout = QFormLayout()
        self.Content.setLayout(self.FormLayout)

        self.error = QtWidgets.QLabel(TEXT.LB_ERR_CORRECT_DATA, objectName='error')
        self.FormLayout.addWidget(self.error)

        self.sys = QComboBox()
        self.sys.addItem(TEXT.EXP)
        # self.sys.addItem("Վեյբուլ")
        # self.system.currentIndexChanged.connect(self.systemChanged)

        self.sysType = [
            (QRadioButton(TEXT.NOT_BACKUP, objectName='0'), QRadioButton(TEXT.BACKUP, objectName='1')),
        ]
        self.btnGroupOne = QButtonGroup(self)
        self.btnGroupOne.addButton(self.sysType[0][0])
        self.btnGroupOne.addButton(self.sysType[0][1])
        self.sysType[0][0].setChecked(True)
        self.groupOne = True
        self.btnGroupOne.buttonClicked.connect(self.onClickedTypeOne)

        self.FormLayout.addRow(QLabel(TEXT.LB_SYSTEM_TYPE), self.sys)
        self.FormLayout.addRow(self.sysType[0][0], self.sysType[0][1])

    def onClickedTypeOne(self, btn):
        if btn.objectName() == '1' and self.groupOne:
            self.groupOne = False
            self.sysType.append((QRadioButton(TEXT.REPLACEMENT, objectName='0'), QRadioButton(TEXT.PERMANENT, objectName='1')))
            self.btnGroupTwo = QButtonGroup(self)
            self.btnGroupTwo.addButton(self.sysType[1][0])
            self.btnGroupTwo.addButton(self.sysType[1][1])
            self.sysType[1][1].setChecked(True)
            self.FormLayout.addRow(self.sysType[1][0], self.sysType[1][1])
            
            self.sysType.append((QRadioButton(TEXT.BY_ELEMENTS, objectName='0'), QRadioButton(TEXT.WHOLE, objectName='1')))
            self.btnGroupThree = QButtonGroup(self)
            self.btnGroupThree.addButton(self.sysType[2][0])
            self.btnGroupThree.addButton(self.sysType[2][1])
            self.sysType[2][0].setChecked(True)
            self.groupThree = True
            self.btnGroupThree.buttonClicked.connect(self.onClickedTypeThree)
            self.FormLayout.addRow(self.sysType[2][0], self.sysType[2][1])
            self.isSame = QCheckBox(TEXT.LB_THE_SAME_VALUE)
            self.FormLayout.addWidget(self.isSame)

            self.row = QLineEdit()
            self.row.setPlaceholderText(TEXT.LEP_1_OR_MORE)
            regexp = QtCore.QRegExp('^([1-9]\\d{0,1})$')
            validator = QRegExpValidator(regexp) # QIntValidator(1, 15)
            self.row.setValidator(validator)
            self.row.textChanged.connect(self.check_state)
            self.row.textChanged.emit(self.row.text())

            self.FormLayout.addRow(QLabel(TEXT.LB_THE_BACKUP_ELM_COUNT), self.row)
        elif btn.objectName() == '0' and not self.groupOne:
            self.groupOne = True
            self.sysType = self.sysType[:1]
            for i in range(5, self.FormLayout.count(), 2):
                self.FormLayout.removeRow(3)

    def onClickedTypeThree(self, btn):
        if btn.objectName() == '1' and self.groupThree:
            self.groupThree = False
            self.col = QLineEdit()
            self.col.setPlaceholderText(TEXT.LEP_2_OR_MORE)
            regexp = QtCore.QRegExp('^([2-9]\\d{0,1})$')
            validator = QRegExpValidator(regexp)  # QIntValidator(1, 15)
            self.col.setValidator(validator)
            self.col.textChanged.connect(self.check_state)
            self.col.textChanged.emit(self.row.text())

            self.FormLayout.addRow(QLabel(TEXT.LB_THE_SYSTEM_ELM_COUNT), self.col)
        elif btn.objectName() == '0' and not self.groupThree:
            self.groupThree = True
            self.FormLayout.removeRow(7)

    def CreateSystem(self):
        switch = {
            0: self.exponential,
            1: self.weibull
        }
        return switch.get(self.System.SysConfig['system'])()

    def exponential(self):
        grid = QHBoxLayout()
        wdg = QWidget()
        wdg.setLayout(grid)

        if self.System.SysConfig['isSame']:
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
            typeText = f'{self.sys.currentText()} համակարգ'
            typeText += f'\n{self.btnGroupOne.checkedButton().text()}'
            if isOne == 1:
                row = int(self.row.text())
                isTwo = self.btnGroupTwo.checkedButton().objectName()
                isThree = self.btnGroupThree.checkedButton().objectName()
                typeText += f'/{row}' \
                            f'\n{self.btnGroupThree.checkedButton().text()}'
                print(row, isThree, isTwo)
                if isThree == '1':
                    col = int(self.col.text())
                    typeText += f'/{col}'

                typeText += f'\n{self.btnGroupTwo.checkedButton().text()}'
                if self.isSame.isChecked():
                    typeText += f'\n{self.isSame.text()}'
        except:
            self.error.setText(TEXT.LB_ERR_WRONG_DATA)
            self.error.show()
            return

        self.error.hide()

        self.System = QWidget()
        self.parent().Systems.layout().addWidget(self.System)
        self.parent().SystemList.append(self.System)

        form = QtWidgets.QFormLayout()
        self.System.setLayout(form)

        toolBar = QToolBar(self.System)
        remove = QAction(TEXT.BTN_DELETE, self.System)
        remove.triggered.connect(self.parent().RemoveCtrl)
        toolBar.addAction(remove)
        # edit = QAction('Խմբագրել', self.System)
        # toolBar.addAction(edit)
        form.addWidget(toolBar)

        self.System.SysConfig = {
            'system': self.sys.currentIndex(),
            'row': row if isOne == 1 else 0,
            'col': col if isOne == 1 and isThree == "1" else 1,
            'typeOne': isOne,
            'typeTwoAndThree': isTwo + isThree if isOne == 1 else None,
            # 'typeThree': isThree if isOne else None,
            'isSame': self.isSame.isChecked() if isOne == 1 else None,
        }

        print(self.System.SysConfig)

        # form.addWidget(QLabel(f'{self.System.SysConfig["system"][1]} համակարգ'))
        # typeText = f'{self.System.SysConfig["typeOne"][1]}/{self.System.SysConfig["row"]}'
        # if self.System.SysConfig["typeOne"][0]:
        #     typeText += f'\n{self.System.SysConfig["typeThree"][1]}/{self.System.SysConfig["col"]}' \
        #                 f'\n{self.System.SysConfig["typeTwo"][1]}'
        #     if self.System.SysConfig["isSame"][0]:
        #         typeText += f'\n{self.System.SysConfig["isSame"][1]}'
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