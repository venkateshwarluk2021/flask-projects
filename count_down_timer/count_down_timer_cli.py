import time

def countdown_timer(seconds):
    while seconds:
        mins,secs= divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
        
    print("Time's up")


if __name__ == "__main__":
    try:
        user_input = int(input("Enter time in seconds:\t"))
        countdown_timer(user_input)
    except ValueError:
        print("\n\nInvlaid number. please enter valid number. \n\n")
