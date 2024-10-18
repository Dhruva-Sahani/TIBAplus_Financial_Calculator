import json
import math

class Amortization:
    #region init
    def __init__(self, display1, display2):
        self.display1 = display1
        self.display2 = display2
        self.file_path = "Amortization.json"
        self.data= {}
        self.load_amortization()

        # Initialize active key and list of keys
        # self.active_key = "P1"  # Start with P1 as the active key
        self.keys_list = list(self.data.keys())  # Dynamically get keys from the JSON
        self.current_index = 0  # Index for navigating between keys

    def load_amortization(self):
        # Load the Amortization JSON file
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading file {self.file_path}: {e}")
            return {}

    def save_amortization(self):
        # Save the modified data back to the Amortization JSON file
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    #endregion

    #region navigation
    def move_up(self):
        # Move up through the keys list
        self.current_index = (self.current_index - 1) % len(self.keys_list)
        self.active_key = self.keys_list[self.current_index]
        self.display_current_key()

    def move_down(self):
        # Move down through the keys list
        self.current_index = (self.current_index + 1) % len(self.keys_list)
        self.active_key = self.keys_list[self.current_index]
        if self.current_index > 1:
            self.computation = Compute()
            attrname = 'compute_'+ self.active_key
            calculate = getattr(self.computation, attrname)
            self.data[self.active_key]['current_value']= calculate()
            self.save_amortization()
        self.display_current_key()
        
    def enter(self, new_value):
    # Ensure the active key is either "P1" or "P2"
        if self.active_key in ["P1", "P2"]:
            try:
                # Convert new_value to an integer
                new_value_int = int(new_value)
                
                # Check if the value is within the valid range (1 to 9999)
                if 1 <= new_value_int <= 9999:
                    # Update the current value for the active key (P1 or P2)
                    self.data[self.active_key]["current_value"] = new_value_int
                    
                    # Save changes and update the display
                    self.save_amortization()
                    self.display_current_key()
                else:
                    # Display an error message for invalid range
                    print("Error: Input must be between 1 and 9999")
            except ValueError:
                # Display an error message for non-integer input
                print("Error: Invalid input. Please enter a valid integer.")

    def display_current_key(self):
        # Display the active key and its current value
        key_data = self.data[self.active_key]
        self.display1.setText(str(key_data["current_value"]))
        self.display2.setText(f"{key_data['key']}=")
        
    def amortization(self):
        """Initiate the amortiztion worksheet and display P1"""
        self.current_index = 0 #reset current key
        self.active_key = self.keys_list[self.current_index]
        self.display_current_key()
    #endregion
    
    def clear_work(self, null):
        for key, data in self.data.items():
             data["current_value"] = data["default_value"]
        self.save_amortization()
        self.display_current_key()     
        
        
        



class Compute:
    def __init__(self):
        self.amortization_file = "Amortization.json"
        self.tvm_file = "TimeValueOfMoney.json"

        # Initialize variables for Amortization values
        self.P1 = 0
        self.P2 = 0
        self.BAL = 0
        self.PRN = 0
        self.INT = 0

        # Initialize variables for Time Value of Money values
        self.PV = 0
        self.PMT = 0
        self.I_Y = 0
        
        self.n_periods = 0
        self.decimal_places = 2  # Default number of decimal places to round to
        self.load_and_set_values()
        self.calculate_i()

    def load_and_set_values(self):
        # Load and set values from Amortization.json
        try:
            with open(self.amortization_file, 'r') as file:
                amort_data = json.load(file)
                self.P1 = amort_data['P1']['current_value']
                self.P2 = amort_data['P2']['current_value']
                self.BAL = amort_data['BAL']['current_value']
                self.PRN = amort_data['PRN']['current_value']
                self.INT = amort_data['INT']['current_value']
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading Amortization file: {e}")

        # Load and set values from TimeValueOfMoney.json
        try:
            with open(self.tvm_file, 'r') as file:
                tvm_data = json.load(file)
                self.PV = tvm_data['PV']['current_value']
                self.PMT = tvm_data['PMT']['current_value']
                self.I_Y = tvm_data['I_Y']['current_value']
                self.P_Y = tvm_data['P_Y']['current_value']
                self.C_Y = tvm_data['C_Y']['current_value']
                self.paymentmode = tvm_data['Payment Mode']['current_value']
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading Time Value of Money file: {e}")
        
  
    def calculate_i(self):
        """Calculate 'i' using the i1 formula when I/Y != 0."""
        x = self.I_Y / 100 / self.C_Y
        y = self.C_Y / self.P_Y
        self.i = math.exp(y * math.log(1 + x)) - 1
        

            
    def RND(self, value):
            # Round to the selected number of decimal places
            return round(value, self.decimal_places)

    def RND12(self, value):
        # Round to 12 decimal places
        return round(value, 12)

    def calculate_bal_int(self):
        # Initialize lists for balance and interest
        self.balance_list = []
        self.interest_list = []

        # Initial balance is the present value, rounded
        if self.paymentmode == 'BGN':
            bal = self.RND(self.PV + self.PMT)
        else:
            bal = self.RND(self.PV)
            
        self.balance_list.append(bal)

        # Iterate from 1 to P2 (n_periods)
        for m in range(1, self.P2 + 1):
            # Calculate the interest for the period lm using the formula: lm = RND[RND12(-i * bal(m-1))]
            lm = self.RND(self.RND12((-self.i) * bal))  # Convert interest rate from percentage to decimal

            # Calculate the balance for the period: bal(m) = bal(m-1) - lm + RND(PMT)
            bal = bal + self.RND(self.PMT) - lm
        
            # Round and store the balance and interest for each period
            self.balance_list.append(self.RND(bal))

        
    def compute_BAL(self):
    # Calculate the balance list
        self.calculate_bal_int()
        balance = self.balance_list[self.P2]
        return balance
        # else:
        #     raise ValueError(f"Period {period} is out of range. Must be between 0 and {len(balance_list) - 1}.")
        
    def compute_PRN(self):
        """ The formula mentioned in the documentation is not the one which is actually implemented in the hardware
         ΣPrn() = bal(P2) - bal(P1) makes sense according to the defination of the paramter
         but in realiy it has to include the principal payment made during P1 as well. In the current formula only P2 is computed"""
        
        self.calculate_bal_int()
        principal_paid = (self.balance_list[self.P1] - self.balance_list[self.P1-1]) + (self.balance_list[self.P2] - self.balance_list[self.P1])
        return principal_paid
    
    def compute_INT(self):
        """ΣInt() = (P2 - P1 + 1) * RND(PMT) - ΣPrn()"""
        interest_paid = (self.P2 - self.P1 + 1) * self.RND(self.PMT) - self.compute_PRN()
        return interest_paid
        
        


