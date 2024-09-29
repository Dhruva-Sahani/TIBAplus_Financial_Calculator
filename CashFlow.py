import json

class CashflowWorksheet:
    def __init__(self, file_path='CashFlow.json'):
        self.file_path = file_path
        self.cashflows = {}
        self.load_cashflows()

    def load_cashflows(self):
        """Loads cashflow data from Cashflow.json file."""
        # try:
        with open(self.file_path, 'r') as file:
            self.cashflows = json.load(file)
        # except FileNotFoundError:
        #     print(f"{self.file_path} not found. Loading default cashflows.")
        #     self.set_default_cashflows()
            
    def save_cashflows(self):
        """Saves the current cashflows back to the Cashflow.json file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.cashflows, file, indent=4)        
    