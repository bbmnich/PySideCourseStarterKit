"""Workshop 1: Build the Greeter Window — profile card form (STARTER).

Deck: "The Event Loop and Your First Window" (topic_400_pyside_event_loop),
Workshop 1. Build your own profile card: a titled window, labels and input
fields for at least three pieces of information, a button at the bottom.
The finished version: workshop01_profile_card.py in PySideCourse.

The button does not need to do anything yet — interactivity arrives in
Session 2.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
)


class ProfileCard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Profile Card")   # TODO: your name here
        self.resize(360, 220)

        # TODO: three (or more) label + QLineEdit pairs — e.g. name,
        #       email, favorite programming language. Position them
        #       manually with setGeometry (layouts arrive in Session 3):
        #       label at the left, field at the right, one row per item.

        # TODO: a QPushButton at the bottom (it does not need to do
        #       anything yet)


def main():
    app = QApplication(sys.argv)
    card = ProfileCard()
    card.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
