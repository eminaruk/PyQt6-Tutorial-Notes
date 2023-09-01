import typing
from PyQt6 import QtCore, QtWidgets, uic
import sys
from PyQt6.QtWidgets import QWidget 
from pyqtgraph import PlotWidget, plot
import os
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Pyqtgraph First App")

        uic.load_ui.loadUi("promoted_widget.ui", self)

        self.plot([1,2,3,4,5,6,7,8,9,10,11], [54,33,2,5,67,43,21,54,66, 67, 45])
    
    def plot(self, hour, tempature):
    
        self.graphWidget.plot(hour, tempature)


def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":

    main()