import pandas as pd
import csv
from datetime import datetime
from data_entry import DataEntry

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

Csv.get_transactions("14-11-2024", "19-06-2025")
