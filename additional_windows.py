import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QVBoxLayout
import sys 
from random import randint


class ExtraWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Extra Window")
        layout = QVBoxLayout()
        text = QLabel("Hello, this is extra window text and I am Mehmet Emin ARUK :)")
        text2 = QLabel("Random page %d " %randint(0, 57)) # if you click again, it replaces the old window with new one
        layout.addWidget(text)
        layout.addWidget(text2)
        self.setLayout(layout)
        

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiple Windows App")
        self.extra_window = None
        button = QPushButton("Click me for extra window!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)
    
    def button_clicked(self, checked):

        if self.extra_window is None:
            self.extra_window = ExtraWindow()
            self.extra_window.show()
        
        else:
            self.extra_window.close()  ### thanks to the this method, we can close window by clicking the button again
            self.extra_window = None
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
