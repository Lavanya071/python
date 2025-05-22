import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import time
import threading
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from playsound import playsound

CSV_FILE = 'data/focus_logs.csv'



def countdown(minutes, label, task_name):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        label.config(text=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        seconds -= 1

    label.config(text="Done!")
    playsound("alarm.mp3")

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().date(), task_name, minutes, 1])

    messagebox.showinfo("Break Time", "Focus session complete! Take a 5-minute break.")



def start_focus_session():
    task_name = simpledialog.askstring("Task", "Enter the task you want to focus on:")
    if not task_name:
        return
    session_label.config(text="Starting Focus Session...")
    thread = threading.Thread(target=countdown, args=(25, session_label, task_name))
    thread.start()

def add_task():
    task = simpledialog.askstring("Add Task", "Enter task name:")
    duration = simpledialog.askinteger("Duration", f"Enter duration in minutes for {task}:")
    if not task or not duration:
        return
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().date(), task, duration, 0])
    messagebox.showinfo("Saved", f"Task '{task}' added successfully!")

def show_report():
    try:
        df = pd.read_csv(CSV_FILE, names=["Date", "Task", "Duration", "Completed"])
        df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce")
        df["Date"] = pd.to_datetime(df["Date"])
        df = df[df["Completed"] == 1]

        daily_summary = df.groupby("Date")["Duration"].sum()
        task_summary = df.groupby("Task")["Duration"].sum()

        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        daily_summary.plot(kind="line", title="Focus Time per Day")
        plt.xlabel("Date")
        plt.ylabel("Minutes")

        plt.subplot(1, 2, 2)
        task_summary.plot(kind="pie", autopct='%1.1f%%', title="Time by Task")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Could not read report: {e}")



def on_enter(e):
    e.widget['background'] = '#555'
    e.widget['fg'] = '#fff'

def on_leave(e):
    e.widget['background'] = e.widget.original_bg
    e.widget['fg'] = '#fff'

def create_button(text, command, bg_color):
    btn = tk.Button(
        root,
        text=text,
        font=("Helvetica", 13, "bold"),
        bg=bg_color,
        fg="#fff",
        activebackground="#333",
        activeforeground="#fff",
        command=command,
        bd=0,
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2"
    )
    btn.original_bg = bg_color
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=8, fill='x', padx=40)
    return btn



root = tk.Tk()
root.title("Smart Study Scheduler")
root.geometry("450x500")
root.configure(bg="#1e1e1e")

title_label = tk.Label(
    root,
    text=" Smart Study Scheduler",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e1e",
    fg="#03DAC6"
)
title_label.pack(pady=30)

session_label = tk.Label(
    root,
    text="00:00",
    font=("Courier", 36, "bold"),
    bg="#1e1e1e",
    fg="#BB86FC"
)
session_label.pack(pady=10)


create_button(" Start Focus Timer", start_focus_session, "#4CAF50")
create_button("Add Study Task", add_task, "#2196F3")
create_button("View Productivity Report", show_report, "#9C27B0")
create_button("Exit", root.quit, "#F44336")

root.mainloop()