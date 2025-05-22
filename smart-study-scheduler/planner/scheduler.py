import csv
from datetime import datetime

def create_study_schedule():
    print("\n Create Your Study Schedule")
    tasks = []
    while True:
        task = input("Enter task name (or 'done' to finish): ")
        if task.lower() == 'done':
            break
        duration = input(f"Enter duration in minutes for '{task}': ")
        tasks.append((task, duration))

    with open('data/focus_logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for task, duration in tasks:
            writer.writerow([datetime.now().date(), task, duration, 0])  # 0 = not completed

    print("Study plan saved!")