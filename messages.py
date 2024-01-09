import sys 
from PyQt5.QtWidgets import *

def show_critical_messagebox(message, title='Ошибка'): 
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Critical) 
    msg.setText(message) 
    msg.setWindowTitle(title) 
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
      
    retval = msg.exec_() 