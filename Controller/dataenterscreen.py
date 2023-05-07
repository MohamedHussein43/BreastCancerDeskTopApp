import csv
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy
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

class dataenterScreen(QDialog):
    da=[]
    def __init__(self):
        super(dataenterScreen, self).__init__()
        loadUi("../View/enterdata.ui", self)

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
        df = self.prepare(self.da)
        self.Hybrid(df)
    def prepare(self,l):
        df = pd.DataFrame(l)
        arr = df.values

        # reshape the array
        reshaped_arr = arr.reshape((1, -1))

        # convert back to dataframe
        new_df = pd.DataFrame(reshaped_arr)
        return new_df

    def LogisticModel(self, x_test):
        loadLogistic = joblib.load('../Machine_Learning/logistic_training_data.joblib')
        lr_probs = loadLogistic.predict_proba(x_test)[:, 1]
        return lr_probs
    
    def RandomForestModel(self, x_test):
        loadRandomForest = joblib.load('../Machine_Learning/randomforest_training_data.joblib')
        rf_probs = loadRandomForest.predict_proba(x_test)[:, 1]
        return rf_probs
    
    def Hybrid(self, x_test):
        LogisticResult = self.LogisticModel(x_test) 
        RandomForstResult = self.RandomForestModel(x_test) 
        Hybird = LogisticResult*0.5004774 + RandomForstResult*0.4995226

        print(float(Hybird))
        return Hybird

    def Browsee(self):
        fname = QFileDialog.getOpenFileName(self, 'open file','C:', "CSV files (*.csv)")
        self.filename.setText(fname[0])
        path = fname[0]
        df = pd.read_csv(path)
        first80 = pd.read_csv('first80.csv')
        x_train = first80.drop('isMalignant',axis = 1).values
        y_test = first80['isMalignant'].values
        x_test = df.drop('isMalignant',axis = 1).values
        #X = cancerSet[['RandomForest','LogisticRegression']]
        y_test = df['isMalignant'].values

        #test with first 50% of dataset
        #Scale data
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

        return self.Hybrid(self.prepare(x_test)), x_test