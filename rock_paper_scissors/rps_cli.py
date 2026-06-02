from game.game_engine import Game

def run_cli():
    game = Game()

    print("\nRock Paper Scissors (API ready version)\n")

    while True:
        choice = input("Enter rock, paper, scissors: ").lower()

        try:
            result = game.play_round(choice)
        except ValueError as e:
            print(e)
            continue

        print(f"\nYou chose: {result['player_choice']}")
        print(f"Computer chose: {result['computer_choice']}")

        if result["winner"] == "Draw":
            print("It is a Draw")
        elif result["winner"] == "player":
            print("You win")
        else:
            print("Computer wins")

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    run_cli()
