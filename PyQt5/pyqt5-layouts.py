import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor


# ********************* Classes ********************

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palatte = self.palette()
        palatte.setColor(QPalette.Window, QColor(color))
        self.setPalette(palatte)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200,200,500,500)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(Color('red'))
        hlayout.addWidget(Color('green'))
        hlayout.addWidget(Color('blue'))
        # hlayout.setContentsMargins(0,50,0,0)
        hlayout.setSpacing(20)
        
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(Color('orange'))
        vlayout.addWidget(Color('black'))
        vlayout.addWidget(Color('brown'))
        vlayout.setSpacing(20)


        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addLayout(hlayout)
        hlayout2.addLayout(vlayout)
        hlayout2.setSpacing(20)



        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color("blue"),0,0)
        # layout.addWidget(Color("yellow"),0,1)
        # layout.addWidget(Color("yellow"),1,0)
        # layout.addWidget(Color("blue"),1,1)
        # layout.addWidget(Color("blue"),2,0)
        # layout.addWidget(Color("yellow"),2,1)
        # layout.addWidget(Color("yellow"),3,0)
        # layout.addWidget(Color("blue"),3,1)


        widget = QWidget()
        widget.setLayout(hlayout2) 
        self.setCentralWidget(widget)


# **************************

def App():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



# *************************** Main ***************************

App()
