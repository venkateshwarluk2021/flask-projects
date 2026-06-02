import random

class Computer:
    def __init__(self):
        self.name = "Computer"
        self.choice = None


    def make_choice(self):
        self.choice = random.choice(["rock", "paper", "scissors"])
        return self.choice

    
