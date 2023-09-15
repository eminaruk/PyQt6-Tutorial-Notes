import sys 
import matplotlib
matplotlib.use("QtAgg")
import random

from PyQt6 import QtCore, QtWidgets, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import pandas as pd


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent = None, width = int, heigh = int, dpi = int):

        fig = Figure(figsize=(width,heigh ), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super(MplCanvas, self).__init__(fig)

    

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.sc = MplCanvas(self, 5, 4, dpi=100)
        
        df = pd.DataFrame([
            [0,1], [2,3], [4,5], [6,7], [8,9], [9,0]
        ], columns= ["A", "B"])

        df.plot(ax=self.sc.axes)
        # print(df)

        ## adding toolbar

        toolbar = NavigationToolbar2QT(self.sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        

        self.setCentralWidget(widget)
        
        self.show()

     
def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":

    main()
    
    
        

