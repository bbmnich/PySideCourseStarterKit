"""Workshop 2: Temperature converter (STARTER).

Deck: "Signals and Slots" (topic_410_pyside_signals_slots), Workshop 2.
Build a ConverterWindow(QWidget): a QSlider and a QSpinBox in two-way
sync (Celsius, −50…+150), a QLabel with the Fahrenheit equivalent updated
live (F = C × 9/5 + 32), water remarks above 100 / below 0, and a Reset
button (stretch goal).
The finished version: workshop02_temperature.py in PySideCourse.

Layouts have not been taught yet — position the widgets with
setGeometry, like in Session 1, or look ahead if you like.
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSlider, QSpinBox,
)


class ConverterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Converter")
        self.resize(320, 160)

        # TODO: a QSlider (Qt.Horizontal) and a QSpinBox, both with
        #       range -50..150 and value 20. Keep them in two-way sync:
        #       slider.valueChanged -> spinner.setValue and
        #       spinner.valueChanged -> slider.setValue. (setValue with
        #       an unchanged value emits nothing — that terminates the loop.)

        # TODO: a QLabel for the result, connected to a slot that reads
        #       the Celsius value and shows "C °C = F °F", plus
        #       " — water boils!" above 100 / " — water freezes!" below 0.

        # TODO (stretch): a "Reset" QPushButton whose slot is ONE line.


def main():
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
