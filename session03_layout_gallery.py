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
        # TODO: QFormLayout with rows "Name:", "Email:" (QLineEdit) and
        #       "Language:" (QComboBox with items, e.g. "English", "German");
        #       add it to main
        # TODO: search row QHBoxLayout: self.search_edit (QLineEdit) with
        #       stretch=1, self.search_button (QPushButton "Search") without
        # TODO: QGridLayout: "City:" label + self.city_edit in row 0,
        #       "Bio:" label + self.bio_edit (QPlainTextEdit) spanning
        #       2 rows x 1 column from (1, 1); give bio_edit an
        #       Expanding/Expanding QSizePolicy; add grid with stretch=1
        # TODO: main.addStretch() — a spring that eats all leftover space —
        #       then a "Close" QPushButton (clicked → self.close)
        #       (see deck: Layouts and a Widget Tour — layout gallery)
        pass


def main():
    app = QApplication(sys.argv)
    window = LayoutGallery()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
