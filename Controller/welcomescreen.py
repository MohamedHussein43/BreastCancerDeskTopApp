import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from createaccscreen import *
from loginscreen import *

class WelcomeScreen(QDialog):
    def __init__(self, app, widget):
        self.app = app
        self.widget = widget
        
        super(WelcomeScreen, self).__init__()
        self.setStyleSheet("background-color: transparent;")
        loadUi("../View/welcomescreen.ui", self)
        
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen(self.app, self.widget)
        self.widget.addWidget(login)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        login.setSizePolicy(size_policy)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen(self.app, self.widget)
        self.widget.addWidget(create)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)