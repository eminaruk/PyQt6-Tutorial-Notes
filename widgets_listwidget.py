import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("list widget app")

        widget = QListWidget()
        widget.addItems(["pandas","numpy","matplotlib","tanserflow"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    def index_changed(self, i):

        print("item index: ", i.text())
    
    def text_changed(self, t):
        print("current text: ", t)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

