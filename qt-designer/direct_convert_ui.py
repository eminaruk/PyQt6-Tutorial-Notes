import sys
import typing 
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import QtCore, uic

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        window = uic.load_ui.loadUi("first_design.ui", self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

