"""Session 2: Bringing the greeter to life.

The static form from session 1, now with a greet slot connected to
the button's clicked signal (still procedural, still setGeometry).
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
)


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Greeter")
    window.resize(300, 150)

    name_edit = QLineEdit(parent=window)
    name_edit.setGeometry(110, 20, 170, 24)

    button = QPushButton("Greet me", parent=window)
    button.setGeometry(110, 60, 170, 28)

    greeting = QLabel("", parent=window)
    greeting.setGeometry(20, 100, 260, 24)

    def greet():
        # TODO: set the greeting label's text to f"Hello, {name_edit.text()}!"
        #       (see deck: Signals and Slots — bringing the greeter to life)
        greeting.setText(f"Hello, {name_edit.text()}!")

    # TODO: connect button.clicked to greet
    button.clicked.connect(greet)
    

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
