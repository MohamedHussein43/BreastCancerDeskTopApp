from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QVBoxLayout,QHBoxLayout,QGroupBox,QTableWidgetItem,QPushButton,QLineEdit
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QFileDialog,QVBoxLayout, QTextEdit,QSizePolicy
from PyQt5.uic import loadUi
from dataenterscreen import dataenterScreen
sys.path.insert(1,'..//Model')
from CreatPatientDatabase import *
from datetime import date
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1100)
        Dialog.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(1920, 1100, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 381, 661))
        self.label_2.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Lowlabel = QtWidgets.QLabel(Dialog)
        self.Lowlabel.setGeometry(QtCore.QRect(830, 70, 151, 141))
        self.Lowlabel.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.Lowlabel.setText("")
        self.Lowlabel.setObjectName("Lowlabel")
        self.LogOut = QtWidgets.QPushButton(Dialog)
        self.LogOut.setGeometry(QtCore.QRect(90, 20, 93, 28))
        self.LogOut.setStyleSheet("QPushButton#LogOut{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#LogOut:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#LogOut:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.LogOut.setObjectName("LogOut")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(560, 230, 800, 400))
        self.tableWidget.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.deletepatient = QtWidgets.QPushButton(Dialog)
        self.deletepatient.setGeometry(QtCore.QRect(180, 687, 121, 41))
        self.deletepatient.setStyleSheet("QPushButton#deletepatient{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#deletepatient:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#deletepatient:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.deletepatient.setObjectName("deletepatient")
        self.mediumlabel = QtWidgets.QLabel(Dialog)
        self.mediumlabel.setGeometry(QtCore.QRect(1020, 70, 151, 141))
        self.mediumlabel.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.mediumlabel.setText("")
        self.mediumlabel.setObjectName("mediumlabel")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(1040, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("12 Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));\n"
"font: 16pt bold \"Calibri\";\n"
"color:rgb(255,255,255);")
        self.label_10.setObjectName("label_10")
        self.hardlabel = QtWidgets.QLabel(Dialog)
        self.hardlabel.setGeometry(QtCore.QRect(1200, 70, 151, 141))
        self.hardlabel.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.hardlabel.setText("")
        self.hardlabel.setObjectName("hardlabel")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(1220, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("12 Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));\n"
"font: 16pt bold \"Calibri\";\n"
"color:rgb(255,255,255);")
        self.label_11.setObjectName("label_11")
        self.nof = QtWidgets.QLabel(Dialog)
        self.nof.setGeometry(QtCore.QRect(580, 70, 231, 141))
        self.nof.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.nof.setText("")
        self.nof.setObjectName("nof")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(590, 80, 201, 51))
        font = QtGui.QFont()
        font.setFamily("12 Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt bold \"Calibri\";\n"
"color:rgb(255,255,255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(850, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("12 Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));\n"
"font: 16pt bold \"Calibri\";\n"
"color:rgb(255,255,255);")
        self.label_13.setObjectName("label_13")
        self.N_patients = QtWidgets.QLineEdit(Dialog)
        self.N_patients.setGeometry(QtCore.QRect(610, 140, 161, 51))
        self.N_patients.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 25pt bold\"Calibri\";")
        self.N_patients.setText("")
        self.N_patients.setObjectName("N_patients")
        self.LowText = QtWidgets.QLineEdit(Dialog)
        self.LowText.setGeometry(QtCore.QRect(850, 140, 101, 51))
        self.LowText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 25pt bold\"Calibri\";")
        self.LowText.setObjectName("LowText")
        self.MediumText = QtWidgets.QLineEdit(Dialog)
        self.MediumText.setGeometry(QtCore.QRect(1040, 140, 101, 51))
        self.MediumText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 25pt bold\"Calibri\";")
        self.MediumText.setObjectName("MediumText")
        self.HardText = QtWidgets.QLineEdit(Dialog)
        self.HardText.setGeometry(QtCore.QRect(1220, 140, 101, 51))
        self.HardText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 25pt bold\"Calibri\";")
        self.HardText.setObjectName("HardText")
        self.NameText = QtWidgets.QLineEdit(Dialog)
        self.NameText.setGeometry(QtCore.QRect(210, 250, 161, 51))
        self.NameText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.NameText.setText("")
        self.NameText.setObjectName("NameText")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 250, 131, 51))
        self.label_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 310, 131, 51))
        self.label_4.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.AgeText = QtWidgets.QLineEdit(Dialog)
        self.AgeText.setGeometry(QtCore.QRect(210, 310, 161, 51))
        self.AgeText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.AgeText.setText("")
        self.AgeText.setObjectName("AgeText")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 370, 131, 51))
        self.label_5.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.label_5.setObjectName("label_5")
        self.PhoneText = QtWidgets.QLineEdit(Dialog)
        self.PhoneText.setGeometry(QtCore.QRect(210, 370, 161, 51))
        self.PhoneText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.PhoneText.setText("")
        self.PhoneText.setObjectName("PhoneText")
        self.WeightText = QtWidgets.QLineEdit(Dialog)
        self.WeightText.setGeometry(QtCore.QRect(210, 430, 161, 51))
        self.WeightText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.WeightText.setText("")
        self.WeightText.setObjectName("WeightText")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 430, 151, 51))
        self.label_6.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 490, 131, 51))
        self.label_7.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.label_7.setObjectName("label_7")
        self.EmailText = QtWidgets.QLineEdit(Dialog)
        self.EmailText.setGeometry(QtCore.QRect(210, 490, 161, 51))
        self.EmailText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.EmailText.setText("")
        self.EmailText.setObjectName("EmailText")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 550, 131, 51))
        self.label_8.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.label_8.setObjectName("label_8")
        self.StatusText = QtWidgets.QLineEdit(Dialog)
        self.StatusText.setGeometry(QtCore.QRect(210, 550, 161, 51))
        self.StatusText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.StatusText.setText("")
        self.StatusText.setObjectName("StatusText")
        self.PredictionText = QtWidgets.QLineEdit(Dialog)
        self.PredictionText.setGeometry(QtCore.QRect(210, 610, 161, 51))
        self.PredictionText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.PredictionText.setText("")
        self.PredictionText.setObjectName("PredictionText")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 610, 161, 51))
        self.label_9.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 19pt \"Calibri\";")
        self.label_9.setObjectName("label_9")
        self.ShowtBar = QtWidgets.QPushButton(Dialog)
        self.ShowtBar.setGeometry(QtCore.QRect(1210, 590, 121, 31))
        self.ShowtBar.setStyleSheet("QPushButton#ShowtBar{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#ShowtBar:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ShowtBar:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.ShowtBar.setObjectName("ShowtBar")
        self.addtable = QtWidgets.QLabel(Dialog)
        self.addtable.setGeometry(QtCore.QRect(1490, 90, 381, 691))
        self.addtable.setStyleSheet("border-radius : 20px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 142), stop:1 rgba(255, 255, 255, 255));")
        self.addtable.setText("")
        self.addtable.setObjectName("addtable")
        self.newEmail = QtWidgets.QLabel(Dialog)
        self.newEmail.setGeometry(QtCore.QRect(1530, 480, 131, 51))
        self.newEmail.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.newEmail.setObjectName("newEmail")
        self.newPredText = QtWidgets.QLineEdit(Dialog)
        self.newPredText.setGeometry(QtCore.QRect(1650, 600, 161, 51))
        self.newPredText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newPredText.setText("")
        self.newPredText.setObjectName("newPredText")
        self.newPred = QtWidgets.QLabel(Dialog)
        self.newPred.setGeometry(QtCore.QRect(1510, 600, 161, 51))
        self.newPred.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 19pt \"Calibri\";")
        self.newPred.setObjectName("newPred")
        self.newPhoneText = QtWidgets.QLineEdit(Dialog)
        self.newPhoneText.setGeometry(QtCore.QRect(1650, 360, 161, 51))
        self.newPhoneText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newPhoneText.setText("")
        self.newPhoneText.setObjectName("newPhoneText")
        self.newWeight = QtWidgets.QLabel(Dialog)
        self.newWeight.setGeometry(QtCore.QRect(1530, 420, 151, 51))
        self.newWeight.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.newWeight.setObjectName("newWeight")
        self.newAge = QtWidgets.QLabel(Dialog)
        self.newAge.setGeometry(QtCore.QRect(1530, 300, 131, 51))
        self.newAge.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.newAge.setObjectName("newAge")
        self.newNameText = QtWidgets.QLineEdit(Dialog)
        self.newNameText.setGeometry(QtCore.QRect(1650, 240, 161, 51))
        self.newNameText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newNameText.setText("")
        self.newNameText.setObjectName("newNameText")
        self.newName = QtWidgets.QLabel(Dialog)
        self.newName.setGeometry(QtCore.QRect(1530, 240, 131, 51))
        self.newName.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.newName.setObjectName("newName")
        self.newAgeText = QtWidgets.QLineEdit(Dialog)
        self.newAgeText.setGeometry(QtCore.QRect(1650, 300, 161, 51))
        self.newAgeText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newAgeText.setText("")
        self.newAgeText.setObjectName("newAgeText")
        self.newPhone = QtWidgets.QLabel(Dialog)
        self.newPhone.setGeometry(QtCore.QRect(1530, 360, 131, 51))
        self.newPhone.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.newPhone.setObjectName("newPhone")
        self.newEmailTex = QtWidgets.QLineEdit(Dialog)
        self.newEmailTex.setGeometry(QtCore.QRect(1650, 480, 161, 51))
        self.newEmailTex.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newEmailTex.setText("")
        self.newEmailTex.setObjectName("newEmailTex")
        self.newWeightText = QtWidgets.QLineEdit(Dialog)
        self.newWeightText.setGeometry(QtCore.QRect(1650, 420, 161, 51))
        self.newWeightText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newWeightText.setText("")
        self.newWeightText.setObjectName("newWeightText")
        self.newStatusText = QtWidgets.QLineEdit(Dialog)
        self.newStatusText.setGeometry(QtCore.QRect(1650, 540, 161, 51))
        self.newStatusText.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.newStatusText.setText("")
        self.newStatusText.setObjectName("newStatusText")
        self.newStatus = QtWidgets.QLabel(Dialog)
        self.newStatus.setGeometry(QtCore.QRect(1530, 540, 131, 51))
        self.newStatus.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255,255,255);\n"
