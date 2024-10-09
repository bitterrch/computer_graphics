from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSpinBox
from PyQt5.QtCore import QSize, pyqtSlot

from calculate import calculateTouchPoints, calculatePoints
from numpy import sqrt
from canvas import Canvas

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.x0, self.y0, self.x1, self.y1, self.r = None, None, None, None, None

        self.p = []

        self.setWindowTitle("Работа №1")
        self.setFixedSize(QSize(750, 500))

        self.chart = Canvas(self)

        central_widget = QWidget(self)

        self.point_lbl = QLabel(central_widget)
        self.x_point_lbl = QLabel(central_widget)
        self.y_point_lbl = QLabel(central_widget)
        self.circle_lbl = QLabel(central_widget)
        self.x_circle_lbl = QLabel(central_widget)
        self.y_circle_lbl = QLabel(central_widget)
        self.radius_lbl = QLabel(central_widget)

        self.x_point_val = QSpinBox(central_widget)
        self.x_point_val.setMaximum(300)
        self.x_point_val.setMinimum(-300)

        self.y_point_val = QSpinBox(central_widget)
        self.y_point_val.setMaximum(300)
        self.y_point_val.setMinimum(-300)

        self.x_circle_val = QSpinBox(central_widget)
        self.x_circle_val.setMaximum(300)
        self.x_circle_val.setMinimum(-300)

        self.y_circle_val = QSpinBox(central_widget)
        self.y_circle_val.setMaximum(300)
        self.y_circle_val.setMinimum(-300)

        self.radius_val = QSpinBox(central_widget)
        self.radius_val.setMaximum(300)
        self.radius_val.setMinimum(1)

        self.submit_btn = QPushButton(central_widget)

        self.point_lbl.setText("Координаты точки: ")
        self.point_lbl.setGeometry(520, 20, 200, 25)

        self.x_point_lbl.setText("x: ")
        self.x_point_lbl.setGeometry(520, 50, 10, 25)
        self.x_point_val.setGeometry(540, 50, 70, 25)

        self.y_point_lbl.setText("y: ")
        self.y_point_lbl.setGeometry(520, 95, 10, 25)
        self.y_point_val.setGeometry(540, 95, 70, 25)

        self.circle_lbl.setText("Координаты центра окружности: ")
        self.circle_lbl.setGeometry(520, 170, 200, 25)

        self.x_circle_lbl.setText("x: ")
        self.x_circle_lbl.setGeometry(520, 200, 10, 25)
        self.x_circle_val.setGeometry(540, 200, 70, 25)

        self.y_circle_lbl.setText("y: ")
        self.y_circle_lbl.setGeometry(520, 245, 10, 25)
        self.y_circle_val.setGeometry(540, 245, 70, 25)

        self.radius_lbl.setText("радиус: ")
        self.radius_lbl.setGeometry(520, 290, 50, 25)
        self.radius_val.setGeometry(570, 290, 70, 25)

        self.submit_btn.setText("Подтвердить")
        self.submit_btn.setGeometry(520, 340, 100, 30)

        self.submit_btn.clicked.connect(self.on_submit_clicked)
        self.show()

    @pyqtSlot()
    def on_submit_clicked(self):
        self.x0 = self.x_circle_val.value()
        self.y0 = self.y_circle_val.value()
        self.x1 = self.x_point_val.value()
        self.y1 = self.y_point_val.value()
        self.r = self.radius_val.value()

        self.chart.clear()
        self.chart.grid()
        self.chart.drawPoint(self.x0, self.y0)
        self.chart.drawPoint(self.x1, self.y1)
        self.chart.drawCircle(self.x0, self.y0, self.r)

        d = sqrt((self.x0 - self.x1) ** 2 + (self.y0 - self.y1) ** 2)
        
        if d > self.r:
            self.p = calculateTouchPoints(self.x0, self.y0, self.x1, self.y1, self.r, d)
            self.chart.setTitle("Точка лежит вне окружности")
            self.chart.drawLine(self.x1, self.y1, self.p[0], self.p[1])
            self.chart.drawLine(self.x1, self.y1, self.p[2], self.p[3])
        elif d == self.r:
            self.p = calculatePoints(self.x0, self.y0, self.x1, self.y1, self.r)
            self.chart.setTitle("Точка лежит на окружности")
            self.chart.drawLine(self.p[0], self.p[1], self.p[2], self.p[3])
        elif d < self.r:
            self.chart.setTitle("Точка лежит внутри окружности")

    




