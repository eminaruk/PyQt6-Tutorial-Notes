import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawPoint(e.position().x(), e.position().y())
        painter.end()
        self.label.setPixmap(canvas)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()