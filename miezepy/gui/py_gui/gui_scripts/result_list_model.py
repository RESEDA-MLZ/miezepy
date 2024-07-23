from PyQt5 import QtCore

class ResultListModel(QtCore.QAbstractTableModel):
    edited_key = QtCore.pyqtSignal(str, str, list)
    def __init__(self, parent, my_dict, col_header, row_header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.my_dict = my_dict
        self._my_dict_keys = list(self.my_dict.keys())
        self.col_header = col_header
        self.row_header = row_header

    def getKeyRepresentationAtKey(self, key):
        '''
        Get the key representation for an given project key
        '''
        return self._getKeyRepresentation(self.my_dict[key][1])

    def _getKeyRepresentationAtRow(self, i):
        '''
        Get the key representation at a given row
        '''
        return self._getKeyRepresentation(self.my_dict[self._my_dict_keys[i]][1])

    def _getKeyRepresentation(self, key):
        '''
        Get the key representation for an input key
        '''
        return '_'.join(key.split('_')[2:])
        
    def rowCount(self, parent):
        return len(self.my_dict)

    def columnCount(self, parent):
        return len(self.col_header)

    def data(self, index: QtCore.QModelIndex, role):
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if index.column() == 1:
                return self._getKeyRepresentationAtRow(index.row())
            else:
                return self.my_dict[self._my_dict_keys[index.row()]][index.column()]
        return None

    def setData(self, index: QtCore.QModelIndex, value, role):
        if not index.isValid():
            return None
        if role == QtCore.Qt.EditRole:
            if index.column() == 1:
                full_key = self._my_dict_keys[index.row()]
                new_key = '_'.join(self.my_dict[self._my_dict_keys[index.row()]][index.column()].split('_')[:2]+[value])
                key_list = [self.my_dict[val][1] for i, val in enumerate(self._my_dict_keys) if i != index.row()]
                self.my_dict[self._my_dict_keys[index.row()]][index.column()] = new_key
                self.edited_key.emit(full_key, new_key, key_list)
                self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex(), [])
                return True
            else:
                self.my_dict[self._my_dict_keys[index.row()]][index.column()] = value
                self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex(), [])
                return True
        return None
    
    def flags(self, index: QtCore.QModelIndex):
        if index.column() < 2:
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.col_header[col] if col < len(self.col_header) else None
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return self.row_header[col] if col < len(self.row_header) else None
        else:
            return None


    def insertRows(self, values: dict) -> bool:
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(None), self.rowCount(None) + len(values) - 1)
        self.my_dict = dict(self.my_dict, **values)
        self._my_dict_keys = list(self.my_dict.keys())
        self.endInsertRows()
