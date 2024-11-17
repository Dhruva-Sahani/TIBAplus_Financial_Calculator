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
        self.load()
        
    def load(self):
        """Load data from Bond.json."""
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
                self.keys = list(self.data.keys())
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
    
    def save(self):
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
        elif key_data["type"] == "date":
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

        # Check the type and apply the appropriate conversion
        if key_data["type"] in ["enter", "entercomp"]:
            try:
                # Convert new_value to float and update current_value
                key_data["current_value"] = float(new_value)
                
            except ValueError:
                print("Error: Invalid number format.")
                return "Error: Invalid number format."

        elif key_data["type"] == "date":
            # Use convert_date method for date conversion
            converted_date = self.convert_date(new_value)
            if "Error" in converted_date:
                print("Error: Invalid date format.")
                return "Error: Invalid date format."
            
            # Extract day, month, and year from converted_date and store them in current_value
            key_data["current_value"]["day"] = int(converted_date["day"])
            key_data["current_value"]["month"] = int(converted_date["month"])
            key_data["current_value"]["year"] = int(converted_date["year"])
            
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
            self.R = data["Annual coupon rate %"]["current_value"] / 100.0
            self.RDT = data["Redemption date"]["current_value"]
            self.RV = data["Redemption value"]["current_value"]
            self.DCM = data["Day count method"]["current_value"]
            self.CPY = data["Coupons per year"]["current_value"]
            self.Y = data["Yield to redemption"]["current_value"] / 100.0
            self.PRI = data["Dollar price"]["current_value"]
            self.AI = data["Accrued interet"]["current_value"]
            
            #Variables for formulas
            self.M = float(self.CPY[0])
            self.DSR = self.daycount(self.SDT, self.RDT)
            self.P1, self.P2 = self.coupon_dates()
            self.E = self.daycount(self.P1, self.P2)
            self.A = self.daycount(self.P1, self.SDT)
            
            
            
            print("Bond data loaded into Compute class variables successfully.")
            print(self.SDT)
            print(self.RDT)
            print(self.P1)
            print(self.P2)
            print(self.DSR)
            print(self.A)
        
        except FileNotFoundError:
            print(f"Error: File {self.filename} not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the file.")
        except KeyError as e:
            print(f"Error: Missing key in JSON data: {e}")

    def save_bond_data(self):
        """
        Save bond data back to the Bond.json file.
        """
        # Create a dictionary structure to match the JSON format
        bond_data = {
            "Settlement date": {"current_value": self.SDT},
            "Annual coupon rate %": {"current_value": self.R * 100.0},  # Convert back to percentage
            "Redemption date": {"current_value": self.RDT},
            "Redemption value": {"current_value": self.RV},
            "Day count method": {"current_value": self.DCM},
            "Coupons per year": {"current_value": self.CPY},
            "Yield to redemption": {"current_value": self.Y * 100.0},  # Convert back to percentage
            "Dollar price": {"current_value": self.PRI},
            "Accrued interet": {"current_value": self.AI},
        }

        # Define the JSON file path
        file_path = "Bond.json"

        try:
            # Open the file and save the updated data
            with open(file_path, "w") as json_file:
                json.dump(bond_data, json_file, indent=4)
            print(f"Bond data successfully saved to {file_path}.")
        except Exception as e:
            print(f"Error saving bond data: {e}")

    def daycount(self, day1_data, day2_data):
        """Calculate the number of days between the settlement date and redemption date using the structured JSON format."""
        
        # # Get date format setting
        # self.settings = Settings()
        # date_format = self.settings.read("Dates")
        
        # # Choose date output format based on date_format setting (for display purposes)
        # if date_format == "US":
        #     date_format_str = "%m-%d-%Y"  # mm-dd-yyyy
        # elif date_format == "Eur":
        #     date_format_str = "%d-%m-%Y"  # dd-mm-yyyy
        # else:
        #     raise ValueError("Error: Unsupported date format setting.")
        
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
            if self.DCM == "ACT":
                # Check that the redemption date is not before the settlement date
                if date2 <= date1:
                    raise ValueError("Error: Redemption date cannot be before or on the settlement date.")
                
                # Calculate the number of days (excluding redemption date)
                days_between = (date2 - date1).days
                print(f"Days between settlement and redemption: {days_between}")
                return days_between

            elif self.DCM == "360":
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
        
        
    def coupon_dates(self):
        """
        Identify the coupon dates just before and after the settlement date (SDT).
        The coupon dates are calculated based on the day and month of RDT, with years assigned to ensure SDT falls between them.

        :return: Dictionary containing `coupon1` and `coupon2` with their respective `day`, `month`, and `year`.
        """
        # Extract SDT and RDT information
        sdt_day = self.SDT["day"]
        sdt_month = self.SDT["month"]
        sdt_year = self.SDT["year"]
        rdt_day = self.RDT["day"]
        rdt_month = self.RDT["month"]

        # Determine the two coupon months based on CPY
        if self.CPY == "1/Y":
            # Both coupon dates have the same day and month as RDT
            coupon_months = [rdt_month, rdt_month]
        elif self.CPY == "2/Y":
            # One coupon date is 6 months apart from the other
            other_month = (rdt_month + 6 - 1) % 12 + 1  # Ensure month stays in range 1-12
            coupon_months = sorted([rdt_month, other_month])  # Ensure chronological order

        # Define the coupon dates (only day and month for now)
        coupons = [{"day": rdt_day, "month": month} for month in coupon_months]

        # Logic for year assignment
        for coupon in coupons:
            coupon["year"] = sdt_year  # Initialize with SDT's year

        if self.CPY == "2/Y":
            # Case 1: Both coupons are larger than SDT
            if all((coupon["month"], coupon["day"]) > (sdt_month, sdt_day) for coupon in coupons):
                coupons[0]["year"] = sdt_year  # Smaller one gets SDT's year
                coupons[1]["year"] = sdt_year - 1  # Larger one gets previous year
            # Case 2: Both coupons are smaller than SDT
            elif all((coupon["month"], coupon["day"]) < (sdt_month, sdt_day) for coupon in coupons):
                coupons[0]["year"] = sdt_year + 1  # Smaller one gets next year
                coupons[1]["year"] = sdt_year  # Larger one gets SDT's year
            # Case 3: One coupon is smaller and one larger than SDT
            else:
                if (coupons[0]["month"], coupons[0]["day"]) == (sdt_month, sdt_day):
                    coupons[0]["year"] = sdt_year
                    coupons[1]["year"] = sdt_year
                elif (coupons[1]["month"], coupons[1]["day"]) == (sdt_month, sdt_day):
                    coupons[0]["year"] = sdt_year + 1
                    coupons[1]["year"] = sdt_year

        elif self.CPY == "1/Y":
            # Both coupons are the same; only one needs year adjustment
            if (rdt_month, rdt_day) > (sdt_month, sdt_day):
                coupons[0]["year"] = sdt_year  # One gets SDT's year
                coupons[1]["year"] = sdt_year - 1  # Other gets previous year
            else:
                coupons[0]["year"] = sdt_year + 1  # One gets next year
                coupons[1]["year"] = sdt_year  # Other gets SDT's year

        # Sort coupons into `coupon1` (before) and `coupon2` (after)
        coupons = sorted(coupons, key=lambda x: (x["year"], x["month"], x["day"]))
        coupon1 = {"day": coupons[0]["day"], "month": coupons[0]["month"], "year": coupons[0]["year"]}
        coupon2 = {"day": coupons[1]["day"], "month": coupons[1]["month"], "year": coupons[1]["year"]}

        # Return the results
        return coupon1,  coupon2
    
    def calculate_PRI(self):
        if self.DSR <= self.E:
            """
            Calculate PRI using the provided formula and variables.
            
            Formula:
            PRI = [ (RV + 100 * R / M) / (1 + (DOY / B) * Y / M) ] - [ (A / B) * (100 * R / M) ]
            """
            # First term of the formula
            first_term = (
                (self.RV + (100 * self.R / self.M))
                / (1 + (self.DSR / self.E) * (self.Y / self.M))
            )

            # Second term of the formula
            second_term = (self.A / self.E) * (100 * self.R / self.M)

            # Final PRI calculation
            self.PRI = first_term - second_term
    
                
            


# calculate = Compute()