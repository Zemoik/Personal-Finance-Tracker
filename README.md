# 💰 Personal Finance Tracker

A command-line personal finance tracker that logs transactions to a CSV file, 
summarizes income vs. expenses over a date range, and plots spending trends 
over time using matplotlib.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)

## Features

- Log income and expense transactions with date, amount, category, and description
- Auto-initializes a CSV file to persist all transaction data locally
- Query transactions within any custom date range
- Summary report showing total income, total expenses, and net savings
- Line chart visualization of income vs. expenses over time using matplotlib
- Input validation on all fields — dates, amounts, and categories

## Demo
```
1. Add a new transaction
2. View transactions and a summary within a date range
3. Exit

Enter your choice: 2
Enter the start date (dd-mm-yyyy): 01-01-2025
Enter the end date (dd-mm-yyyy): 31-03-2025

Transactions from 01-01-2025 to 31-03-2025
date        amount  category   description
01-01-2025  2500.00  Income    Paycheck
05-01-2025   120.00  Expense   Groceries
...

Summary:
Total Income:   $5000.00
Total Expense:  $1340.00
Net Savings:    $3660.00

Do you want to see a plot (y/n): y
```

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3 |
| Data handling | pandas |
| Visualization | matplotlib |
| Storage | CSV (via Python csv module) |

## Setup
```bash
git clone https://github.com/Zemoik/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker
pip install pandas matplotlib
python main.py
```

No database or internet connection required. All data is stored locally 
in `finance_data.csv`.

## Project Structure
```
Personal-Finance-Tracker/
├── main.py          # Main app loop, transaction logic, plotting
├── data_entry.py    # Input validation for date, amount, category, description
├── finance_data.csv # Auto-generated on first run
└── README.md
```

## What I Learned

- Reading, writing, and filtering CSV data with pandas DataFrames
- Date parsing and range filtering using pandas and Python's datetime module
- Plotting time-series data with matplotlib including reindexing to fill date gaps
- Separating concerns across modules (data_entry.py vs main.py)
- Building a CLI app with input validation and recursive error handling

## Author

**Dev Patel** — [LinkedIn](https://www.linkedin.com/in/dev--patel--/) 
· [GitHub](https://github.com/Zemoik)
