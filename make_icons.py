"""Generate the PNG icons for session10_drawing_app.py.

Run once with the project's PySide6 environment:

    python make_icons.py

Creates icons/app.png and icons/undo.png (32x32) next to this script,
drawn programmatically with QImage + QPainter. Afterwards bundle them
into the Qt resource system:

    pyside6-rcc resources.qrc -o resources_rc.py
"""

import os
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")  # no display needed

from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import QColor, QImage, QPainter, QPen, QPolygon
from PySide6.QtWidgets import QApplication

SIZE = 32
HERE = Path(__file__).parent


def make_canvas():
    image = QImage(SIZE, SIZE, QImage.Format_ARGB32)
    image.fill(Qt.transparent)
    painter = QPainter(image)
    painter.setRenderHint(QPainter.Antialiasing)
    return image, painter


def draw_app_icon(path):
    """A circle on a canvas — the shape the app draws."""
    image, painter = make_canvas()
    painter.setBrush(QColor("white"))
    painter.setPen(QPen(QColor("gray"), 1))
    painter.drawRect(1, 1, SIZE - 3, SIZE - 3)          # the canvas
    painter.setBrush(QColor("crimson"))
    painter.setPen(QPen(QColor("navy"), 2))
    painter.drawEllipse(7, 7, 18, 18)                   # a circle shape
    painter.end()
    image.save(str(path))


def draw_undo_icon(path):
    """A curved back-arrow."""
    image, painter = make_canvas()
    pen = QPen(QColor("navy"), 3)
    pen.setCapStyle(Qt.RoundCap)
    painter.setPen(pen)
    painter.setBrush(Qt.NoBrush)
    painter.drawArc(QRect(8, 8, 20, 20), -30 * 16, 240 * 16)  # the curve
    painter.setBrush(QColor("navy"))
    painter.setPen(Qt.NoPen)
    painter.drawPolygon(QPolygon([QPoint(4, 14), QPoint(13, 9), QPoint(13, 19)]))
    painter.end()
    image.save(str(path))


def main():
    app = QApplication([])  # QPainter on QImage wants a GUI application
    icons_dir = HERE / "icons"
    icons_dir.mkdir(exist_ok=True)
    draw_app_icon(icons_dir / "app.png")
    draw_undo_icon(icons_dir / "undo.png")
    print(f"Wrote {icons_dir / 'app.png'} and {icons_dir / 'undo.png'}")


if __name__ == "__main__":
    main()
