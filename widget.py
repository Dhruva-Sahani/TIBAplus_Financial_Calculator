# This Python file uses the following encoding: utf-8
import sys
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
        self.operator = OperationsLogic(self.ui.screennumber) #Create an instance of operationslogic class
        self.secondflag = False
        
        #region Number buttons routing
        self.ui.number0.clicked.connect(lambda: self.number0_clicked())
        self.ui.number1.clicked.connect(lambda: self.number1_clicked())
        self.ui.number2.clicked.connect(lambda: self.number2_clicked())
        self.ui.number3.clicked.connect(lambda: self.number3_clicked())
        self.ui.number4.clicked.connect(lambda: self.number4_clicked())
        self.ui.number5.clicked.connect(lambda: self.number5_clicked())
        self.ui.number6.clicked.connect(lambda: self.number6_clicked())
        self.ui.number7.clicked.connect(lambda: self.number7_clicked())
        self.ui.number8.clicked.connect(lambda: self.number8_clicked())
        self.ui.number9.clicked.connect(lambda: self.number9_clicked())
        self.ui.decimal.clicked.connect(lambda: self.decimal_clicked())
        self.ui.negative.clicked.connect(lambda: self.negative_clicked())
        self.ui.backspace.clicked.connect(lambda: self.backspace_clicked())
        #endregion
        
        #region operator buttons routing
        self.ui.addition.clicked.connect(lambda: self.addition_clicked())
        self.ui.subtraction.clicked.connect(lambda: self.subtraction_clicked())
        self.ui.multiplication.clicked.connect(lambda: self.multiplication_clicked())
        self.ui.division.clicked.connect(lambda: self.division_clicked())
        self.ui.power.clicked.connect(lambda: self.power_clicked())
        self.ui.reciprocal.clicked.connect(lambda: self.reciprocal_clicked())
        self.ui.square.clicked.connect(lambda: self.square_clicked())
        self.ui.squareroot.clicked.connect(lambda: self.squareroot_clicked())
        self.ui.percent.clicked.connect(lambda: self.percent_clicked())
        self.ui.log.clicked.connect(lambda: self.log_clicked())
        self.ui.parenthesisleft.clicked.connect(lambda: self.left_parenthesis_clicked())
        self.ui.parenthesisright.clicked.connect(lambda: self.right_parenthesis_clicked())
        self.ui.inverse.clicked.connect(lambda: self.inv_clicked())
        #endregion
        
        #region Refresh buttons routing
        self.ui.clearwork.clicked.connect(lambda: self.clearwork_clicked())
        self.ui.equalto.clicked.connect(lambda: self.equalto_clicked())
        #endregion
        
        #region High level buttons routing
        self.ui.second.clicked.connect(lambda: self.second_clicked())
        #endregion

    """ Slots for all the buttons are defined below. 
    Buttons without a second functions and similar funcionality may have a mutual functions."""  
    @Slot()
    
    #region number
    def number0_clicked(self):
        self.operator.add_number(0)
    
    def number1_clicked(self):
        self.operator.add_number(1)
        
    def number2_clicked(self):
        self.operator.add_number(2)
        
    def number3_clicked(self):
        self.operator.add_number(3)
        
    def number4_clicked(self):
        self.operator.add_number(4)
        
    def number5_clicked(self):
        self.operator.add_number(5)
        
    def number6_clicked(self):
        self.operator.add_number(6)
        
    def number7_clicked(self):
        self.operator.add_number(7)
        
    def number8_clicked(self):
        self.operator.add_number(8)
        
    def number9_clicked(self):
        self.operator.add_number(9)
    
    def decimal_clicked(self):
        self.operator.add_decimal()
    
    def negative_clicked(self):
        # if self.secondflag:
            
        #     self.secondflag = False
        self.operator.toggle_sign()
        
    def backspace_clicked(self):
        self.operator.backspace()
    #endregion
    
    #region operators    
    def addition_clicked(self):
        if self.secondflag:
            self.operator.percomb_operation('comb')  
            self.secondflag = False
        else:  
            self.operator.enter_operator('+')
        
    def subtraction_clicked(self):
        if self.secondflag:
            self.operator.percomb_operation('perm')
            self.secondflag = False
        else:
            self.operator.enter_operator('-')
        
    def multiplication_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator("factorial")
            self.secondflag = False
        else:
            self.operator.enter_operator('*')
        
    def division_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator("rand")
            self.secondflag = False
        else:
            self.operator.enter_operator('/')
        
    def power_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator('tan')
            self.secondflag = False
        else:
            self.operator.enter_operator('**')
        
    def reciprocal_clicked(self):
        self.operator.enter_instant_operator('**-1')
        
    def square_clicked(self):
        self.operator.enter_instant_operator('**2')
        
    def squareroot_clicked(self):
        self.operator.enter_instant_operator('**0.5')
        
    def percent_clicked(self):
        self.operator.enter_instant_operator('*0.01')
        
    def log_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator("e**x")
            self.secondflag = False
        else:
            self.operator.enter_instant_operator('log')
            
    def inv_clicked(self):
        if self.secondflag:
            self.operator.inv("hyp")
            self.secondflag = False
        else:
            self.operator.inv("inv")
        
    def left_parenthesis_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator('sin')
            self.secondflag = False
        else:
            self.operator.enter_parenthesis("(")
            
    def right_parenthesis_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator('cos')
            self.secondflag = False
        else:
            self.operator.enter_parenthesis(")")
        
    #endregion
    
    #region refresh    
    def clearwork_clicked(self):
        self.operator.clear_display()
        
    def equalto_clicked(self):
        self.operator.finalize_result()
    #endregion
    
    #region highlevel   
    def second_clicked(self):
        self.secondflag = True
    #endregion
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
