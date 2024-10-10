import json

class CashFlow:
    def __init__(self, display1, display2):
        self.file_path = 'CashFlow.json'
        self.cashflows = {}
        self.load_cashflows()
        self.display1 = display1
        self.display2 = display2

    def load_cashflows(self):
        """Loads cashflow data from Cashflow.json file."""
        # try:
        with open(self.file_path, 'r') as file:
            self.cashflows = json.load(file)
        # except FileNotFoundError:
        #     print(f"{self.file_path} not found. Loading default cashflows.")
        #     self.set_default_cashflows()
            
    def save_cashflows(self):
        """Saves the current cashflows back to the Cashflow.json file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.cashflows, file, indent=4) 
        
    def display_current_cashflow(self):
        """Display the current cashflow key and its value."""
        keys = list(self.cashflows.keys())
        if 0 <= self.current_index < len(keys):
            current_key = keys[self.current_index]
            current_value = self.cashflows[current_key]["current_value"]
            self.display2.setText(str(current_key))  # Display key on display2
            self.display1.setText(str(current_value))  # Display value on display1

    def move_up(self):
        """Move up through the cashflows (navigate upwards in a loop)."""
        keys = list(self.cashflows.keys())

        if self.current_index == 0:
            # If at Cf0, move to the last key with a non-zero F type value
            found_non_zero = False
            for i in range(len(keys) - 1, -1, -1):
                if keys[i].startswith('F') and self.cashflows[keys[i]]["current_value"] > 0:
                    self.current_index = i
                    self.display_current_cashflow()
                    found_non_zero = True
                    return
            
            # If no non-zero F key was found, set to F01
            if not found_non_zero:
                self.current_index = keys.index('F01')
                self.display_current_cashflow()
        else:
            # Move up normally if not at index 0
            self.current_index -= 1
            self.display_current_cashflow()

    def move_down(self):
        """Move down through the cashflows (navigate downwards) with condition for F type keys."""
        keys = list(self.cashflows.keys())
        
        # Check if the current key is an F type and its value is zero
        current_key = keys[self.current_index]
        if current_key.startswith('F') and self.cashflows[current_key]["current_value"] == 0:
            # Do not proceed if the current key is F and its value is 0
            print("Cannot move down, current F type value is 0")
            self.current_index = 0
            self.display_current_cashflow()
        
        # Move down if within bounds
        elif self.current_index < len(keys) - 1:
            self.current_index += 1
            self.display_current_cashflow()
    
    def enter(self, new_value):
        """Update the current value of the displayed key with constraints for F type keys."""
        keys = list(self.cashflows.keys())
        current_key = keys[self.current_index]
        
        # If current key is F type, apply conditions for decimal and negative values
        if current_key.startswith('F'):
            try:
                new_value = int(new_value)
                if new_value < 0:
                    print("Negative values are not allowed for F type keys.")
                    return
                new_value = round(new_value)  # Round to nearest integer if decimal
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return
        else:
            # Update the current value of C type keys
            try:
                new_value = int(new_value)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return

            # Set the corresponding F key's value to 1
            frequency_key = f"F{current_key[1:]}"  # E.g., for C01, F01 will be derived
            if frequency_key in self.cashflows:
                self.cashflows[frequency_key]["current_value"] = 1

        # Update the current value of the key
        self.cashflows[current_key]["current_value"] = int(new_value)
        
        # Update display1 and display2
        self.display1.setText(str(new_value))  # Show the new value in display1
        self.display2.setText(f"{current_key}=")  # Show the key with '=' in display2
        
        # Save the updated cashflows to file
        self.save_cashflows()

    def cashflow(self):
        """Initiate the cashflow worksheet and display the first cashflow (Cf0)."""
        self.current_index = 0  # Reset to the first index (Cf0)
        self.display_current_cashflow()  # Display Cf0 when the cashflow process starts       
        
        


class CashFlowReturns:
    def __init__(self, display1, display2):
        self.file_path = 'CashFlowReturns.json'
        self.returns = {}
        self.load_returns()
        self.display1 = display1  # Display for current value
        self.display2 = display2  # Display for key
        self.current_index = 0    # Index for navigation
        self.npv_active = False   # Flag for NPV navigation activation
        self.irr_active = False   # Flag for IRR display

    def load_returns(self):
        """Loads CashFlowReturns data from the JSON file."""
        with open(self.file_path, 'r') as file:
            self.returns = json.load(file)

    def save_returns(self):
        """Saves the current returns data to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.returns, file, indent=4)

    def display_current_value(self):
        """Display the key and its current value."""
        # If IRR is active, display only IRR values and stop navigation
        if self.irr_active:
            self.display1.setText(str(self.returns['IRR']['current_value']))
            self.display2.setText('IRR')
        else:
            # Normal display for I and NPV
            keys = list(self.returns.keys())
            current_key = keys[self.current_index]
            current_value = self.returns[current_key]["current_value"]
        
            # Update display1 and display2
            self.display1.setText(str(current_value))  # Display current value
            self.display2.setText(current_key)         # Display key

    def move_up(self):
        """Move up through the keys (I and NPV) if NPV is active."""
        if not self.npv_active:
            print("NPV is not active, cannot navigate.")
            return

        keys = list(self.returns.keys())
        
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(keys) - 2  # Skip 'IRR' by default

        self.display_current_value()

    def move_down(self):
        """Move down through the keys (I and NPV) if NPV is active."""
        if not self.npv_active:
            print("NPV is not active, cannot navigate.")
            return

        keys = list(self.returns.keys())

        if self.current_index < len(keys) - 2:
            self.current_index += 1
        else:
            self.current_index = 0  # Loop back to "I" if at NPV
        
        self.display_current_value()

    def enter(self, new_value):
        """Update the current value of the key if it's of entry type."""
        if self.irr_active:
            print("Cannot enter values while IRR is active.")
            return
        
        keys = list(self.returns.keys())
        current_key = keys[self.current_index]

        # Only update if the key is of type 'entry'
        if self.returns[current_key]["type"] == "entry":
            try:
                new_value = float(new_value)
                self.returns[current_key]["current_value"] = new_value

                # Update display1 and display2
                self.display1.setText(str(new_value))  # Show the new value
                self.display2.setText(f"{current_key}=")  # Show the key with '='

                # Save updated values to file
                self.save_returns()

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def npv(self):
        """Activate NPV mode and allow navigation."""
        self.npv_active = True
        self.irr_active = False
        self.current_index = 0  # Set to 'I' as starting point
        self.display_current_value()

    def irr(self):
        """Display IRR values and disable navigation."""
        self.npv_active = False
        self.irr_active = True
        self.display_current_value()

    def cashflow_returns(self):
        """Activate CashFlowReturns and display the first parameter (I)."""
        self.npv_active = False
        self.irr_active = False
        self.current_index = 0  # Start at 'I'
        self.display_current_value()


     
            
    
    