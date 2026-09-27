"""Workshop 3: Settings dialog mockup (STARTER).

Deck: "Layouts and a Widget Tour" (topic_420_pyside_layouts), Workshop 3.
Build a NON-functional SettingsWindow(QWidget) for an imaginary code
editor. The finished version: workshop03_settings.py in PySideCourse.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QCheckBox, QComboBox, QRadioButton,
    QButtonGroup, QGroupBox, QHBoxLayout, QSpinBox, QVBoxLayout, QFormLayout,
)


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor Settings")
        self.resize(420, 420)

        main = QVBoxLayout(self)

        # TODO: "Editor" QGroupBox with a QFormLayout: font size
        #       (QSpinBox, 8-32, default 11), tab width (QSpinBox, 1-16,
        #       default 4), color theme (QComboBox: Light/Dark/Solarized)

        # TODO: "Files" QGroupBox with a QHBoxLayout: checkboxes
        #       "Restore last session" and "Auto-save every minute"

        # TODO: "Keybindings" QGroupBox with a QHBoxLayout: three
        #       QRadioButtons (Default/Vim/Emacs) in a QButtonGroup,
        #       "Default" checked

        # TODO: a Save row (QHBoxLayout) whose addStretch() pushes the
        #       QPushButton to the bottom right; clicking it calls on_save

    def on_save(self):
        # TODO: print ALL current settings — one getter per widget:
        #       .value() for spin boxes, .currentText() for the combo,
        #       .isChecked() for checkboxes, checkedButton() for the group
        pass


def main():
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
