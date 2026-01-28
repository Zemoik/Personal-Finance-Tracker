import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_date, get_category, get_description
import os
import matplotlib.pyplot as plt

class CSV:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_File = os.path.join(BASE_DIR, "finance_data.csv")
    Columns = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_File)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.Columns)
            df.to_csv(cls.CSV_File, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open (cls.CSV_File, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.Columns)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transcations(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_File)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        mask = (df["date"] >= start_date) & (df["date"]<=end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index = False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))


            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            print("\nSummery:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: $ {(total_income-total_expense):.2f}")

        return filtered_df

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy): or enter for today's date: ", allow_default=True,)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date, amount, category, description)


def plot_transactions(df):
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df = df.sort_values("date")

    # Create full date range
    all_dates = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq="D")

    income_df = df[df["category"] == "Income"].groupby("date")["amount"].sum()
    expense_df = df[df["category"] == "Expense"].groupby("date")["amount"].sum()

    # Reindex to full range and fill missing with 0
    income_df = income_df.reindex(all_dates, fill_value=0)
    expense_df = expense_df.reindex(all_dates, fill_value=0)

    plt.figure()
    plt.plot(all_dates, income_df, label="Income")
    plt.plot(all_dates, expense_df, label="Expense")

    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income vs Expense Over Time")
    plt.legend()
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and a summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice =="1":
            add()
        elif choice == "2":
            start = get_date("Enter the start date (dd-mm-yyyy): ")
            end = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transcations(start, end)
            if input("Do you want to see a plot (y/n) ").lower()=="y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3. ")


if __name__ == "__main__":
    main()