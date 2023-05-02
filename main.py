import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import sqlite3
#data={}

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.back.clicked.connect(self.backfunction)

    def backfunction(self):
        back = WelcomeScreen()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")

        else:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\''+user+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]

            if result_pass == password:
                print("Successfully logged in.")
                self.error.setText("")

                dataenter = dataenterScreen()
                widget.addWidget(dataenter)
                widget.setCurrentIndex(widget.currentIndex()+1)

            else:
                self.error.setText("Invalid username or password")


class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui", self)

        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.back.clicked.connect(self.backfunction)

    def backfunction(self):
        back = WelcomeScreen()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.error.setText("Please fill in all inputs.")

        elif password != confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute(
                'INSERT INTO login_info (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            dataenter = dataenterScreen()
            widget.addWidget(dataenter)
            widget.setCurrentIndex(widget.currentIndex()+1)


class dataenterScreen(QDialog):
    da=[]
    def __init__(self):
        super(dataenterScreen, self).__init__()
        loadUi("enterdata.ui", self)

        self.enterdata.clicked.connect(self.enter_data)
        self.Browse.clicked.connect(self.Browsee)
    def enter_data(self):

        name = self.patient_name_enter.text()
        radius = self.radius_mean_enter.text()
        perimeter = self.perimeter_mean_enter.text()
        smoothness = self.smoothness_mean_enter.text()
        concavity = self.concavity_mean_enter.text()
        symmetry = self.symmetry_mean_enter.text()
        date = self.date_enter.text()
        texture = self.texture_mean_enter.text()
        area = self.area_mean_enter.text()
        compactness = self.compactness_mean_enter.text()
        concave = self.concave_points_mean_enter.text()
        fractal = self.fractal_dimension_mean_enter.text()
        self.da.append(name)
        self.da.append(radius)
        self.da.append(perimeter)
        self.da.append(smoothness)
        self.da.append(concavity)
        self.da.append(symmetry)
        self.da.append(date)
        self.da.append(texture)
        self.da.append(area)
        self.da.append(compactness)
        self.da.append(concave)
        self.da.append(fractal)
        print(name)

    def Browsee(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', 'D:', "CSV files (*.csv)")
        self.filename.setText(fname[0])
        path = fname[0]
        with open(path , "r") as f:
            print(f.read())





# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
