from ui_login import Ui_MainWindow as login
from PyQt5 import uic, QtWidgets

class Main():
    def __init__(self):
        self.open_login()
        
    def open_login(self):
        login.show()


Main()