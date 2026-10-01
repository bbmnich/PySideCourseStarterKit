"""Session 5: Model/View Programming I — a list model with two views.

Deck: "Model/View Programming I" (topic_440_pyside_model_view).
A QStringListModel drives a QListView and a QComboBox at the same time
(two views, one model); buttons change, add, and remove rows through the
model, and a label follows the list selection.
"""

import sys

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QListView,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ListModelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("People")

        # TODO: create self.model = QStringListModel() and populate it with
        #       setStringList(["Ada", "Grace", "Edsger"])
        #       (see deck: Model/View Programming I)
        self.model = QStringListModel()
        self.model.setStringList(["Ada", "Grace", "Edger"])


        self.view = QListView()
        # TODO: self.view.setModel(self.model)
        self.view.setModel(self.model)

        self.combo = QComboBox()
        # TODO: let the combo share the same model — a combo box is a view too!
        self.combo.setModel(self.model)  # a combo box is a view too!



        self.detail_label = QLabel("Selected: —")
        # TODO: connect self.view.selectionModel().currentChanged to a lambda
        #       (current, previous) that calls self.on_selection()
        self.view.selectionModel().currentChanged.connect(
            lambda current, previous: self.on_selection()
        )


        change_button = QPushButton("Change row 0")
        change_button.clicked.connect(self.change_first_row)
        add_button = QPushButton("Add row")
        add_button.clicked.connect(self.add_row)
        remove_button = QPushButton("Remove selected")
        remove_button.clicked.connect(self.remove_selected_row)

        buttons = QHBoxLayout()
        buttons.addWidget(change_button)
        buttons.addWidget(add_button)
        buttons.addWidget(remove_button)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.detail_label)
        layout.addLayout(buttons)
        layout.addWidget(self.combo)
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

    def on_selection(self):
        # TODO: read self.view.currentIndex(); if it is not valid, show
        #       "Selected: —" and return; otherwise show
        #       f"Selected: {index.data()}"
        index = self.view.currentIndex()
        if not index.isValid():
            self.detail_label.setText("Selected: —")
            return  # nothing selected
        name = index.data()  # the string at that row
        self.detail_label.setText(f"Selected: {name}")



    def change_first_row(self):
        # TODO: self.model.setData(self.model.index(0), "Ada Lovelace")
        self.model.setData(self.model.index(0), "Ada Lovelace")



    def add_row(self):
        # TODO: insertRow at self.model.rowCount(), then setData on the new
        #       row to "Alan"
        row = self.model.rowCount()
        self.model.insertRow(row)
        self.model.setData(self.model.index(row), "Alan")



    def remove_selected_row(self):
        # TODO: if the view's currentIndex() is valid, removeRow its row
        #       through the model
        index = self.view.currentIndex()
        if index.isValid():
            self.model.removeRow(index.row())



def main():
    app = QApplication(sys.argv)
    window = ListModelWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
