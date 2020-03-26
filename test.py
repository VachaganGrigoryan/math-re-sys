# import sys
#
# from PyQt5.QtWidgets import QToolBox, QPlainTextEdit, QVBoxLayout, QApplication, QWidget
#
#
# class Window(QWidget):
#     def __init__(self, parent=None):
#         super(Window, self).__init__(parent)
#
#         # tool box
#         tool_box = QToolBox()
#
#         # items
#         tool_box.addItem(QPlainTextEdit('Text 1'),
#                          'Page 1')
#         tool_box.addItem(QPlainTextEdit('Text 2'),
#                          'Page 2')
#
#         # vertical box layout
#         vlayout = QVBoxLayout()
#         vlayout.addWidget(tool_box)
#         self.setLayout(vlayout)
#
#
# application = QApplication(sys.argv)
#
# # window
# window = Window()
# window.setWindowTitle('Tool Box')
# window.resize(280, 300)
# window.show()
#
# sys.exit(application.exec_())

import numpy
numpy.seterr(divide='ignore', invalid='ignore')
print(numpy.divide(1, 0))