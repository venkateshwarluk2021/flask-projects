import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# load expenses from a CSV if exists
def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode="r", newline="") as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

    except FileNotFoundError:
        pass
    return expenses

# save expenses to csv
def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as fp:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# add new expense
def add_expense(expenses):
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category: (Food/transport/shopping) etc:\t")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional) :\t")
    expense = {"date": date, "category": category, "amount": amount, "note": note}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully ")

# view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")

# view total by category
def view_summary(expenses):
    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    print("Expenses summary by Category :")
    for category, total in summary.items():
        print(f"{category} : {total}")


# search expenses by note, category, date
def search_expenses(expenses):
    keyword = input("Enter search keyword (category/note/date)").lower()
    results = [exp for exp in expenses if keyword in exp["category"].lower()
               or keyword in exp["note"].lower()
               or keyword in exp["date"]]
    if results:
        print("Search results")
        for i, exp in enumerate(results, 1):
            print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")
    else:
        print("No matching expenses found")

# delete expense by index from list
def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("Enter the expense number to delete: \t"))
        if 1 <= index <= len(expenses):
            deleted = expenses.pop(index - 1)
            save_expenses(expenses)
            print(f"Deleted: {deleted['date']} | {deleted['category']} | {deleted['amount']}")
        else:
            print("invalid number ")
    except ValueError:
        print("Enter a valid number: ")


# edit response

def edit_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("Enter the expense number to edit: \t"))
        if 1 <= index <= len(expenses):
            exp = expenses[index - 1]
            print(f"\nEditing: {exp['date']} | {exp['category']} | {exp['amount']} | {exp['note']}")

            new_category = input(f"New category: (or Enter to keep {exp['category']})")
            new_amount = input(f"New amount: (or Enter to keep {exp['amount']})")
            new_note = input(f"New note: (or Enter to keep {exp['note']})")

            if new_category.strip():
                exp['category'] = new_category
            if new_amount.strip():
                try:
                    exp["amount"] = float(new_amount)
                except ValueError:
                    print("Invalid amount, keeping the old value")
            if new_note.strip():
                exp["note"] = new_note

            save_expenses(expenses)
            print("Expense updated successfully")

        else:
            print("Invalid Number")
    except ValueError:
        print("enter a valid number")
       

# main menu
def main():
    expenses = load_expenses()
    while True:
        print("\n-----------Personal expense tracker---------------")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Search expenses")
        print("5. Delete expenses")
        print("6. Edit expense")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            search_expenses(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            edit_expense(expenses)
        elif choice == "7":
            print("Exiting .....Goodbye")
            break
        else:
            print("Invalid choice. try again")


if __name__ == "__main__":
    main()
