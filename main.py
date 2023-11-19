import sys
from random import randint

from PyQt5 import uic, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.is_draw_circle = False

        uic.loadUi("UI.ui", self)
        self.setStyleSheet("""background: transparent;""")
        self.draw_circle_button.clicked.connect(self.draw_circle)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.is_draw_circle:
            draw = QPainter(self)
            draw.begin(self)
            draw.setPen(QColor(255, 255, 0))

            w, h = self.width(), self.height()
            r = randint(1, 100)
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
