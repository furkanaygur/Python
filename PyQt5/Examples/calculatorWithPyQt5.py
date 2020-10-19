import sys
from PyQt5 import QtWidgets



class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lblNumber1= QtWidgets.QLabel(self)
        self.lblNumber1.setText("Number1: ")
        self.lblNumber1.move(50,30)
        
        self.txtNumber1 = QtWidgets.QLineEdit(self)
        self.txtNumber1.move(150,30)
        self.txtNumber1.resize(100,32)

        self.lblNumber2= QtWidgets.QLabel(self)
        self.lblNumber2.setText("Number2: ")
        self.lblNumber2.move(50,80)

        self.txtNumber2 = QtWidgets.QLineEdit(self)
        self.txtNumber2.move(150,80)
        self.txtNumber2.resize(100,32)

        self.btnAdd = QtWidgets.QPushButton(self)
        self.btnAdd.move(270,30)
        self.btnAdd.setText("+")
        self.btnAdd.clicked.connect(self.Result)

        self.btnSubstract = QtWidgets.QPushButton(self)
        self.btnSubstract.move(380,30)
        self.btnSubstract.setText("-")
        self.btnSubstract.clicked.connect(self.Result)

        self.btnMultiply = QtWidgets.QPushButton(self)
        self.btnMultiply.move(270,80)
        self.btnMultiply.setText("*")
        self.btnMultiply.clicked.connect(self.Result)

        self.btnDivide = QtWidgets.QPushButton(self)
        self.btnDivide.move(380,80)
        self.btnDivide.setText("/")        
        self.btnDivide.clicked.connect(self.Result)

        self.lblResult= QtWidgets.QLabel(self)
        self.lblResult.move(150,130)

    def Result(self):
        sender = self.sender()

        if sender.text() == "+":
            result = int(self.txtNumber1.text()) + int(self.txtNumber2.text())
        
        elif sender.text() == "-":
            result = int(self.txtNumber1.text()) - int(self.txtNumber2.text())
       
        elif sender.text() == "*":
            result = int(self.txtNumber1.text()) / int(self.txtNumber2.text())
        
        elif sender.text() == "/":
            result = int(self.txtNumber1.text()) * int(self.txtNumber2.text())

        self.lblResult.setText("Result: "+ str(result))
 

def app():
    app= QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())


# ************************ Main **********************

app()