"font: 23pt \"Calibri\";")
        self.newStatus.setObjectName("newStatus")
        self.AddNew = QtWidgets.QPushButton(Dialog)
        self.AddNew.setGeometry(QtCore.QRect(1510, 680, 121, 31))
        self.AddNew.setStyleSheet("QPushButton#AddNew{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#AddNew:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#AddNew:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.AddNew.setObjectName("AddNew")
        self.Browse = QtWidgets.QPushButton(Dialog)
        self.Browse.setGeometry(QtCore.QRect(1510, 730, 121, 31))
        self.Browse.setStyleSheet("QPushButton#Browse{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#Browse:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#Browse:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.Browse.setObjectName("Browse")
        self.filename = QtWidgets.QLineEdit(Dialog)
        self.filename.setGeometry(QtCore.QRect(1640, 720, 201, 41))
        self.filename.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 85), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 18pt bold\"Calibri\";")
        self.filename.setText("")
        self.filename.setObjectName("filename")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.LogOut.setText(_translate("Dialog", "LogOut"))
        self.deletepatient.setText(_translate("Dialog", "Delete"))
        self.label_10.setText(_translate("Dialog", " Medium"))
        self.label_11.setText(_translate("Dialog", "   Hard"))
        self.label_12.setText(_translate("Dialog", "Number of patients"))
        self.label_13.setText(_translate("Dialog", "   Low"))
        self.label_3.setText(_translate("Dialog", "Name "))
        self.label_4.setText(_translate("Dialog", "Age "))
        self.label_5.setText(_translate("Dialog", "Phone "))
        self.label_6.setText(_translate("Dialog", "Weight"))
        self.label_7.setText(_translate("Dialog", "email "))
        self.label_8.setText(_translate("Dialog", "Status "))
        self.label_9.setText(_translate("Dialog", "Prediction "))
        self.ShowtBar.setText(_translate("Dialog", "Add"))
        self.newEmail.setText(_translate("Dialog", "email "))
        self.newPred.setText(_translate("Dialog", "Prediction "))
        self.newWeight.setText(_translate("Dialog", "Weight"))
        self.newAge.setText(_translate("Dialog", "Age "))
        self.newName.setText(_translate("Dialog", "Name "))
        self.newPhone.setText(_translate("Dialog", "Phone "))
        self.newStatus.setText(_translate("Dialog", "Status "))
        self.AddNew.setText(_translate("Dialog", "Add Patient"))
        self.Browse.setText(_translate("Dialog", "Upload"))

    # the method of load products
    '''def loadProducts(self):
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(column)'''

