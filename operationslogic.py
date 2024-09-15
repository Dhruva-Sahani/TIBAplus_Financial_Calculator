class operationslogic:
    def __init__(self, display_widget):
        # Display logic attributes
        self.current_value = "0"  # Initial value of the display
        self.decimal_added = False  # Flag to track if a decimal has been added
        self.display_widget = display_widget  # Reference to the qlineedit widget

        # Operator logic attributes
        self.current_number = ""  # The number currently being entered. Use this for all on screen number calculation functions eg. exponential, inverse, log etc.
        self.expression = ""      # Full expression being built up
        self.last_result = 0      # Last computed result to display
        self.new_number = True    # Track if we are starting a new number after an operator
        self.open_parentheses = 0 # Track unbalanced opening parentheses
    
    # Properties to expose current number and result
    @property
    def current_number_value(self):
        """Provides access to the current number being entered."""
        return self.current_number or self.current_value  # Return current number or value

    @property
    def last_result_value(self):
        """Provides access to the last computed result."""
        return self.last_result

    # Display Logic Methods
    def add_number(self, num):
        """Adds a number to the current value string or starts a new number."""
        if self.new_number:
            self.current_value = str(num)
            self.new_number = False  # We are now editing the current number
        else:
            if self.current_value == "0":
                self.current_value = str(num)
            else:
                self.current_value += str(num)
        
        self.current_number = self.current_value  # Set current number
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

    def clear_display(self):
        """Clears the display to 0 and resets the decimal flag."""
        self.current_value = "0"
        self.decimal_added = False
        self.current_number = ""
        self.expression = ""
        self.new_number = True
        self.last_result = 0
        self.update_display()

    # Operator Logic Methods
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

        self.expression += operator  # Add operator to expression
        self.current_value = str(self.last_result)  # Update display with result
        self.new_number = True  # The next number should be a new number
        self.decimal_added = False  # Reset decimal flag
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
            self.new_number = True  # After closing a parenthesis, expect new input
        
        self.update_display()

    def finalize_result(self):
        """Finalize the result when = is pressed."""
        if self.current_number:
            self.expression += self.current_number  # Add last entered number

        # Evaluate the complete expression
        result = self.evaluate_expression(self.expression)
        self.current_value = str(result)  # Update display with final result

        # Reset expression after showing result
        self.expression = ""
        self.current_number = str(result)  #current number becomes the result or else next equal to or operator press would result in an error. Loop of calculations wont be possible
        self.last_result = result
        self.new_number = True
        self.decimal_added = False

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
            # Check if parentheses are balanced
            if self.open_parentheses == 0:
                while '(' in expr and ')' in expr:
                    expr = str(eval(expr))  # Evaluate the innermost parentheses
                return eval(expr)  # Evaluate the remaining expression
            else:
                return self.current_value  # Don't evaluate if parentheses aren't balanced
        except Exception:
            return "Error"

    def update_display(self):
        """Updates the QTextEdit with the current display value."""
        self.display_widget.setText(self.current_value)
