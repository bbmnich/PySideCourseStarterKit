"""Session 9 (Long-Running Tasks): watching a freeze happen.

A Start button runs a slow loop directly in the GUI thread: the window
stops repainting and reacting until the loop is done. The freeze IS the
demo — the timer and worker demos show the two fixes.
"""

import sys
import time

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

NUM_STEPS = 10


class FreezeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Session 9: The Freeze")

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start)
        self.progress = QProgressBar()
        self.progress.setRange(0, NUM_STEPS)

        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.progress)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_start(self):
        # TODO: loop over range(NUM_STEPS): time.sleep(1) to simulate slow
        #       work, then self.progress.setValue(i + 1) — and watch the UI
        #       freeze, because the event loop never runs
        #       (see deck: Long-Running Tasks)
        pass


def main():
    app = QApplication(sys.argv)
    window = FreezeWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
