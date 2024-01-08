import sys
from PyQt5 import uic, QtWidgets

class Main(object):
    def __init__(self):
        uic.loadUi('ui/login.ui', self)
        self.loginBtn.clicked.connect(self.login)

        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        window.show()

    def login():
        pass


Main()