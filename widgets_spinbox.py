import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("spinbox app")

        widget = QSpinBox()

        widget.setMinimum(-7)
        widget.setMaximum(7)

        widget.setPrefix("-> ")
        widget.setSuffix(" <-")
        widget.setSingleStep(1)
        widget.lineEdit().setReadOnly(True)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    def value_changed(self, i):
        print(i)

    def text_changed(self, t):
        print(t)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()