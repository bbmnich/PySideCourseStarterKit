"""Session 6: Model/View II — the Student model, without any window.

Deck: "Model/View II: Custom Models" (topic_450_pyside_custom_models).
A QAbstractTableModel over Student dataclass objects: DisplayRole/EditRole
text, a checkbox column via CheckStateRole, editing via setData, safe row
insertion/removal, and column headers. Windows and tests both import this.
"""

from dataclasses import dataclass

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


@dataclass
class Student:
    name: str
    student_id: str
    grade: float  # 0.0 – 100.0
    enrolled: bool = True


class StudentModel(QAbstractTableModel):
    HEADERS = ["Name", "Student ID", "Grade", "Enrolled"]

    def __init__(self, students=None, parent=None):
        super().__init__(parent)
        self._students = list(students) if students else []

    def rowCount(self, parent=QModelIndex()):
        return len(self._students)

    def columnCount(self, parent=QModelIndex()):
        return len(self.HEADERS)

    def data(self, index, role=Qt.DisplayRole):
        # TODO: return None for invalid indexes; for DisplayRole/EditRole
        #       return name (col 0), student_id (col 1), f"{grade:.1f}"
        #       (col 2), None (col 3 — shown as checkbox instead); for
        #       CheckStateRole on column 3 return Qt.Checked/Qt.Unchecked
        #       from student.enrolled; for ToolTipRole on column 2 return
        #       "Final grade, 0–100"; None for every other role
        #       (see deck: Model/View II — Custom Models)
        return None

    def flags(self, index):
        # TODO: replace this safe baseline with base = Qt.ItemIsEnabled |
        #       Qt.ItemIsSelectable; column 3 gets base |
        #       Qt.ItemIsUserCheckable, columns 0–2 get base |
        #       Qt.ItemIsEditable
        return Qt.NoItemFlags

    def setData(self, index, value, role=Qt.EditRole):
        # TODO: return False for invalid indexes; for EditRole update name /
        #       student_id / grade (float(value)) by column, for
        #       CheckStateRole on column 3 set enrolled from
        #       value == Qt.Checked, else return False; on success emit
        #       self.dataChanged.emit(index, index, [role]) and return True
        return False

    def add_student(self, student):
        # TODO: append the student inside beginInsertRows(QModelIndex(),
        #       row, row) / endInsertRows() — row = len(self._students)
        pass

    def remove_student(self, row):
        # TODO: delete the row inside beginRemoveRows(QModelIndex(), row,
        #       row) / endRemoveRows()
        pass

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # TODO: return self.HEADERS[section] for DisplayRole + horizontal
        #       orientation, None otherwise
        pass
