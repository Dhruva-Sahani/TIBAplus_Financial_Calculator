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
        self.display_widget.setPlainText(self.current_value)
