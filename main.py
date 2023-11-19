import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.is_draw_circle = False
        self.setStyleSheet("""background: transparent;""")
        self.draw_circle_button.clicked.connect(self.draw_circle)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.is_draw_circle:
            draw = QPainter(self)
            draw.begin(self)
            w, h = self.width(), self.height()
            r = randint(1, 100)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            draw.setPen(color)
            draw.drawEllipse(QPoint(w // 2, h // 2), r, r)
            draw.end()
            self.is_draw_circle = False

    def draw_circle(self):
        self.is_draw_circle = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
