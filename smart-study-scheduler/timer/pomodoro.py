import time
import csv
from datetime import datetime
from playsound import playsound

def countdown(minutes):
    for i in range(minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)

def start_pomodoro_session():
    task = input("\n Enter task you want to focus on: ")
    print("Starting 25-minute focus session...")
    countdown(25)

    print(" Timer finished!")

  # Add an alarm.mp3 file in the project folder

    with open('data/focus_logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().date(), task, 25, 1])  # 1 = completed

    print("\n Focus session completed!")
    print("Take a 5-minute break...")
    countdown(5)
    playsound("alarm.mp3")