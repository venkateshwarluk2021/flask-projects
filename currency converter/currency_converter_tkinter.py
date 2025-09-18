import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "https://api.frankfurter.app/latest"

def currency_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_combo.get()
        to_curr = to_combo.get()

        if from_curr == to_curr:
            messagebox.showwarning("Warning","Source and Target currencies must be different")
            return

        response = requests.get(f"{API_URL}?amount={amount}&from={from_curr}&to={to_curr}")
        data = response.json()

        if "rates" in data and to_curr in data["rates"]:
            result = data["rates"][to_curr]
            result_label.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
        else:
            messagebox.showerror("Error", "conversion failed.check currency rates")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of amount")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong {e}")



#-----------tkinter UI----------
root = tk.Tk()
root.title("Currency Converter.")
root.geometry("400x250")
root.resizable(False, False)

currencies = ["USD", "INR", "EUR", "GBP", "JPY"]

# Amount input
tk.Label(root, text="Enter Amount: ").pack(pady=5)
amount_entry = tk.Entry(root, width=20)
amount_entry.pack()


# currency dropdowns
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0,padx=5)
from_combo = ttk.Combobox(frame, values=currencies, state="readonly")
from_combo.grid(row=0, column=1)
from_combo.set("USD")

tk.Label(frame, text="To:").grid(row=0, column=2, padx=5)
to_combo = ttk.Combobox(frame, values=currencies, state="readonly")
to_combo.grid(row=0, column=3)
to_combo.set("INR")

# convert button
convert_button = tk.Button(root, text="Convert", command=currency_convert, bg="blue", fg="white")
convert_button.pack(pady=10)

# result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
