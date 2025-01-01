import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

from sqlalchemy import create_engine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("penis balls")
        x= 30
        y= 40
        width = 1000
        height = 1000
        self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("imij.jpg"))
        #self.initUI()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        group1 = QGroupBox("Score", central_widget)
        group1.setGeometry(0, 0, 499, 499)
        group2 = QGroupBox("Daily progress", central_widget)
        group2.setGeometry(0, 501, 499, 499)
        group3 = QGroupBox("History", central_widget)
        group3.setGeometry(501, 0, 499, 499)
        group4 = QGroupBox("Settings", central_widget)
        group4.setGeometry(501, 501, 499, 499)

        scoreLayout = QGridLayout()

        Lname = QLabel("name: ")
        self.Iname = QLineEdit()
        Lage = QLabel("Age: ")
        self.Iage = QLineEdit()
        btnSubmit = QPushButton("Submit")

        btnSubmit.clicked.connect(self.funcSubmit)

        scoreLayout.addWidget(Lname, 0, 0)
        scoreLayout.addWidget(self.Iname, 0, 1)
        scoreLayout.addWidget(Lage, 1, 0)
        scoreLayout.addWidget(self.Iage, 1, 1)
        scoreLayout.addWidget(btnSubmit, 2, 0, 1,2)

        group1.setLayout(scoreLayout)
        
    def funcSubmit(self):
        print("CUM")
        txtName = self.Iname.text()
        print(txtName)
        