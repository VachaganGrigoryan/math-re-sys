from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class CreateTable(QTableWidget):

    def __init__(self, parent=None, row=None, col=None, HHeaders=None, *args, **kwargs):
        super(CreateTable, self).__init__(parent=parent)
        self.setRowCount(row)
        self.setColumnCount(col)

        for i in range(col):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(HHeaders[i]))

        for item in zip(range(row), *args):
            for i in range(col):
                self.setItem(item[0], i, QTableWidgetItem('%G' % item[i+1]))
