import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from data_entry import DataEntry


class FinanceCSV:
    FILE_NAME = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize(cls):
        try:
            pd.read_csv(cls.FILE_NAME)
        except FileNotFoundError:
            pd.DataFrame(columns=cls.COLUMNS).to_csv(cls.FILE_NAME, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.FILE_NAME, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.FILE_NAME)
        df["date"] = pd.to_datetime(df["date"], format=cls.DATE_FORMAT)
        start_dt = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_dt = datetime.strptime(end_date, cls.DATE_FORMAT)

        filtered_df = df[(df["date"] >= start_dt) & (df["date"] <= end_dt)]

        if filtered_df.empty:
            print("No transactions found in the date range.")
        else:
            print(f"Transactions from {start_dt.strftime(cls.DATE_FORMAT)} to {end_dt.strftime(cls.DATE_FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(cls.DATE_FORMAT)}))

            income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            print("\nSummary:")
            print(f"Total Income: ${income:.2f}")
            print(f"Total Expense: ${expense:.2f}")
            print(f"Net Savings: ${income - expense:.2f}")

        return filtered_df


class FinanceApp:
    def __init__(self):
        self.data_entry = DataEntry()
        FinanceCSV.initialize()

    def add_transaction(self):
        date = self.data_entry.get_date(
            "Enter transaction date (dd-mm-yyyy) or press enter for today: ", allow_default=True)
        amount = self.data_entry.get_amount()
        category = self.data_entry.get_category()
        description = self.data_entry.get_description()
        FinanceCSV.add_entry(date, amount, category, description)

    def plot_transactions(self, df):
        df.set_index("date", inplace=True)
        income_df = (
            df[df["category"] == "Income"]
            .resample("D").sum()
            .reindex(df.index, fill_value=0)
        )
        expense_df = (
            df[df["category"] == "Expense"]
            .resample("D").sum()
            .reindex(df.index, fill_value=0)
        )

        plt.figure(figsize=(10, 5))
        plt.plot(income_df.index, income_df["amount"], label="Income", color="green")
        plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="red")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income vs Expenses Over Time")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def run(self):
        while True:
            print("\n===== Finance Tracker Menu =====")
            print("1. Add a new transaction")
            print("2. View transactions in date range")
            print("3. Exit")
            choice = input("Choose an option (1-3): ").strip()

            if choice == '1':
                self.add_transaction()
            elif choice == '2':
                start = self.data_entry.get_date("Enter start date (dd-mm-yyyy): ")
                end = self.data_entry.get_date("Enter end date (dd-mm-yyyy): ")
                df = FinanceCSV.get_transactions(start, end)
                if not df.empty:
                    if input("Would you like to plot the transactions? (y/n): ").lower() == 'y':
                        self.plot_transactions(df)
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid option. Please choose from 1-3.")


if __name__ == "__main__":
    app = FinanceApp()
    app.run()
