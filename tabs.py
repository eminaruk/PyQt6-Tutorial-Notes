import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTabWidget, QWidget
from PyQt6.QtGui import QColor, QPalette

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("My tab widget application")

        tabs = QTabWidget()
        tabs.setMovable(True)
        tabs.setTabPosition(QTabWidget.TabPosition.East)
        tabs.setDocumentMode(False)

        for n, color in enumerate(["yellow", "green","blue","red"]):
            
            tabs.addTab(Color(color), color)
        
        
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

            