class DisplayLogic:
    def __init__(self, display_widget):
        self.current_value = "0"  # Initial value of the display
        self.decimal_added = False  # Flag to track if a decimal has been added
        self.display_widget = display_widget  # Reference to the QTextEdit widget

    def add_number(self, num):
        """Adds a number to the current value string."""
        if self.current_value == "0":
            self.current_value = str(num)
        else:
            self.current_value += str(num)
        self.update_display()

    def add_decimal(self):
        """Adds a decimal point if not already present."""
        if not self.decimal_added:
            self.current_value += "."
            self.decimal_added = True
        self.update_display()
        
    def toggle_sign(self):
        """Toggles the sign of the current value between positive and negative."""
        if self.current_value.startswith("-"):
            self.current_value = self.current_value[1:]  # Remove the negative sign
        else:
            # Avoid adding a negative sign if the value is zero
            if self.current_value != "0":
                self.current_value = "-" + self.current_value
        self.update_display()

    def clear_display(self):
        """Clears the display to 0 and resets the decimal flag."""
        self.current_value = "0"
        self.decimal_added = False
        self.update_display()

    def update_display(self):
        """Updates the QTextEdit with the current display value."""
        self.display_widget.setText(self.current_value)


class OperatorLogic:
    def __init__(self, display_widget):
        self.current_number = ""  # The number currently being entered
        self.expression = ""      # Full expression being built up
        self.last_result = 0      # Last computed result to display
        self.display_widget = display_widget
        
    def enter_number(self, number):
        """Handles when a number is typed."""
        self.current_number += str(number)
        
    def enter_decimal(self):
        """Handles when the decimal point (.) is typed."""
        if not self.decimal_added:
            if not self.current_number:
                # If no number is entered yet, start with '0.'
                self.current_number = "0."
            else:
                self.current_number += "."
            self.decimal_added = True  # Mark that decimal has been added

    def toggle_sign(self):
        """Handles when the +/- button is pressed to toggle negative/positive."""
        if self.current_number.startswith("-"):
            self.current_number = self.current_number[1:]  # Remove negative sign
        else:
            self.current_number = "-" + self.current_number  # Add negative sign

    def enter_operator(self, operator):
        """Handles when an operator (+, -, *, /) is typed."""
        if self.current_number:
            self.expression += self.current_number
            self.current_number = ""  # Reset the current number after adding it to expression

        # Display the result based on operator precedence
        if operator in ("*", "/"):
            self.last_result = self.evaluate_expression(self.expression)  # Solve multiplication/division first
        elif operator in ("+", "-"):
            # Display result for addition/subtraction (considering BODMAS)
            self.last_result = self.evaluate_lowest_precedence(self.expression)
        else:
            return "Invalid Operator"

        # Add the operator to the expression
        self.expression += operator
        self.update_display()

    def enter_parenthesis(self, parenthesis):
        """Handles when '(' or ')' is typed."""
        if self.current_number:
            self.expression += self.current_number
            self.current_number = ""
        
        # Add the parenthesis to the expression
        self.expression += parenthesis
        
        # Display the smallest solvable parentheses result
        self.last_result = self.evaluate_smallest_parenthesis(self.expression)
        self.update_display()

    def evaluate_expression(self, expr):
        """Evaluate the expression handling BODMAS, return the result."""
        try:
            return eval(expr)  # Python's eval handles BODMAS and parentheses automatically
        except Exception:
            return "Error"

    def evaluate_lowest_precedence(self, expr):
        """Evaluate only low precedence operators like + and -."""
        try:
            # Here we split based on + and - only, ignoring * and /
            return eval(expr)  # eval handles the order of operations internally
        except Exception:
            return "Error"

    def evaluate_smallest_parenthesis(self, expr):
        """Evaluate and return the result of the smallest solvable parenthesis."""
        try:
            while '(' in expr and ')' in expr:
                # Evaluate the innermost parenthesis first
                expr = eval(expr)
            return eval(expr)
        except Exception:
            return "Error"

    def finalize_result(self):
        """Finalize the result when = is pressed."""
        if self.current_number:
            self.expression += self.current_number  # Add last entered number

        # Evaluate the complete expression
        result = self.evaluate_expression(self.expression)
        str_result = str(result)
        # Reset expression and current number after showing result
        self.expression = ""
        self.current_number = ""
        self.last_result = 0

        self.display_widget.setText(str_result)
        

    def clear(self):
        """Clears the current state (useful for clear or reset)."""
        self.current_number = ""
        self.expression = ""
        self.last_result = 0
        
    def update_display(self):
        """Updates the QTextEdit with the current display value."""
        str_last_result = str(self.last_result)
        self.display_widget.setText(str_last_result)


# # Example usage
# calc = CalculatorLogic()

# # Simulating typing numbers and operators
# calc.enter_number(5)              # Entering 5
# print(calc.enter_operator("+"))   # After +, should display 5
# calc.enter_number(10)             # Entering 10
# print(calc.enter_operator("*"))   # After *, result should be 10 (since 10* follows BODMAS)
# calc.enter_number(2)              # Entering 2
# print(calc.enter_operator("+"))   # After +, result should be 20 (10 * 2)
# calc.enter_number(5)              # Entering 5
# print(calc.finalize_result())     # Pressing =, final result should be 25 (20 + 5)
