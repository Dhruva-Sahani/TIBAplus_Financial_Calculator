import math
import random
import re
from BehaviorNavigation import Settings


class OperationsLogic:
    def __init__(self, display_widget):
        self.settings= Settings() #Creating instance of settings class
        
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

    #region number edits
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
    
    def backspace(self):
        """Removes the last digit from the current value if the last key was a number."""
        if self.last_key_type == 'number':  # Only backspace if last key was a number
            if len(self.current_value) > 1:
                self.current_value = self.current_value[:-1]  # Remove last character
            else:
                self.current_value = "0"  # If only one digit left, reset to 0

            self.current_number = self.current_value  # Update the current number
            self.update_display()  # Update the display
    #endregion 
    
    #region operators
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

            # Handle open parentheses: only evaluate the innermost parenthesis
            if self.open_parentheses > 0:
                inside_paren_expr = self.extract_innermost_parenthesis(self.expression)
                self.last_result = self.evaluate_expression(inside_paren_expr)
                self.current_value = str(self.last_result)
            else:
                # Evaluate based on operator precedence
                if operator in ['*', '/']:
                    # For *, /: show partial result only for the * / expression part
                    last_high_precedence_expr = self.extract_last_high_precedence_expression(self.expression)
                    self.last_result = self.evaluate_expression(last_high_precedence_expr)
                    self.current_value = str(self.last_result)
                elif operator in ['+', '-']:
                    # For +, -: evaluate the entire expression so far and display result
                    self.last_result = self.evaluate_expression(self.expression)
                    self.current_value = str(self.last_result)

            # Append the operator to the expression
            self.expression += operator

        self.new_number = True
        self.decimal_added = False
        self.last_key_type = 'operator'
        self.update_display()


    def extract_last_high_precedence_expression(self, expr):
        """
        Extracts the last segment of the expression involving only higher precedence operators (* or /),
        stopping at the last occurrence of + or -.
        """
        try:
            # Find the last index of + or - to split the expression
            last_low_precedence_index = max(expr.rfind('+'), expr.rfind('-'))
            if last_low_precedence_index == -1:
                # If no + or - found, return the entire expression
                return expr
            else:
                # Return only the part after the last + or - (to handle * /)
                return expr[last_low_precedence_index + 1:]
        except ValueError:
            return expr  # In case of error, return the whole expression
        
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
    #endregion    

    #region parenthesis behaviors
    def enter_parenthesis(self, parenthesis):
        """Handles when '(' or ')' is typed."""
        if parenthesis == '(':
            self.open_parentheses += 1
        elif parenthesis == ')':
            if self.open_parentheses == 0:
                return  # Ignore if closing parenthesis is unmatched
            self.open_parentheses -= 1

        # Append current number to expression if there is one
        if self.current_number:
            self.expression += self.current_number
            self.current_number = ""

        # Add the parenthesis to the expression
        self.expression += parenthesis

        # Only evaluate when parentheses are balanced and a closing parenthesis is typed
        if parenthesis == ')' and self.open_parentheses == 0:
            # Extract and evaluate the expression within parentheses
            inside_paren_expr = self.extract_innermost_parenthesis(self.expression)
            self.last_result = self.evaluate_expression(inside_paren_expr)
            self.current_value = str(self.last_result)
            self.new_number = True

        self.update_display()

    def extract_innermost_parenthesis(self, expr):
        """Extract the innermost unclosed parenthesis for evaluation."""
        try:
            open_index = expr.rfind('(')  # Find the last opened '('
            close_index = expr.find(')', open_index)  # Find the corresponding closing ')'
            if close_index == -1:
                # Handle the case where there's no closing parenthesis yet
                return expr[open_index + 1:]
            return expr[open_index + 1:close_index]  # Return everything inside the innermost parentheses
        except ValueError:
            return expr  # If no parentheses, return the whole expression
        
    # def evaluate_smallest_parenthesis(self, expr):
    #     """Evaluate and return the result of the smallest solvable parenthesis."""
    #     try:
    #         while '(' in expr and ')' in expr:
    #             expr = str(eval(expr))  # Evaluate the innermost parentheses
    #         return eval(expr)  # Evaluate the remaining expression
    #     except Exception:
    #         return "Error small"
    #endregion
    
    #region evaluation
    def evaluate_expression(self, expr):
        """Evaluate the expression based on the selected method in settings."""
        method = self.settings.read_setting("calculation_method")
        if method == 'AoS':
            return self.evaluate_algebraic(expr)
        elif method == 'Chn':
            return self.evaluate_chain_value(expr)

    def evaluate_algebraic(self, expr):
        """Evaluate the expression using BODMAS (default algebraic)."""
        try:
            return eval(expr)  # Default BODMAS handling
        except Exception:
            return "Error evalag"

    def evaluate_chain_value(self, expr):
        """Evaluate the expression in chain-value method (left-to-right, no precedence) while handling parentheses."""
        try:
            # Ensure parentheses are balanced
            if expr.count('(') != expr.count(')'):
                return "Error: Unbalanced parentheses"

            # First, handle parentheses: evaluate innermost parentheses first
            while '(' in expr:
                # Find the innermost parenthesis
                open_index = expr.rfind('(')
                close_index = expr.find(')', open_index)
                
                if close_index == -1:
                    return "Error: Unbalanced parentheses"
                
                # Extract the expression inside the innermost parenthesis
                inner_expr = expr[open_index + 1:close_index]
                
                # Recursively evaluate the expression inside the parentheses
                inner_result = self.evaluate_chain_value(inner_expr)
                
                # Replace the parenthesized part with its result
                expr = expr[:open_index] + str(inner_result) + expr[close_index + 1:]
            
            # Now, we are left with an expression without parentheses, so split and calculate left to right
            tokens = re.split(r'(\D)', expr)  # Split by any non-digit character (operator)
            
            # Initialize result with the first number
            result = float(tokens.pop(0))
            
            # Iterate through the remaining tokens and apply operators left-to-right
            while tokens:
                operator = tokens.pop(0)
                if tokens:
                    next_number = float(tokens.pop(0))
                    
                    if operator == '+':
                        result += next_number
                    elif operator == '-':
                        result -= next_number
                    elif operator == '*':
                        result *= next_number
                    elif operator == '/':
                        result /= next_number  # Handle division by zero if necessary

            return result
        
        except Exception as e:
            return f"Error: {str(e)}"
    #endregion
    
    #region cleanscreen
    def clear_display(self):
        """Clears the display to 0 and resets the decimal flag."""
        self.current_value = "0"
        self.decimal_added = False
        self.current_number = "0"
        self.expression = ""
        self.new_number = True
        self.last_result = 0
        self.update_display()
        
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
    #endregion

    #region display
    def update_display(self):
        """Updates the display widget with the current value."""
        self.display_widget.setText(self.current_value)
    #endregion
    
