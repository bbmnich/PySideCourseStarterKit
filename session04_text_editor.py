"""Session 4: Main Windows and Dialogs — a real text editor.

Deck: "Main Windows and Dialogs" (topic_430_pyside_main_windows).
Merges the deck demo (QActions, menu + toolbar, status bar) with the
workshop starter (dirty tracking) into a complete editor: QFileDialog
open/save with cancel handling and an "unsaved changes" question on close.
"""

import sys

from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
)

FILE_FILTER = "Text files (*.txt);;All files (*)"


class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_path = None
        self.dirty = False

        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.on_text_changed)
        self.setCentralWidget(self.editor)
        self.statusBar().showMessage("Ready")

        # TODO: create the &New, &Open…, &Save and &Quit QActions with
        #       QKeySequence.New/.Open/.Save shortcuts (Quit: setShortcut("Ctrl+Q")
#       — QKeySequence.Quit has no default binding on Windows), connecting
        #       triggered to self.new_file / self.open_file / self.save /
        #       self.close (see deck: Main Windows and Dialogs — actions)
        # TODO: build the &File menu (menuBar().addMenu) with the actions
        #       and a separator before Quit
        # TODO: add a "File" toolbar (addToolBar) with New/Open/Save

        self.update_title()

    def update_title(self):
        name = self.current_path if self.current_path else "Untitled"
        star = "*" if self.dirty else ""
        self.setWindowTitle(f"{star}{name} — Editor")

    def on_text_changed(self):
        self.dirty = True
        self.statusBar().showMessage("Modified")
        self.update_title()

    def new_file(self):
        # TODO: if self.maybe_save() fails, return; otherwise clear the
        #       editor, reset current_path/dirty, show "Ready", update_title()
        pass

    def open_file(self):
        # TODO: if self.maybe_save() fails, return; ask for a path with
        #       QFileDialog.getOpenFileName(self, "Open file", "", FILE_FILTER)
        #       and return if it is empty (user cancelled); read the file
        #       (encoding="utf-8") into the editor, set current_path,
        #       clear dirty, show "Ready", update_title()
        pass

    def save(self):
        """Save the document; returns False if the user cancelled."""
        # TODO: if current_path is None, ask with
        #       QFileDialog.getSaveFileName(...) and return False on cancel;
        #       write editor.toPlainText() to the file (encoding="utf-8"),
        #       clear dirty, show "Saved." for 3 s, update_title(),
        #       return True
        pass

    def maybe_save(self):
        """Ask about unsaved changes; returns False to abort the action."""
        # TODO: if not self.dirty, return True; else ask with
        #       QMessageBox.question (Save | Discard | Cancel):
        #       Save → return self.save(), Discard → return True,
        #       Cancel → return False
        pass

    def closeEvent(self, event):
        # TODO: accept the event if self.maybe_save() succeeds,
        #       otherwise ignore it
        pass


def main():
    app = QApplication(sys.argv)
    window = EditorWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
