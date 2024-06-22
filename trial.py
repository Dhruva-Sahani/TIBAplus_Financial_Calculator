from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("Clicked")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,100, 600, 300)
    win.setWindowTitle("Texas Instruments BA Plus Financial Calculator")
    
    lable =QtWidgets.QLabel(win)
    lable.setText("My first lable")
    lable.move(20,45)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


window()