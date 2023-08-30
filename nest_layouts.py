import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self,color):
        super(Color, self).__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My New Application")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(1,1,3,3)
        layout1.setSpacing(17)

        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("blue"))
        layout2.addWidget(Color("red"))

        layout1.addLayout(layout2)
        layout1.addWidget(Color("gray"))

        layout3.addWidget(Color("brown"))
        layout3.addWidget(Color("yellow"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)
        

        widget = QWidget()
        widget.setLayout(layout1)
    
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

