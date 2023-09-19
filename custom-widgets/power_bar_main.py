from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
import sys
from power_bar import PowerBar

app = QtWidgets.QApplication([])
vlm = PowerBar(["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
vlm.setColors(["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
vlm.setBarPadding(7)
vlm.setBarSolidPercent(0.7)
vlm.setBackgroundColor("gray")
vlm.show()
app.exec()