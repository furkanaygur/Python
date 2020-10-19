import sys
from PyQt5 import QtWidgets
from radiobuttonForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.ui.radioButton.setChecked(True)
        # self.ui.radioButton_6.setChecked(True)
        
        self.ui.radioButton.toggled.connect(self.onChecked)
        self.ui.radioButton_2.toggled.connect(self.onChecked)
        self.ui.radioButton_3.toggled.connect(self.onChecked)
        self.ui.radioButton_4.toggled.connect(self.onChecked)
        self.ui.radioButton_5.toggled.connect(self.onChecked)
        self.ui.radioButton_6.toggled.connect(self.onChecked)
        self.ui.radioButton_7.toggled.connect(self.onChecked)
        self.ui.radioButton_8.toggled.connect(self.onChecked)

        self.ui.btnSubmit.clicked.connect(self.onClicked)

    def onChecked(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())
    
    def onClicked(self):
        items = self.ui.centralwidget.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblResult.setText(rb.text())

app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())