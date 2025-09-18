import time
import datetime
import platform
import threading


#Global stop flag
stop_alarm = False

def play_sound():
    """ Play a soun depending on OS"""
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
        print("Sound not availble", e)


def alarm_clock(alarm_time):
    global stop_alarm
    print(f"Alarm set for time: {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("wake up. Time's up")

            # run sound in a separate thead so we can stop it
            sound_thread = threading.Thread(target=play_sound, daemon=True)
            sound_thread.start()

            input("press ENTER to stop the alarm:\t")
            stop_alarm = True   # tell thread to stop
            sound_thread.join(timeout=1)    #wait briefly for cleanup
            break
        time.sleep(1)


if __name__ == "__main__":
    print("===========Alarm Clock CLI===============")
    alarm_time = input("Enter time HH:MM (24 hour format):\t")

    # validate time format
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValeuError:
        print("Ivalid time format. please enter 24hour HH:MM format....")
        exit(1)
    alarm_clock(alarm_time)
