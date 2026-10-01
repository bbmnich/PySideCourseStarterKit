"""Session 3: Layout gallery.

One window combining the layout toolbox: QFormLayout label-field rows,
a QGridLayout with a spanning QPlainTextEdit, spacing/margins,
addStretch, stretch factors, and a QSizePolicy on the bio field.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QPlainTextEdit, QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout,
    QSizePolicy,
)


class LayoutGallery(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout gallery")
        self.resize(480, 400)

        # TODO: main QVBoxLayout(self) with setSpacing(12) and
        #       setContentsMargins(16, 16, 16, 16)
        main = QVBoxLayout(self)
        main.setSpacing(12)
        main.setContentsMargins(16, 16, 16, 16)

        # TODO: QFormLayout with rows "Name:", "Email:" (QLineEdit) and
        #       "Language:" (QComboBox with items, e.g. "English", "German");
        #       add it to main
        form = QFormLayout()
        form.addRow("Name:", QLineEdit())
        form.addRow("Email:", QLineEdit())

        # QComboBox anlegen, Sprachen hinzufügen
        self.language_combo = QComboBox()
        self.language_combo.addItems(["English", "German"])
        form.addRow("Language:", self.language_combo)

        main.addLayout(form)


        # TODO: search row QHBoxLayout: self.search_edit (QLineEdit) with
        #       stretch=1, self.search_button (QPushButton "Search")
        self.search_edit = QLineEdit()
        self.search_button = QPushButton("Search")
        row = QHBoxLayout()
        row.addWidget(self.search_edit, stretch=1)
        row.addWidget(self.search_button)
        main.addLayout(row)

        # TODO: QGridLayout: "City:" label + self.city_edit in row 0,
        #       "Bio:" label + self.bio_edit (QPlainTextEdit) spanning
        #       2 rows x 1 column from (1, 1); give bio_edit an
        #       Expanding/Expanding QSizePolicy; add grid with stretch=1
        self.city_edit = QLineEdit()
        self.bio_edit = QPlainTextEdit()
        self.bio_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid = QGridLayout()
        grid.addWidget(QLabel("City:"), 0, 0)
        grid.addWidget(self.city_edit, 0, 1)
        grid.addWidget(QLabel("Bio:"), 1, 0)
        grid.addWidget(self.bio_edit, 1, 1, 2, 1)
        main.addLayout(grid, stretch=1)

        # TODO: main.addStretch() — a spring that eats all leftover space —
        #       then a "Close" QPushButton (clicked → self.close)
        #       (see deck: Layouts and a Widget Tour — layout gallery)
        main.addStretch()
        button = QPushButton("Close")
        button.clicked.connect(self.close)
        main.addWidget(button)



def main():
    app = QApplication(sys.argv)
    window = LayoutGallery()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
