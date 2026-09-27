"""Session 10 (Persistence and Polish): the drawing app, shippable.

Ties sessions 7-9 together: an undoable click/drag canvas (Sessions 7+8),
JSON documents with a version field and defensive loading, QSettings for
window geometry and the last-used directory, and icons bundled via the
Qt resource system (importing resources_rc registers them).
"""

import json
import math
import sys
from dataclasses import asdict, dataclass, replace
from pathlib import Path

from PySide6.QtCore import QRect, QSettings, QSize, Qt
from PySide6.QtGui import QColor, QIcon, QKeySequence, QPainter, QPen, QUndoCommand, QUndoStack
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QWidget,
)

import resources_rc  # noqa: F401  (importing it registers the :/icons data)

FILE_FILTER = "Drawing files (*.draw.json);;All files (*)"
BASE_TITLE = "Drawing App"
COLORS = ["crimson", "navy", "forestgreen", "darkorange"]
CIRCLE_RADIUS = 15
RECT_WIDTH = 50
RECT_HEIGHT = 30
NOTE_WIDTH = 90
NOTE_HEIGHT = 40
NOTE_BACKGROUND = "#fff4b0"


@dataclass
class Shape:
    kind: str
    x: int
    y: int
    color: str
    text: str = ""


class AddShapeCommand(QUndoCommand):
    def __init__(self, canvas, shape):
        super().__init__(f"Add {shape.kind}")
        self.canvas = canvas
        self.shape = shape

    def redo(self):
        self.canvas.shapes.append(self.shape)
        self.canvas.update()

    def undo(self):
        self.canvas.shapes.pop()
        self.canvas.update()


class MoveShapeCommand(QUndoCommand):
    def __init__(self, canvas, index, old, new):
        super().__init__(f"Move {old.kind}")
        self.canvas = canvas
        self.index = index
        self.old = old
        self.new = new

    def redo(self):
        self.canvas.shapes[self.index] = self.new
        self.canvas.update()

    def undo(self):
        self.canvas.shapes[self.index] = self.old
        self.canvas.update()


