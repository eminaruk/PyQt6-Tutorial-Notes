import sys
import typing 
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import QModelIndex, QObject, Qt
from PyQt6.QtWidgets import QWidget
import datetime


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
    
    def data(self, index, role):

        colors = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']
        if role == Qt.ItemDataRole.DecorationRole:

            value = self._data[index.row()][index.column()]

            if (isinstance(value, int) or isinstance(value, float)):

                value = int(value)

                value = max(-5, value) ## what does that mean?
                value = min(5, value)
                value+=5 

                return QtGui.QColor(colors[value])

            if isinstance(value, datetime.datetime):
                return QtGui.QIcon("calendar.png")

            if isinstance(value, bool):

                value = self._data[index.row()][index.column()]
                
                if value:
                    return QtGui.QIcon("tick.png")
                
                else:
                    return QtGui.QIcon("cross.png")

        
        # if role == Qt.ItemDataRole.BackgroundRole:
        #     value = self._data[index.row()][index.column()]
            
        #     if (isinstance(value, int) or isinstance(value, float)):

        #         value = int(value)

        #         value = max(-5, value) ## what does that mean?
        #         value = min(5, value)
        #         value+=5 

        #         return QtGui.QColor(colors[value])

        if role == Qt.ItemDataRole.ForegroundRole:

            value = self._data[index.row()][index.column()]

            if (isinstance(value, int) or isinstance(value, float)) and (value < 0):

                return QtGui.QColor("red")


        if role == Qt.ItemDataRole.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

        if role == Qt.ItemDataRole.DisplayRole:

            value = self._data[index.row()][index.column()]

            if isinstance(value, datetime.datetime):

                return value.strftime("%Y-%m-%d")
            
            if isinstance(value, float):

                return "{:.2f}".format(value)
            
            if isinstance(value, str):

                return str(value)
            
            return value
        
            
        
        
    def rowCount(self, index):

        return len(self._data)
    
    def columnCount(self, index):

        return len(self._data[0])
    

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
    
        self.table = QtWidgets.QTableView()

        data = [
          [True, -7, 2],
          [1, "hello", 0],
          [3, 5, datetime.datetime(2023,9,11)],
          [3, 3, -3],
          [False, 4.006, 9],
 ]
        
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
    

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
