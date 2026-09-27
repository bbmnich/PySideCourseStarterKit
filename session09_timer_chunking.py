"""Session 9 (Long-Running Tasks): chunking work with a QTimer.

Same window shape as the freeze demo, but the work is chopped into
slices: a QTimer with interval 0 fires whenever the event loop is idle,
each timeout processes exactly ONE item, so the UI stays responsive.
"""

import sys
import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

NUM_STEPS = 10


class ChunkedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Session 9: Chunking with a QTimer")

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

        self.queue = []
        # Keep one owned timer: creating a new timer on every Start can leave
        # the previous zero-interval timer active and spinning forever.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_one)

    def on_start(self):
        # TODO: if this single timer is already active, return; otherwise
        #       reset the progress bar (setValue(0)), fill self.queue with
        #       list(range(NUM_STEPS)) — the work, as data — disable Start,
        #       and start self.timer with interval 0 (as fast as the loop
        #       allows). Reuse this timer rather than creating another one.
        #       (see deck: Long-Running Tasks — chunking with a QTimer)
        pass

    def process_one(self):
        # TODO: if the queue is empty, stop the timer, re-enable Start, show
        #       "Done" in the status bar, and return; otherwise pop ONE item,
        #       process it with self.do_one_fast_slice(item), and advance the
        #       progress bar by one. After the last item, perform that same
        #       stop/re-enable completion immediately so no empty callback
        #       keeps running.
        pass

    def do_one_fast_slice(self, item):
        time.sleep(0.05)  # one slice of work, small enough to stay smooth


def main():
    app = QApplication(sys.argv)
    window = ChunkedWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
