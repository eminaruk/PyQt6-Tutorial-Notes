import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import (

    QApplication,
    QMainWindow,    
    QPushButton,
    QVBoxLayout,
    QWidget,   
    QLabel
)
from random import randint

class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("External Window")
        layout = QVBoxLayout()
        label = QLabel("Another Window %d " % randint(1, 8))
        layout.addWidget(label)
        self.setLayout(layout)
    

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiple Windows App")

        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        page_layout = QVBoxLayout()
        button1 = QPushButton("Toggle window 1")
        button2 = QPushButton("Toggl2 window 2")
        # button1.clicked.connect(self.toggled_window1)
        # button2.clicked.connect(self.toggled_window2)

        button1.clicked.connect(lambda checked: self.toggle_window(self.window1))  ### you can also use lambda method to make it shorter
        button2.clicked.connect(lambda checked: self.toggle_window(self.window2))

        page_layout.addWidget(button1)
        page_layout.addWidget(button2)
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)
    
    def toggled_window1(self, checked):

        if self.window1.isVisible():

            self.window1.hide()
        else:
            self.window1.show()

    def toggled_window2(self, checked):

            if self.window2.isVisible():

                self.window2.hide()
            else:
                self.window2.show()
    
    def toggle_window(self, window):

        if window.isVisible():
            window.hide()
        
        else: 
            window.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
