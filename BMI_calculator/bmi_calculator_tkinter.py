import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        height = height/100

        bmi = (weight)/(height**2)
        if bmi < 18.5:
            category = 'underweight'
        elif bmi < 25:
            category = 'normal'
        elif bmi < 30:
            category = 'overweight'
        else:
            category = 'obese'
        category = category.capitalize()
        result = f"BMI: {bmi:.2f} - Category: {category}"
        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Enter weight(kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.focus()
weight_entry.pack()

tk.Label(root, text="Enter Height(cm): ").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()


calc_btn = tk.Button(root, text="Calculate BMI", bg="blue", fg="white", command=calculate_bmi)
calc_btn.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12,"bold"))
result_label.pack(pady=10)

weight_entry.delete(0, tk.END)
height_entry.delete(0, tk.END)

root.mainloop()
