from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sqlite3
from LoginAndRegister import CreateAccScreen
import sys,loginres,signupres

from information import Information
class LoginScreen(QDialog):
    def __init__(self, app, widget):
        self.app = app
        self.widget = widget
        super(LoginScreen, self).__init__()
        self.setStyleSheet("background-color: transparent;")
        loadUi("../View/login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.label_5.clicked.connect(self.backfunction)

    def backfunction(self):
        back = CreateAccScreen(self.app, self.widget)
        self.widget.addWidget(back)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")

        else:
            try:
                conn = sqlite3.connect("../Database/users.db")
                cur = conn.cursor()
                query = 'SELECT * FROM login_info WHERE username =\''+user+"\'"
                cur.execute(query)
                result_user,result_pass = cur.fetchone()
                print('3')
                if (result_user == ''):
                    self.move(100,50)
                    self.error.setText("Invalid username or password")
                else :
                    print (result_user)
                    if result_pass == password:
                        print("Successfully logged in.")
                        self.error.setText("")
                        information = Information(self.app, self.widget)
                        self.widget.addWidget(information)
                        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
                        ''' dataenter = dataenterScreen()
                        self.widget.addWidget(dataenter)
                        self.widget.setCurrentIndex(self.widget.currentIndex()+1)'''
                    

                    else:
                        self.error.setText("Invalid username or password")
            except Exception as e:
                self.error.setText("Invalid username or password")
                print("Login Exceotion:",e)
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = LoginScreen(app, Form)

        Form.show()
        sys.exit(app.exec_())