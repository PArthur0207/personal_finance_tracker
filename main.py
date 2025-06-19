import pandas as pd
import csv
from datetime import datetime
from data_entry import DataEntry
import matplotlib.pyplot as plt

class Csv:
    csv_file = "finance_data.csv"
    columns = ["date", "amount", "category", "description"]
    date_format = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            data_frame = pd.DataFrame(columns = cls.columns)
            data_frame.to_csv(cls.csv_file, index = False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.csv_file, "a", newline = "") as csv_file_2:
            writer = csv.DictWriter(csv_file_2, fieldnames = cls.columns)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        data_frame = pd.read_csv(cls.csv_file)
        data_frame["date"] = pd.to_datetime(data_frame["date"], format = Csv.date_format)
        start_date = datetime.strptime(start_date, Csv.date_format)
        end_date = datetime.strptime(end_date, Csv.date_format)

        mask = (data_frame["date"] >= start_date) & (data_frame["date"] <= end_date)
        filtered_data_frame = data_frame.loc[mask]

        if filtered_data_frame.empty:
            print("No transaction found in the date range")
        else:
            print(f"Transaction from {start_date.strftime(Csv.date_format)} to {end_date.strftime(Csv.date_format)}")
            print(filtered_data_frame.to_string(index = False, formatters = {"date": lambda x: x.strftime(Csv.date_format)}))

            total_income = filtered_data_frame[filtered_data_frame["category"] == "Income"] ["amount"].sum()
            total_expense = filtered_data_frame[filtered_data_frame["category"] == "Expense"] ["amount"].sum()
            print("\nSummary:")
            print(f"Total income: ${total_income:.2f}")
            print(f"Total expense: ${total_expense:.2f}")
            print(f"Net savings ${(total_income - total_expense):.2f}")

        return filtered_data_frame

get_entry = DataEntry()
class TrialInputs:
    def __init__(self):
        Csv.initialize_csv()
        
    def add_to_csv(self):
        self.date = get_entry.get_date(
            "Enter the date of the transaction (dd-mm-yyyy) or enter for todays date: ",
            allow_default = True
            )
        self.amount = get_entry.get_amount()
        self.category = get_entry.get_category()
        self.description = get_entry.get_description()
        Csv.add_entry(self.date, self.amount, self.category, self.description)

    def plot_transactions(self, data_frame):
        self.data_frame.set_index("date", inplace = True)

        self.income_data_frame = (
            self.data_frame[self.data_frame["category"] == "Income"]
            .resample("D")
            .sum()
            .reindex(self.data_frame.index, fill_value = 0)
            )
        self.expense_data_frame = (
            self.data_frame[self.data_frame["category"] == "Expense"]
            .resample("D")
            .sum()
            .reindex(self.data_frame.index, fill_value = 0)
            )
        plt.figure(figsize = (10, 5))
        plt.plot(self.income_data_frame.index, self.income_data_frame["amount"], label = "Income", color = "g")
        plt.plot(self.expense_data_frame.index, self.expense_data_frame["amount"], label = "Expense", color = "r")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income and Expenses over time")
        plt.legend()
        plt.grid(True)
        plt.show()

    def main(self):
        while True:
            print("1. Add a new transaction")
            print("2. Print transaction summary within a date range")
            print("3. Exit")
            self.choice = input("Choose from 1-3: ").strip()
            if self.choice == '1':
                self.add_to_csv()
            elif self.choice == '2':
                self.start_date = get_entry.get_date("Enter the start date (dd-mm-yyyy): ")
                self.end_date = get_entry.get_date("Enter the end date (dd-mm-yyyy): ")
                self.data_frame = Csv.get_transactions(self.start_date, self.end_date)
                if input("Do you want to see a plot of this? (y/n) ").lower() != 'n':
                    self.plot_transactions(self.data_frame)
            elif self.choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please pick from 1-3")

try_now = TrialInputs()

if __name__ == "__main__":
    try_now.main()
    
