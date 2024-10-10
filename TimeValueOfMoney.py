import json
import math

class TimeValueOfMoney:
    #region init
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
            
    #endregion

    #region main functions
    def tvm(self, keytype, new_value):
        # Main function for handling Enter or Compute type keys        
        if keytype in self.data:
            key_data = self.data[keytype]
                
            if key_data["key_type"] == "Enter and Compute":
                # try:
                    # Set the new value as current_value for the keytype
                    key_data["current_value"] = float(new_value)
                    
                    # Update the displays
                    self.display2.setText(f"{key_data['key']}=")
                    self.display1.setText(str(new_value))

                    # Save the updated value in the JSON file
                    self.save_time_value_of_money()
                    
    def calculation(self, keytype):
        if keytype in self.data:
            key_data = self.data[keytype]
            self.computation = Compute()
            function_name = f"calculate_{keytype}"
            calculate = getattr(self.computation, function_name)
            key_data["current_value"]=float(calculate())
            self.save_time_value_of_money()
            self.display2.setText(f"{key_data['key']}=")
            self.display1.setText(str(key_data['current_value']))
        
        
    def paymentperyear(self):
            # Activate P/Y and C/Y mode
            self.py_cy_mode_active = True
            self.current_index = 0  # Reset to start at P/Y
            self.active_key = self.keys_list[self.current_index]
            self.display_current_key()
            
    #endregion
    
    #region navigation and enter         
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
            
    #endregion
            
    #region displays and clear
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



    def display_payment_mode(self):
        # Display the current payment mode on the display
        key_data = self.data["Payment Mode"]
        self.display2.setText(key_data["current_value"])
        self.display1.setText("")
        
        
    def clear_tvm(self):
        # List of keys to reset
        keys_to_reset = ["N", "I/Y", "PV", "PMT", "FV"]

        # Reset each key to its default value
        for key in keys_to_reset:
            if key in self.data:
                self.data[key]['current_value'] = self.data[key]['default_value']

        # Save the changes to the JSON file
        self.save_time_value_of_money()
        
        
    def clear_work(self, worksheet_type):
        """
        Clears the values for P/Y and C/Y or Payment Mode based on the argument passed.
        :param work_type: A string, either "P/Y_C/Y" or "Payment_Mode".
        """
        if worksheet_type == "P/Y":
            # Reset P/Y and C/Y to their default values
            self.data["P/Y"]["current_value"] = self.data["P/Y"]["default_value"]
            self.data["C/Y"]["current_value"] = self.data["C/Y"]["default_value"]
            self.save_time_value_of_money()
            self.display_current_key()
        
        elif worksheet_type == "Payment_Mode":
            # Reset Payment Mode to its default value
            self.data["Payment Mode"]["current_value"] = self.data["Payment Mode"]["default_value"]
            self.save_time_value_of_money()
            self.display_payment_mode()
       #endregion  
            
        

class Compute:
    def __init__(self, file_path='TimeValueOfMoney.json'):
        self.file_path = file_path
        self.data = {}
        self.N = None
        self.I_Y = None
        self.PV = None
        self.PMT = None
        self.FV = None
        self.P_Y = None
        self.C_Y = None
        self.payment_mode = None

        # Automatically load data and set variables upon class instantiation
        self.load_and_set_variables()

    def load_and_set_variables(self):
        """Load data from the JSON file and set class variables."""
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.N = self.data['N']['current_value']
                self.I_Y = self.data['I/Y']['current_value']
                self.PV = self.data['PV']['current_value']
                self.PMT = self.data['PMT']['current_value']
                self.FV = self.data['FV']['current_value']
                self.P_Y = self.data['P/Y']['current_value']
                self.C_Y = self.data['C/Y']['current_value']
                self.payment_mode = self.data['Payment Mode']['current_value']
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Starting with default values.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Check file format.")
            
            
    def calculate_i(self):
        """Calculate 'i' using the i1 formula when I/Y != 0."""
        x = self.I_Y / 100 / self.C_Y
        y = self.C_Y / self.P_Y
        i = math.exp(y * math.log(1 + x)) - 1
        return i

    def calculate_N(self):
        """Calculate N based on the two cases."""
        print("called")
        if self.I_Y != 0:
            # Case 1: I/Y != 0
            i = self.calculate_i()

            # Set G based on payment mode
            if self.payment_mode == 'END':
                G = 1
            else:  # payment_mode == 'BGN'
                G = 1 + i

            # Calculate N using the N1 formula
            numerator = (self.PMT * G - self.FV * i)
            denominator = (self.PMT * G + self.PV * i)

            if denominator == 0:  # Avoid division by zero
                raise ValueError("Denominator in N1 calculation is zero, check the values.")

            N = math.log(numerator / denominator) / math.log(1 + i)
            return round(N)
        else:
            # Case 2: I/Y == 0, use N2 formula
            if self.PMT == 0:
                raise ValueError("PMT cannot be zero for N2 calculation.")
            
            N = -(self.PV + self.FV) / self.PMT
            return round(N)
        
        
    def calculate_PV(self):
        """Calculate PV based on the two cases."""
        if self.I_Y != 0:
            # Case 1: I/Y != 0
            i = self.calculate_i()
            print(i)
            # Set G based on payment mode
            if self.payment_mode == 'END':
                G = 1
            else:  # payment_mode == 'BGN'
                G = 1 + i

            # Calculate PV using the PV1 formula
            try:
                PV = ((self.PMT * G / i) - self.FV) * ((1 / (1 + i) ** self.N)) - (self.PMT * G / i)
            except ZeroDivisionError:
                raise ValueError("i value resulted in division by zero.")

            return PV
        else:
            # Case 2: I/Y == 0, use PV2 formula
            PV = -1 * (self.FV - self.PMT * self.N)
            return PV
        
        
    def calculate_PMT(self):
        """Calculate PV based on the two cases."""
        if self.I_Y != 0:
            # Case 1: I/Y != 0
            i = self.calculate_i()
            # Set G based on payment mode
            if self.payment_mode == 'END':
                G = 1
            else:  # payment_mode == 'BGN'
                G = 1 + i

            # Calculate PV using the PV1 formula
            try:
                # term1 = i * (self.PV * (1 + i) ** self.N + self.FV)
                # term2 = G * (1 - (1 + i) ** (-self.N))
                # PMT = term1 / term2
                PMT = (i / G) * (self.PV + ((self.PV + self.FV)/(((1 + i) ** self.N) - 1)))
            except ZeroDivisionError:
                raise ValueError("i value resulted in division by zero.")

            return PMT
        else:
            # Case 2: I/Y == 0, use PV2 formula
            PMT = -1 * (self.PV + self.FV) / self.N
            return PMT
        
    
    def calculate_FV(self):
        """Calculate PV based on the two cases."""
        if self.I_Y != 0:
            # Case 1: I/Y != 0
            i = self.calculate_i()
            print(i)
            # Set G based on payment mode
            if self.payment_mode == 'END':
                G = 1
            else:  # payment_mode == 'BGN'
                G = 1 + i

            # Calculate PV using the PV1 formula
            try:
                # term1 = i * (self.PV * (1 + i) ** self.N + self.FV)
                # term2 = G * (1 - (1 + i) ** (-self.N))
                # PMT = term1 / term2
                FV = (self.PMT * G / i) - ((1 + i) ** self.N) * (self.PV + (self.PMT * G / i))
            except ZeroDivisionError:
                raise ValueError("i value resulted in division by zero.")

            return FV
        else:
            # Case 2: I/Y == 0, use PV2 formula
            FV = -1 * (self.PV * self.PMT * self.N)
            return FV
        
            
        