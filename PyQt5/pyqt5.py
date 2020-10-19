import sys
from PyQt5 import QtWidgets
 
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Application")
        self.setGeometry(200,200,600,600)
        self.initUI()
    
    def initUI(self):   
        self.lbl1 = QtWidgets.QLabel(self)
        self.lbl1.setText("Name: ")
        self.lbl1.move(50,30)

        self.txt1 = QtWidgets.QLineEdit(self)
        self.txt1.move(120,30)
        self.txt1.resize(120,32)

        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Surname: ")
        self.lbl2.move(50,80)

        self.lblResult = QtWidgets.QLabel(self)
        self.lblResult.resize(100,50)
        self.lblResult.move(120,180)


        self.txt2 = QtWidgets.QLineEdit(self)
        self.txt2.move(120,80)
        self.txt2.resize(120,32)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Submit")
        self.btn.move(120,130)
        self.btn.resize(120,32)
        self.btn.clicked.connect(self.clicked)

    def clicked(self): 
        self.lblResult.setText("Name: "+self.txt1.text() + "\nSurname: "+self.txt2.text())


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


# ******************* Main *********************

window()