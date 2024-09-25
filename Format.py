import json

class Settings:
    def __init__(self, display1, display2):
        # Load settings from the JSON file
        self.display1= display1
        self.display2 = display2
        self.file_path = "Settings.json"
        self.settings_data = self.load_settings()
        self.keys_list = list(self.settings_data.keys())  # List of keys to navigate
        self.current_index = 0  # Keep track of which key is currently selected
        self.resetflag = False
    
    def load_settings(self):
        # Load the settings JSON file
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading file {self.file_path}: {e}")
            return {}

    def save_settings(self):
        # Save the modified settings back to the JSON file
        with open(self.file_path, 'w') as file:
            json.dump(self.settings_data, file, indent=4)

    def move_up(self):
        # Move up in the list of keys
        self.current_index = (self.current_index - 1) % len(self.keys_list)
        self.display_current_key()

    def move_down(self):
        # Move down in the list of keys
        self.current_index = (self.current_index + 1) % len(self.keys_list)
        self.display_current_key()

    def set(self):
        # Switch between available options if the current key is of type "switch"
        current_key = self.keys_list[self.current_index]
        key_data = self.settings_data[current_key]
        
        if key_data["type"] == "switch":
            options = key_data["options"]
            current_value = key_data["current_value"]
            # Find the next option in the list
            next_index = (options.index(current_value) + 1) % len(options)
            key_data["current_value"] = options[next_index]
            self.save_settings()  # Save the changes
            self.display_current_key()

    def enter(self, new_value):
        # Set the number displayed on the screen as the current value for keys of type "input"
        new_value= int(new_value)
        new_value= round(new_value)
        current_key = self.keys_list[self.current_index]
        key_data = self.settings_data[current_key]
        
        if self.resetflag:
            self.reset()
        
        elif key_data["type"] == "input":
            if key_data["range"][0] <= new_value <= key_data["range"][1]:
                key_data["current_value"] = new_value
                self.save_settings()  # Save the changes
                # print(f"{current_key} set to {key_data['current_value']}")
            else:
                print(f"Value {new_value} is out of range for {current_key}.")

    def read(self, key):
        # Read and return the current value for a given key
        if key in self.settings_data:
            return self.settings_data[key]["current_value"]
        else:
            print(f"Key '{key}' not found.")
            return None
        
    def reset_activate(self):
        self.resetflag= True
        self.display2.setText('RST')
        self.display1.setText('?          ')
        
    def reset(self):
        for key, key_data in self.settings_data.items():
            key_data['current_value'] = key_data['default_value']
        self.save_settings()
        self.display2.setText('RST')
        self.display1.setText('0.00')
        self.resetflag = False
        

    def display_current_key(self):
        # Display the current key and its value (for debugging purposes)
        current_key = self.keys_list[self.current_index]
        current_type = self.settings_data[current_key]["type"]
        
        if current_type == 'switch':
            current_value = self.settings_data[current_key]["current_value"]
            options = self.settings_data[current_key]["options"]
            options_example = self.settings_data[current_key]["options_example"]  # Get examples
            
            # Get the index of the current value in the options
            value_index = options.index(current_value)
            
            # Set display2 to show the current value
            self.display2.setText(str(current_value))
            
            # Set display1 to show the example corresponding to the current value's index
            self.display1.setText(str(options_example[value_index]))
            
        elif current_type == 'input':
            self.display2.setText(str(self.settings_data[current_key]['display_key']))
            self.display1.setText(str(self.settings_data[current_key]["current_value"]))
            
    
