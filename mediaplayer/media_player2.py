import typing
from PyQt6 import QtCore
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtWidgets import QWidget


from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow).__init__()

        self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.error.connect(self.erroralert)
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.timeSlider.valueChanged.connect(self.player.setPosition)
        self.player.durationChanged.connect(self.player.update_duration)
        self.player.positionChanged.connect(self.player.update_position)

        self.playlist = QMediaPlaylist()
        self.pla


