# This Python file uses the following encoding: utf-8
import sys
import math
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget 
#from operator_number_logic import DisplayLogic, OperatorLogic
from OperationsLogic import OperationsLogic

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #self.displayn = DisplayLogic(self.ui.screennumber)  # Create an instance of the displayn class
        self.operator = OperationsLogic(self.ui.screennumber)
        
        # Number buttons routing
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
        self.ui.decimal.clicked.connect(self.decimal_clicked)
        self.ui.negative.clicked.connect(self.negative_clicked)
        self.ui.backspace.clicked.connect(self.backspace_clicked)
        
        # operator button routing
        self.ui.addition.clicked.connect(lambda: self.operator_clicked('+'))
        self.ui.subtraction.clicked.connect(lambda: self.operator_clicked('-'))
        self.ui.multiplication.clicked.connect(lambda: self.operator_clicked('*'))
        self.ui.division.clicked.connect(lambda: self.operator_clicked('/'))
        self.ui.power.clicked.connect(lambda: self.operator_clicked('**'))
        self.ui.reciprocal.clicked.connect(lambda: self.instant_operator_clicked('**-1'))
        self.ui.square.clicked.connect(lambda: self.instant_operator_clicked('**2'))
        self.ui.squareroot.clicked.connect(lambda: self.instant_operator_clicked('**0.5'))
        self.ui.percent.clicked.connect(lambda: self.instant_operator_clicked('*0.01'))
        self.ui.log.clicked.connect(lambda: self.instant_operator_clicked('log'))
        self.ui.parenthesisleft.clicked.connect(lambda: self.paranthesis_clicked('('))
        self.ui.parenthesisright.clicked.connect(lambda: self.paranthesis_clicked(')'))
        
        # Final calculations buttons routing
        self.ui.clearwork.clicked.connect(self.clearwork_clicked)
        self.ui.equalto.clicked.connect(self.equalto_clicked)
        

    
    @Slot()
    
    def number_clicked(self, num):
        self.operator.add_number(num)
        
    def decimal_clicked(self):
        self.operator.add_decimal()
    
    def backspace_clicked(self):
        self.operator.backspace()
    
    def clearwork_clicked(self):
        self.operator.clear_display()
        
    def negative_clicked(self):
        self.operator.toggle_sign()
        
    def operator_clicked(self, op):
        self.operator.enter_operator(op)
        
    def instant_operator_clicked(self, opr):
        self.operator.enter_instant_operator(opr)
        
    def paranthesis_clicked(self, parenthesis):
        self.operator.enter_parenthesis(parenthesis)
        
    def equalto_clicked(self):
        self.operator.finalize_result()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
