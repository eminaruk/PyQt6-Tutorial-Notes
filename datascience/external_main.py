from PyQt6.QtWidgets import (QApplication, QPlainTextEdit, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QProgressBar)
from PyQt6.QtCore import QProcess
import sys
import re

progress_re = re.compile(r"Total complete: (\d+)%")

def basic_percent_parser(output):

    m = progress_re.search(output)
    if m:
        print(m)
        pc_complete = m.group(1)
        return int(pc_complete)

class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.p = None
        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        button = QPushButton("Execute")
        button.clicked.connect(self.execute_app)

        self.progress = QProgressBar()
        self.progress.setRange(0,100)

       
        layout.addWidget(button)
        layout.addWidget(self.progress)
        layout.addWidget(self.text)
        

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()
    
    def message(self, message):

        self.text.appendPlainText(message)
    
    def execute_app(self):
        
        if self.p is None:

            self.message("Executing...")
            self.p = QProcess()
            self.p.readyReadStandardError.connect(self.handle_err)
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start("C://Users//byemi//AppData//Local//Programs//Python//Python310//python.exe", ["external.py"])
    
    def handle_err(self):
        
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")

        progress = basic_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)

        self.message(stderr)


    def handle_stdout(self):

        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)
    

    def handle_state(self, state):

        states = {

            QProcess.ProcessState.NotRunning : "Not running",
            QProcess.ProcessState.Running : "Running",
            QProcess.ProcessState.Starting: "Starting"
        }

        status = states[state]
        self.message(f"Status: {status}")
    
    def process_finished(self):

        self.text.appendPlainText("Process finished.")
        self.p = None



app = QApplication(sys.argv)
window = MainWindow()
app.exec()



        
        