class Information(QDialog):
    def __init__(self, app, widget):
        self.app = app
        self.widget = widget
        super(Information, self).__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.widget)
        
        loadUi("../View/information.ui", self)
        self.Table_info()
        self.hidden = False
        self.hide_show()
        self.UserID = -1
        self.tableWidget.doubleClicked.connect(self.doublclick)
        self.LogOut.clicked.connect(self.gotologin)
        self.ShowtBar.clicked.connect(self.hide_show)
        self.AddNew.clicked.connect(self.InsertPatient)
        self.deletepatient.clicked.connect(self.DeletePatient)
        self.Browse.clicked.connect(self.Browsee)
    

    


    def hide_show(self):
            print("hello from")
            if self.hidden:
                self.addtable.show()

                self.newName.show()
                self.newNameText.show()
                self.newNameText.setText('Olivia')

                self.newAge.show()
                self.newAgeText.show()
                self.newAgeText.setText('43')

                self.newPhone.show()
                self.newPhoneText.show()
                self.newPhoneText.setText('6541531')

                self.newWeight.show()
                self.newWeightText.show()
                self.newWeightText.setText('65')

                self.newEmail.show()
                self.newEmailTex.show()
                self.newEmailTex.setText('aslmd@Qgmail.com')

                self.newStatus.show()
                self.newStatusText.show()
                self.newStatusText.setText('married')

                self.newPred.show()
                self.newPredText.show()

                self.Browse.show()
                self.filename.show()
                self.AddNew.show()


                self.hidden = False
            else:
                self.addtable.hide()
                self.newName.hide()
                self.newNameText.hide()
                self.newNameText.setText('')

                self.newAge.hide()
                self.newAgeText.hide()
                self.newAgeText.setText('')

                self.newPhone.hide()
                self.newPhoneText.hide()
                self.newPhoneText.setText('')

                self.newWeight.hide()
                self.newWeightText.hide()
                self.newWeightText.setText('')

                self.newEmail.hide()
                self.newEmailTex.hide()
                self.newEmailTex.setText('')

                self.newStatus.hide()
                self.newStatusText.hide()
                self.newStatusText.setText('')

                self.newPred.hide()
                self.newPredText.hide()
                self.newPredText.setText('')
                self.Browse.hide()
                self.filename.hide()
                self.AddNew.hide()
                self.hidden = True
    def Table_info(self):
            print("Table function 1")
            column = 4
            vbox = QVBoxLayout()
            print("Table function 2")
            database = Database()
            Table_information = database.getPatients()
            print("Table function 3")
            print("-----------------------------------------------------------")
            print(Table_information)
            print("-----------------------------------------------------------")
            '''[{'Id':'1', 'Name':'mmm' ,'BLABLA':'sss'},
                {'Id': '2', 'Name': 'ss', 'BLABLA': 'sss'},
                {'Id': '3', 'Name': 'dd', 'BLABLA': 'aa'},
                {'Id': '4', 'Name': 'fff', 'BLABLA': 'ww'},]'''

            tb_row = self.tableWidget.setRowCount(len(Table_information))
            vbox.addWidget(tb_row)
            tb_col = self.tableWidget.setColumnCount(column)
            vbox.addWidget(tb_col)
            self.tableWidget.setHorizontalHeaderLabels(('Id', 'Name', 'Phone', 'Cancer Level'))
            self.tableWidget.setFixedSize(800, 300)
            id_width = self.tableWidget.setColumnWidth(0, 50)  # set the id column width
            vbox.addWidget(id_width)
            print("Table function 4")

            # fill the data
            # ya zhz you can use a list of the dictionaray to retriev the data from the data base
            index = 0  # the number of the keys in the dictionary from data base
            Cancer_Level = [0, 0, 0]
            for i in range(column):
                    self.tableWidget.setColumnWidth(i, 195)

            for info in Table_information:

                    self.tableWidget.setItem(index, 0, QTableWidgetItem(str(info['id'])))
                    self.tableWidget.setItem(index, 1, QTableWidgetItem(str(info['name'])))
                    self.tableWidget.setItem(index, 2, QTableWidgetItem(str(info['phone'])))

                    if info['Prediction'] <= 0.3*100:
                            self.tableWidget.setItem(index, 3, QTableWidgetItem(str('Low')))
                            Cancer_Level[0] += 1

                    elif info['Prediction'] >= 0.7*100:
                            self.tableWidget.setItem(index, 3, QTableWidgetItem(str('High')))
                            Cancer_Level[2] += 1
                    else:
                            self.tableWidget.setItem(index, 3, QTableWidgetItem(str('Middle')))
                            Cancer_Level[1] += 1
                    button = QPushButton("Addpatient")

                    self.tableWidget.setCellWidget(index, len(Table_information), button)
                    index += 1
            self.LowText.setText(str(Cancer_Level[0]))
            self.MediumText.setText(str(Cancer_Level[1]))
            self.HardText.setText(str(Cancer_Level[2]))
            self.N_patients.setText(str(len(Table_information)))
            print(Cancer_Level)
            print("Table function 5")

            self.widget.setLayout(vbox)
            print("Table function 6")


    # double click ----> change print withe the action
    
    def doublclick(self, item):
        for item in self.tableWidget.selectedItems():
                print(item.row(), item.column(), item.text())
                data = self.gitDataFromTable(item.row())
                self.UserID = data['id']
                if self.UserID > -1:
                    self.NameText.setText(str(data['name']))
                    self.AgeText.setText(str(data['age']))
                    self.PhoneText.setText(str(data['phone']))
                    self.WeightText.setText(str(data['weight']))
                    self.EmailText.setText(str(data['email']))
                    self.StatusText.setText(str(data['status']))
                    self.PredictionText.setText(str(data['Prediction']))

    def gitDataFromTable(sefl, rowNum):
            database = Database()
            Table_information = database.getPatients()
            for i in range(rowNum + 1):
                    if i == rowNum:
                            return Table_information[i]
    


    def InsertPatient(self):
        # Get the current date
        today = date.today()
        data = []
        name = self.newNameText.text()
        age = self.newAgeText.text()
        phone = self.newPhoneText.text()
        weight = self.newWeightText.text()
        email = self.newEmailTex.text()
        status = self.newStatusText.text()
        pred = self.newPredText.text()
        data.append(name)
        data.append(age)
        data.append(phone)
        data.append(weight)
        data.append(email)
        data.append(status)
        data.append(str(today))
        data.append(pred)
        f = True
        for i in data:
                print(i)
                if len(i) == 0:
                        f = False
        if f:
                print(data)
                database = Database()
                database.insertPatient(data)
                Table_information = database.getPatients()
                global medicaldata
                print("------------medicaldata--------")
                print(medicaldata)
                print(type(medicaldata))
                print("------------medicaldata--------")
                (medicaldata.insert(0, int(Table_information[-1]['id'])))
                database.setMedicalData(medicaldata)
                self.Table_info()
                self.hide_show()
                print('Done')
                print("------------medicaldata--------")
                print(medicaldata)
                print(type(medicaldata))
                print("------------medicaldata--------")

        else:
                print("Enter all data")
                self.showMessage();

    def showMessage(self):
        #create instance of the messageBox Class
        msg = QMessageBox()
        msg.setWindowTitle("warning")
        msg.setText("Enter all data.      ")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('clipboard.png'))

        #show the message box
        x = msg.exec_()

    def DeletePatient(self):
        database = Database()
        if self.UserID > -1:
                database.deletePatient(self.UserID)
                self.Table_info()
                self.NameText.setText('')
                self.AgeText.setText('')
                self.PhoneText.setText('')
                self.WeightText.setText('')
                self.EmailText.setText('')
                self.StatusText.setText('')
                self.PredictionText.setText('')
    
    
    medicaldata = []
    def Browsee(self):
        d = dataenterScreen()
        result, allData= d.Browsee()
        global medicaldata
        medicaldata = list(allData[0])
        print (allData)
        self.newPredText.setText(str("{:.2f}".format(float(result)*100)))

    def gotologin(self):
        
        while self.widget.count() > 0:
                widget = self.widget.widget(1)
                print("current index before remove: ",self.widget.currentIndex())
                print("widget index before remove: ",self.widget.widget(0))
                self.widget.removeWidget(widget)
                print("current index after remove: ",self.widget.currentIndex())
                print("widget index after remove: ",self.widget.widget(0))
                if self.widget.currentIndex() !=0:
                      widget.deleteLater()
                else:
                      break
                print("current index after delete: ",self.widget.currentIndex())
                print("widget index after delete: ",self.widget.widget(0))
        print("After loop: ",self.widget.currentIndex())
        self.widget.setCurrentIndex(self.widget.currentIndex())
        
        '''login = LoginScreen(self.app, self.widget)
        self.widget.addWidget(login)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        login.setSizePolicy(size_policy)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)'''
        
