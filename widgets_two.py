import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mehmet Emin's Application Name")

        widget = QLabel("Welcome, Mr. Wick")
        font = widget.font()
        font.setPointSize(42)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        widget.setScaledContents(True)
        widget.setPixmap(QPixmap("space.jpg"))
        

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
