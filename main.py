import sys
from PyQt5.QtWidgets import (QApplication,  QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QPushButton, QGroupBox)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


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


        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()