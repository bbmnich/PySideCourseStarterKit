"""Session 7: The Command Pattern and Undo/Redo (slides_pyside_undo).

Extends the Session 6 student table with undo support: every mutation goes
through a QUndoCommand on a QUndoStack — grade edits from the table, Add /
Remove buttons, a multi-command macro, and clean-state dirty tracking.
"""
import sys
from dataclasses import dataclass

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QKeySequence, QUndoCommand, QUndoStack
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)


@dataclass
class Student:
    name: str
    student_id: str
    grade: float        # 0.0 – 100.0
    enrolled: bool = True


class StudentModel(QAbstractTableModel):
    HEADERS = ["Name", "Student ID", "Grade", "Enrolled"]

    def __init__(self, students=None, parent=None):
        super().__init__(parent)
        self._students = list(students) if students else []
        # TODO: add self.undo_stack = None — the window assigns its
        #       QUndoStack here (see deck: Undo with the Command Pattern)

    def rowCount(self, parent=QModelIndex()):
        return len(self._students)

    def columnCount(self, parent=QModelIndex()):
        return len(self.HEADERS)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        student = self._students[index.row()]

        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.column() == 0:
                return student.name
            if index.column() == 1:
                return student.student_id
            if index.column() == 2:
                return f"{student.grade:.1f}"
            if index.column() == 3:
                return None                    # shown as checkbox instead

        if role == Qt.CheckStateRole and index.column() == 3:
            return Qt.Checked if student.enrolled else Qt.Unchecked

        if role == Qt.ToolTipRole and index.column() == 2:
            return "Final grade, 0–100"

        return None                            # every other role: no data

    def flags(self, index):
        base = Qt.ItemIsEnabled | Qt.ItemIsSelectable
        if index.column() == 3:
            return base | Qt.ItemIsUserCheckable
        return base | Qt.ItemIsEditable      # columns 0–2: editable text

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False

        student = self._students[index.row()]
        if role == Qt.EditRole and index.column() == 2:
            # TODO: route this grade edit through the undo stack: remember
            #       the old grade, push ChangeGradeCommand(self, index.row(),
            #       float(value), old), and return True. push() applies the
            #       command via redo(); redo calls set_grade, not setData, so
            #       it cannot recursively create another command.
            #       (see deck: Undo with the Command Pattern)
            return False

        # Session 6 behavior remains intact for edits that Session 7 does not
        # make undoable. QAbstractTableModel.setData cannot provide this.
        if role == Qt.EditRole and index.column() == 0:
            student.name = value
        elif role == Qt.EditRole and index.column() == 1:
            student.student_id = value
        elif role == Qt.CheckStateRole and index.column() == 3:
            student.enrolled = value == Qt.Checked
        else:
            return False

        self.dataChanged.emit(index, index, [role])
        return True

    def set_grade(self, row, new_grade):
        # TODO: set the student's grade and emit dataChanged for the index
        #       at (row, 2) with [Qt.DisplayRole, Qt.EditRole]
        pass

    def set_name(self, row, new_name):
        student = self._students[row]
        student.name = new_name
        idx = self.index(row, 0)
        self.dataChanged.emit(idx, idx, [Qt.DisplayRole, Qt.EditRole])

    def add_student(self, student):
        row = len(self._students)
        self.beginInsertRows(QModelIndex(), row, row)
        self._students.append(student)
        self.endInsertRows()

    def insert_student(self, row, student):
        self.beginInsertRows(QModelIndex(), row, row)
        self._students.insert(row, student)
        self.endInsertRows()

    def remove_student(self, row):
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._students[row]
        self.endRemoveRows()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.HEADERS[section]
        return None


class ChangeGradeCommand(QUndoCommand):
    def __init__(self, model, row, new_grade, old_grade):
        super().__init__(f"Change grade of row {row + 1}")
        self.model = model
        self.row = row
        self.new_grade = new_grade
        self.old_grade = old_grade

    def redo(self):
        # TODO: apply the new grade via self.model.set_grade
        pass

    def undo(self):
        # TODO: restore the old grade via self.model.set_grade
        pass


