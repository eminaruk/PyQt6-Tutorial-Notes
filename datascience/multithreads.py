import typing
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import time
import traceback, sys

class WorkerSignals(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)



class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):

        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
    
    
    @pyqtSlot()
    def run(self):

        # print("Thread start")
        # time.sleep(5)
        # print("Thread ended")
  
        # print(self.args, self.kwargs)
        # print(self.args)
        # print(self.kwargs)
        # self.fn(*self.args, **self.kwargs)

        ### make it with threadIO

        try: 
            result = self.fn(

                *self.args, **self.kwargs
            )
        
        except:

            traceback.print_exc()
            exctype ,value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.counter = 0
        self.threadpool = QThreadPool()
        print("Multithreading max %d thread/s" % self.threadpool.maxThreadCount())


        layout = QVBoxLayout()

        self.l = QLabel("Start!")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("change text")
        c.pressed.connect(self.change_text)

        layout.addWidget(self.l)
        layout.addWidget(b)
        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()

        # setting timer

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()


    def execute_this_function(self, *args, **kwargs):

        for number in range(5):
            time.sleep(1)
        
        return "Done!"

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("COMPLETED :)")

    def oh_no(self):
        # self.message = "Pressed :)"
        # for n in range(100):
            
        #     time.sleep(0.1)
        #     self.l.setText(self.message)
        #     QApplication.processEvents()

        worker = Worker(self.execute_this_function, 1, 2,3,45, name = "emin")
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        
        self.threadpool.start(worker)

    
    def change_text(self):

        self.message = "Oh noooooo"

    def recurring_timer(self):

        self.counter += 1
        self.l.setText("Counter %d" % self.counter)

app = QApplication([])
window = MainWindow()
# window.show()
app.exec()
