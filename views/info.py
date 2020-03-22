import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile, QTextStream, QMimeData, QByteArray, QBuffer, QIODevice, Qt
from PyQt5.QtGui import QImage, QTextDocument, QPainter, QFont, QTextCursor, QPixmap, QCursor
from PyQt5.QtSvg import QSvgWidget

from io import BytesIO, StringIO
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QLabel, QSizePolicy, QPlainTextEdit, QAction, QMenu, \
    QApplication

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# $ % & ~ _ ^ \ { } \( \) \[ \]


class MathFormulaSVG(QSvgWidget):

    def __init__(self, formula, size=15, dpi=300, parent=None, **kwargs):
        super(MathFormulaSVG, self).__init__(parent, **kwargs)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        plt.rc('mathtext', fontset='cm')
        fig = plt.figure(figsize=(0.05, 0.05), dpi=dpi)
        figure_text = fig.text(0, 0, f'${formula}$', fontsize=size) #size=QFont().pointSize() * size)
        output = BytesIO()
        fig.savefig(output, dpi=dpi, transparent=True, format='svg', bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)

        output.seek(0)
        text = output.read()
        self.load(text)

        (x0, y0), (x1, y1) = figure_text.get_window_extent().get_points()
        width, height = x1 - x0, y1 - y0

        self.image = QImage(width, height, QImage.Format_ARGB32)
        self.render(QPainter(self.image))

    def savePNG(self, pngFilepath):
        self.image.save(pngFilepath)


# class MathFormulaLabel(QWidget):
#
#     def __init__(self, formula, size=2, parent=None, **kwargs):
#         super(MathFormulaLabel, self).__init__(parent, **kwargs)
#
#         r, g, b, a = self.palette().base().color().getRgbF()
#         self._figure = Figure(edgecolor=(r, g, b), facecolor=(r, g, b))
#         self.canvas = FigureCanvas(self._figure)
#
#         layout = QVBoxLayout(self)
#         layout.setContentsMargins(5, 5, 5, 5)
#         layout.addWidget(self.canvas)
#
#         self._figure.clear()
#         figure_text = self._figure.suptitle(
#             f'${formula}$',
#             x=0,
#             y=1,
#             horizontalalignment='left',
#             verticalalignment='top',
#             size=QFont().pointSize() * size
#         )
#         self.canvas.draw()
#
#         (x0, y0), (x1, y1) = figure_text.get_window_extent().get_points()
#         width, height = x1 - x0, y1 - y0
#
#         self._figure.set_size_inches(width, height)
#         self.setFixedSize(width + 15, height + 15)


class TextView(QTextEdit):

    def __init__(self, parent=None):
        super(TextView, self).__init__(parent)
        # self.resize(600, 400)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._buffer = StringIO()
        self.setReadOnly(True)

        # Setup the QTextEdit editor configuration
        self.setAutoFormatting(QTextEdit.AutoAll)
        # Initialize default font size.
        font = QFont('Times', 12)
        self.setFont(font)
        # We need to repeat the size to init the current format.
        self.setFontPointSize(12)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.context_menu)

    def keyPressEvent(self, event):
        super(TextView, self).keyPressEvent(event)
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            self.copyData()

    def context_menu(self):
        contextMenu = QMenu(self)
        select = QAction("Նշել", self, triggered=self.selectAll)
        copy = QAction("Պատճենել", self, triggered=self.copy)

        contextMenu.addAction(select)
        contextMenu.addSeparator()
        contextMenu.addAction(copy)
        contextMenu.exec_(QCursor.pos())

    def write(self, text):
        self.moveCursor(QTextCursor.End)
        # self.insertPlainText(text)
        self.insertHtml(text)
        self._buffer.write(text)
        # self.moveNewLine()
        self.moveCursor(QTextCursor.Start)

    def insert(self, image):
        self.moveCursor(QTextCursor.End)
        cursor = self.textCursor()
        cursor.insertImage(image)
        self.setTextCursor(cursor)
        # self.moveNewLine()
        self.moveCursor(QTextCursor.Start)

    def copyData(self):
        print("Copy")
        QApplication.clipboard().setImage()

    def __getattr__(self, attr):
        return getattr(self._buffer, attr)

    def moveNewLine(self):
        fragment = QtGui.QTextDocumentFragment.fromHtml("<br>")
        self.textCursor().insertFragment(fragment)
        self.moveCursor(QTextCursor.Start)

class Info(QtWidgets.QWidget):

    def __init__(self, name='test.html', path='./documents', parent=None, **kwargs):
        super(Info, self).__init__(parent, **kwargs)
        self.resize(500, 500)
        self.setLayout(QtWidgets.QHBoxLayout(self))
        self.infoView = TextView()
        self.layout().addWidget(self.infoView)

        file = QFile(f'{path}/{name}')
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        content = stream.readAll()
        file.close()


        self.renderFormula(content)

    def renderFormula(self, content):
        def _render(text):
            start = text.find('{%')
            if start != -1:
                self.infoView.write(text[:start])
                end = text.find('%}')
                print(text[:start], text[start+2:end])
                size, formula = text[start+2:end].split(':;')
                formula = MathFormulaSVG(formula=formula, size=size)
                self.infoView.insert(formula.image)
                _render(text[end+2:])
            else:
                self.infoView.write(text)
        _render(content)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    widgets = Info('weibull.html')
    widgets.show()

    sys.exit(app.exec_())
