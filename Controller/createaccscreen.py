import csv
import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from information import Information
from LoginAndRegister import LoginScreen

class CreateAccScreen(QDialog):
    def __init__(self, app, widget):
        self.app = app
        self.widget = widget
        super(CreateAccScreen, self).__init__()
        loadUi("../View/createacc.ui", self)

        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.back.clicked.connect(self.backfunction)

    def backfunction(self):
        back = LoginScreen(self.app, self.widget)
        self.widget.addWidget(back)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.error.setText("Please fill in all inputs.")

        elif password != confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("../Database/users.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute(
                'INSERT INTO login_info (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            dataenter = Information(self.app, self.widget)
            self.widget.addWidget(dataenter)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)