from ui_login import Ui_MainWindow as login
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Main():
    def __init__(self):
        self.open_login()
        
    def open_login(self):
        app = QtWidgets.QApplication(sys.argv)
        
        l = login(app)
        l.show()

Main()