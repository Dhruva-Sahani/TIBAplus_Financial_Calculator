import json

class Breakeven:
    def __init__(self, display1, display2):
        self.file_path = "Breakeven.json"
        self.display1 = display1
        self.display2 = display2
        self.current_index = 0
        self.keys = []
        self.data = {}
        self.load()
        
    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.keys = list(self.data.keys())
        except FileNotFoundError:
            print("Breakeven worksheet file not found. Initializing with empty data.")
            self.data = {}
        except json.JSONDecodeError:
            print("Error decoding JSON. Initializing with empty data.")
            self.data = {}
            
    def save(self):
        """
        Save the current Breakeven worksheet data to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving: {e}")
            
    def display_current_key(self):
        """Display the current key and its value in display1 and display2."""
        current_key = self.keys[self.current_index]
        key_data = self.data[current_key]
        
        self.display1.setText(str(key_data["current_value"]))
        self.display2.setText(str(key_data["key"])) 
        
    def move_up(self):
        """Move up to the previous bond key in a loop."""
        self.current_index = (self.current_index - 1) % len(self.keys)
        self.display_current_key()

    def move_down(self):
        """Move down to the next bond key in a loop."""
        self.current_index = (self.current_index + 1) % len(self.keys)
        self.display_current_key()
        
    def enter(self, new_value):
        current_key = self.keys[self.current_index]
        self.data[current_key]["current_value"] = float(new_value)
        self.save()
        self.display_current_key()
        
    def breakeven(self):
        self.current_index = 0
        self.display_current_key()
        
    def calculate_instant(self):
        self.computation = Compute()
        current_key = self.keys[self.current_index]
        calculate_function = getattr(self.computation, f"calculate_{current_key}")
        result, error = calculate_function()
        if error:
            self.display1.setText("Error 1    ")
            self.display2.setText("")
        else:
            self.data[current_key]["current_value"] = result
            self.save()
            self.display_current_key()
        
        
    def clear_work(self, Null):
        for key in self.data:
            self.data[key]["current_value"] = self.data[key]["default_value"] 
        self.save()
        self.display_current_key()
        
        
    
class Compute:
    def __init__ (self, file_path = "Breakeven.json"):
        self.file_path = file_path
        self.data = {}
        self.FC = None
        self.VC = None
        self.P = None
        self.PFT = None
        self.Q = None
        self.load_and_set_variables()
        
    def load_and_set_variables(self):
        try:
             with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.FC = self.data['FixedCost']["current_value"]
                self.VC = self.data["VariableCostPU"]["current_value"]
                self.P = self.data["UnitPrice"]["current_value"]
                self.PFT = self.data["Profit"]["current_value"]
                self.Q = self.data["Quantity"]["current_value"]
                
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Starting with default values.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Check file format.")
            
    def calculate_FixedCost(self):
        try:
            self.FC = self.P * self.Q - self.PFT - self.VC * self.Q 
            return self.FC, None  # No error
        except Exception as e:
            return None, e  # Return error object
        
    def calculate_VariableCostPU(self):
        try:
            self.VC = (self.P * self.Q - self.PFT - self.FC) / self.Q
            return self.VC, None  # No error
        except ZeroDivisionError as e:
            return None, e  # Return error object
        except Exception as e:
            return None, e  # Return other errors
        
    def calculate_UnitPrice(self):
        try:
            self.P = (self.PFT + self.FC + self.VC * self.Q) / self.Q
            return self.P, None  # No error
        except ZeroDivisionError as e:
            return None, e  # Return error object
        except Exception as e:
            return None, e  # Return other errors
        
    def calculate_Profit(self):
        try:
            self.PFT = self.P * self.Q - (self.FC + self.VC * self.Q)
            return self.PFT, None  # No error
        except Exception as e:
            return None, e  # Return error object
    
    def calculate_Quantity(self):
        try:
            self.Q = (self.PFT + self.FC) / (self.P - self.VC)
            return self.Q, None  # No error
        except ZeroDivisionError as e:
            return None, e  # Return error object
        except Exception as e:
            return None, e  # Return other errors
    