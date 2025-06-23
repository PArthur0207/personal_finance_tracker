# 💰 Finance Tracker CLI

A simple and interactive finance tracker built in Python. It uses object-oriented programming (OOP) principles to log, view, and analyze your income and expenses using the command line.

## 📌 Features

- Add transactions (date, amount, category, description)
- Store data in both **CSV** and **JSON** formats
- Filter transactions by date range
- Summarize income, expenses, and net savings
- Visualize daily income vs. expenses with line plots
- User input validation

## 🛠️ Technologies Used

- Python 3.x  
- `pandas` for data manipulation  
- `csv` and `json` modules for file I/O  
- `matplotlib` for visualizing transactions  
- Object-Oriented Programming (OOP) concepts  

## 🚀 How to Use

1. Clone the repository:

   git clone https://github.com/PArthur0207/personal_finance_tracker.git
   cd personal_finance_tracker

2. Install dependencies:

   pip install pandas matplotlib

3. Run the app:

   python main.py

4. Choose from the menu:
   - 1 - Add a new transaction
   - 2 - View and plot transactions in a date range
   - 3 - Exit

## 🧠 OOP Concepts Used

This project demonstrates the 4 pillars of Object-Oriented Programming (OOP):

🔒 Encapsulation
Groups related data and behavior into classes like DataEntry and FinanceStorage, hiding internal logic and exposing only useful interfaces.

Used in: DataEntry, FinanceStorage, FinanceApp

🎭 Abstraction
Complex logic is hidden inside clean, user-friendly methods like get_amount(), add_entry(), and plot_transactions().

Used in: All class methods

🧬  Inheritance
Allows a class to reuse and extend the functionality of another class. CustomDataEntry inherits all methods from DataEntry and modifies only the get_description() method to customize its behavior.

Used in: CustomDataEntry inherits from DataEntry

🔁 Polymorphism  
The method `write_entry(data)` is defined in the base class but behaves differently in each subclass.
 
Used in: CSVStorage.write_entry() saves to CSV, JSONStorage.write_entry() saves to JSON  

## 📁 Project Structure

```
finance_tracker/
├── main.py               # Main app logic and menu
├── data_entry.py         # Handles user input
├── custom_data_entry.py  # Handles user input
├── finance_data.csv      # Your transaction records (CSV)
├── finance_data.json     # Same records in JSON format
├── README.md             # This file
```


## 🙏 Credits

This project is based on a tutorial by Tech With Tim  
Original video: [https://youtube.com/\[VIDEO_ID\]](https://youtu.be/Dn1EjhcQk64?si=aYOAeSP6G2fKhbwy)

Special thanks to the creator for the inspiration and learning experience.
