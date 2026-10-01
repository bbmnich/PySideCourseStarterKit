"""Session 2: Custom signals.

A NameEditor widget that emits its own name_submitted signal (carrying
the entered text), embedded in a small demo window that prints what it
receives.
"""
import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
)


class NameEditor(QWidget):

    # TODO: declare name_submitted = Signal(str) as a CLASS attribute
    #       (see deck: Signals and Slots — custom signals)
    name_submitted = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.edit = QLineEdit(self)
        self.edit.setGeometry(10, 10, 180, 24)
        button = QPushButton("Submit", self)
        button.setGeometry(10, 44, 180, 28)
        button.clicked.connect(self._submit)

    def _submit(self):
        # TODO: emit name_submitted with the current text: self.edit.text()
        self.name_submitted.emit(self.edit.text())


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Custom signals")
    window.resize(200, 90)

    editor = NameEditor(window)
    # The guard keeps the starter runnable before name_submitted is declared.
    if hasattr(editor, "name_submitted"):
        editor.name_submitted.connect(lambda name: print("Got:", name))

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
