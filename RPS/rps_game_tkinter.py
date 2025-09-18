import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "it's a tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win"
    else:
        result = "Computer wins"

    label_result.config(text=f"You chose: {user_choice} \nComputer chose: {computer_choice}\n\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")

label_title = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text="Rock", width=10, command=lambda: play("rock"))
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(frame_buttons, text="Paper", width=10, command=lambda: play("paper"))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(frame_buttons, text="Scissors", width=10, command=lambda: play("scissors"))
btn_scissors.grid(row=0, column=2, padx=5)

label_result = tk.Label(root, text="", font=("Arial", 12), wraplength=300, justify="center")
label_result.pack(pady=20)

root.mainloop()
