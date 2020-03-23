from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QAction, QSizePolicy


class TableView(QTableWidget):

    def __init__(self, parent=None, row=None, col=None, headers=None, *args, **kwargs):
        super(TableView, self).__init__(parent=parent)
        self.headers = headers
        self.args = args
        self.setRowCount(row)
        self.setColumnCount(col)

        self.setMinimumSize(100*(col+1), 400)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setEditTriggers(self.NoEditTriggers)
        self.doubleClicked.connect(self.onDoubleClick)
        self.addAction(QAction("Պատճենել", self, triggered=self.copyData))


        self.initHeader()
        self.initData()
        # self.horizontalHeader().ResizeMode(QtWidgets.QHeaderView.Interactive)
        # header = self.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)



    def onDoubleClick(self, index):
        print(index.row(), index.column(), index.data())

    def keyPressEvent(self, event):
        super(TableView, self).keyPressEvent(event)

        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.copyData()

    def copyData(self):
        count = len(self.selectedIndexes())
        if count == 0:
            return
        if count == 1:
            QApplication.clipboard().setText(
                self.selectedIndexes()[0].data())
            QMessageBox.information(self, "Հուշում", "Մեկ տվյալ է պատճենվել")
            return
        rows = set()
        cols = set()
        for index in self.selectedIndexes():
            rows.add(index.row())
            cols.add(index.column())

        print(rows, cols)
        if len(rows) == 1:
            QApplication.clipboard().setText("\t".join(
                [index.data() for index in self.selectedIndexes()]))
            QMessageBox.information(self, "Հուշում", "Պատճենահանվել է տվյալների մեկ շարքը")
            return
        if len(cols) == 1:
            QApplication.clipboard().setText("\r\n".join(
                [index.data() for index in self.selectedIndexes()]))
            QMessageBox.information(self, "Հուշում", "Պատճենահանված տվյալների մեկ սյունակ")
            return
        mirow, marow = min(rows), max(rows)
        micol, macol = min(cols), max(cols)
        print(mirow, marow, micol, macol)
        arrays = [
            [
                "" for _ in range(macol - micol + 1)
            ] for _ in range(marow - mirow + 1)
        ]
        print(arrays)

        for index in self.selectedIndexes():
            arrays[index.row() - mirow][index.column() - micol] = index.data()
        print(arrays)
        data = '\r\n'.join('\t'.join(row) for row in arrays)
        # for row in arrays:
        #     data += "\t".join(row) + "\r\n"
        print(data)
        QApplication.clipboard().setText(data)
        QMessageBox.information(self, "Հուշում", "Պատճենվել է")

    def initHeader(self):
        header = self.horizontalHeader()
        for i in range(self.columnCount()):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(self.headers[i]))
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def initData(self):
        for item in zip(range(self.rowCount()), *self.args):
            for i in range(self.columnCount()):
                self.setItem(item[0], i, QTableWidgetItem('%G' % item[i + 1]))

