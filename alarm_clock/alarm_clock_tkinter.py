import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import platform

stop_alarm = False
alarm_thread = None

def play_sound():
    """ play sound until stopped"""
    global stop_alarm
    try:
        if platform.system() == "Windows":
            import winsound
            while not stop_alarm:
                winsound.Beep(1000, 500)
                time.sleep(0.5)
        else:
            while not stop_alarm:
                print('\a', end="", flush=True)
                time.sleep(0.5)
    except Exception as e:
        print("sound not availble..", e)


def start_alarm(alarm_time):
    """Check tiem and trigger alarm"""
    global stop_alarm
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time and not stop_alarm:
            status_label.config(text="Time's up", fg="red")

            #start sound first
            sound_thread = threading.Thread(target=play_sound, daemon=True)
            sound_thread.start()

            # showing pop up
            messagebox.showinfo("Alarm", "Time's up")
            break
        time.sleep(1)


def set_alarm():
    global stop_alarm, alarm_thread
    stop_alarm = False
    alarm_time = f"{hour_var.get()}:{minute_var.get()}"
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format")
        return

    # cancel existing alrm thread if any
    if alarm_thread and alarm_thread.is_alive():
        stop_alarm_sound()

    alarm_thread = threading.Thread(target=start_alarm, args=(alarm_time,), daemon=True)
    alarm_thread.start()
    status_label.config(text=f"Alarm set for time: {alarm_time}", fg="blue")



def stop_alarm_sound():
    global stop_alarm
    stop_alarm = True
    status_label.config(text="Alarm stopped", fg="gray")

def cancel_alarm():
    global stop_alarm
    stop_alarm = True
    status_label.config(text="Alarm cancelled", fg="gray")

def update_clock():
    """update live clock display every second"""
    now = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# ==================tkinter gui=======================
root = tk.Tk()
root.title("Alarm clock")

tk.Label(root, text="Hour (HH):").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Minute (MM):").grid(row=1, column=0, padx=5, pady=5)

hour_var = tk.StringVar(value="07")
minute_var = tk.StringVar(value="00")

hour_entry = tk.Entry(root, textvariable=hour_var, width=5)
minute_entry = tk.Entry(root, textvariable=minute_var, width=5)

hour_entry.grid(row=0, column=1, padx=5, pady=5)
minute_entry.grid(row=1, column=1, padx=5, pady=5)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
cancel_button = tk.Button(root, text="Cancel Alarm", command=cancel_alarm)
stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm_sound)

set_button.grid(row=2, column=0, padx=5, pady=10)
cancel_button.grid(row=2, column=1, padx=5, pady=10)
stop_button.grid(row=2, column=2, padx=5, pady=10)


#status label
status_label = tk.Label(root, text="No alarm set", fg="blue")
status_label.grid(row=3, column=0, columnspan=2, pady=10)


#live clock
clock_label = tk.Label(root, text="", font=("Helvetica", 16), fg="green")
clock_label.grid(row=4, column=0, columnspan=3, pady=10)
update_clock()
root.mainloop()