class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 200)
        self.shapes = []              # the STATE: plain data
        self.selected_index = None
        self.drag_index = None
        self.drag_start = None
        self.undo_stack = None        # set by the window

    def sizeHint(self):
        return QSize(400, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor("white"))
        for shape in self.shapes:
            painter.setPen(QPen(QColor(shape.color), 2))
            painter.setBrush(Qt.NoBrush)
            if shape.kind == "circle":
                painter.drawEllipse(
                    shape.x - CIRCLE_RADIUS,
                    shape.y - CIRCLE_RADIUS,
                    2 * CIRCLE_RADIUS,
                    2 * CIRCLE_RADIUS,
                )
            elif shape.kind == "rect":
                painter.drawRect(self._shape_rect(shape, RECT_WIDTH, RECT_HEIGHT))
            elif shape.kind == "note":
                rect = self._shape_rect(shape, NOTE_WIDTH, NOTE_HEIGHT)
                painter.fillRect(rect, QColor(NOTE_BACKGROUND))
                painter.drawRect(rect)
                painter.drawText(
                    rect.adjusted(6, 4, -6, -4),
                    Qt.AlignLeft | Qt.AlignVCenter,
                    shape.text,
                )
        painter.end()

    @staticmethod
    def _shape_rect(shape, width, height):
        return QRect(shape.x - width // 2, shape.y - height // 2, width, height)

    def shape_at(self, x, y):
        for i in range(len(self.shapes) - 1, -1, -1):   # topmost first
            shape = self.shapes[i]
            if shape.kind == "circle":
                hit = (x - shape.x) ** 2 + (y - shape.y) ** 2 <= CIRCLE_RADIUS ** 2
            elif shape.kind == "rect":
                hit = self._shape_rect(shape, RECT_WIDTH, RECT_HEIGHT).contains(x, y)
            else:
                hit = self._shape_rect(shape, NOTE_WIDTH, NOTE_HEIGHT).contains(x, y)
            if hit:
                return i
        return None

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
        pos = event.position()              # QPointF, widget coords
        x, y = int(pos.x()), int(pos.y())
        self.drag_index = self.shape_at(x, y)
        if self.drag_index is not None:
            self.drag_start = self.shapes[self.drag_index]  # old position
        else:
            color = COLORS[len(self.shapes) % len(COLORS)]
            self.undo_stack.push(AddShapeCommand(self, Shape("circle", x, y, color)))

    def mouseMoveEvent(self, event):
        if self.drag_index is None:
            return
        pos = event.position()
        old = self.shapes[self.drag_index]
        self.shapes[self.drag_index] = replace(old, x=int(pos.x()), y=int(pos.y()))
        self.update()

    def mouseReleaseEvent(self, event):
        if self.drag_index is not None:
            self.undo_stack.push(MoveShapeCommand(
                self, self.drag_index, self.drag_start,
                self.shapes[self.drag_index]))
        self.drag_index = None


class DrawingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.undo_stack = QUndoStack(self)
        self.canvas = Canvas()
        self.canvas.undo_stack = self.undo_stack
        self.setCentralWidget(self.canvas)

        self.current_path = None
        self.last_dir = QSettings().value("last_dir", "")

        self.undo_stack.cleanChanged.connect(self.on_clean_changed)
        self.on_clean_changed(True)

        self.setWindowIcon(QIcon(":/icons/app.png"))

        undo_action = self.undo_stack.createUndoAction(self, "&Undo")
        undo_action.setShortcut(QKeySequence.Undo)
        undo_action.setIcon(QIcon(":/icons/undo.png"))
        redo_action = self.undo_stack.createRedoAction(self, "&Redo")
        redo_action.setShortcut(QKeySequence.Redo)

        file_menu = self.menuBar().addMenu("&File")
        new_action = file_menu.addAction("&New")
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self.on_new)
        open_action = file_menu.addAction("&Open...")
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.on_open)
        save_action = file_menu.addAction("&Save")
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.on_save)
        save_as_action = file_menu.addAction("Save &As...")
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.triggered.connect(self.on_save_as)
        file_menu.addSeparator()
        quit_action = file_menu.addAction("&Quit")
        quit_action.setShortcut("Ctrl+Q")  # QKeySequence.Quit has no Windows default
        quit_action.triggered.connect(self.close)

        edit_menu = self.menuBar().addMenu("&Edit")
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # TODO: restore the window itself — if QSettings() has "geometry" /
        #       "windowState" values, pass them to self.restoreGeometry /
        #       self.restoreState (see closeEvent, and deck: Persistence and
        #       Polish — remembering the window)

    def closeEvent(self, event):
        # TODO: call maybe_save(); ignore the event and return if it fails.
        #       Otherwise store saveGeometry()/saveState() in QSettings and
        #       accept the event (deck: Persistence and Polish — lifecycle).
        pass

    def maybe_save(self):
        # TODO: return True immediately while undo_stack.isClean(). Otherwise
        #       ask Save/Discard/Cancel with QMessageBox.question. Save returns
        #       self.on_save(), Discard returns True, Cancel returns False.
        pass

    def on_clean_changed(self, clean):
        self.setWindowTitle(BASE_TITLE if clean else BASE_TITLE + " *")

    def save_document(self, path):
        # TODO: in one try block build
        #       {"version": 1, "shapes": [asdict(s) for each shape]} and
        #       write indented UTF-8 JSON. Catch OSError, UnicodeError,
        #       TypeError, and ValueError; show Save failed and return False.
        #       Return True only after the write succeeds.
        pass

    def load_document(self, path):
        # TODO: read and json.load the file; first validate that the top level
        #       is an object containing only version/shapes, version is the
        #       integer 1, and shapes is a list. Each shape must be an object
        #       with at least kind/x/y/color (text is optional, defaults to
        #       ""): kind is circle/rect/note,
        #       x/y are finite numbers (not bool; use math.isfinite) with
        #       abs(value) <= 1_000_000 so Qt's integer drawing API cannot
        #       overflow, and color/text are strings. Only then rebuild the
        #       Shape list. On
        #       OSError, JSONDecodeError, UnicodeDecodeError, TypeError, or
        #       ValueError show a QMessageBox.warning and return False; on
        #       success replace self.canvas.shapes, clear the selection,
        #       self.canvas.update()
        #       (state changed -> repaint) and self.undo_stack.clear()
        #       (the undo history belongs to the OLD document); return True
        pass

    def on_save(self):
        # TODO: if current_path is None, return on_save_as(). Otherwise call
        #       save_document(current_path); return False on failure. Only on
        #       success setClean() and return True.
        pass

    def on_save_as(self):
        # TODO: ask getSaveFileName(...); return False on cancel. Save directly
        #       to the proposed path and return False on failure. Only after a
        #       successful write update current_path/last_dir/QSettings, call
        #       setClean(), and return True.
        pass

    def on_new(self):
        # TODO: first return False unless maybe_save() succeeds. Then clear
        #       canvas.shapes/selected_index, update(), clear the undo stack,
        #       reset current_path to None, setClean(), return True.
        pass

    def on_open(self):
        # TODO: first return False unless maybe_save() succeeds. Then ask
        #       getOpenFileName(...); return False on cancel or failed load.
        #       Only after load_document(path) succeeds update current_path,
        #       last_dir, and QSettings; return True.
        pass


def main():
    app = QApplication(sys.argv)
    # TODO: app.setOrganizationName("MyCourse") and
    #       app.setApplicationName("DrawingApp") — call ONCE, at startup,
    #       so QSettings knows where to store
    #       (see deck: Persistence and Polish — QSettings)
    window = DrawingWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
