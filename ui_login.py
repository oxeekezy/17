from PyQt5 import QtCore, QtGui, QtWidgets
import messages


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 284)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginBox = QtWidgets.QLineEdit(self.centralwidget)
        self.loginBox.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.loginBox.setAlignment(QtCore.Qt.AlignCenter)
        self.loginBox.setObjectName("loginBox")
        self.passwordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordBox.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.passwordBox.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordBox.setObjectName("passwordBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginBtn.clicked.connect(self.loginClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.label.setText(_translate("MainWindow", "Имя пользователя"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.loginBtn.setText(_translate("MainWindow", "Вход"))

    def loginClick(self):
        from user import User
        us = User()
        canLogin = User.login(us, self.loginBox.text(), self.passwordBox.text())

        if(not canLogin):
            messages.show_critical_messagebox('Неправильный логин или пароль!')


    def show():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    
