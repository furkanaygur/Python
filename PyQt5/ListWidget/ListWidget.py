import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox , QInputDialog, QLineEdit
from ListWidgetForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Load
        self.loadItems()
        # Add
        self.ui.btnAdd.clicked.connect(self.addItem)
        # Edit
        self.ui.btnEdit.clicked.connect(self.editItem)
        # # Remove
        self.ui.btnRemove.clicked.connect(self.removeItem)
        # # Up
        self.ui.btnUp.clicked.connect(self.upItem)
        # Down
        self.ui.btnDown.clicked.connect(self.downItem)
        # Sort
        self.ui.btnSort.clicked.connect(self.sortItems)
        # # Exit
        self.ui.btnExit.clicked.connect(self.close)

    def loadItems(self):
        self.ui.ListWidget.addItems(["Furkan","Aygur"])
        self.ui.ListWidget.setCurrentRow(0)
    
    def addItem(self):
        text, ok = QInputDialog.getText(self, "New Item", "Item Name: ")
        if ok and text is not None:
            last = self.ui.ListWidget.count()
            self.ui.ListWidget.insertItem(last,text)

    def editItem(self):
        index = self.ui.ListWidget.currentRow()
        item = self.ui.ListWidget.item(index)
        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Item", "Item Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def removeItem(self):
        index = self.ui.ListWidget.currentRow()
        item = self.ui.ListWidget.item(index)
        if item is None:
            return
        q = QMessageBox.question(self, "Remove", "Do you wanna remove Item: "+item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.ListWidget.takeItem(index)
            del item

    def upItem(self):
        index = self.ui.ListWidget.currentRow()
        if index >= 1:
            item = self.ui.ListWidget.takeItem(index)
            self.ui.ListWidget.insertItem(index-1, item)
            self.ui.ListWidget.setCurrentItem(item)

    def downItem(self):
        index = self.ui.ListWidget.currentRow()
        if index < self.ui.ListWidget.count() -1 :
            item = self.ui.ListWidget.takeItem(index)
            self.ui.ListWidget.insertItem(index+1,item)
            self.ui.ListWidget.setCurrentItem(item)


    def sortItems(self):
        self.ui.ListWidget.sortItems()
    
    def close(self):
        quit()



def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


# ********************* Main ***********************
window()
