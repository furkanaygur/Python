from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.Result)
        self.ui.BtnSubstract .clicked.connect(self.Result)
        self.ui.BtnDivide.clicked.connect(self.Result)
        self.ui.btnMultiply.clicked.connect(self.Result)


    def Result(self):
        sender = self.sender()
        result = 00
        if sender.text() == "+":
            result = int(self.ui.txt1.text()) + int(self.ui.txt2.text())
        
        elif sender.text() == "-":
            result = int(self.ui.txt1.text()) - int(self.ui.txt2.text())
        
        elif sender.text() == "*":
            result = int(self.ui.txt1.text()) / int(self.ui.txt2.text())
        
        elif sender.text() == "/":
            result = int(self.ui.txt1.text()) * int(self.ui.txt2.text())

        self.ui.lblResult.setText("Result: "+ str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()

    win.show()
    sys.exit(app.exec_())



# ***************** Main ********************

app()