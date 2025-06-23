from datetime import datetime

class DataEntry:
    DATE_FORMAT = "%d-%m-%Y"
    CATEGORY_MAP = {"I": "Income", "E": "Expense"}

    def get_date(self, prompt, allow_default=False):
        user_input = input(prompt).strip()

        if allow_default and not user_input:
            return datetime.today().strftime(self.DATE_FORMAT)

        try:
            parsed_date = datetime.strptime(user_input, self.DATE_FORMAT)
            return parsed_date.strftime(self.DATE_FORMAT)
        except ValueError:
            print("Invalid date format. Please enter the date as dd-mm-yyyy.")
            return self.get_date(prompt, allow_default)

    def get_amount(self):
        try:
            amount = float(input("Enter the amount: ").strip())
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            return amount
        except ValueError as e:
            print(e)
            return self.get_amount()

    def get_category(self):
        category = input("Enter category ('I' for Income, 'E' for Expense): ").strip().upper()
        if category in self.CATEGORY_MAP:
            return self.CATEGORY_MAP[category]
        print("Invalid input. Use 'I' for Income or 'E' for Expense.")
        return self.get_category()

    def get_description(self):
        return input("Enter a description (optional): ").strip()
