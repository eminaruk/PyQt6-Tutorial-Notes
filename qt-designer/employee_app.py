import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QDialog
from employee import Ui_Dialog


class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Employee app fire window")

        self.button = QPushButton("Fire the app!")
        self.button.clicked.connect(self.employeeBtnClicked)
        self.setCentralWidget(self.button)
    
    def employeeBtnClicked(self):

        dlg = EmployeeDlg(self)
        dlg.exec()


class EmployeeDlg(QDialog):

    def __init__(self, parent= None):
        super().__init__(parent)

        self.ui_dlg = Ui_Dialog()
        self.ui_dlg.setupUi(self)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
