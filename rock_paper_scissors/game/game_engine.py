from game.player import Player
from game.computer import Computer

class Game:
    def __init__(self):
        self.player = Player("You")
        self.computer = Computer()

    def play_round(self, player_choice):
        # set player choice
        self.player.set_choice(player_choice)
        # computer choice
        computer_choice = self.computer.make_choice()

        # decide winner
        winner = self.decide_winner()

        return {
            "player_choice":self.player.choice,
            "computer_choice":computer_choice,
            "winner" : winner
            }

    def decide_winner(self):
        p = self.player.choice
        c = self.computer.choice

        if p == c:
            return "Draw"

        if ( p == "rock" and c == "scissors") or \
           ( p == "paper" and c == "rock" ) or \
           ( p == "scissors" and c == "paper" ):
            return "player"

        return "computer"
    
