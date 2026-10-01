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
        main = QVBoxLayout(self)
        # TODO: "Account" QGroupBox with a QFormLayout: self.name /
        #       self.email QLineEdits and self.language (QComboBox with
        #       ["Python", "Rust", "Go"]); connect its currentTextChanged
        #       to self.on_language
        account = QGroupBox("Account")
        form = QFormLayout(account)
        self.name = QLineEdit()
        form.addRow("Name:", self.name)
        self.email = QLineEdit()
        form.addRow("Email:", self.email)
        self.language = QComboBox()
        self.language.addItems(["Python", "Rust", "Go"])
        self.language.currentTextChanged.connect(self.on_language)
        form.addRow("Language:", self.language)
        main.addWidget(account)

        # TODO: "Notifications" QGroupBox with a QHBoxLayout: self.newsletter
        #       (QCheckBox "Email me", checked, toggled → self.on_toggle)
        #       and a "Desktop alerts" QCheckBox
        notifications = QGroupBox("Notifications")
        box = QHBoxLayout(notifications)
        self.newsletter = QCheckBox("Email me")
        self.newsletter.setChecked(True)
        self.newsletter.toggled.connect(self.on_toggle)
        self.desktop = QCheckBox("Desktop alerts")
        box.addWidget(self.newsletter)
        box.addWidget(self.desktop)
        main.addWidget(notifications)

        # TODO: "Plan" QGroupBox with a QHBoxLayout: self.basic / self.pro
        #       QRadioButtons in a QButtonGroup (Basic checked by default)
        plan = QGroupBox("Plan")
        plan_row = QHBoxLayout(plan)
        self.basic = QRadioButton("Basic")
        self.pro = QRadioButton("Pro")
        self.basic.setChecked(True)
        self.plan_group = QButtonGroup(self)
        self.plan_group.addButton(self.basic)
        self.plan_group.addButton(self.pro)
        plan_row.addWidget(self.basic)
        plan_row.addWidget(self.pro)
        main.addWidget(plan)

        # TODO: self.bio QPlainTextEdit with placeholder
        #       "Tell us about yourself…"
        self.bio = QPlainTextEdit()
        self.bio.setPlaceholderText("Tell us about yourself…")
        main.addWidget(self.bio)

        # TODO: Save row QHBoxLayout: addStretch() first so the "Save"
        #       QPushButton (clicked → self.on_save) sits at the right
        #       (see deck: Layouts and a Widget Tour — widget tour)
        save_row = QHBoxLayout()
        save_row.addStretch()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.on_save)
        save_row.addWidget(save_button)
        main.addLayout(save_row)


    def on_toggle(self, checked):     # checked: bool
        print("Newsletter:", checked)

    def on_language(self, text):
        print("Selected:", text)

    def on_save(self):
        # TODO: print ALL current settings — one getter per widget:
        #       name/email .text(), language .currentText(),
        #       newsletter/desktop .isChecked(), plan, bio .toPlainText()
        plan = "Pro" if self.pro.isChecked() else "Basic"
        print(
            "Saved:",
            "| name:", self.name.text(),
            "| email:", self.email.text(),
            "| language:", self.language.currentText(),
            "| newsletter:", self.newsletter.isChecked(),
            "| desktop alerts:", self.desktop.isChecked(),
            "| plan:", plan,
            "| bio:", self.bio.toPlainText(),
        )



def main():
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
