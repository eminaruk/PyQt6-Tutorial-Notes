import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from random import choice
title_list = [

"emis",
"emis technology", 
"hello",
"it has been along time friend :)", 
"my name is mehmet emin",
"it is hard to be get used the typing by ten finger",
"something went wrong"
]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("my application")

        self.button = QPushButton("Change the title")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

   
    def the_button_was_clicked(self):

        print("button clicked succesfully")
        new_title = choice(title_list)
        print("the new title is setting as ", new_title)
        self.setWindowTitle(new_title)
    
    def the_window_title_changed(self, window_title):
        
        if window_title == "something went wrong":
            
            self.button.setDisabled(True)


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()


