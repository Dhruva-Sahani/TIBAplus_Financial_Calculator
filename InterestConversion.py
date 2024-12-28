import json
from Settings import Settings
import math

class InterestConversion:
    def __init__(self, display1, display2):
        self.file_path = "InterestConversion.json"
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
            print("InterestCOnversion worksheet file not found. Initializing with empty data.")
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
        
    def interestconversion(self):
        self.current_index = 0
        self.display_current_key()
        
    def enter(self, new_value):
        
        current_key = self.keys[self.current_index]
        key_data = self.data[current_key]

        if current_key == 'Periods':
            if float(new_value)>0:
                key_data["current_value"] = float(new_value)
            elif float(new_value)<=0:
                self.display1.setText("Error 4    ")
                self.display2.setText("")
                return None 
                
        else:
            key_data["current_value"] = float(new_value)
            
        self.data[current_key] = key_data
        self.save()
        self.display_current_key()
        
    def calculate_instant(self):
        self.computation = Compute()
        if self.current_index == 0:
            self.data["NominalRate"]["current_value"] = self.computation.calculate_NominalRate()
            self.save()
            self.display_current_key()
        elif self.current_index == 1:
            self.data["EffectiveRate"]["current_value"] = self.computation.calculate_EffectiveRate()
            self.save()
            self.display_current_key()
            
    def clear_work(self, Null):
        self.data['NominalRate']["current_value"] = self.data['NominalRate']["default_value"]
        self.data['EffectiveRate']["current_value"] = self.data['EffectiveRate']["default_value"]
        self.save()
        self.display_current_key()
    
    
class Compute:
    def __init__(self, file_path = "InterestConversion.json"):
        self.file_path = file_path
        self.data = {}
        self.Eff = None
        self.Nom = None
        self.C_Y = None
        self.load_and_set_variables()
        
        
    def load_and_set_variables(self):
        try:
             with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.Nom = self.data['NominalRate']["current_value"]
                self.Eff = self.data["EffectiveRate"]["current_value"]
                self.C_Y = self.data["Periods"]["current_value"]
                
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Starting with default values.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Check file format.")
            
    def calculate_NominalRate(self):
        Nominal = self.C_Y * (((self.Eff/100) + 1) ** (1 / self.C_Y) - 1)
        return Nominal*100
    
    def calculate_EffectiveRate(self):
        Effective = (1 + (self.Nom/100) / self.C_Y) ** self.C_Y - 1
        return Effective*100
        