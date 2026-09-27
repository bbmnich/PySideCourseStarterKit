"""Session 9 (Long-Running Tasks): the QThreadPool + QRunnable worker.

Genuinely slow work runs on a pool thread; the GUI thread only receives
progress/finished signals. A Cancel button demonstrates cooperative
cancellation: it sets a flag, the worker checks it between items.
"""

import sys
import time

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def process(item):
    time.sleep(0.5)  # the slow part — allowed on a worker thread!
    return item * item


class WorkerSignals(QObject):
    # TODO: declare progress = Signal(int) and finished = Signal(bool), where
    #       the bool says whether processing was cancelled (signals must live
    #       on a QObject — QRunnable is not one!)
    #       (see deck: Long-Running Tasks — the worker)
    pass


class ProcessWorker(QRunnable):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.signals = WorkerSignals()
        self._cancelled = False

    def run(self):                       # runs on a pool thread
        # TODO: set completed = 0; loop over enumerate(self.items); break if
        #       self._cancelled; process(item), set completed = i + 1, then
        #       emit completed as progress. After the loop, emit
        #       completed < len(self.items) with finished: cancellation means
        #       work remained, so a request during the final item is success.
        pass


class WorkerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Session 9: Worker with QThreadPool")

        self.items = list(range(10))
        self.worker = None

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.on_cancel)
        self.progress = QProgressBar()

        buttons = QHBoxLayout()
        buttons.addWidget(self.start_button)
        buttons.addWidget(self.cancel_button)
        layout = QVBoxLayout()
        layout.addLayout(buttons)
        layout.addWidget(self.progress)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_start(self):
        # TODO: return immediately if self.worker is already running. Otherwise
        #       create self.worker = ProcessWorker(self.items); connect
        #       worker.signals.progress to self.progress.setValue and
        #       worker.signals.finished to self.on_finished
        # TODO: self.progress.setRange(0, len(self.items)), disable the
        #       start button, and start the worker via
        #       QThreadPool.globalInstance().start(self.worker)
        pass

    def on_cancel(self):
        # TODO: if self.worker is not None, set self.worker._cancelled =
        #       True — a cancellation REQUEST, not a command: the worker
        #       checks the flag between items
        pass

    def on_finished(self, cancelled=False):
        self.start_button.setEnabled(True)
        self.statusBar().showMessage(
            "Processing cancelled" if cancelled else "Processing finished"
        )
        self.worker = None


def main():
    app = QApplication(sys.argv)
    window = WorkerWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
