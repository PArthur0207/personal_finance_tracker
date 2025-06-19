import pandas as pd
import csv
from datetime import datetime
from data_entry import DataEntry

class Csv:
    csv_file = "finance_data.csv"
    columns = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.columns)
            df.to_csv(cls.csv_file, index = False)
    
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

test = TrialInputs()
test.add_to_csv()
