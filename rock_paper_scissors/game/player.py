class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def set_choice(self, choice):
        if choice not in ["rock", "paper", "scissors"]:
            raise ValueError("Invalid Choice")
        self.choice = choice
