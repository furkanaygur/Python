import sys
from dateEditForm import Ui_MainWindow
from PyQt5 import QtWidgets
from dateEditForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        birthday = self.ui.dateEdit.date()
        now = QDate.currentDate()
        age = int(birthday.daysTo(now) / 365)
        self.ui.lblResult.setText("Your Age: "+ str(age))
        


app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())
