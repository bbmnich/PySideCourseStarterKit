"""Session 1: The event loop and your first window.

The smallest possible PySide program, with a bit of personality:
a window title and an explicit size before entering the event loop.
"""
# TODO: import sys (see deck: The Event Loop and Your First Window)
# TODO: import QApplication and QWidget from PySide6.QtWidgets
import sys
from PySide6.QtWidgets import QApplication, QWidget



def main():
    # TODO: create the QApplication from sys.argv
    app = QApplication(sys.argv)
    # TODO: create a QWidget, set its title to "Session 1 — Hello Qt",
    #       and resize it to 400x300
    window = QWidget()
    window.setWindowTitle("Session 1 — Hello Qt")
    window.resize(400, 300)

    # TODO: show the window
    window.show()

    # TODO: enter the event loop with sys.exit(app.exec())
    sys.exit(app.exec())




if __name__ == "__main__":
    main()
