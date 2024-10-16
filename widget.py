# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget 
# importing all the classes for the different worksheets
from OperationsLogic import OperationsLogic
from Settings import Settings
from TimeValueOfMoney import TimeValueOfMoney
from CashFlow import CashFlow, CashFlowReturns

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.operator = OperationsLogic(self.ui.screennumber) #Create an instance of operationslogic class
        self.setting = Settings(self.ui.screennumber, self.ui.screenletter)
        self.timevalueofmoney = TimeValueOfMoney(self.ui.screennumber, self.ui.screenletter)
        self.cashflow = CashFlow(self.ui.screennumber, self.ui.screenletter)
        self.cashflowreturns = CashFlowReturns(self.ui.screennumber, self.ui.screenletter)
        self.worksheetflag = None
        self.secondflag = False
        self.activekeyclass = None
        self.clrdisplay2flag = False
        self.compute_flag = False
        
        """ Slot and signals for all buttons implemented below"""
        """ Avoid passing any argument while calling a slot"""
        
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
        self.ui.up.clicked.connect(lambda: self.up_clicked())
        self.ui.down.clicked.connect(lambda: self.down_clicked())
        self.ui.enter.clicked.connect(lambda: self.enter_clicked())
        self.ui.compute.clicked.connect(lambda: self.compute_clicked())
        #endregion
        
        #region time value of money buttons routing
        self.ui.period.clicked.connect(lambda: self.period_clicked())
        self.ui.interestrate.clicked.connect(lambda: self.interestrate_clicked())
        self.ui.presentvalue.clicked.connect(lambda: self.presentvalue_clicked())
        self.ui.payment.clicked.connect(lambda: self.payment_clicked())
        self.ui.futurevalue.clicked.connect(lambda: self.futurevalue_clicked())
        #endregion
        
        #region cashflow buttons routing
        self.ui.cashflow.clicked.connect(lambda: self.cashflow_clicked())
        self.ui.netpresentvalue.clicked.connect(lambda: self.netpresentvalue_clicked())
        self.ui.internalratereturn.clicked.connect(lambda: self.internalratereturn_clicked())

    """ Slots for all the buttons are defined below. """
    """ Functions are named and categorised according to the primary action of the buttons """
    """ Buttons without a second functions and similar funcionality may have a mutual functions."""  
    
    @Slot()
    
    #region number
    def number0_clicked(self):
        self.operator.add_number(0)
        self.display2clear()
    
    def number1_clicked(self):
        self.operator.add_number(1)
        self.display2clear()
        
    def number2_clicked(self):
        self.operator.add_number(2)
        self.display2clear()
        
    def number3_clicked(self):
        self.operator.add_number(3)
        self.display2clear()
        
    def number4_clicked(self):
        self.operator.add_number(4)
        self.display2clear()
        
    def number5_clicked(self):
        self.operator.add_number(5)
        self.display2clear()
        
    def number6_clicked(self):
        self.operator.add_number(6)
        self.display2clear()
        
    def number7_clicked(self):
        self.operator.add_number(7)
        self.display2clear()
        
    def number8_clicked(self):
        self.operator.add_number(8)
        self.display2clear()
        
    def number9_clicked(self):
        self.operator.add_number(9)
        self.display2clear()
    
    def decimal_clicked(self):
        if self.secondflag:
            self.worksheetflag = self.setting
            self.setting.display_current_key()
            self.activekeyclass = "Setting"
            self.secondflag = False
        else:
            self.operator.add_decimal()
            self.display2clear()
    
    def negative_clicked(self):
        if self.secondflag:
            self.worksheetflag = self.setting
            self.setting.reset_activate()
            self.secondflag = False
        else:
            self.operator.toggle_sign()
            self.display2clear()
        
    def backspace_clicked(self):
        self.operator.backspace()
    #endregion
    
    #region operators    
    def addition_clicked(self):
        if self.secondflag:
            self.operator.percomb_operation('comb')  
            self.display2clear()
            self.secondflag = False
        else:  
            self.operator.enter_operator('+')
            self.display2clear()
        
    def subtraction_clicked(self):
        if self.secondflag:
            self.operator.percomb_operation('perm')
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_operator('-')
            self.display2clear()
        
    def multiplication_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator("factorial")
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_operator('*')
            self.display2clear()
        
    def division_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator("rand")
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_operator('/')
            self.display2clear()
        
    def power_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator('tan')
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_operator('**')
            self.display2clear()
        
    def reciprocal_clicked(self):
        self.operator.enter_instant_operator('**-1')
        self.display2clear()
        
    def square_clicked(self):
        self.operator.enter_instant_operator('**2')
        self.display2clear()
        
    def squareroot_clicked(self):
        self.operator.enter_instant_operator('**0.5')
        self.display2clear()
        
    def percent_clicked(self):
        self.operator.enter_instant_operator('*0.01')
        self.display2clear()
        
    def log_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator("e**x")
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_instant_operator('log')
            self.display2clear()
            
    def inv_clicked(self):
        if self.secondflag:
            self.operator.inv("hyp")
            self.secondflag = False
        else:
            self.operator.inv("inv")
        
    def left_parenthesis_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator('sin')
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_parenthesis("(")
            self.display2clear()
            
    def right_parenthesis_clicked(self):
        if self.secondflag:
            self.operator.enter_instant_operator('cos')
            self.display2clear()
            self.secondflag = False
        else:
            self.operator.enter_parenthesis(")")
            self.display2clear()
        
    #endregion
    
    #region refresh    
    def clearwork_clicked(self):
        if self.secondflag:
            self.worksheetflag.clear_work(self.activekeyclass)
            self.secondflag = False
        else:
            self.operator.clear_display()
            self.ui.screenletter.setText("")
            self.display2clear
        
    def equalto_clicked(self):
        self.operator.finalize_result()
        self.display2clear()
    #endregion
    
    #region highlevel   
    def second_clicked(self):
        self.secondflag = True
        
    def up_clicked(self):
        if self.worksheetflag!= None:
            self.worksheetflag.move_up()
            self.operator.new_number = True
            
    def down_clicked(self):
        if self.worksheetflag!= None:
            self.worksheetflag.move_down()
            self.operator.new_number = True
            
    def enter_clicked(self):
        self.thenumber =  self.operator.current_number_value
        if self.secondflag:
            if self.worksheetflag != None:
                self.worksheetflag.set()
            self.secondflag = False
        else: 
            if self.worksheetflag != None:
                self.worksheetflag.enter(self.thenumber)
                self.operator.new_number = True
            
    def compute_clicked(self):
        if self.secondflag:
            self.operator.clear_display()
            self.ui.screenletter.setText("")
            self.worksheetflag = None
            self.secondflag = False
            self.setting.__init__(self.ui.screennumber, self.ui.screenletter)
        else:
            if hasattr(self.worksheetflag, 'calculate_instant'):
                self.worksheetflag.calculate_instant()
            else:
                self.compute_flag = True
            
    #endregion
    
    #region timevalueofmoney
    def period_clicked(self):
        if self.compute_flag:
            self.timevalueofmoney.calculation('N')
            self.worksheetflag = self.timevalueofmoney
            self.compute_flag = False
        else:
            self.timevalueofmoney.tvm('N', self.operator.current_number_value)
            self.operator.new_number = True
            self.clrdisplay2flag = True
            self.worksheetflag = self.timevalueofmoney
            self.activekeyclass = 'TVM'
        
    def interestrate_clicked(self):
        if self.secondflag:
            self.timevalueofmoney.paymentperyear()
            self.worksheetflag = self.timevalueofmoney
            self.activekeyclass = 'P_Y'
            self.secondflag = False
        else:
            if self.compute_flag:
                self.timevalueofmoney.calculation('I_Y')
                self.worksheetflag = self.timevalueofmoney
                self.compute_flag = False
                self.clrdisplay2flag = True
            else:
                self.timevalueofmoney.tvm('I_Y', self.operator.current_number_value)
                self.worksheetflag = self.timevalueofmoney
                self.operator.new_number = True
                self.clrdisplay2flag = True
                self.activekeyclass = 'TVM'
        
    def presentvalue_clicked(self):
        if self.compute_flag:
            self.timevalueofmoney.calculation('PV')
            self.worksheetflag = self.timevalueofmoney
            self.compute_flag = False
            self.clrdisplay2flag = True
        else:
            self.timevalueofmoney.tvm('PV', self.operator.current_number_value)
            self.worksheetflag = self.timevalueofmoney
            self.operator.new_number = True
            self.clrdisplay2flag = True
            self.activekeyclass = 'TVM'
        
    def payment_clicked(self):
        if self.secondflag:
            self.timevalueofmoney.payment_mode()
            self.worksheetflag = self.timevalueofmoney
            self.activekeyclass = 'Payment_Mode'
            self.secondflag = False
        else:
            if self.compute_flag:
                self.timevalueofmoney.calculation('PMT')
                self.worksheetflag = self.timevalueofmoney
                self.compute_flag = False
                self.clrdisplay2flag = True
            else:
                self.timevalueofmoney.tvm('PMT', self.operator.current_number_value)
                self.worksheetflag = self.timevalueofmoney
                self.operator.new_number = True
                self.clrdisplay2flag = True
                self.activekeyclass = 'TVM'
        
    def futurevalue_clicked(self):
        if self.secondflag:
            self.timevalueofmoney.clear_tvm()
            if self.activekeyclass == 'TVM':
                self.ui.screenletter.setText("")
            self.secondflag = False
        else:
            if self.compute_flag:
                self.timevalueofmoney.calculation('FV')
                self.worksheetflag = self.timevalueofmoney
                self.clrdisplay2flag = True
                self.compute_flag = False
            else:
                self.timevalueofmoney.tvm('FV', self.operator.current_number_value)
                self.worksheetflag = self.timevalueofmoney
                self.operator.new_number = True
                self.clrdisplay2flag = True
                self.activekeyclass = 'TVM'
    #endregion
    
    #region cashflow
    def cashflow_clicked(self):
        self.cashflow.cashflow()
        self.worksheetflag = self.cashflow
        
    def netpresentvalue_clicked(self):
        self.cashflowreturns.npv()
        self.worksheetflag = self.cashflowreturns
        
    def internalratereturn_clicked(self):
        self.cashflowreturns.irr()
        self.worksheetflag = self.cashflowreturns
       
    #endregion
       
        
    def display2clear(self):
        if self.clrdisplay2flag:
            self.ui.screenletter.setText('')
            self.clrdisplay2flag = False
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
