import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        total_seconds = int(entry.get())
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid input", "Plese enter a valid number of seconds")


def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        label.config(text=time_format)
        root.after(1000, countdown, seconds-1)
    else:
        label.config(text="00:00")
        messagebox.showinfo("Time's up", "Countdown finished")


root = tk.Tk()
root.title("Countdown timer")
root.geometry("300x200")
root.config(bg="#f4f4f9")


heading = tk.Label(root, text="Countdown timer", font=("Arial", 18, "bold"), bg="#f4f4f9")
heading.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)
entry.insert(0,"10")


start_button = tk.Button(root, text="start", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", width=10, command=start_timer)
start_button.pack(pady=10)


label = tk.Label(root, text="00:00", font=("Arial", 24,"bold"), bg="#f4f4f9")
label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Aria", 10,"bold"), bg="#f44336",
                        fg="white", width=8, command=root.destroy)
exit_button.pack(pady=5)

root.mainloop()
