import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("dial app")

        widget = QDial()

        widget.setRange(-70, 70)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    
    def value_changed(self, i):
        print(i)

    def slider_moved(self, p):
        pass

    def slider_pressed(self):
        pass
    def slider_released(self):
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()