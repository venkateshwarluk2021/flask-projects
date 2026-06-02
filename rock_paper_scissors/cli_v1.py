import random

class Player:
    def __init__(self,name):
        self.name = name
        self.choice = None

    def make_choice(self):
        while True:
            user_input = input("Enter rock, paper, scissors: ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                self.choice = user_input
                break
            else:
                print("invalid input. try again")


class Computer:
    def __init__(self):
        self.name = "Computer"
        self.choice = None

    def make_choice(self):
        self.choice = random.choice(["rock","paper","scissors"])


class Game:
    def __init__(self):
        self.player = Player("You")
        self.computer = Computer()

    def decide_winner(self):
        p = self.player.choice
        c = self.computer.choice

        if p == c:
            return "Draw"

        if (p == "rock" and c == "scissors") or \
           (p == "paper" and c == "rock") or \
           (p == "scissors" and c == "paper"):
            return "Player"

        return "Computer"

    def play(self):
        print ("\n Rock, Paper, Scissors game started \n")

        while True:
            self.player.make_choice()
            self.computer.make_choice()

            print(f"\nYou Chose: {self.player.choice}")
            print(f"Computer Chose: {self.computer.choice}")

            winner = self.decide_winner()

            if winner == "Draw":
                print("It is a draw")
            elif winner == "Player":
                print("You win")
            else:
                print("Computer wins")

            again = input("\nPlay again?(y/n):").lower()
            if again != "y":
                print("Thanks for playing")
                break

if __name__ == "__main__":
    game = Game()
    game.play()
