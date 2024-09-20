import json

class Settings:
    def __init__(self, settings_file="settings.json"):
        self.settings_file = settings_file
        self.default_settings = {
            "decimal_places": 2,
            "angle_unit": "DEG",
            "date_format": "US",
            "number_separators": "US",
            "calculation_method": "Chn"
        }
        self.load_settings()

    def load_settings(self):
        """Load settings from the JSON file, or use default if the file doesn't exist."""
        try:
            with open(self.settings_file, "r") as file:
                self.settings = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.settings = self.default_settings
            self.save_settings()

    def save_settings(self):
        """Save the current settings to the JSON file."""
        with open(self.settings_file, "w") as file:
            json.dump(self.settings, file, indent=4)

    def update_setting(self, key, value):
        """Update a specific setting."""
        if key in self.settings:
            self.settings[key] = value
            self.save_settings()
            
    def read_setting(self, key):
        """Read and return a specific setting."""
        return self.settings.get(key, None)

    def reset_to_default(self):
        """Reset all settings to default."""
        self.settings = self.default_settings.copy()
        self.save_settings()
        
