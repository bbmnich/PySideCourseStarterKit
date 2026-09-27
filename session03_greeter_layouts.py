"""Session 3: The greeter, rebuilt with layouts.

The same GreeterWindow as session 2, but QVBoxLayout/QHBoxLayout
replace setGeometry — the layout recomputes geometry automatically.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout,
)


class GreeterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Greeter")

        self.name_edit = QLineEdit()
        self.greeting = QLabel("")
        button = QPushButton("Greet me")
        button.clicked.connect(self.greet)

        # TODO: build a QHBoxLayout "row" with QLabel("Your name:") and
        #       self.name_edit
        # TODO: build the main QVBoxLayout(self) — passing the parent to the
        #       constructor is the shorthand — then addLayout(row),
        #       addWidget(button), addWidget(self.greeting)
        #       (see deck: Layouts and a Widget Tour)

    def greet(self):
        self.greeting.setText(f"Hello, {self.name_edit.text()}!")


def main():
    app = QApplication(sys.argv)
    window = GreeterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
