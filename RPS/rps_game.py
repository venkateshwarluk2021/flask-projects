import random

def play():
    choices = ["rock", "paper", "scissors"]
    user_c = input("Enter your choice (rock, paper, scissors):\t").lower()
    computer_c = random.choice(choices)

    if user_c not in choices:
        print("Invalid choice. choose rock , paper, scissors")
        return

    print(f"\nYou chose: {user_c}")
    print(f"\nComputer chose: {computer_c}")

    if user_c == computer_c:
        print("it is a tie!")
    elif (user_c == "rock" and computer_c == "scissors") or \
         (user_c == "paper" and computer_c == "rock") or \
         (user_c == "scissors" and computer_c == "paper"):
        print("You win")
    else:
        print("Computer wins")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nDo you want to play again(y/n):\t").lower()
        if again.strip() != "y":
            print("Thank you for playing")
            break
