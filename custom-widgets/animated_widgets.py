
# class MyCustomValue:

#     def __init__(self):

#         self._value = None
    
#     @property
#     def value(self):

#         print("now, getting the value: ", self._value)
#         return self._value

#     @value.setter
#     def value(self, value):

#         print("now, setting the value: ", value)
#         self._value = value
#         # return self._value
    

# obj = MyCustomValue()

# first_value = obj.value
# print(first_value)
# obj.value = 'HELLO'
# setted_value = obj.value
# print(setted_value)

# import typing
# from PyQt6.QtCore import pyqtProperty, pyqtSignal
# from PyQt6.QtCore import QObject

# class CustomObject(QObject):

#     valueChanged = pyqtSignal(int)

#     def __init__(self):
        
#         super().__init__()
#         self._value = 0
        

#     @property
#     def value(self):

#         return self._value 
    
#     @value.setter
#     def value(self, value):

#         if value != self._value:

#             self._value = value
#             self.valueChanged.emit(self._value)

# obj = CustomObject()
# obj.value = 7
# print(obj.value)

from PyQt6.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSequentialAnimationGroup, QSize, QParallelAnimationGroup
import sys


class MyAnimation(QWidget):

    def __init__(self):

        super().__init__()

        self.resize(700, 700)
        self.child = QWidget(self)
        self.child.resize(70,70)

        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)

        self.child.setStyleSheet("background-color:red;border-radius:13px;")
        self.animation = QPropertyAnimation(self.child, b"pos")  ### pos is not just a single value, it is also a function
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.setStartValue(QPoint(0,0))
        self.animation.setEndValue(QPoint(470, 470))
        self.animation.setDuration(2100)

        # self.animation_2 = QPropertyAnimation(self.child, b"size")
        # self.animation_2.setEndValue(QSize(70, 150))
        # self.animation_2.setDuration(1700)

        self.animation_2 = QPropertyAnimation(effect, b"opacity")
        self.animation_2.setStartValue(0)
        self.animation_2.setEndValue(1)
        self.animation_2.setDuration(2100)

        self.animation_grup = QParallelAnimationGroup()
        self.animation_grup.addAnimation(self.animation)
        self.animation_grup.addAnimation(self.animation_2)
        self.animation_grup.start()


def main():
    
    my_app = QApplication(sys.argv)
    animation = MyAnimation()
    animation.show()
    my_app.exec()


if __name__ == "__main__":

    main()