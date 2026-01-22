import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_File = "fiance_data.csv"
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
    


CSV.initialize_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")