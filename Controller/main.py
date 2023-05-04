import csv
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import sqlite3

import joblib
import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
#data={}

from welcomescreen import WelcomeScreen

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
welcome = WelcomeScreen(app,widget)
size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
welcome.setSizePolicy(size_policy)

widget.addWidget(welcome)
widget.setWindowTitle("Breast Cancer Detection")
widget.setFixedSize(1920,1100)

widget.setWindowIcon(QIcon('pink-ribbon.png'))
widget.setWindowFlags(Qt.WindowMinMaxButtonsHint |Qt.WindowCloseButtonHint )
widget.show()
sys.exit(app.exec_())
