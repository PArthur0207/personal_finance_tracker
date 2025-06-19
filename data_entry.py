from datetime import datetime

class DataEntry:
    date_format = "%d-%m-%Y"
    categories = {"I": "Income", "E" : "Expense"}

    def get_date(self, prompt, allow_default = False):
        self.date_string = input(prompt)
        if allow_default and not self.date_string:
            return datetime.today().strftime(self.date_format)   
        
        try:
            self.valid_date = datetime.strptime(self.date_string, self.date_format)
            return self.valid_date.strftime(self.date_format)
        except ValueError:
            print("Invalid date input. Please enter the date in dd-mm-yyyy format")
            return self.get_date(prompt, allow_default)
        
    def get_amount(self):
        try:
            self.amount = float(input("Enter the amount: "))
            if self.amount <= 0:
                raise ValueError("Amount must be a non-negative and non-zero number")
            return self.amount
        except ValueError as e:
            print(e)
            return self.get_amount()
        
    def get_category(self):
        self.category = input("Input the category here('I' for Income, 'E' for Expense): ").upper()
        if self.category in self.categories:
            return self.categories[self.category]
        print("Invalid input. Please enter 'I' for Income, 'E' for Expense")
    
    def get_description(self):
        return input("Enter a description(optional): ")




