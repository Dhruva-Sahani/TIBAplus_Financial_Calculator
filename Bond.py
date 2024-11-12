import json
from Settings import Settings
from datetime import datetime

class Bond:
    def __init__(self, display1, display2 ):
        self.filename = "Bond.json"
        self.display1 = display1
        self.display2 = display2
        self.current_index = 0
        self.keys = []
        self.data = {}  # Dictionary to hold Bond data
        self.load_bond()
        
    def load_bond(self):
        """Load data from Bond.json."""
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
                self.keys = list(self.data.keys())
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
    
    def save_bond(self):
        """Save current data to Bond.json."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)
            print("Bond data saved successfully.")
        except IOError:
            print("An error occurred while saving the file.")
            
    def move_up(self):
        """Move up to the previous bond key in a loop."""
        self.current_index = (self.current_index - 1) % len(self.keys)
        self.display_current_key()

    def move_down(self):
        """Move down to the next bond key in a loop."""
        self.current_index = (self.current_index + 1) % len(self.keys)
        self.display_current_key()

    def display_current_key(self):
        """Display the current key and its value in display1 and display2."""
        current_key = self.keys[self.current_index]
        key_data = self.data[current_key]
        
        current_value = key_data.get("current_value", "")  # Value to show in display1
        if key_data["type"] == "switch":
            self.display2.setText(str(key_data["current_value"]))  # Show current value directly for "switch" type
            self.display1.setText("")
        else:
            self.display2.setText(str(key_data["key"])) 
            self.display1.setText(str(current_value))
            
    def bond(self):
        self.current_index = 0
        self.display_current_key()
        
    def convert_date(self, date_str):
        self.settings = Settings()
        try:
            # Read the date format setting
            dateformat = self.settings.read("Dates")
            
            # Ensure the input string has at least "dd.mm" format
            if '.' not in date_str:
                raise ValueError("Invalid date input: missing separator")
            
            parts = date_str.split('.')
            if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                raise ValueError("Invalid date format")
            
            # Parse day, month, and year parts
            day_or_month, month_or_day_and_year = parts
            if dateformat == "US":
                mm = int(day_or_month)
                dd = int(month_or_day_and_year[:2]) if len(month_or_day_and_year) >= 2 else 1
                yy = int(month_or_day_and_year[2:]) if len(month_or_day_and_year) > 2 else 0
            elif dateformat == "Eur":
                dd = int(day_or_month)
                mm = int(month_or_day_and_year[:2]) if len(month_or_day_and_year) >= 2 else 1
                yy = int(month_or_day_and_year[2:]) if len(month_or_day_and_year) > 2 else 0
            else:
                raise ValueError("Invalid date format setting")

            # Determine the full year
            if 0 <= yy <= 79:
                year = 2000 + yy
            elif 80 <= yy <= 99:
                year = 1900 + yy
            else:
                raise ValueError("Year out of valid range")
            
            # Validate and format the date
            date = datetime(year, mm, dd)
            if dateformat == "US":
                return date.strftime("%m-%d-%Y")
            elif dateformat == "Eur":
                return date.strftime("%d-%m-%Y")
        
        except (ValueError, IndexError):
            return "Error: Invalid date input"
        
    def enter(self, new_value):
        """
        Update the current value of the active key based on the key's type.
        - For "enter" or "entercomp" types: sets current_value as float(new_value).
        - For "enterdate" type: sets current_value as the date string returned by convert_date(new_value).
        """
        current_key = self.keys[self.current_index]
        key_data = self.data[current_key]

        # Check the type and apply the appropriate conversion
        if key_data["type"] in ["enter", "entercomp"]:
            try:
                # Convert new_value to float and update current_value
                key_data["current_value"] = float(new_value)
                
            except ValueError:
                print("Error: Invalid number format.")
                return "Error: Invalid number format."

        elif key_data["type"] == "enterdate":
            # Use convert_date method for date conversion
            converted_date = self.convert_date(new_value)
            if "Error" in converted_date:
                print("Error: Invalid date format.")
                return "Error: Invalid date format."
            key_data["current_value"] = converted_date
            
        self.data[current_key] = key_data
        self.save_bond()
        self.display_current_key()

       