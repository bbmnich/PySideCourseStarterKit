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
        new_action = QAction("&New", self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("&Open…", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("&Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save)

        quit_action = QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)

        # TODO: build the &File menu (menuBar().addMenu) with the actions
        #       and a separator before Quit
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        # TODO: add a "File" toolbar (addToolBar) with New/Open/Save
        toolbar = self.addToolBar("File")
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)


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
        if not self.maybe_save():
            return
        self.editor.clear()
        self.current_path = None
        self.dirty = False
        self.statusBar().showMessage("Ready")
        self.update_title()


    def open_file(self):
        # TODO: if self.maybe_save() fails, return; ask for a path with
        #       QFileDialog.getOpenFileName(self, "Open file", "", FILE_FILTER)
        #       and return if it is empty (user cancelled); read the file
        #       (encoding="utf-8") into the editor, set current_path,
        #       clear dirty, show "Ready", update_title()
        if not self.maybe_save():
            return
        path, _selected_filter = QFileDialog.getOpenFileName(
            self, "Open file", "", FILE_FILTER
        )
        if not path:
            return
        with open(path, encoding="utf-8") as file:
            self.editor.setPlainText(file.read())
        self.current_path = path
        self.dirty = False
        self.statusBar().showMessage("Ready")
        self.update_title()



    def save(self):
        """Save the document; returns False if the user cancelled."""
        # TODO: if current_path is None, ask with
        #       QFileDialog.getSaveFileName(...) and return False on cancel;
        #       write editor.toPlainText() to the file (encoding="utf-8"),
        #       clear dirty, show "Saved." for 3 s, update_title(),
        #       return True
        if self.current_path is None:
            path, _selected_filter = QFileDialog.getSaveFileName(
                self, "Save file", "", FILE_FILTER
            )
            if not path:
                return False  # user cancelled
            self.current_path = path
        with open(self.current_path, "w", encoding="utf-8") as file:
            file.write(self.editor.toPlainText())
        self.dirty = False
        self.statusBar().showMessage("Saved.", 4000)
        self.update_title()
        return True


    def maybe_save(self):
        """Ask about unsaved changes; returns False to abort the action."""
        # TODO: if not self.dirty, return True; else ask with
        #       QMessageBox.question (Save | Discard | Cancel):
        #       Save → return self.save(), Discard → return True,
        #       Cancel → return False
        if not self.dirty:
            return True
        answer = QMessageBox.question(
            self,
            "Unsaved changes",
            "The document has unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
        )
        if answer == QMessageBox.Save:
            return self.save()
        if answer == QMessageBox.Discard:
            return True
        return False


    def closeEvent(self, event):
        # TODO: accept the event if self.maybe_save() succeeds,
        #       otherwise ignore it
        if self.maybe_save():
            event.accept()
        else:
            event.ignore()





def main():
    app = QApplication(sys.argv)
    window = EditorWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
