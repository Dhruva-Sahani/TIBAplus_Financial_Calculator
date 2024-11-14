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
        
        
    def set(self):
        """
        Cycle the 'key' of the current 'switch' type to the next option.
        """
        current_key = self.keys[self.current_index]
        key_data = self.data[current_key]

        # Check if the type is "switch"
        if key_data["type"] == "switch":
            options = key_data["options"]
            current_option = key_data["current_value"]

            # Find the index of the current option and move to the next one
            if current_option in options:
                current_index = options.index(current_option)
                next_index = (current_index + 1) % len(options)  # Wrap around to the start if at the end
                key_data["current_value"] = options[next_index]  # Update key to the next option

            # Save the updated data and refresh the display
            self.save_bond()
            self.display_current_key()
            
            
            


class Compute:
    def __init__(self, filename="Bond.json"):
        self.filename = filename
        
        # Initialize variables for bond attributes (short forms)
        self.SDT = None  # Settlement Date
        self.CPN = None  # Annual Coupon Rate %
        self.RDT = None  # Redemption Date
        self.RV = None   # Redemption Value
        self.DCM = None  # Day Count Method
        self.CPY = None  # Coupons per Year
        self.YLD = None  # Yield to Redemption
        self.PRI = None  # Dollar Price
        self.AI = None   # Accrued Interest
        
        self.load_and_set()

    def load_and_set(self):
        """Load current values from the JSON file into class variables."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)

            # Map JSON keys to the short variable names
            self.SDT = data["Settlement date"]["current_value"]
            self.CPN = data["Annual coupon rate %"]["current_value"]
            self.RDT = data["Redemption date"]["current_value"]
            self.RV = data["Redemption value"]["current_value"]
            self.DCM = data["Day count method"]["current_value"]
            self.CPY = data["Coupons per year"]["current_value"]
            self.YLD = data["Yield to redemption"]["current_value"]
            self.PRI = data["Dollar price"]["current_value"]
            self.AI = data["Accrued interet"]["current_value"]
            self.Day = self.daycount()

            print("Bond data loaded into Compute class variables successfully.")
        
        except FileNotFoundError:
            print(f"Error: File {self.filename} not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the file.")
        except KeyError as e:
            print(f"Error: Missing key in JSON data: {e}")


    def daycount(self):
        """Calculate the number of days between the settlement date and redemption date."""
        
        # Get date format setting
        self.settings = Settings()
        date_format = self.settings.read("Dates")
        
        # Choose date parsing format based on date_format setting
        if date_format == "US":
            date_format_str = "%m-%d-%Y"  # mm-dd-yyyy
        elif date_format == "Eur":
            date_format_str = "%d-%m-%Y"  # dd-mm-yyyy
        else:
            raise ValueError("Error: Unsupported date format setting.")
        
        if self.DCM == "ACT":
            try:
                # Convert SDT and RDT strings to datetime objects
                settlement_date = datetime.strptime(self.SDT, date_format_str)
                redemption_date = datetime.strptime(self.RDT, date_format_str)
                
                # Check that the redemption date is not before the settlement date
                if redemption_date <= settlement_date:
                    raise ValueError("Error: Redemption date cannot be before or on the settlement date.")
                
                # Calculate the number of days (excluding redemption date)
                days_between = (redemption_date - settlement_date).days

                print(f"Days between settlement and redemption: {days_between}")
                return days_between

            except ValueError as e:
                print(f"Error: {e}")
                return f"Error: {e}"
            
        elif self.DCM == "360":
            try:
                # Convert SDT and RDT strings to datetime objects
                settlement_date = datetime.strptime(self.SDT, date_format_str)
                redemption_date = datetime.strptime(self.RDT, date_format_str)
                
                # Extract year, month, and day components
                Y1, M1, DT1 = settlement_date.year, settlement_date.month, settlement_date.day
                Y2, M2, DT2 = redemption_date.year, redemption_date.month, redemption_date.day
                
                # Apply day adjustment rules
                if DT1 == 31:
                    DT1 = 30
                if DT2 == 31 and (DT1 == 30 or DT1 == 31):
                    DT2 = 30
                
                # Calculate DBD using the 30/360 convention
                days_between = (Y2 - Y1) * 360 + (M2 - M1) * 30 + (DT2 - DT1)
                
                print(f"Days between (30/360 convention): {days_between}")
                return days_between

            except ValueError as e:
                print(f"Error: {e}")
                return f"Error: {e}"
            
            
            
            
compute = Compute()


       