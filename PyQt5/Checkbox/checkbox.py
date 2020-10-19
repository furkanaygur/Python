import sys
from PyQt5 import QtWidgets
from checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.checkBox.stateChanged.connect(self.show_state)
        self.ui.checkBox_2.stateChanged.connect(self.show_state)
        self.ui.checkBox_3.stateChanged.connect(self.show_state)
        self.ui.checkBox_4.stateChanged.connect(self.show_state)
        self.ui.checkBox_5.stateChanged.connect(self.show_state)
        self.ui.checkBox_6.stateChanged.connect(self.show_state)

        self.ui.btnSubmit.clicked.connect(self.display)


    def show_state(self, value):
        result = self.sender()
        print(result.isChecked())
    
    def display(self):
        result = ''
        # items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        items = self.ui.grpbox1.findChildren(QtWidgets.QCheckBox)
        
        for cb in items:
            if cb.isChecked():
                result += cb.text()+ '\n'
        
        self.ui.lblResult.setText(result)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())




# ***************** Main ****************
app()