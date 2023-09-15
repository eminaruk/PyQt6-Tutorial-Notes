import sys
import os
import typing 
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from pyqtgraph import plot, PlotWidget
import pyqtgraph as pg
from random import randint
import numpy as np



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Cingöz")

        self.graphWidget = PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setTitle("Data Visualization", color = "w", size="13pt")
        # self.graphWidget.addLegend(offset = (0,5))
        self.graphWidget.showGrid(x = True, y = True)
        # self.graphWidget.setXRange(5, 20, padding=0)
        # self.graphWidget.setYRange(30, 40, padding=0)
        self.x =np.array(list(range(100)))
        self.y = np.array([randint(0,100) for _ in range(100)])


        ### writing the data
        
        # hour = [1,2,3,4,5,6,7,8,9,10]
        # temperature_1= [45,  34, 45, 44, 34, 39, 23, 27, 29, 30]
        # temperature_2 = [50,35,44,22,38,32,27,38,32,44]
        # temp1 = self.plot(hour, temperature_1, "temperature 1", "#03C988", QtCore.Qt.PenStyle.DotLine)
        # temp2 = self.plot(hour, temperature_2, "temperature 2", "#ED2B2A", QtCore.Qt.PenStyle.DotLine)

        self.data_line = self.plot(self.x, self.y, plot_name="Realtime", color="#03C988", pen_style=QtCore.Qt.PenStyle.DotLine)

       
        
        self.graphWidget.setBackground("#27374D")
        styles = {"color" : "#B6EADA", "font-size" : "13pt"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.updatePlotData)
        self.timer.start()
        
        # self.clearplot()
    
    def plot(self, x,y, plot_name, color, pen_style = QtCore.Qt.PenStyle):

        pen = pg.mkPen(color = color, width = 7, style = pen_style)
        return self.graphWidget.plot(x, y, name= plot_name, pen= pen, symbol= "o", symbolSize = 11, symbolBrush = "#1F6E8C" )


    def clearplot(self):

        self.graphWidget.clear()
    
    def updatePlotData(self):

        self.x = self.x[1:] + [self.x[-1] + randint(1,5)]
        self.y = self.y[1:] + [randint(0, 100)]

        # Create NumPy arrays from updated data
        x_np = np.array(self.x)
        y_np = np.array(self.y)

        # Update the data_line with the new data
        self.data_line.setData(x=x_np, y=y_np)



def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":

    main()
    