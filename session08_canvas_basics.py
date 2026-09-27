"""Session 8: Custom Widgets and Painting (slides_pyside_custom_widgets).

The paint gallery: one Canvas widget whose paintEvent fills the background
and demonstrates the basic QPainter draw calls — rect, ellipse, line, text.
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPaintEvent, QPen
from PySide6.QtWidgets import QApplication, QWidget


class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 200)

    def paintEvent(self, event: QPaintEvent):
        # TODO: create QPainter(self), setRenderHint(QPainter.Antialiasing),
        #       and fillRect(self.rect(), QColor("white"))
        # TODO: navy 2px pen (QPen(QColor("navy"), 2)) + lightblue brush,
        #       then drawRect(20, 20, 100, 60), drawEllipse(150, 20, 60, 60),
        #       drawLine(20, 120, 250, 120), drawText(20, 150,
        #       "Hello, canvas"); finish with setBrush(Qt.NoBrush) and
        #       painter.end()
        #       (see deck: Custom Widgets and Painting — the paint gallery)
        pass


def main():
    app = QApplication(sys.argv)
    canvas = Canvas()
    canvas.setWindowTitle("Paint Gallery")
    canvas.show()
    app.exec()


if __name__ == "__main__":
    main()
