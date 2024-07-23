from PyQt5 import QtCore

class ComparisonSetupModel(QtCore.QAbstractTableModel):
    edited_key = QtCore.pyqtSignal(str, str, list)
    def __init__(self, parent, header_data, fetch_model, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.header_data = header_data
        self._header_data_keys = list(self.header_data.keys())
        self.model_data = {key: [False, 'Circle', 5] for key in self._header_data_keys}
        self._fetch_model = fetch_model
        self._col_headers = [
            'View',
            'Symbol',
            'Thickness',
        ]
        
        self.available_symbols = {
            'Circle':'o',
            'Square': 's',
            'Triangle': 't',
            'Diamond': 'd'
        }
        
    def rowCount(self, parent):
        return len(self._header_data_keys)

    def columnCount(self, parent):
        return 4

    def data(self, index: QtCore.QModelIndex, role):
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            row_data = self.model_data[self._header_data_keys[index.row()]]
            if index.column() < len(row_data):
                return row_data[index.column()]
        return None

    def setData(self, index: QtCore.QModelIndex, value, role):
        if not index.isValid():
            return None
        if role == QtCore.Qt.EditRole:
            row_data = self.model_data[self._header_data_keys[index.row()]]
            if index.column() < len(row_data):
                self.model_data[self._header_data_keys[index.row()]][index.column()] = value
                self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex(), [])
                return True
        return None
    
    def flags(self, index: QtCore.QModelIndex):
        if index.column() < 3:
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._col_headers[col] if col < len(self._col_headers) else None
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return self._header_data_keys[col] if col < len(self._header_data_keys) else None
        else:
            return None

    def insertRows(self, header_data: dict) -> bool:
        
        keys_to_add = []
        for key in header_data.keys():
            if key not in self._header_data_keys:
                keys_to_add.append(key)
        
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(None), self.rowCount(None) + len(keys_to_add) - 1)
        self.header_data = dict(header_data)
        self._header_data_keys.extend(keys_to_add)
        self.model_data.update({key: [False, 'Circle', 5] for key in keys_to_add})
        self.endInsertRows()
        