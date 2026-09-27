"""Session 3: Widget tour — a settings mockup.

The design sketch from the deck, built for real: an Account QGroupBox
with a QFormLayout (name, email, language QComboBox), a Notifications
QGroupBox with two QCheckBoxes, a Basic/Pro QRadioButton pair in a
QButtonGroup, a QPlainTextEdit bio, and a right-aligned Save button.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QCheckBox,
    QRadioButton, QButtonGroup, QPlainTextEdit, QGroupBox,
    QVBoxLayout, QHBoxLayout, QFormLayout,
)


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.resize(420, 480)

        # TODO: main QVBoxLayout(self)
        # TODO: "Account" QGroupBox with a QFormLayout: self.name /
        #       self.email QLineEdits and self.language (QComboBox with
        #       ["Python", "Rust", "Go"]); connect its currentTextChanged
        #       to self.on_language
        # TODO: "Notifications" QGroupBox with a QHBoxLayout: self.newsletter
        #       (QCheckBox "Email me", checked, toggled → self.on_toggle)
        #       and a "Desktop alerts" QCheckBox
        # TODO: "Plan" QGroupBox with a QHBoxLayout: self.basic / self.pro
        #       QRadioButtons in a QButtonGroup (Basic checked by default)
        # TODO: self.bio QPlainTextEdit with placeholder
        #       "Tell us about yourself…"
        # TODO: Save row QHBoxLayout: addStretch() first so the "Save"
        #       QPushButton (clicked → self.on_save) sits at the right
        #       (see deck: Layouts and a Widget Tour — widget tour)
        pass

    def on_toggle(self, checked):     # checked: bool
        print("Newsletter:", checked)

    def on_language(self, text):
        print("Selected:", text)

    def on_save(self):
        # TODO: print ALL current settings — one getter per widget:
        #       name/email .text(), language .currentText(),
        #       newsletter/desktop .isChecked(), plan, bio .toPlainText()


def main():
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
