import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# load expenses
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


# save expenses
def save_expenses(expenses):
    with open(FILE_NAME, mode="w", newline="") as fp:
        fieldnames = ["date", "category", "amount", "note"]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.expenses = load_expenses()

        # input Frame
        input_frame = tk.Frame(root, padx=10, pady=10)
        input_frame.pack(fill="x")
        
        tk.Label(input_frame, text="Category").grid(row=0, column=0, padx=5)
        self.category_entry = tk.Entry(input_frame)
        self.category_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Amount").grid(row=0, column=2, padx=5)
        self.amount_entry = tk.Entry(input_frame, width=30)
        self.amount_entry.grid(row=0, column=3, padx=5)


        tk.Label(input_frame, text="Note").grid(row=0, column=4, padx=5)
        self.note_entry = tk.Entry(input_frame, width=30)
        self.note_entry.grid(row=0, column=5, padx=5)

        tk.Button(input_frame, text="Add expense", command=self.add_expense).grid(row=0, column=6, padx=5)

        # treeview for table
        self.tree = ttk.Treeview(root, columns=("Date", "Category", "Amount", "Note"), show="headings", height=12)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        for col in  ("Date", "Category", "Amount", "Note"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.load_tree()


        # buttons
        btn_frame = tk.Frame(root, pady=5)
        btn_frame.pack()

        tk.Button(btn_frame, text="Delete", command=self.delete_expense).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Edit", command=self.edit_expense).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Search", command=self.search_expenses).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Summary", command=self.view_summary).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.load_tree).grid(row=0, column=4, padx=5)

    def load_tree(self, filtered=None):
        # clear table
        for row in self.tree.get_children():
            self.tree.delete(row)

        data = filtered if filtered else self.expenses
        for exp in data:
            self.tree.insert("", "end", values=(exp["date"], exp["category"], exp["amount"], exp["note"]))


    def add_expense(self):
        try:
            category = self.category_entry.get().strip()
            amount = float(self.amount_entry.get().strip())
            note = self.note_entry.get().strip()
            date = datetime.now().strftime("%Y-%m-%d")

            if not category or amount <= 0:
                raise ValueError("Invalid input")

            exp = {"date":date, "category":category, "amount":amount, "note":note}
            self.expenses.append(exp)
            save_expenses(self.expenses)
            self.load_tree()
            self.category_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.note_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid data: {e}")

    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select an expense to delete")
            return
        index = self.tree.index(selected[0])
        deleted = self.expenses.pop(index)
        save_expenses(self.expenses)
        self.load_tree()
        messagebox.showinfo("Deleted", f"deleted: {deleted['category']} {deleted['amount']}")


    def edit_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("warning", "select an expense to edit")
            return
        index = self.tree.index(selected[0])
        exp = self.expenses[index]

        edit_win = tk.Toplevel(self.root)
        edit_win.title("Edit expense")

        tk.Label(edit_win, text="Category").grid(row=0, column=0)
        cat_entry = tk.Entry(edit_win)
        cat_entry.insert(0, exp["category"])
        cat_entry.grid(row=0, column=1)

        tk.Label(edit_win, text="Amount").grid(row=1, column=0)
        amt_entry = tk.Entry(edit_win)
        amt_entry.insert(0, exp["amount"])
        amt_entry.grid(row=1, column=1)

        tk.Label(edit_win, text="Note").grid(row=2, column=0)
        note_entry = tk.Entry(edit_win)
        note_entry.insert(0, exp["note"])
        note_entry.grid(row=2, column=1)


        def save_edit():
            try:
                exp["category"] = cat_entry.get().strip()
                exp["amount"] = float(amt_entry.get().strip())
                exp["note"] = note_entry.get().strip()
                save_expenses(self.expenses)
                self.load_tree()
                edit_win.destroy()
            except ValueError:
                messagebox.showerror("error", "Invalid amount")

        tk.Button(edit_win, text="Save", command=save_edit).grid(row=3, column=0, columnspan=2)

    def search_expenses(self):
        keyword = tk.simpledialog.askstring("Search", "Enter category: (category/date/note):")
        if keyword:
            results = [exp for exp in self.expenses if keyword.lower() in exp["category"].lower()
                      or keyword.lower() in exp["note"].lower()
                      or keyword in exp["date"]]
            self.load_tree(results)

    def view_summary(self):
        summary = {}
        for exp in self.expenses:
            summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
        msg = "\n".join([f"{cat}: {total}" for cat,total in summary.items()])
        messagebox.showinfo("Summary", msg if msg else "No Data")


# run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
        
