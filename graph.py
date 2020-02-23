from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import random

class PlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot()

        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)

        FigureCanvasQTAgg.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)
 

    def plot(self, X, Y, name=''):
        pass


class StaticCanvas(PlotCanvas):
    """Simple canvas with a sine plot."""

    def plot(self, X, Y, name=''):
        self.axes.plot(X, Y)
        self.axes.set_title(name)
        self.draw()


class DynamicCanvas(PlotCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        PlotCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda: self.update_figure([1,2,3,4,5,95], 6))
        timer.start(1000)

    def plot(self, X, Y, name=''):
        self.axes.plot(X, Y, 'r')
        self.axes.set_title(name)

    def update_figure(self, X, n):
        l = [random.randint(0, 100) for i in range(n)]
        self.axes.cla()
        self.axes.plot(X, l, 'r')
        self.draw()