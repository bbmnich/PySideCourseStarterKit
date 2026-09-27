"""Workshop 5: Address list (STARTER).

Deck: "Model/View Programming I" (topic_440_pyside_model_view), Workshop 5.
Build AddressWindow(QMainWindow): a QListView + QStringListModel with
three starter entries and Add…/Edit…/Remove buttons.
The finished version: workshop05_address.py in PySideCourse.

If your Workshop 3 settings window works, you can also continue in your
own file — this starter is the same starting point for everyone.
"""
import sys
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QInputDialog, QMainWindow, QPushButton,
    QListView, QVBoxLayout, QWidget,
)


class AddressWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Address Book")

        # The model owns the data — everything mutates THROUGH it.
        self.model = QStringListModel(["Ada Lovelace", "Grace Hopper",
                                       "Alan Turing"])

        central = QWidget()
        layout = QVBoxLayout(central)

        # TODO: a QListView; give it the model with setModel(self.model)

        # TODO: a row (QHBoxLayout) with "Add…", "Edit…", "Remove"
        #       QPushButtons connected to on_add / on_edit / on_remove

        self.setCentralWidget(central)

    def selected_row(self):
        index = self.list_view.currentIndex()
        return index.row() if index.isValid() else -1

    def on_add(self):
        # TODO: QInputDialog.getText(self, "Name", "Full name:") returns
        #       (text, ok); return early if not ok or empty. Otherwise
        #       insertRow(rowCount()), then setData(index(row), text)
        pass

    def on_edit(self):
        # TODO: like on_add, but prefill the dialog with the selected
        #       name (text=...) and setData on the SELECTED row
        pass

    def on_remove(self):
        # TODO: removeRow(selected_row()) if a row is selected
        pass


def main():
    app = QApplication(sys.argv)
    window = AddressWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
