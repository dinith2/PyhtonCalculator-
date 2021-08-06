import sys
import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com") 

        pybutton = QPushButton('roll die', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(50, 50)        

    def clickMethod(self):
        
        self.setMinimumSize(QSize(300, 200))
        pybutton = QPushButton('yes')
        pybutton =QPushButton('no')
        question = input('Would you like to roll the dice [y/n]?\n')
        while question != 'n':
            if question == 'y':
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                print(die1, die2)
                question = input('Would you like to roll the dice [y/n]?\n')
            else:
                print('Invalid response. Please type "y" or "n".')
                question = input('Would you like to roll the dice [y/n]?\n')
                print('Clicked Pyqt button.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )