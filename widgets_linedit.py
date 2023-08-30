import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("line edit app")

        widget = QLineEdit()
        widget.setPlaceholderText("please enter your text")
        widget.setMaxLength(13)
        widget.textChanged.connect(self.text_changed)
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    
    def text_changed(self, t):

        print(t)
    
    def return_pressed(self):
        
        self.centralWidget().setText("you are done :)")
    
    def selection_changed(self):

        self.centralWidget().selectedText()
    
    def text_changed(self, text):
        print("text: ", text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()