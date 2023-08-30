import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("my combobox app")

        widget = QComboBox()
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        widget.addItems(["emin","ali","faruk"])
        
        

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    
    def index_changed(self, i):

        print(i)
    
    def text_changed(self, t):

        print(t)
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()