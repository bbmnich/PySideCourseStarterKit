"""Session 2: Organizing a window as a class.

The live greeter reorganized as a GreeterWindow class — widgets become
instance attributes, the slot becomes a method.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel,
)


class GreeterWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_edit = QLineEdit(self)
        self.name_edit.setGeometry(110, 20, 170, 24)

        # TODO: set the window title "Greeter" and resize(300, 150)
def main():
    app = QApplication(sys.argv)
    window = GreeterWindow()
    window.setWindowTitle("Greeter")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec())

        # TODO: create self.name_edit (QLineEdit) at setGeometry(110, 20, 170, 24)
    self.name_edit = QLineEdit(self)
    self.name_edit.setGeometry(110, 20, 170, 24)

        # TODO: create the "Greet me" QPushButton at setGeometry(110, 60, 170, 28)
    button = QPushButton("Greet me", self)
    button.setGeometry(110, 60, 170, 28)

        # TODO: create self.greeting (empty QLabel) at setGeometry(20, 100, 260, 24)
    self.greeting = QLabel("", self)
    self.greeting.setGeometry(20, 100, 260, 24)

        # TODO: connect the button's clicked signal to self.greet
        #       (see deck: Signals and Slots — organizing a window as a class)
    button.clicked.connect(self.greet)

    def greet(self):
        # TODO: set self.greeting's text to f"Hello, {self.name_edit.text()}!"
        self.greeting.setText(f"Hello, {self.name_edit.text()}!")


if __name__ == "__main__":
    main()