class AddStudentCommand(QUndoCommand):
    def __init__(self, model, student):
        super().__init__(f"Add {student.name}")
        self.model = model
        self.student = student

    def redo(self):
        # TODO: add the student via self.model.add_student
        #       (begin/append/end happens inside)
        pass

    def undo(self):
        # TODO: remove the LAST student via self.model.remove_student
        pass


class RemoveStudentCommand(QUndoCommand):
    # Mirror image of AddStudentCommand — and it must remember the index,
    # because after later edits the row is no longer "the last one".
    def __init__(self, model, row):
        super().__init__(f"Remove {model._students[row].name}")
        self.model = model
        self.row = row
        self.student = model._students[row]

    def redo(self):
        # TODO: remove the student at self.row
        pass

    def undo(self):
        # TODO: re-insert the remembered student at self.row
        #       (self.model.insert_student)
        pass


class ChangeNameCommand(QUndoCommand):
    def __init__(self, model, row, new_name, old_name):
        super().__init__(f"Change name of row {row + 1}")
        self.model = model
        self.row = row
        self.new_name = new_name
        self.old_name = old_name

    def redo(self):
        # TODO: apply the new name via self.model.set_name
        pass

    def undo(self):
        # TODO: restore the old name via self.model.set_name
        pass

    def id(self):
        # TODO: return a constant id — same id = same "kind" of change,
        #       which enables merging
        pass

    def mergeWith(self, other):
        # TODO: if other.row != self.row, return False; otherwise keep MY
        #       old_name, take THEIR new_name, and return True
        pass


class StudentsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students")

        self.model = StudentModel([
            Student("Ada Lovelace", "s001", 91.5),
            Student("Grace Hopper", "s002", 88.0),
        ])
        # TODO: create self.undo_stack = QUndoStack(self) and assign it to
        #       self.model.undo_stack — the model records grade edits by
        #       pushing commands (see setData), so it needs the stack

        self.table = QTableView()
        self.table.setModel(self.model)

        add_button = QPushButton("Add student")
        add_button.clicked.connect(self.add_student)
        remove_button = QPushButton("Remove selected")
        remove_button.clicked.connect(self.remove_selected)
        enroll_button = QPushButton("Enroll and grade")
        enroll_button.clicked.connect(self.enroll_and_grade)

        buttons = QHBoxLayout()
        buttons.addWidget(add_button)
        buttons.addWidget(remove_button)
        buttons.addWidget(enroll_button)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(self.table)
        layout.addLayout(buttons)
        self.setCentralWidget(central)

        # TODO: create the &Undo/&Redo actions with
        #       self.undo_stack.createUndoAction/createRedoAction, set the
        #       QKeySequence.Undo/.Redo shortcuts, and add both to an
        #       &Edit menu
        # TODO: add a &Save action (QKeySequence.Save, triggered → self.save)
        #       to a &File menu
        # TODO: connect self.undo_stack.cleanChanged to self.on_clean_changed

    def add_student(self):
        # TODO: build a Student (f"Student {row + 1}", id f"s{row + 1:03d}",
        #       grade 0.0) and push AddStudentCommand on the undo stack
        pass

    def remove_selected(self):
        # TODO: if the table's currentIndex() is valid, push
        #       RemoveStudentCommand for its row
        pass

    def enroll_and_grade(self):
        # TODO: wrap AddStudentCommand + ChangeGradeCommand (grade 88.0) in
        #       self.undo_stack.beginMacro("Enroll and grade") / endMacro()
        pass

    def on_clean_changed(self, clean):
        # TODO: window title "Students" when clean, "Students *" otherwise
        pass

    def save(self):
        # TODO: self.undo_stack.setClean() (a real app would write to disk
        #       first) and show "Saved" in the status bar for 3 s
        pass


def main():
    app = QApplication(sys.argv)
    window = StudentsWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
