import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("qslider app")

        widget = QSlider(Qt.Orientation.Horizontal)

        widget.setRange(-7,7)
        widget.setSingleStep(3)

        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)
    
    def slider_moved(self):
        print("slider is being moved")
    
    def slider_pressed(self):
        print("slider has been pressed")
    
    def value_changed(self, i):
        print(i)
    
    def slider_released(self):
        print("released")
    
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
