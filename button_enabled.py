import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys




class MyWindow(QMainWindow):

    def __init__(self) :
        super().__init__()

        self.setWindowTitle("emis Technology")

        self.my_button = QPushButton("Press me!")
        self.my_button.clicked.connect(self.button_was_clicked)

        self.setCentralWidget(self.my_button)

    
    def button_was_clicked(self):

        print("you clicked me :)")
        self.my_button.setEnabled(False)

        self.setWindowTitle("You changed the window title :)")


app = QApplication(sys.argv)

window  = MyWindow()
window.show()

app.exec()

