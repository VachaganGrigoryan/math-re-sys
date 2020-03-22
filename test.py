import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(CustomLineEdit, self).__init__(*args, **kwargs)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.__contextMenu)

    def __contextMenu(self):
        self._normalMenu = self.createStandardContextMenu()
        self._addCustomMenuItems(self._normalMenu)
        self._normalMenu.exec_(QCursor.pos())

    def _addCustomMenuItems(self, menu):
        menu.addSeparator()
        menu.addAction(u'Test', self.testFunc)

    def testFunc(self):
        print ("Call")


class CustomDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = CustomLineEdit(parent)
        return editor


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create Widgets
    window = QMainWindow()
    widget = QWidget()
    layout = QVBoxLayout(widget)
    treeview = QTreeView()
    layout.addWidget(treeview)
    window.setCentralWidget(widget)
    window.show()

    # Create Model
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['Header 1','Header 2'])
    treeview.setModel(model)

    # Create custom Delegate which instantiates our custom editor
    delegate = CustomDelegate()
    # Set this delegate for the first column only
    treeview.setItemDelegateForColumn(0, delegate)

    # Populate the model with some test data
    row1 = []
    row1.append(QStandardItem("asd"))
    row1.append(QStandardItem("fgh"))
    model.appendRow(row1)
    row2 = []
    row2.append(QStandardItem("qwe"))
    row2.append(QStandardItem("rty"))
    model.appendRow(row2)

    app.exec_()