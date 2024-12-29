import json

class Profit:
    def __init__(self, display1, display2):
        self.file_path = "Profit.json"
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
            print("Profit worksheet file not found. Initializing with empty data.")
            self.data = {}
        except json.JSONDecodeError:
            print("Error decoding JSON. Initializing with empty data.")
            self.data = {}

    def save(self):
        """
        Save the current date worksheet data to the JSON file.
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
        
    def profit(self):
        self.current_index = 0
        self.display_current_key()
        
    
    def calculate_instant(self):
        self.computation = Compute()
        current_key = self.keys[self.current_index]
        calculate_function = getattr(self.computation, f"calculate_{current_key}")
        self.data[current_key]["current_value"] = calculate_function()
        self.save()
        self.display_current_key()  
        
    def clear_work(self, Null):
        for key in self.data:
            self.data[key]["current_value"] = self.data[key]["default_value"] 
        self.save()
        self.display_current_key()
        
    
class Compute:
    def __init__ (self, file_path = "Profit.json"):
        self.file_path = file_path
        self.data = {}
        self.CST = None
        self.SEL = None
        self.MAR = None
        self.load_and_set_variables()
        
        
    def load_and_set_variables(self):
        try:
             with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.CST = self.data['CostPrice']["current_value"]
                self.SEL = self.data["SellingPrice"]["current_value"]
                self.MAR = self.data["ProfitMargin"]["current_value"]
                
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Starting with default values.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Check file format.")
            
    def calculate_CostPrice(self):
        self.CST = self.SEL * (1 - self.MAR / 100)
        return self.CST
    
    def calculate_SellingPrice(self):
        self.SEL = self.CST / (1 - self.MAR / 100)
        return self.SEL
    
    def calculate_ProfitMargin(self):
        self.MAR = ((self.SEL - self.CST) / self.SEL) * 100
        return self.MAR
        
        

        
        
        
        
        
        