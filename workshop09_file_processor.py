"""Workshop 9: The file processor — timer version (STARTER).

Deck: "Long-Running Tasks" (topic_480_pyside_long_running_tasks),
Workshop 9. Build ProcessorWindow(QMainWindow): ~20 fake files, a
QProgressBar, Start/Cancel buttons, a status line naming the current
file. Version A uses QTimer chunking; Version B (thread) is the stretch
part. The finished version (both): workshop09_file_processor.py in
PySideCourse — run it with "thread" as an argument for Version B.
"""
import sys
import time

from PySide6.QtCore import QObject, QRunnable, QTimer, QThreadPool, Signal
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow, QProgressBar, QPushButton,
    QVBoxLayout, QWidget,
)

FILES = [f"report_{n:02d}.txt" for n in range(20)]
SLICE_SECONDS = 0.3     # deliberately coarse — feel the difference


class ProcessorWindow(QMainWindow):
    """Version A: QTimer chunking — one file per tick."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Processor (timer)")
        self.queue = []
        self.cancel_requested = False

        central = QWidget()
        layout = QVBoxLayout(central)

        self.progress = QProgressBar()
        self.progress.setRange(0, len(FILES))
        layout.addWidget(self.progress)

        buttons = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setEnabled(False)
        self.cancel_button.clicked.connect(self.on_cancel)
        buttons.addWidget(self.start_button)
        buttons.addWidget(self.cancel_button)
        layout.addLayout(buttons)

        self.setCentralWidget(central)
        self.statusBar().showMessage("Ready")

        # one owned timer, reused — never create a second one
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_one)

    def on_start(self):
        # TODO: reject duplicate starts while the timer is active;
        #       reset the progress bar (a fresh QProgressBar starts at
        #       -1!); refill self.queue from FILES; clear the cancel
        #       flag; swap the button enabled states; start the timer
        #       with interval 0
        pass

    def on_cancel(self):
        # TODO: just set the flag — the handler between ticks notices it
        pass

    def process_one(self):
        # TODO: if the queue is empty OR cancel was requested: stop the
        #       timer, restore the buttons, show Done/Cancelled.
        #       Otherwise: pop one file, name it in the status bar,
        #       time.sleep(SLICE_SECONDS), advance the progress bar.
        #       Add a comment answering: why does this never freeze?
        pass


class WorkerSignals(QObject):
    progress = Signal(int)          # files completed
    current_file = Signal(str)      # file being processed
    finished = Signal(bool)         # True = work remained unprocessed


class ProcessWorker(QRunnable):
    """Version B (stretch): the whole batch on a pool thread."""

    def __init__(self, files):
        super().__init__()
        self.files = files
        self.cancel_requested = False
        self.signals = WorkerSignals()

    def run(self):
        # TODO: loop over the files, checking the cancel flag before each
        #       one; emit current_file, sleep, emit progress. At the end
        #       emit finished(completed < len(self.files)) — True means
        #       CANCELLED (work remained), not "success".
        pass


def main():
    app = QApplication(sys.argv)
    window = ProcessorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
