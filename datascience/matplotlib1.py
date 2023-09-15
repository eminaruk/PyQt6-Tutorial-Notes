import sys 
import matplotlib
matplotlib.use("QtAgg")
import random

from PyQt6 import QtCore, QtWidgets, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent = None, width = int, heigh = int, dpi = int):

        fig = Figure(figsize=(width,heigh ), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super(MplCanvas, self).__init__(fig)

    

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.sc = MplCanvas(self, 5, 4, dpi=100)
        self.setCentralWidget(self.sc)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0,10) for i in range(n_data)]
        
        # self.update_data()

        self.plot_reference = None
        self.update_data_by_plotReference()
        toolbar = NavigationToolbar2QT(self.sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_data)
        self.timer.start()
    

    def update_data(self):

        
        self.ydata = self.ydata[1:] + [random.randint(0,10)]  ### be careful about here! You had a very basic mistake
        self.sc.axes.cla()
        self.sc.axes.plot(self.xdata, self.ydata, 'r')
        self.sc.draw()
    
    def update_data_by_plotReference(self):

        self.ydata = self.ydata[1:] + [random.randint(0,10)]

        if self.plot_reference is None:

            plot_ref = self.sc.axes.plot(self.xdata, self.ydata, "r")
            self.plot_reference = plot_ref[0]
            
        else:

            self.plot_reference.set_ydata(self.ydata)
        
        self.sc.draw()


def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":

    main()
    
    
        

