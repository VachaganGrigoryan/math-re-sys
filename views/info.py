import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtSvg import QSvgWidget

from io import BytesIO
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# $ % & ~ _ ^ \ { } \( \) \[ \]

class MathFormulaSVG(QSvgWidget):

    def __init__(self, formula, size=3, dpi=300, parent=None, **kwargs):
        super(MathFormulaSVG, self).__init__(parent, **kwargs)

        fig = plt.figure(figsize=(0.01, 0.01))
        fig_text = fig.text(0, 0, f'${formula}$', size=QtGui.QFont().pointSize() * size)

        output = BytesIO()
        fig.savefig(output, dpi=dpi, transparent=False, format='svg',
                    bbox_inches='tight', pad_inches=0.1)

        (x0, y0), (x1, y1) = fig_text.get_window_extent().get_points()
        width, height = x1 - x0, y1 - y0

        fig.set_size_inches(width, height)
        self.setFixedSize(width, height)
        plt.close(fig)

        output.seek(0)
        self.load(output.read())


class MathFormulaLabel(QtWidgets.QWidget):

    def __init__(self, formula, size=2, parent=None, **kwargs):
        super(MathFormulaLabel, self).__init__(parent, **kwargs)

        r, g, b, a = self.palette().base().color().getRgbF()
        self._figure = Figure(edgecolor=(r, g, b), facecolor=(r, g, b))
        self._canvas = FigureCanvas(self._figure)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(self._canvas)

        self._figure.clear()
        figure_text = self._figure.suptitle(
            f'${formula}$',
            x=0,
            y=1,
            horizontalalignment='left',
            verticalalignment='top',
            size=QtGui.QFont().pointSize() * size
        )
        self._canvas.draw()

        (x0, y0), (x1, y1) = figure_text.get_window_extent().get_points()
        width, height = x1 - x0, y1 - y0

        self._figure.set_size_inches(width, height)
        self.setFixedSize(width + 15, height + 15)


class Info(QtWidgets.QWidget):

    def __init__(self, parent=None, **kwargs):
        super(Info, self).__init__(parent, **kwargs)



if __name__ == '__main__':
    FORMULA = r'\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi} C_{soil}=(1 - n) C_m + \theta_w C_w \lim_{x \to a} \frac{f(x) - f(a)}{x-a}'
    app = QtWidgets.QApplication(sys.argv)

    text = MathFormulaLabel(FORMULA)
    text.show()
    # text = MathFormulaLabel(FORMULA)
    # text.show()

    sys.exit(app.exec_())
