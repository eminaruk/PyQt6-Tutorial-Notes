import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My checkbox app")
        
        widget = QCheckBox("Hello, i am checkbox")
        widget.setCheckState(Qt.CheckState.Checked)

        widget.stateChanged.connect(self.the_state_changed)
        self.setCentralWidget(widget)


    def the_state_changed(self, s):

        s = Qt.CheckState.Checked
        print("the state: ", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()