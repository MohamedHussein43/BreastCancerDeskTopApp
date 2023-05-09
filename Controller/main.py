import csv
import sys
#sys.path.append('c:\users\moham\appdata\local\programs\python\python310\lib\site-packages')

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy,QLayout
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import joblib
import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
#data={}

from welcomescreen import WelcomeScreen

import sqlite3
from sqlite3 import Error

# main
app = QApplication(sys.argv)
layout = QVBoxLayout()
widget = QtWidgets.QStackedWidget()

welcome = WelcomeScreen(app,widget)
size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
welcome.setSizePolicy(size_policy)
layout.addWidget(welcome)
widget.addWidget(welcome)
widget.setWindowTitle("Breast Cancer Detection")


widget.setWindowIcon(QIcon('pink-ribbon.png'))
widget.setWindowFlags(Qt.WindowMinMaxButtonsHint |Qt.WindowCloseButtonHint )


widget.sizeHint()
widget.showMaximized()
sys.exit(app.exec_())
