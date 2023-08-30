import typing
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import sys

from PyQt5.QtWidgets import QWidget 

app = QApplication(sys.argv)

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Emis Technology")

        random_label = QLabel("Hello guys")
        random_label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(random_label)

my_window = MyWindow()
my_window.show()



app.exec_()

