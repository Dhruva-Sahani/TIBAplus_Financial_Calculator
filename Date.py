import json
from Settings import Settings
from datetime import datetime, timedelta
import math

class Date:
    def __init__(self, display1, display2):
        self.file_path = "Date.json"
        self.display1 = display1
        self.display2 = display2
        self.current_index = 0
        self.keys = []
        self.data = {}
        self.load()

    def load(self):
        """
        Load the date worksheet data from the JSON file.
        """
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
                self.keys = list(self.data.keys())
                print("Date worksheet data loaded successfully.")
        except FileNotFoundError:
            print("Date worksheet file not found. Initializing with empty data.")
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
                print("Date worksheet data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving: {e}")
            
    def date(self):
        self.current_index = 0
        self.display_current_key()
            
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
        elif key_data["type"] == "dates":
            try:
                day = key_data["current_value"]["day"]
                month = key_data["current_value"]["month"]
                year = key_data["current_value"]["year"]

                # Check the date format setting
                self.settings = Settings()
                date_format = self.settings.read("Dates")

                # Create a datetime object
                date_obj = datetime(year, month, day)

                # Format date based on the date format setting
                if date_format == "US":
                    # mm-dd-yyyy format
                    formatted_date = date_obj.strftime("%m-%d-%Y")
                elif date_format == "Eur":
                    # dd-mm-yyyy format
                    formatted_date = date_obj.strftime("%d-%m-%Y")
                else:
                    raise ValueError("Invalid date format setting")

            except (KeyError, ValueError, TypeError) as e:
                print("Error: Invalid date data.")
                return "Error: Invalid date data."
            
            self.display2.setText(str(key_data["key"])) 
            self.display1.setText(str(formatted_date))
            
        else:
            self.display2.setText(str(key_data["key"])) 
            self.display1.setText(str(current_value))
            
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
                # Assume MM.DDYY or MM.DD format
                mm = int(day_or_month)
                dd = int(month_or_day_and_year[:2]) if len(month_or_day_and_year) >= 2 else 1
                yy = int(month_or_day_and_year[2:]) if len(month_or_day_and_year) > 2 else 0
            elif dateformat == "Eur":
                # Assume DD.MMYY or DD.MM format
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
            
            # Validate the date
            date = datetime(year, mm, dd)  # This will raise an error if the date is invalid
            
            # Return the date in the new format (dictionary with day, month, year keys)
            return {"day": dd, "month": mm, "year": year}
        
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

        if key_data["type"] == "dates":
            # Use convert_date method for date conversion
            converted_date = self.convert_date(new_value)
            if "Error" in converted_date:
                print("Error: Invalid date format.")
                return "Error: Invalid date format."
            
            # Extract day, month, and year from converted_date and store them in current_value
            key_data["current_value"]["day"] = int(converted_date["day"])
            key_data["current_value"]["month"] = int(converted_date["month"])
            key_data["current_value"]["year"] = int(converted_date["year"])
            
        if key_data["type"] == "entercompute":
            key_data["current_value"] = float(new_value)
            
        self.data[current_key] = key_data
        self.save()
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
            self.save()
            self.display_current_key() 
    
    def calculate_instant(self):
        current_key = self.keys[self.current_index]
        key_data = self.data[current_key]
        if key_data["type"] == "dates" and self.data["Day count method"]["current_value"] == "ACT":
            key_data["current_value"], self.weekday = self.finddate(self.current_index)
            self.data[current_key] = key_data
            self.save()
            self.display_current_key()
            self.display2.setText(self.weekday)
        elif key_data["type"] == "entercompute":
            key_data['current_value'] = self.daycount()   
            self.data[current_key] = key_data
            self.save()
            self.display_current_key()   
              
    def daycount(self):
        """Calculate the number of days between the settlement date and redemption date using the structured JSON format."""
        day1_data = self.data["Date1"]["current_value"]
        day2_data = self.data["Date2"]["current_value"]
        
        try:
            # Extract day, month, and year from the JSON format for both dates
            day1 = day1_data["day"]
            month1 = day1_data["month"]
            year1 = day1_data["year"]
            
            day2 = day2_data["day"]
            month2 = day2_data["month"]
            year2 = day2_data["year"]
            
            # Create datetime objects from the extracted values
            date1 = datetime(year1, month1, day1)
            date2 = datetime(year2, month2, day2)
            
            # Check if we are using the "ACT" or "360" day count convention
            if self.data["Day count method"]["current_value"] == "ACT":
                # Check that the redemption date is not before the settlement date
                # if date2 <= date1:
                #     raise ValueError("Error: Redemption date cannot be before or on the settlement date.")
                
                # Calculate the number of days (excluding redemption date)
                days_between = (date2 - date1).days
                print(f"Days between settlement and redemption: {days_between}")
                return days_between

            elif self.data["Day count method"]["current_value"]  == "360":
                # Extract year, month, and day components for 30/360 convention calculation
                Y1, M1, DT1 = date1.year, date1.month, date1.day
                Y2, M2, DT2 = date2.year, date2.month, date2.day
                
                # Apply day adjustment rules according to the 30/360 convention
                if DT1 == 31:
                    DT1 = 30
                if DT2 == 31 and (DT1 == 30 or DT1 == 31):
                    DT2 = 30
                
                # Calculate days between using the 30/360 convention
                days_between = (Y2 - Y1) * 360 + (M2 - M1) * 30 + (DT2 - DT1)
                print(f"Days between (30/360 convention): {days_between}")
                return days_between

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return f"Error: {e}"
        
    def finddate(self, day):
        daybetween = float(self.data["DayBetweenDate"]["current_value"])
        if day == 0:
            date = self.data["Date2"]["current_value"]
            try:
                # Convert the dictionary to a datetime object
                date_obj = datetime(
                    year=date["year"],
                    month=date["month"],
                    day=date["day"]
                )
                # Calculate the new date
                new_date = date_obj - timedelta(days= math.ceil(daybetween))
                
                day_names = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
                day_of_week = day_names[new_date.weekday()]
                # Return the new date as a dictionary
                return {
                    "day": new_date.day,
                    "month": new_date.month,
                    "year": new_date.year
                }, day_of_week
            except KeyError:
                print("Invalid date format. Please provide 'day', 'month', and 'year'.")
                return None
            except ValueError as e:
                print(f"Error processing the date: {e}")
                return None
        else: 
            date = self.data["Date1"]["current_value"]
            try:
                # Convert the dictionary to a datetime object
                date_obj = datetime(
                    year=date["year"],
                    month=date["month"],
                    day=date["day"]
                )
                # Calculate the new date
                new_date = date_obj + timedelta(days= math.ceil(daybetween))
                
                day_names = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
                day_of_week = day_names[new_date.weekday()]
                # Return the new date as a dictionary
                return {
                    "day": new_date.day,
                    "month": new_date.month,
                    "year": new_date.year
                }, day_of_week
            except KeyError:
                print("Invalid date format. Please provide 'day', 'month', and 'year'.")
                return None
            except ValueError as e:
                print(f"Error processing the date: {e}")
                return None
            
    
            
        

            
   
            
            
            
            
            
            
