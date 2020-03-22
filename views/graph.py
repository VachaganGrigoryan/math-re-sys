from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

import random


class PlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=3, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvasQTAgg.__init__(self, self.figure)
        self.setParent(parent)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Fixed, QSizePolicy.Fixed)
        FigureCanvasQTAgg.updateGeometry(self)
        # self.toolbar = NavigationToolbar2QT(canvas=self, parent=self)

    def plot(self, X, Y, name='', x_name='', y_name=''):
        self.figure.clear()
        self.figure.subplots_adjust(bottom=0.15, left=0.17)
        self.axes = self.figure.add_subplot(111)
        self.axes.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
        self.axes.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        self.axes.set_xlabel(x_name)
        self.axes.set_ylabel(y_name)
        self.axes.set_title(name)
        self.axes.plot(X, Y)
        self.axes.format_coord = lambda x, y: ''  # f'{"%.2f"%x}\n{"%.4f"%y}'
        self.figure.tight_layout()
        self.draw()


class Graph(QWidget):  # QDialog
    """Simple canvas with a sine plot."""

    def __init__(self, parent=None, *args, **kwargs):  # x, y, name='',
        super(Graph, self).__init__(parent=parent, *args, **kwargs)
        self.canvas = PlotCanvas(parent)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)

    def plot(self, *args):
        self.canvas.plot(*args)
