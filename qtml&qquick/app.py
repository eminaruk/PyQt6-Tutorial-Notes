### we can build modern applications with  QML

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys
from time import strftime, localtime
from PyQt6.QtCore import QTimer, QObject, pyqtSignal

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load("main.qml")

class BackEnd(QObject):

    updated = pyqtSignal(str, arguments=['time'])

    def __init__(self):

        super().__init__() 
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()
    
    def update_time(self):
        currtime = strftime("%H:%M:%S", localtime())
        # engine.rootObjects()[0].setProperty("currTime", currtime)
        self.updated.emit(currtime)


backend = BackEnd()
engine.rootObjects()[0].setProperty("backend", backend)

backend.update_time()

sys.exit(app.exec())



