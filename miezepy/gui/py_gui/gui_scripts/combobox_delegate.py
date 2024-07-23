from PyQt5 import QtCore, QtWidgets

class ComboBoxDelegate(QtWidgets.QItemDelegate):
    available_symbols = ['Circle', 'Square', 'Triangle', 'Diamond']
    height = 25
    width = 200
    def createEditor(self, parent, option, index):
        self.editor = QtWidgets.QListWidget(parent)
        self.editor.currentItemChanged.connect(self.currentItemChanged)
        return self.editor

    def setEditorData(self, editor, index):
        z = 0
        for item in self.available_symbols:
            ai = QtWidgets.QListWidgetItem(item)
            editor.addItem(ai)
            if item == index.data():
                editor.setCurrentItem(editor.item(z))
            z += 1
        editor.setGeometry(0,index.row()*self.height,self.width,self.height*len(self.available_symbols))

    def setModelData(self, editor, model, index):
        editorIndex=editor.currentIndex()
        text=editor.currentItem().text() 
        model.setData(index, text, QtCore.Qt.EditRole)

    @QtCore.pyqtSlot()
    def currentItemChanged(self): 
        self.commitData.emit(self.sender())
        self.closeEditor.emit(self.editor)