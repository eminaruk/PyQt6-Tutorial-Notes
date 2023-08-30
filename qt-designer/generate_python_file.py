### if you want generate python file from .ui file you can use "pyuic6 first_design.ui -o first_design.py"
### -o means output!

import sys
from first_design import Ui_MainWindow
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
