import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("emis Technology")
        self.button_is_checked = True

        button = QPushButton("clik me!")
        button.setCheckable(True)

        button.clicked.connect(self.button_was_toggled)
        button.setChecked(self.button_is_checked)


        self.setCentralWidget(button)

    def button_was_clicked(self):

        print("Buttton was clicked succesfully :)")
    
    def button_was_toggled(self, checked):

        self.button_is_checked = checked

        print("Checked?: ", self.button_is_checked)


    
    


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()
