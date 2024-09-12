# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget 
from displaylogic import DisplayLogic

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.displayn = DisplayLogic(self.ui.textEditNumber)  # Create an instance of the displayn class

        # Connect buttons to their respective slots
        self.ui.number0.clicked.connect(lambda: self.number_clicked(0))
        self.ui.number1.clicked.connect(lambda: self.number_clicked(1))
        self.ui.number2.clicked.connect(lambda: self.number_clicked(2))
        self.ui.number3.clicked.connect(lambda: self.number_clicked(3))
        self.ui.number4.clicked.connect(lambda: self.number_clicked(4))
        self.ui.number5.clicked.connect(lambda: self.number_clicked(5))
        self.ui.number6.clicked.connect(lambda: self.number_clicked(6))
        self.ui.number7.clicked.connect(lambda: self.number_clicked(7))
        self.ui.number8.clicked.connect(lambda: self.number_clicked(8))
        self.ui.number9.clicked.connect(lambda: self.number_clicked(9))

        # Connect decimal and clear negative buttons
        self.ui.decimal.clicked.connect(self.decimal_clicked)
        self.ui.clearwork.clicked.connect(self.clearwork_clicked)
        self.ui.negative.clicked.connect(self.negative_clicked)

    
    @Slot()
    
    def number_clicked(self, num):
        self.displayn.add_number(num)
        
    def decimal_clicked(self):
        self.displayn.add_decimal()
        
    def clearwork_clicked(self):
        self.displayn.clear_display()
        
    def negative_clicked(self):
        self.displayn.toggle_sign()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
