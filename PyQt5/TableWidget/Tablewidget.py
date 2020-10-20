import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from TableWidgetForm import Ui_MainWindow



class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Add
        self.ui.btnAdd.clicked.connect(self.addItem)

        # Double Clicked
        self.ui.tableProducts.doubleClicked.connect(self.doubleClicked)

        self.loadItems()
    
    def loadItems(self):
        # self.ui.tableProducts.setRowCount(2)
        # self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        # self.ui.tableProducts.setItem(0,0, QTableWidgetItem("Iphone 12"))
        # self.ui.tableProducts.setItem(0,1, QTableWidgetItem("1000"))
        # self.ui.tableProducts.setItem(1,0, QTableWidgetItem("Iphone 11"))
        # self.ui.tableProducts.setItem(1,1, QTableWidgetItem("700"))

        products = [
            {"name":"Iphone 12", "price":1000},
            {"name":"Iphone 10", "price":700},
            {"name":"Iphone 8", "price":400}
        ]

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)

        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))
            
            rowIndex+=1

    def addItem(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()

            self.ui.tableProducts.insertRow(rowCount)

            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(price))

    def doubleClicked(self):
        for item in self.ui.tableProducts.selectedItems():
            if item.text().isnumeric():
                self.ui.txtPrice.setText(item.text())
            else:
                self.ui.txtName.setText(item.text())


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

# ****************** Main *****************
window()