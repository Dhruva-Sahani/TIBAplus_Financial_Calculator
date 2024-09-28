import json

class TimeValueOfMoney:
    def __init__(self, display1, display2):
        self.display1 = display1
        self.display2 = display2
        self.file_path = "TimeValueOfMoney.json"
        self.data = self.load_time_value_of_money()

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
                try:
                    # Set the new value as current_value for the keytype
                    key_data["current_value"] = int(new_value)
                    
                    # Update the displays
                    self.display2.setText(f"{key_data['key']}=")
                    self.display1.setText(str(new_value))

                    # Save the updated value in the JSON file
                    self.save_time_value_of_money()

                except ValueError:
                    print(f"Invalid value for {keytype}. Please check the input.")
            else:
                print(f"Key {keytype} is not of type 'Enter-or-compute'.")
        else:
            print(f"Key {keytype} not found in TimeValueOfMoney data.") 