import sys
import typing
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QWidget
from PyQt6.QtCore import Qt



class MainWindow(QMainWindow):

    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Mouse application")
        self.label = QLabel("you can click this window")
        self.setCentralWidget(self.label)

    
    def mouseMoveEvent(self, e) :
        
        if e.button() == Qt.MouseButton.LeftButton: # I made a mistake in here :) 
                                                    # So, I tried to catch side of mouse when it moves :)
            self.label.setText("mouse move event: left")

        elif e.button() == Qt.MouseButton.RightButton:

            self.label.setText("mouse move event: right")
        
        elif e.button() == Qt.MouseButton.MiddleButton:

            self.label.setText("mouse move event: middle")
    
    def mouseDoubleClickEvent(self, e) :

        if e.button() == Qt.MouseButton.RightButton:
            
            self.label.setText("mouse double click event: right")
        
        elif e.button() == Qt.MouseButton.LeftButton:

            self.label.setText("mouse double click event: left")
        
        elif e.button() == Qt.MouseButton.MiddleButton:

            self.label.setText("mouse double click event: middle")
    
    def mousePressEvent(self,e):

        if e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouse press event: right")
        
        elif e.button() == Qt.MouseButton.LeftButton:

            self.label.setText("mouse press event: left")
        
        elif e.button() == Qt.MouseButton.MiddleButton:

            self.label.setText("mouse press event: middle")        
        
    
    def mouseReleaseEvent(self, e):

        if e.button() == Qt.MouseButton.RightButton:

            self.label.setText("mouse release event: right")  
        
        elif e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouse release event: left")
        
        elif e.button() == Qt.MouseButton.MiddleButton:

            self.label.setText("mouse release event: middle")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

