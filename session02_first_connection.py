"""Session 2: Your first connection.

A button whose clicked signal is connected to a function —
the handler runs every time the button is clicked.
"""
import sys
from PySide6.QtWidgets import QApplication, QPushButton


# TODO: define a function on_click() that prints "Clicked!"
#       (see deck: Signals and Slots — your first connection)


def main():
    app = QApplication(sys.argv)

    button = QPushButton("Click me")
    # TODO: connect the button's clicked signal to your on_click function
    button.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
