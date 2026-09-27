"""Session 6: Model/View II — testing the StudentModel without a GUI.

Deck: "Model/View II: Custom Models" (topic_450_pyside_custom_models).
The model never touches widgets, so pytest can exercise it directly:
editing a grade, toggling the Enrolled checkbox, adding/removing rows,
and reading the column headers. Run: pytest test_student_model.py
"""

import os
import sys

from PySide6.QtCore import Qt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from session06_student_model import Student, StudentModel


def test_grade_edit():
    model = StudentModel([Student("Ada", "s001", 90.0)])
    idx = model.index(0, 2)
    assert model.setData(idx, "95.5", Qt.EditRole) is True
    assert model.data(idx) == "95.5"
    assert model.rowCount() == 1


def test_checkbox_toggle():
    model = StudentModel([Student("Ada", "s001", 90.0)])
    idx = model.index(0, 3)
    assert model.data(idx, Qt.CheckStateRole) == Qt.Checked
    assert model.setData(idx, Qt.Unchecked, Qt.CheckStateRole) is True
    assert model.data(idx, Qt.CheckStateRole) == Qt.Unchecked
    assert model.setData(idx, Qt.Checked, Qt.CheckStateRole) is True
    assert model.data(idx, Qt.CheckStateRole) == Qt.Checked


def test_add_and_remove_student():
    model = StudentModel([Student("Ada", "s001", 90.0)])
    assert model.rowCount() == 1
    model.add_student(Student("Grace", "s002", 88.0))
    assert model.rowCount() == 2
    assert model.data(model.index(1, 0)) == "Grace"
    model.remove_student(0)
    assert model.rowCount() == 1
    assert model.data(model.index(0, 0)) == "Grace"


def test_header_data():
    model = StudentModel()
    assert model.headerData(0, Qt.Horizontal) == "Name"
    assert model.headerData(1, Qt.Horizontal) == "Student ID"
    assert model.headerData(2, Qt.Horizontal) == "Grade"
    assert model.headerData(3, Qt.Horizontal) == "Enrolled"
    assert model.headerData(0, Qt.Vertical) is None
