import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(5, 5))
        super().__init__(fig)
        self.setParent(parent)

        self.ax.axis("equal")
        self.ax.plot()
        self.ax.grid()

    def drawLine(self, x1, y1, x2, y2):
        x = [x1, x2]
        y = [y1, y2]
        self.ax.plot(x, y, marker ='o')
        self.draw()

    def drawCircle(self, x0, y0, r):
        n = 64
        t = np.linspace(0, 2*np.pi, n+1)
        x = r*np.cos(t) + x0
        y = r*np.sin(t) + y0
        self.ax.plot(x, y)
        self.draw()

    def drawTouchline(self, x0, y0, x1, y1, r):
        A = x1-x0
        B = y1-y0
        C = A*x1 + B*y1
        x_tan = np.linspace(x0 - r - 2, x0 + r + 2, 65)
        y_tan = (C - A * x_tan) / B
        self.ax.plot(x_tan, y_tan)
        self.draw()

    def drawPoint(self, x, y):
        self.ax.plot(x, y, marker='o')
        self.draw()

    def clear(self):
        self.ax.clear()

    def setTitle(self, name):
        self.ax.set(title=name)
        self.draw()

    def grid(self):
        self.ax.grid()