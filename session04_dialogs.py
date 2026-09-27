"""Session 4: Main Windows and Dialogs — custom dialogs and message boxes.

Deck: "Main Windows and Dialogs" (topic_430_pyside_main_windows).
Shows a custom QDialog (NameDialog) used modally via exec() and modeless
via show(), the session-3 settings mockup converted into a real
SettingsDialog with an Ok/Cancel button box, and the QMessageBox
information/warning/question statics.
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class NameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Your name")
        self.name_edit = QLineEdit()

        # TODO: create a QDialogButtonBox with Ok | Cancel and connect its
        #       accepted signal to self.accept and rejected to self.reject
        #       (see deck: Main Windows and Dialogs — custom dialogs)

        layout = QVBoxLayout(self)
        layout.addWidget(self.name_edit)
        # TODO: add the button box to the layout


class SettingsDialog(QDialog):  # TODO (deck): changed from QWidget to QDialog
    """The session-3 settings mockup as a real dialog with Ok/Cancel."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")

        self.font_size = QSpinBox()
        self.font_size.setRange(6, 72)
        self.font_size.setValue(12)
        self.tab_width = QSpinBox()
        self.tab_width.setRange(1, 16)
        self.tab_width.setValue(4)
        self.theme = QComboBox()
        self.theme.addItems(["Light", "Dark", "Solarized"])

        editor_group = QGroupBox("Editor")
        form = QFormLayout(editor_group)
        form.addRow("Font size:", self.font_size)
        form.addRow("Tab width:", self.tab_width)
        form.addRow("Color theme:", self.theme)

        self.restore_session = QCheckBox("Restore last session")
        self.auto_save = QCheckBox("Auto-save every minute")
        files_group = QGroupBox("Files")
        files_box = QVBoxLayout(files_group)
        files_box.addWidget(self.restore_session)
        files_box.addWidget(self.auto_save)

        self.keys_default = QRadioButton("Default")
        self.keys_vim = QRadioButton("Vim")
        self.keys_emacs = QRadioButton("Emacs")
        self.keys_default.setChecked(True)  # always have a default
        self.keys_group = QButtonGroup(self)
        self.keys_group.addButton(self.keys_default)
        self.keys_group.addButton(self.keys_vim)
        self.keys_group.addButton(self.keys_emacs)
        keys_group = QGroupBox("Keybindings")
        keys_box = QVBoxLayout(keys_group)
        keys_box.addWidget(self.keys_default)
        keys_box.addWidget(self.keys_vim)
        keys_box.addWidget(self.keys_emacs)

        # TODO: add a QDialogButtonBox with Ok | Cancel, wiring accepted →
        #       self.accept and rejected → self.reject, and append it to the
        #       main layout (see deck: Main Windows and Dialogs — turning the
        #       mockup into a dialog)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(editor_group)
        main_layout.addWidget(files_group)
        main_layout.addWidget(keys_group)


class DialogsDemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialogs")
        self.modeless_dialogs = []  # every open modeless dialog stays alive

        modal_button = QPushButton("Enter name (modal)")
        modal_button.clicked.connect(self.ask_name_modal)
        modeless_button = QPushButton("Enter name (modeless)")
        modeless_button.clicked.connect(self.ask_name_modeless)
        settings_button = QPushButton("Settings…")
        settings_button.clicked.connect(self.edit_settings)
        info_button = QPushButton("Information")
        info_button.clicked.connect(self.show_information)
        warning_button = QPushButton("Warning")
        warning_button.clicked.connect(self.show_warning)
        question_button = QPushButton("Question")
        question_button.clicked.connect(self.ask_question)

        layout = QVBoxLayout()
        layout.addWidget(modal_button)
        layout.addWidget(modeless_button)
        layout.addWidget(settings_button)
        layout.addWidget(info_button)
        layout.addWidget(warning_button)
        layout.addWidget(question_button)
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

    def ask_name_modal(self):
        # MODAL: blocks interaction with the rest of the app until closed
        dialog = NameDialog(self)
        if dialog.exec() == QDialog.Accepted:
            print("Name:", dialog.name_edit.text())

    def ask_name_modeless(self):
        # MODELESS: keep every dialog alive and capture this specific dialog
        # in its callbacks, so several dialogs can be open safely at once.
        dialog = NameDialog(self)
        self.modeless_dialogs.append(dialog)
        dialog.accepted.connect(
            lambda dialog=dialog: print("Name:", dialog.name_edit.text())
        )
        dialog.finished.connect(
            lambda _result, dialog=dialog: self.modeless_dialogs.remove(dialog)
        )
        dialog.show()

    def edit_settings(self):
        dialog = SettingsDialog(self)
        if dialog.exec() == QDialog.Accepted:
            # read the values back only after acceptance
            print("Font size:", dialog.font_size.value())
            print("Tab width:", dialog.tab_width.value())
            print("Color theme:", dialog.theme.currentText())
            print("Restore session:", dialog.restore_session.isChecked())
            print("Auto-save:", dialog.auto_save.isChecked())
            print("Vim keybindings:", dialog.keys_vim.isChecked())

    def show_information(self):
        # TODO: show QMessageBox.information(self, "Saved",
        #       "Your document was saved.")
        #       (see deck: Main Windows and Dialogs — message boxes)
        pass

    def show_warning(self):
        # TODO: show QMessageBox.warning(self, "Oops",
        #       "Could not open the file.")
        pass

    def ask_question(self):
        # TODO: ask with QMessageBox.question (Save | Discard | Cancel) and
        #       print which button was chosen ("Save chosen" / "Discard
        #       chosen" / "Cancel chosen")
        pass


def main():
    app = QApplication(sys.argv)
    window = DialogsDemoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
