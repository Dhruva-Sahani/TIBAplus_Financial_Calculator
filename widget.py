# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget 
from operator_number_logic import DisplayLogic, OperatorLogic

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.displayn = DisplayLogic(self.ui.screennumber)  # Create an instance of the displayn class
        self.operator = OperatorLogic(self.ui.screennumber)
        
        # Number button routing
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
        
        # operator button routing
        self.ui.addition.clicked.connect(lambda: self.operator_clicked('+'))
        self.ui.subtraction.clicked.connect(lambda: self.operator_clicked('-'))
        self.ui.multiplication.clicked.connect(lambda: self.operator_clicked('*'))
        self.ui.division.clicked.connect(lambda: self.operator_clicked('/'))
        self.ui.parenthesisleft.clicked.connect(lambda: self.paranthesis_clicked('('))
        self.ui.parenthesisright.clicked.connect(lambda: self.paranthesis_clicked(')'))
        
        # Final calculations buttons routing
        self.ui.clearwork.clicked.connect(self.clearwork_clicked)
        self.ui.equalto.clicked.connect(self.equalto_clicked)
        

    
    @Slot()
    
    def number_clicked(self, num):
        self.displayn.add_number(num)
        self.operator.enter_number(num)
        
    def decimal_clicked(self):
        self.displayn.add_decimal() 
        self.operator.enter_decimal()
        
    def clearwork_clicked(self):
        self.displayn.clear_display()
        self.operator.clear()
        
    def negative_clicked(self):
        self.displayn.toggle_sign()
        self.operator.toggle_sign()
        
    def operator_clicked(self, op):
        self.operator.enter_operator(op)
        
    def paranthesis_clicked(self, parenthesis):
        self.operator.enter_parenthesis(parenthesis)
        
    def equalto_clicked(self):
        self.operator.finalize_result()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
