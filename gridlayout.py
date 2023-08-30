import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
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
        super(MainWindow, self).__init__()

        self.setWindowTitle("Hello, my application is that :)")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0,0)
        layout.addWidget(Color("blue"),1, 1)
        layout.addWidget(Color("yellow"), 2,2)
        layout.addWidget(Color("brown"), 0,2)
        layout.addWidget(Color("gray"), 2,0)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

