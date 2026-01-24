import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_date, get_category, get_description
import os

class CSV:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_File = os.path.join(BASE_DIR, "finance_data.csv")
    Columns = ["date", "amount", "category", "description"]

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
    
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy): or enter for today's date: ", allow_default=True,)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date, amount, category, description)

add()