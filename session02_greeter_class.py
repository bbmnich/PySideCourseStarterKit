"""Session 2: Organizing a window as a class.

The live greeter reorganized as a GreeterWindow class — widgets become
instance attributes, the slot becomes a method.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel,
)


class GreeterWindow(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: set the window title "Greeter" and resize(300, 150)
        # TODO: create self.name_edit (QLineEdit) at setGeometry(110, 20, 170, 24)
        # TODO: create the "Greet me" QPushButton at setGeometry(110, 60, 170, 28)
        # TODO: create self.greeting (empty QLabel) at setGeometry(20, 100, 260, 24)
        # TODO: connect the button's clicked signal to self.greet
        #       (see deck: Signals and Slots — organizing a window as a class)
        pass

    def greet(self):
        # TODO: set self.greeting's text to f"Hello, {self.name_edit.text()}!"
        pass


def main():
    app = QApplication(sys.argv)
    window = GreeterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
