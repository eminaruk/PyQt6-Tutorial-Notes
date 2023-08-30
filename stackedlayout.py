import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStackedLayout
from PyQt6.QtGui import QPalette, QColor
import random


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        
        self.setAutoFillBackground(True)

        pallete = self.palette()
        pallete.setColor(QPalette.ColorRole.Window, QColor(color))

        self.setPalette(pallete)

    
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("muharrem cok yakisikli")

        pagelayout = QVBoxLayout()
        self.stackedlayout = QStackedLayout()
        button_layout = QHBoxLayout()

        button = QPushButton("change the color")
        button.clicked.connect(self.change_the_color)
        button_layout.addWidget(button)



        self.stackedlayout.addWidget(Color("red"))
        self.stackedlayout.addWidget(Color("purple"))
        self.stackedlayout.addWidget(Color("blue"))
        self.stackedlayout.addWidget(Color("yellow"))
        self.stackedlayout.addWidget(Color("green"))

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stackedlayout)
        

        self.stackedlayout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    
    def change_the_color(self):
        
        random_number = random.randint(0, 5)
        self.stackedlayout.setCurrentIndex(random_number)
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

