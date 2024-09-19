import math
import random
class OperationsLogic:
    def __init__(self, display_widget):
        # Display logic attributes
        self.current_value = "0"  # Initial value of the display
        self.decimal_added = False  # Flag to track if a decimal has been added
        self.display_widget = display_widget  # Reference to the QTextEdit widget

        # Operator logic attributes
        self.current_number = "0"  # The number currently being entered
        self.expression = ""      # Full expression being built up
        self.last_result = 0      # Last computed result to display
        self.new_number = True    # Track if we are starting a new number after an operator
        self.open_parentheses = 0  # Track unbalanced opening parentheses
        self.last_key_type = None  # Track if last key was numkey or non-numkey
        
    # Properties to expose current number and result
    @property
    def current_number_value(self):
        """Provides access to the current number being entered."""
        return self.current_number or self.current_value  # Return current number or value
    
        # !!!! when coding for other worksheets, may need to add a condition to choose the string with greater lenght,
        #  because if there's a toggle sign pressed after operator key, the sign is ignored for the expression, 
        # but for a worksheet the negative sign is considered. current number and current value are the same until ..... ahh nevermind ignore, need to confirm this later.    

    @property
    def last_result_value(self):
        """Provides access to the last computed result."""
        return self.last_result

    def add_number(self, num):
        """Adds a number to the current value string or starts a new number."""
        if self.new_number:
            self.current_value = str(num)
            self.new_number = False
        else:
            if self.current_value == "0":
                self.current_value = str(num)
            else:
                self.current_value += str(num)

        self.current_number = self.current_value
        self.last_key_type = 'number'
        self.update_display()
        
    def add_decimal(self):
        """Adds a decimal point if not already present."""
        if not self.decimal_added:
            if self.new_number:
                self.current_value = "0."  # Start new number with 0.
                self.new_number = False
            else:
                self.current_value += "."
            self.decimal_added = True
        self.current_number = self.current_value
        self.last_key_type = 'number'
        self.update_display()
        
    def toggle_sign(self):
        """Toggles the sign of the current value between positive and negative."""
        if self.current_value.startswith("-"):
            self.current_value = self.current_value[1:]  # Remove the negative sign
        else:
            # Avoid adding a negative sign if the value is zero
            if self.current_value != "0":
                self.current_value = "-" + self.current_value
        self.current_number = self.current_value
        self.update_display()

    def enter_operator(self, operator):
        """Handles when an operator (+, -, *, /) is typed."""
        if self.last_key_type == 'operator':
            # Replace the last operator with the new one
            self.expression = self.expression[:-1] + operator
        else:
            # Add the current number to the expression
            if self.current_number:
                self.expression += self.current_number
                self.current_number = ""

            # Check if there are unclosed parentheses
            if self.open_parentheses > 0:
                # Evaluate only the expression within the unclosed parentheses
                inside_paren_expr = self.extract_innermost_parenthesis(self.expression)
                self.last_result = self.evaluate_expression(inside_paren_expr)
            else:
                self.last_result = self.evaluate_expression(self.expression)

            self.current_value = str(self.last_result)

            # Append the operator to the expression
            self.expression += operator

        self.new_number = True
        self.decimal_added = False
        self.last_key_type = 'operator'
        self.update_display()
        
    def enter_instant_operator(self, instant_operator):
        if instant_operator == "log":
            self.current_value = str(math.log(int(self.current_value))  )  
        elif instant_operator == "e**x":
            self.current_value = str(math.exp(int(self.current_value)))
        elif instant_operator == "rand":
            self.current_value = str(random.uniform(0, 1))
        elif instant_operator == "factorial":
            if float(self.current_value)>= 0 and float(self.current_value)<=69:
                self.current_value = str(math.factorial(int(self.current_value)))
            else:
                self.current_value = "Error"   
        else:
            self.current_value = str(eval("{num}{op}".format(num=self.current_value, op=instant_operator)))
        self.current_number = self.current_value
        self.update_display()
            
    def backspace(self):
        """Removes the last digit from the current value if the last key was a number."""
        if self.last_key_type == 'number':  # Only backspace if last key was a number
            if len(self.current_value) > 1:
                self.current_value = self.current_value[:-1]  # Remove last character
            else:
                self.current_value = "0"  # If only one digit left, reset to 0

            self.current_number = self.current_value  # Update the current number
            self.update_display()  # Update the display

    def clear_display(self):
        """Clears the display to 0 and resets the decimal flag."""
        self.current_value = "0"
        self.decimal_added = False
        self.current_number = "0"
        self.expression = ""
        self.new_number = True
        self.last_result = 0
        self.update_display()

    def enter_parenthesis(self, parenthesis):
        """Handles when '(' or ')' is typed."""
        if parenthesis == '(':
            self.open_parentheses += 1
        elif parenthesis == ')':
            if self.open_parentheses == 0:
                return  # Ignore if closing parenthesis is unmatched
            self.open_parentheses -= 1

        if self.current_number:
            self.expression += self.current_number
            self.current_number = ""

        # Add the parenthesis to the expression
        self.expression += parenthesis

        # Only evaluate when parentheses are balanced
        if self.open_parentheses == 0 and parenthesis == ')':
            self.last_result = self.evaluate_smallest_parenthesis(self.expression)
            self.current_value = str(self.last_result)
            self.new_number = True

        self.update_display()

    def extract_innermost_parenthesis(self, expr):
        """Extract the innermost unclosed parenthesis for evaluation."""
        try:
            open_index = expr.rfind('(')  # Find the last opened '('
            return expr[open_index + 1:]  # Return everything inside the innermost parentheses
        except ValueError:
            return expr

    def evaluate_expression(self, expr):
        """Evaluate the expression handling BODMAS, return the result."""
        try:
            return eval(expr)
        except Exception:
            return "Error"

    def evaluate_smallest_parenthesis(self, expr):
        """Evaluate and return the result of the smallest solvable parenthesis."""
        try:
            while '(' in expr and ')' in expr:
                expr = str(eval(expr))  # Evaluate the innermost parentheses
            return eval(expr)  # Evaluate the remaining expression
        except Exception:
            return "Error"
        
    def finalize_result(self):
        """Finalize the result when = is pressed."""
        if self.current_number:
            self.expression += self.current_number  # Add the last entered number

        # Automatically close any unclosed parentheses
        self.expression += ')' * self.open_parentheses
        self.open_parentheses = 0  # Reset parentheses count after finalizing

        # Evaluate the complete expression
        result = self.evaluate_expression(self.expression)
        self.current_value = str(result)  # Update display with final result

        # Reset expression after showing result
        self.expression = ""
        self.current_number = str(result)  # Current number becomes the result for further calculations
        self.last_result = result
        self.new_number = True
        self.decimal_added = False

        self.update_display()

    def update_display(self):
        """Updates the display widget with the current value."""
        self.display_widget.setText(self.current_value)
        
