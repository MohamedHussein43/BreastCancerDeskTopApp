import sys


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizePolicy
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtWidgets

app = QApplication(sys.argv)
layout = QVBoxLayout()
widget = QtWidgets.QStackedWidget()

welcome = loadUi("../View/welcomescreen.ui")
size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
welcome.setSizePolicy(size_policy)
layout.addWidget(welcome)
widget.addWidget(welcome)
widget.setWindowTitle("Breast Cancer Detection")


widget.setWindowIcon(QIcon('pink-ribbon.png'))
widget.setWindowFlags(Qt.WindowMinMaxButtonsHint |Qt.WindowCloseButtonHint )


widget.sizeHint()
widget.show()
sys.exit(app.exec_())