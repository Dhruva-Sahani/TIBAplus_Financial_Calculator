import json
from OperationsLogic import OperationsLogic

class Memory:
    def __init__(self, display1, display2):
        self.file_path = 'Memory.json'
        self.display1 = display1
        self.display2 = display2
        self.current_index = 0 #setting current display to 1
        self.recall_flag = False
        self.memory_data = {}
        self.load_memory()

    def load_memory(self):
        """Loads memory values from the Memory.json file."""
        try:
            with open(self.file_path, 'r') as file:
                self.memory_data = json.load(file)
        except FileNotFoundError:
            print("Memory file not found, loading defaults.")
            self.memory_data = {
                str(i): {"key": f"M{i}", "current_value": 0, "default_value": 0}
                for i in range(10)
            }

    def save_memory(self):
        """Saves the current memory values to the Memory.json file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.memory_data, file, indent=4)
       
        
    def move_up(self):
            """Move up to the previous memory key in a loop (M0 to M9)."""
            self.current_index = (self.current_index - 1) % 10
            self.display_current_key()

    def move_down(self):
        """Move down to the next memory key in a loop (M0 to M9)."""
        self.current_index = (self.current_index + 1) % 10
        self.display_current_key()

    def display_current_key(self):
        """Display the current key and its value."""
        current_key = self.memory_data[str(self.current_index)]["key"]
        current_value = self.memory_data[str(self.current_index)]["current_value"]
        self.display1.setText(str(current_value))  # Displaying the current value in display1
        self.display2.setText(f"{current_key}=")  # Displaying the key followed by '=' in display2
        
    def memory(self):
        self.current_index = 0
        self.display_current_key()
        
    def enter(self, new_value):
        """Update the current key's value, save, and update display."""
        # Set the new value for the currently displayed key
        self.memory_data[str(self.current_index)]["current_value"] = float(new_value)
        # Save the updated memory data to file
        self.save_memory()
        # Update the display with the new value
        self.display_current_key()
        
    def clear_work(self, null):
        for key, data in self.memory_data.items():
            data['current_value'] = data['default_value']
        self.save_memory()
        self.display_current_key()
        
    def recall_active(self):
        self.recall_flag = True
        
    def recall_deactive(self):
        self.recall_flag = False
        
    def recall_num(self, instance, num):
        instance.current_number = str(self.memory_data[str(num)]['current_value']) 
        self.display1.setText(instance.current_number)
        self.recall_deactive()
        
    def recall_tvm(self, instancetvm, instanceop, para):
        instanceop.current_number = str(instancetvm.data[para]['current_value'])
        self.display2.setText(f"{instancetvm.data[para]['key']}=")
        self.display1.setText(str(instancetvm.data[para]['current_value']))
        self.recall_deactive()
        
    
        
    
        
        