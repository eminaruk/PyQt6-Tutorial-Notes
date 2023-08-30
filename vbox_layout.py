import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color) -> None:
        super(Color, self).__init__()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))

        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("my vbox | hbox layout application")

        # layout = QVBoxLayout() # It inserts them by order vertical line
        layout = QHBoxLayout() # It inserts them by order horizontal line
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()