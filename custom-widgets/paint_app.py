import sys
import typing
from PyQt6 import QtWidgets, QtCore, QtGui, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
import random

COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]

SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10 


class PaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):

        super().__init__()

        self.setFixedSize(QtCore.QSize(17,17))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)

class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.spray_mode = False
        self.pen_width = 1

        self.setWindowTitle("My Paint App")

        self.last_x, self.last_y = None, None
        canvas = QtGui.QPixmap(700, 500)
        canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(canvas)
        self.pen_color = QtGui.QColor("#000000")
    
    def set_pen_color(self,c ):

        self.pen_color = QtGui.QColor(c)
    
    def mouseMoveEvent(self, e):
        # print(self.spray_mode)
        
        if self.last_x is None:
            self.last_x = int(e.position().x())
            self.last_y = int(e.position().y())

        canvas = self.pixmap()
        my_painter = QtGui.QPainter(canvas)

        ## setting the pen

        p = my_painter.pen()
        p.setWidth(self.pen_width)
        p.setColor(self.pen_color)
        my_painter.setPen(p)

        if self.spray_mode:
            
            
            for n in range(SPRAY_PARTICLES):

                xo = random.gauss(0, SPRAY_DIAMETER)
                yo = random.gauss(0, SPRAY_DIAMETER)
                my_painter.drawPoint(int(e.position().x() + xo), int(e.position().y() + yo))
        
        else:
            my_painter.drawLine(int(self.last_x), int(self.last_y), int(e.position().x()), int(e.position().y()))

        my_painter.end()
        self.setPixmap(canvas)
        

        self.last_x = int(e.position().x())
        self.last_y = int(e.position().y())
    
    def mouseReleaseEvent(self, e):
        
        self.last_x, self.last_y = None, None


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cingöz | Basic Paint Work :)")

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        self.switch = QtWidgets.QPushButton("Change Pen Style")
        self.switch.setCheckable(True)
        self.width = QtWidgets.QSpinBox()
        self.width.setValue(1)
        self.width.valueChanged.connect(self.change_pen_width)
        self.switch.pressed.connect(self.change_pen_style)

        w.setLayout(l)
        l.addWidget(self.canvas)
  


        palette = QtWidgets.QHBoxLayout()
        
        self.add_palette_buttons(palette)
        palette.addWidget(self.switch)
        palette.addWidget(self.width)
        l.addLayout(palette)
        

        self.setCentralWidget(w)
    
    def change_pen_style(self):
        
        if self.switch.isChecked():

            self.canvas.spray_mode = False
        
        else:
            # print("a")
            self.canvas.spray_mode = True

    def change_pen_width(self):
        
        new_width = self.width.value()
        self.canvas.pen_width = new_width
    
    def add_palette_buttons(self, layout = QtWidgets.QHBoxLayout):

        for c in COLORS:
            b = PaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


def main():

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":

    main()
