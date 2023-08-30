import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QStatusBar, QWidget, QCheckBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

### this file contains toolbar, action, menus



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("my pretty app")

        label = QLabel("Hello, my name is mehmet emin")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("this is my awesome toolbar")
        toolbar.setIconSize(QSize(17,17))
        
        self.addToolBar(toolbar)

        button_action = QAction("my button", self)
        button_action.setIcon(QIcon("battery-low.png"))
        button_action.setStatusTip("you reveal the tip :)")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        button_action2 = QAction(QIcon("bug.png"), "my second button", self)
        button_action2.setStatusTip("you reveal the tip of button 2 :)")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        self.check_box = QCheckBox("Are you sure?")
        toolbar.addAction(button_action)
        toolbar.addAction(button_action2)
        toolbar.addWidget(QLabel("Hello guys!"))
        toolbar.addWidget(self.check_box)
        self.check_box.setCheckable(True)
        self.check_box.stateChanged.connect(self.onMyToolBarButtonClick)
        

        self.setStatusBar(QStatusBar(self)) # it show the status (status tip) bottom of the window

        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        submenu = file_menu.addMenu("submenu")
        submenu.addAction(button_action2)
    
    def onMyToolBarButtonClick(self, s):

        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

