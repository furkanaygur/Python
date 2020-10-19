import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Application")
        self.setGeometry(200,200,600,600)
        self.initUI()
    
    def initUI(self):   

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Exit")
        self.btn.move(200,150)
        self.btn.resize(200,200)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        result = QMessageBox.warning(self, 'Close App', 'Are you sure?', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            QtWidgets.qApp.quit()

    # <=====>
    #     msg = QMessageBox()
    #     msg.setWindowTitle("Close App")
    #     msg.setText("Are You Sure ?")
    #     msg.setIcon(QMessageBox.Warning)
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.setDefaultButton(QMessageBox.Cancel)
    #     # msg.setDetailedText('details...')
    #     msg.buttonClicked.connect(self.popup_Button)
    #     x = msg.exec_()
        
    # def popup_Button(self, x):
    #     if x.text() == 'OK':
    #         QtWidgets.qApp.quit()




def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


# ******************* Main *********************

window()