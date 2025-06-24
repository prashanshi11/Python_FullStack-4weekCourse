import os
from datetime import datetime
FILENAME = "expenses.csv"
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME,'w')as file:
            file.write("Date,Category,Description,Amount\n")

def add_expense():
    date=datetime.today().strftime('%Y-%m-%d')
category=input("Enter category(e.g.,Food,Transport,etc):").strip()
description=input("Enter description: ").strip()
amount = input("Enter amount: ").strip()


try:
    float(amount)
except ValueError:
    print ("Invalid amount.")
    return

line = f"{date},{category},{description},{amount}\n"
with open(FILENAME,'a')as file:
    file.write(line)

print("Expense added successfully")

def view_expenses():
    try:
        with open(FILENAME,'r')as file:
            for line in file: 
                parts= line.strip().split(',')
                if 

def search_expenses():
    if not os.path.exists(FILENAME):
        print("No expense file found.")
        return
    
    choice=input()
    keyword=input()
    found=False


    with open(FILENAME,'r')as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            if len(parts) !=4:
                continue
            date.category, description, amount = parts

def main():
    initialize_file()
    while True:
        print("\n--- Personal Expense Tracker---")
        print("1. Add Expenses")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Exit")


        choice = input("choose an option: ")

        if choice == '1':
            add_expense()
            