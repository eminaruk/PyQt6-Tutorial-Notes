import sys
import typing 
from PyQt6 import QtWidgets, QtCore, QtGui, uic
from PyQt6.QtCore import QModelIndex, QObject, Qt
from PyQt6.QtWidgets import QWidget
import json

ui_filename = "mvc_method.ui"
Ui_MainWindow , QtBaseClass = uic.load_ui.loadUiType(ui_filename)

tick = QtGui.QImage("tick.png")

class TodoModel(QtCore.QAbstractListModel):

    def __init__(self, todos = None):
        super(TodoModel, self).__init__()

        self.todos = todos or []

    
    def data(self, index, role):

        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text 

        if role == Qt.ItemDataRole.DecorationRole:

            status, _ = self.todos[index.row()]

            if status:
                return tick
    
    def rowCount(self, index):
        return len(self.todos)

    


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
    
    def add(self):

        text = self.todoEdit.text()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todoEdit.setText("")
            self.save()
    
    def delete(self):

        indexes = self.todoView.selectedIndexes()

        if indexes:

            index = indexes[0]

            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            self.save()
    
    def complete(self):

        indexes = self.todoView.selectedIndexes()

        if indexes:

            index = indexes[0]
            row = index.row()

            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()
            self.save()
    
    def load(self):

        try:

            with open("data.json", "r") as f:

                self.model.todos = json.load(f)
            
        except Exception:
            pass
    
    def save(self):

        with open("data.json","w") as f:
            data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
