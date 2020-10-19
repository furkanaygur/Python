import sys
from PyQt5 import QtWidgets
from comboboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        box = self.ui.comboBox
        box.addItem("1")
        box.addItems(["2","3"])
        
        self.ui.btnGet.clicked.connect(self.getItem)
        self.ui.btnSubmit_2.clicked.connect(self.loadItems)
        self.ui.btnGet_2.clicked.connect(self.ClearItems)

    def ClearItems(self):
        self.ui.comboBox.clear()

    def getItem(self):
        index = self.ui.comboBox.currentIndex()
        text = self.ui.comboBox.currentText()
        self.ui.lblResult.setText("index: "+str(index)+" Text:"+text)
            

    def loadItems(self):
        items = ["4","5","6"]
        self.ui.comboBox.addItems(items)
        



app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())
        