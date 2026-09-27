"""Session 6: Model/View II — the student table window.

Deck: "Model/View II: Custom Models" (topic_450_pyside_custom_models).
A QTableView backed by the StudentModel from session06_student_model.py,
with Add student and Remove selected buttons.

Note: this module imports session06_student_model, so run it from the
project directory (examples/PySideCourse).
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QInputDialog,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from session06_student_model import Student, StudentModel


class StudentsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students")

        self.model = StudentModel(
            [
                Student("Ada Lovelace", "s001", 91.5),
                Student("Grace Hopper", "s002", 88.0),
            ]
        )

        self.table = QTableView()
        self.table.setModel(self.model)

        add_button = QPushButton("Add student")
        add_button.clicked.connect(self.add_student)
        remove_button = QPushButton("Remove selected")
        remove_button.clicked.connect(self.remove_selected)

        buttons = QHBoxLayout()
        buttons.addWidget(add_button)
        buttons.addWidget(remove_button)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(buttons)
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

    def add_student(self):
        name, ok = QInputDialog.getText(self, "Add student", "Name:")
        if not ok or not name:
            return  # user cancelled or typed nothing
        row = self.model.rowCount()
        self.model.add_student(Student(name, f"s{row + 1:03d}", 0.0))

    def remove_selected(self):
        index = self.table.currentIndex()
        if index.isValid():
            self.model.remove_student(index.row())


def main():
    app = QApplication(sys.argv)
    window = StudentsWindow()
    window.resize(500, 300)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
