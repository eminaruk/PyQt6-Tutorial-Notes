# import sys
# import random
# import matplotlib
# matplotlib.use('QtAgg')

# from PyQt6 import QtCore, QtWidgets

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure


# class MplCanvas(FigureCanvas):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)


# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
#         self.setCentralWidget(self.canvas)

#         n_data = 50
#         self.xdata = list(range(n_data))
#         self.ydata = [random.randint(0, 10) for i in range(n_data)]
#         self.update_plot()

#         self.show()

#         # Setup a timer to trigger the redraw by calling update_plot.
#         self.timer = QtCore.QTimer()
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.update_plot)
#         self.timer.start()

#     def update_plot(self):
#         # Drop off the first y element, append a new one.
#         self.ydata = self.ydata[1:] + [random.randint(0, 10)]
#         self.canvas.axes.cla()  # Clear the canvas.
#         self.canvas.axes.plot(self.xdata, self.ydata, 'r')
#         # Trigger the canvas to update and redraw.
#         self.canvas.draw()


# app = QtWidgets.QApplication(sys.argv)
# w = MainWindow()
# app.exec()

# from PyQt6.QtGui import *
# from PyQt6.QtWidgets import *
# from PyQt6.QtCore import *

# import time

# class MainWindow(QMainWindow):


#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         self.counter = 0

#         layout = QVBoxLayout()

#         self.l = QLabel("Start")
#         b = QPushButton("DANGER!")
#         b.pressed.connect(self.oh_no)

#         layout.addWidget(self.l)
#         layout.addWidget(b)

#         w = QWidget()
#         w.setLayout(layout)

#         self.setCentralWidget(w)

#         self.show()

#         self.timer = QTimer()
#         self.timer.setInterval(1000)
#         self.timer.timeout.connect(self.recurring_timer)
#         self.timer.start()

#     def oh_no(self):
#         time.sleep(5)

#     def recurring_timer(self):
#         self.counter +=1
#         self.l.setText("Counter: %d" % self.counter)


# app = QApplication([])
# window = MainWindow()
# app.exec()

# from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
#                                 QVBoxLayout, QWidget)
# from PyQt6.QtCore import QProcess
# import sys


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.p = None

#         self.btn = QPushButton("Execute")
#         self.btn.pressed.connect(self.start_process)
#         self.text = QPlainTextEdit()
#         self.text.setReadOnly(True)

#         l = QVBoxLayout()
#         l.addWidget(self.btn)
#         l.addWidget(self.text)

#         w = QWidget()
#         w.setLayout(l)

#         self.setCentralWidget(w)

#     def message(self, s):
#         self.text.appendPlainText(s)

#     def start_process(self):
#         if self.p is None:  # No process running.
#             self.message("Executing process")
#             self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
#             self.p.readyReadStandardOutput.connect(self.handle_stdout)
#             self.p.readyReadStandardError.connect(self.handle_stderr)
#             self.p.stateChanged.connect(self.handle_state)
#             self.p.finished.connect(self.process_finished)  # Clean up once complete.
#             self.p.start("python3", ['external.py'])

#     def handle_stderr(self):
#         data = self.p.readAllStandardError()
#         stderr = bytes(data).decode("utf8")
#         self.message(stderr)

#     def handle_stdout(self):
#         data = self.p.readAllStandardOutput()
#         stdout = bytes(data).decode("utf8")
#         self.message(stdout)

#     def handle_state(self, state):
#         states = {
#             QProcess.ProcessState.NotRunning: 'Not running',
#             QProcess.ProcessState.Starting: 'Starting',
#             QProcess.ProcessState.Running: 'Running',
#         }
#         state_name = states[state]
#         self.message(f"State changed: {state_name}")

#     def process_finished(self):
#         self.message("Process finished.")
#         self.p = None


# app = QApplication(sys.argv)

# w = MainWindow()
# w.show()

# app.exec()

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget, QProgressBar)
from PyQt6.QtCore import QProcess
import sys
import re

# A regular expression, to extract the % complete.
progress_re = re.compile("Total complete: (/d+)%")

def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.progress)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("C://Users//byemi//AppData//Local//Programs//Python//Python310//python.exe", ['external.py'])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.ProcessState.NotRunning: 'Not running',
            QProcess.ProcessState.Starting: 'Starting',
            QProcess.ProcessState.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()