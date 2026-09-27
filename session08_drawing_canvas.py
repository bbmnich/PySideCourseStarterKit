"""Session 8: Custom Widgets and Painting (slides_pyside_custom_widgets).

The interactive drawing canvas: click to add circles, drag to move them,
moves are undoable via MoveShapeCommand, and the canvas announces
selections through its own shape_selected signal.
"""
import sys

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QColor, QKeySequence, QPainter, QUndoCommand, QUndoStack
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


class Canvas(QWidget):
    # TODO: declare shape_selected = Signal(int) as a CLASS attribute —
    #       index, or -1 for "nothing"
    #       (see deck: Custom Widgets and Painting — custom signals)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(300, 200)
        # TODO: self.shapes = [] — the STATE: plain data
        # TODO: self.drag_index = None and self.drag_start = None
        #       (for click-drag moving)
        self.undo_stack = None    # the window assigns its QUndoStack here

    def add_circle(self, x, y):
        # TODO: append ("circle", x, y) to self.shapes, then self.update()
        #       to schedule a repaint
        pass

    def shape_at(self, x, y):
        # TODO: scan self.shapes topmost-first (reversed order) and return
        #       the index of the first shape within 15 px of (x, y)
        #       ((x - sx) ** 2 + (y - sy) ** 2 <= 15 ** 2), else None
        pass

    def paintEvent(self, event):
        # TODO: QPainter(self) with Antialiasing and a white background;
        #       set a visible pen and brush (e.g. QPen(QColor("navy"), 2)
        #       and QColor("lightblue")) — without them the default 1px
        #       gray outline is nearly invisible on white; then for every
        #       (kind, x, y) in self.shapes drawEllipse(x - 15, y - 15,
        #       30, 30); then painter.end()
        pass

    def mousePressEvent(self, event):
        # TODO: on left button: self.drag_index = self.shape_at(x, y) —
        #       None means add_circle(x, y), otherwise remember the shape
        #       under the cursor as self.drag_start; in both cases emit
        #       shape_selected (index, or -1 for "nothing")
        #       (event.position() gives a QPointF in widget coords)
        pass

    def mouseMoveEvent(self, event):
        # TODO: while dragging (drag_index not None), replace the dragged
        #       shape's position with the mouse position and self.update()
        pass

    def mouseReleaseEvent(self, event):
        # TODO: if a drag was active, push MoveShapeCommand(self,
        #       self.drag_index, self.drag_start, self.shapes[drag_index])
        #       on the undo stack; end the drag (drag_index = None)
        pass

    def sizeHint(self):
        return QSize(400, 300)


class MoveShapeCommand(QUndoCommand):
    def __init__(self, canvas, index, old_shape, new_shape):
        super().__init__(f"Move shape {index + 1}")
        self.canvas = canvas
        self.index = index
        self.old_shape = old_shape
        self.new_shape = new_shape

    def redo(self):
        # TODO: set canvas.shapes[self.index] to the new shape, then update()
        pass

    def undo(self):
        # TODO: restore the old shape, then update()
        pass


class DrawingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Canvas")

        self.canvas = Canvas()
        self.undo_stack = QUndoStack(self)
        # The canvas pushes a MoveShapeCommand when a drag ends, so it
        # needs the stack — assign it now that both exist.
        self.canvas.undo_stack = self.undo_stack
        self.setCentralWidget(self.canvas)

        undo_action = self.undo_stack.createUndoAction(self, "&Undo")
        undo_action.setShortcut(QKeySequence.Undo)
        self.menuBar().addMenu("&Edit").addAction(undo_action)

        # The guard keeps the starter runnable before the signal is declared.
        if hasattr(self.canvas, "shape_selected"):
            self.canvas.shape_selected.connect(self.on_shape_selected)

    def on_shape_selected(self, index):
        if index >= 0:
            self.statusBar().showMessage(f"Selected shape {index + 1}")
        else:
            self.statusBar().showMessage("Nothing selected")


def main():
    app = QApplication(sys.argv)
    window = DrawingWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
