import json

class TimeValueOfMoney:
    def __init__(self, display1, display2):
        self.display1 = display1
        self.display2 = display2
        self.file_path = "TimeValueOfMoney.json"
        self.data = self.load_time_value_of_money()
        
        self.active_key = "P/Y"  # Start with P/Y as the active key
        self.keys_list = ["P/Y", "C/Y"]  # Only P/Y and C/Y keys to navigate
        self.current_index = 0  # Index for navigating between P/Y and C/Y
        
        self.py_cy_mode_active = False  # Flag for P/Y and C/Y mode

    def load_time_value_of_money(self):
        # Load the TimeValueOfMoney JSON file
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading file {self.file_path}: {e}")
            return {}

    def save_time_value_of_money(self):
        # Save the modified data back to the TimeValueOfMoney JSON file
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def tvm(self, keytype, new_value):
        # Main function for handling Enter or Compute type keys
        if keytype in self.data:
            key_data = self.data[keytype]
            if key_data["key_type"] == "Enter and Compute":
                # try:
                    # Set the new value as current_value for the keytype
                    key_data["current_value"] = int(new_value)
                    
                    # Update the displays
                    self.display2.setText(f"{key_data['key']}=")
                    self.display1.setText(str(new_value))

                    # Save the updated value in the JSON file
                    self.save_time_value_of_money()

        #         except ValueError:
        #             print(f"Invalid value for {keytype}. Please check the input.")
        #     else:
        #         print(f"Key {keytype} is not of type 'Enter-or-compute'.")
        # else:
        #     print(f"Key {keytype} not found in TimeValueOfMoney data.") 
        
        
    def paymentperyear(self):
            # Activate P/Y and C/Y mode
            self.py_cy_mode_active = True
            self.current_index = 0  # Reset to start at P/Y
            self.active_key = self.keys_list[self.current_index]
            self.display_current_key()
            
            
    def move_up(self):
        # Move up between P/Y and C/Y when P/Y and C/Y mode is active
        if self.py_cy_mode_active:
            self.current_index = (self.current_index - 1) % len(self.keys_list)
            self.active_key = self.keys_list[self.current_index]
            self.display_current_key()

    def move_down(self):
        # Move down between P/Y and C/Y when P/Y and C/Y mode is active
        if self.py_cy_mode_active:
            self.current_index = (self.current_index + 1) % len(self.keys_list)
            self.active_key = self.keys_list[self.current_index]
            self.display_current_key()

    def enter(self, new_value):
        # Update the current_value of the active key (P/Y or C/Y) when P/Y and C/Y mode is active
        if self.py_cy_mode_active:
            key_data = self.data[self.active_key]
            
            if key_data["type"] == "input":
                key_data["current_value"] = int(new_value)
                self.save_time_value_of_money()
                self.display_current_key()
                self.display2.setText(key_data["display_key"] + "=")
            
    
    def display_current_key(self):
        # Display the active key and its current value when P/Y and C/Y mode is active
        if self.py_cy_mode_active:
            key_data = self.data[self.active_key]
            self.display2.setText(key_data["display_key"])
            self.display1.setText(str(key_data["current_value"]))
            
    def payment_mode(self):
        # Activate Payment Mode and display the current mode
        self.payment_mode_active = True
        self.display_payment_mode()

    # def deactivate_payment_mode(self):
    #     # Deactivate Payment Mode
    #     self.payment_mode_active = False
    #     self.display1.setText("")  # Clear display1
    #     self.display2.setText("")  # Clear display2

    def set(self):
        # Switch the payment mode between "END" and "BGN"
        if self.payment_mode_active:
            key_data = self.data["Payment Mode"]
            current_value = key_data["current_value"]
            options = key_data["options"]

            # Find the index of the current value and toggle to the next option
            current_index = options.index(current_value)
            new_index = (current_index + 1) % len(options)
            key_data["current_value"] = options[new_index]

            # Save the updated mode to JSON and display it
            self.save_time_value_of_money()
            self.display_payment_mode()

    def display_payment_mode(self):
        # Display the current payment mode on the display
        key_data = self.data["Payment Mode"]
        self.display2.setText(key_data["current_value"])
        self.display1.setText("")
        
        