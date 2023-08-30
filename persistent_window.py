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
        super().__init__()  ### __init__ part runs just one time. So, the random number of extra window doesn't change
        buttons_layout = QVBoxLayout()
        self.setWindowTitle("Multiple Windows App")
        self.extra_window = ExtraWindow()
        button = QPushButton("Click me for extra window!")
        button2 = QPushButton("Toggle window!")
        button.clicked.connect(self.button_clicked)
        button2.clicked.connect(self.toggle_window)


        buttons_layout.addWidget(button)
        buttons_layout.addWidget(button2)
        self.widget = QWidget()
        self.widget.setLayout(buttons_layout)
        self.setCentralWidget(self.widget)
    
    def button_clicked(self, checked):
        
        self.extra_window.show()
    
    def toggle_window(self, checked):

        if self.extra_window.isVisible():

            self.extra_window.hide()
        
        else:
            self.extra_window.show()
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
