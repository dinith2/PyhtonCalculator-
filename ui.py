from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys 

def demo():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(300,300,300,300)
    win.setWindowTitle("demo ui")
    label=QtWidgets.QLabel(win)
    label.setText("roll dice")
    label.move(100,100)

    win.show()
    sys.exit(app.exec_())
demo()