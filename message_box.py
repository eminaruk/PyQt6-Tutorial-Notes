import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QPushButton,QMessageBox, QWidget, QLabel, QMainWindow, QVBoxLayout

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message Box App")

        page_layout = QVBoxLayout()

        button = QPushButton("Please click me!!! :)")
        button.clicked.connect(self.button_clicked)

        customized_message_box_button = QPushButton("Click me for customized message box!")
        customized_message_box_button.clicked.connect(self.customized_message_box_button_clicked)

        page_layout.addWidget(button)
        page_layout.addWidget(customized_message_box_button)

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    
    def button_clicked(self):

        dialog = QMessageBox(self)
        dialog.setWindowTitle("Alert!")
        dialog.setText("I love you :))")
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dialog.setIcon(QMessageBox.Icon.Question)
        
        button = dialog.exec()  # this code line gives an evetn idntity to the button object
        # button = QMessageBox.question(self, "Alert!","I have a question?") ## we can also use this QMessageBox.question method to make it easy


        if button == QMessageBox.StandardButton.Yes:

            print("Ok")
        
        else:
            print("it's not okey !")
    
    def customized_message_box_button_clicked(self):  ## you can customize your button features
        
        button = QMessageBox.information(self,
                                         
                                         "Hello guys",
                                         "there is a problem :)",
                                         buttons= QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
                                         defaultButton= QMessageBox.StandardButton.Cancel)

        if button == QMessageBox.StandardButton.Yes:

            print("okey :)")
        
        elif button == QMessageBox.StandardButton.No:
            print("it's not okey")
        
        else:

            print("oh my ...")
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
