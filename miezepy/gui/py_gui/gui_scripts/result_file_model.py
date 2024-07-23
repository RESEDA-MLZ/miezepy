from PyQt5 import QtCore
import os

class ResultFileModel(QtCore.QAbstractListModel):
    def __init__(self, parent, files, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.my_files = files

    def rowCount(self, parent):
        return len(self.my_files)

    def columnCount(self, parent):
        return 1

    def data(self, index: QtCore.QModelIndex, role):
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole:
            return os.path.basename(self.my_files[index.row()])
        return None

    def flags(self, index: QtCore.QModelIndex):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def clear(self):
        self.beginRemoveRows(QtCore.QModelIndex(), 0, len(self.my_files) - 1)
        self.my_files = []
        self.endRemoveRows()
        
    def insertRows(self, files):
        self.beginInsertRows(QtCore.QModelIndex(), 0, len(self.my_files) + len(files) - 1)
        self.my_files.extend(files)
        self.endInsertRows()