"""Session 2: Two-way synchronization.

A QSlider and a QSpinBox that keep each other in sync by connecting
each one's valueChanged signal to the other one's setValue slot.
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QSlider, QSpinBox,
)


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Two-way sync")
    window.resize(300, 110)

    # TODO: create a horizontal QSlider (range 0-100, initial value 50)
    slider = QSlider(Qt.Horizontal, parent=window)
    slider.setRange(0, 100)
    slider.setValue(50)
    #       at setGeometry(20, 20, 260, 24)
    slider.setGeometry(20, 20, 260, 24)
    # TODO: create a QSpinBox (range 0-100, initial value 50)
    spin = QSpinBox(parent=window)
    spin.setRange(0, 100)
    spin.setValue(50)
    #       at setGeometry(20, 60, 80, 24)
    spin.setGeometry(20, 60, 80, 24)

    # TODO: connect slider.valueChanged to spin.setValue
    slider.valueChanged.connect(spin.setValue)
    # TODO: connect spin.valueChanged to slider.setValue
    spin.valueChanged.connect(slider.setValue)
    #       (see deck: Signals and Slots — two-way synchronization)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
