import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MyForm(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Create labels, line edits, and button
        self.lbl_name = QLabel('Name:', self)
        self.lbl_age = QLabel('age:', self)
        self.lbl_phone = QLabel('phone:', self)
        self.lbl_weight = QLabel('weight:', self)
        self.lbl_email = QLabel('email :', self)
        self.lbl_status = QLabel('status:', self)
        self.lbl_dateOfBirth = QLabel('dateOfBirth ', self)
        self.lbl_reportDate = QLabel('reportDate:', self)
        self.lbl_Prediction = QLabel('Prediction:', self)

        self.le_name = QLineEdit(self)
        self.le_age = QLineEdit(self)
        self.le_phone = QLineEdit(self)
        self.le_weight = QLineEdit(self)
        self.le_email = QLineEdit(self)
        self.le_status = QLineEdit(self)
        self.le_dateOfBirth = QLineEdit(self)
        self.le_reportDate = QLineEdit(self)
        self.le_Prediction= QLineEdit(self)

        self.btn_submit = QPushButton('Submit', self)
        self.btn_submit.clicked.connect(self.submitForm)

        # Create layout and add widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_name)
        vbox.addWidget(self.le_name)
        vbox.addWidget(self.lbl_age)
        vbox.addWidget(self.le_age)
        vbox.addWidget(self.lbl_phone)
        vbox.addWidget(self.le_phone)
        vbox.addWidget(self.lbl_weight)
        vbox.addWidget(self.le_weight)
        vbox.addWidget(self.lbl_email)
        vbox.addWidget(self.le_email)
        vbox.addWidget(self.lbl_status)
        vbox.addWidget(self.le_status)
        vbox.addWidget(self.lbl_dateOfBirth)
        vbox.addWidget(self.le_dateOfBirth)
        vbox.addWidget(self.lbl_reportDate)
        vbox.addWidget(self.lbl_reportDate)
        vbox.addWidget(self.le_Prediction)
        vbox.addWidget(self.lbl_Prediction)
        vbox.addWidget(self.btn_submit)

        self.setLayout(vbox)

        self.setWindowTitle('My Form')
        self.show()

    def submitForm(self):

        # Get values from line edits
        name = self.le_name.text()
        email = self.le_email.text()
        message = self.le_message.text()

        # Process form data here (e.g. send email, save to database, etc.)
        print('Name:', name)
        print('Email:', email)
        print('Message:', message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    sys.exit(app.exec_())
