import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QtMsgType
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("widgets application")
        layout = QVBoxLayout()
    
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()