# 💰 Finance Tracker CLI

A simple and interactive finance tracker built in Python. It uses object-oriented programming (OOP) principles to log, view, and analyze your income and expenses using the command line.

## 📌 Features

- Record transactions (date, amount, category, description)
- Automatically store data in a CSV file
- Filter transactions within a date range
- Calculate total income, expenses, and net savings
- Visualize transactions using line plots
- Robust input validation

## 🛠️ Technologies Used

- Python 3.x
- pandas for data manipulation
- csv module for file I/O
- matplotlib for plotting
- Object-Oriented Programming (OOP)

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

Encapsulation — Groups related behavior (e.g., data input, file operations) into classes. Hides internal logic from users.  
→ Used in: DataEntry, FinanceCSV, AppController

Abstraction — Simplifies complex operations into clean methods like get_amount(), add_entry().  
→ Used in: All class methods

Inheritance — Planned for future 
→ To be implemented

Polymorphism — Example: get_date() behaves differently depending on the input (with or without default).  
→ Used in: get_date() in DataEntry

## 📁 Project Structure

finance-tracker-cli/
├── data_entry.py       # Handles user input and validation  
├── finance_csv.py      # Handles CSV operations  
├── main.py             # Main application and menu    
├── README.md  

## 🙏 Credits

This project is based on a tutorial by Tech With Tim  
Original video: [https://youtube.com/\[VIDEO_ID\]](https://youtu.be/Dn1EjhcQk64?si=aYOAeSP6G2fKhbwy)

Special thanks to the creator for the inspiration and learning experience.


