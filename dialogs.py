import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QDialogButtonBox,QVBoxLayout, QLabel

class CustomDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Alert | Emin")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.button_box = QDialogButtonBox(QBtn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(self.button_box)
        self.layout.addWidget(message)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Dialog App")

        dialog_button = QPushButton("Please click me for dialog!")
        dialog_button.clicked.connect(self.button_clicked)
        
        self.setCentralWidget(dialog_button)


    def button_clicked(self, s):

        print("clicked", s)
        
        dialog = CustomDialog(self)
        
        if dialog.exec():
            print("success")
        
        else:
            print("cancel")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()