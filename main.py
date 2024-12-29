import sys
from PyQt5.QtWidgets import (QApplication,  QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QPushButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("penis balls")
        x= 100
        y= 100
        width = 500
        height = 500
        self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("imij.jpg"))
        self.initUI()
        #label = QLabel("yeetSkeet", self)
        #label.setFont(QFont("Arial", 30))
        #label.setGeometry(100, 0, 300, 100)
        #label.setStyleSheet("color: blue;"
          #                  "background-color: red;"
          #                  "font-weight: bold;"
          #                  "font-Style: italic;"
          #                  "text-decoration: underline")
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )

        #label2 = QLabel("tits", self)
        #label2.setGeometry(125, 125, 250, 250)
        #label2.setStyleSheet("background-color: purple;")

        #pixmap = QPixmap("imij.jpg")
        #label2.setPixmap(pixmap)
        #label2.setScaledContents(True)

    #def initUI(self):
        #self.button = QPushButton("Click me!", self)
        #self.button.setGeometry(150, 200, 200, 100)
        #self.button.setStyleSheet("font-size: 30px")
        #self.button.clicked.connect(self.on_click)

    #def on_click(self):
        #print("Button clicked")
        #self.button.setText("CUNT")

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()