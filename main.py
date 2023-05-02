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
        loadLogistic = joblib.load('logistic_training_data.joblib')
        lr_probs = loadLogistic.predict_proba(x_test)[:, 1]
        return lr_probs
    
    def RandomForestModel(self, x_test):
        loadRandomForest = joblib.load('randomforest_training_data.joblib')
        rf_probs = loadRandomForest.predict_proba(x_test)[:, 1]
        return rf_probs
    
    def Hybrid(self, x_test):
        LogisticResult = self.LogisticModel(x_test) 
        RandomForstResult = self.RandomForestModel(x_test) 
        Hybird = LogisticResult*0.5004774 + RandomForstResult*0.4995226

        print(((Hybird)> 0.5).astype(int))

    def Browsee(self):
        fname = QFileDialog.getOpenFileName(self, 'open file','C:', "CSV files (*.csv)")
        self.filename.setText(fname[0])
        path = fname[0]
        df = pd.read_csv(path)
        x = df.drop('isMalignant',axis = 1).values
        #X = cancerSet[['RandomForest','LogisticRegression']]
        y = df['isMalignant'].values

        #test with first 50% of dataset
        n_samples = x.shape[0]
        n_train = int(n_samples*0.8)

        x_test, y_test= x[n_train:], y[n_train:]
        x_train, y_train= x[:n_train], y[:n_train]

        #Scale data
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)

        self.Hybrid(x_test)





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
