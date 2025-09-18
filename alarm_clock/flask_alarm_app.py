from flask import Flask, render_template, request, jsonify
import datetime, time, threading, platform

app = Flask(__name__)

stop_alarm = False
alarm_thread = None
alarm_time = None

def play_sound():
    """play sound until stopped"""
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
        print("Sound not available", e)


def start_alarm():
    global stop_alarm, alarm_time
    while not stop_alarm:
        now = datetime.datetime.now().strftime("%H:%M")
        if alarm_time and now==alarm_time:
            sound_thread = threading.Thread(target=play_sound, daemon=True)
            sound_thread.start()
            break
        time.sleep(1)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set_alarm", methods=["POST"])
def set_alarm():
    global alarm_thread, stop_alarm, alarm_time
    hour = request.form.get("hour")
    minute = request.form.get("minute")
    alarm_time = f"{hour}:{minute}"
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        return jsonify({"status":"error", "message":"Invalid time format"})

    stop_alarm = False
    if alarm_thread and alarm_thread.is_alive():
        stop_alarm = True

    alarm_thread = threading.Thread(target=start_alarm, daemon=True)
    alarm_thread.start()

    return jsonify({"status":"success", "message":f"alarm set for {alarm_time}"})


@app.route("/stop_alarm", methods=["POST"])
def stop_alarm_sound():
    global stop_alarm
    stop_alarm = True
    return jsonify({"status":"success", "message":"Alarm stopped"})

@app.route("/cancel_alarm", methods=["POST"])
def cancel_alarm():
    global stop_alarm, alarm_time
    stop_alarm = True
    alarm_time = None
    return jsonify({"status":"success", "message":"Alarm cancelled"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

