import pandas as pd
import matplotlib.pyplot as plt

def show_report():
    try:
        df = pd.read_csv('data/focus_logs.csv', names=["Date", "Task", "Duration", "Completed"])
        df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce")
        df["Date"] = pd.to_datetime(df["Date"])

        daily_summary = df[df["Completed"] == 1].groupby("Date")["Duration"].sum()
        task_summary = df[df["Completed"] == 1].groupby("Task")["Duration"].sum()

        print("\n Productivity Report:\n")
        print("Daily Summary:\n", daily_summary)
        print("\nTime Spent per Task:\n", task_summary)

        plt.figure(figsize=(12,5))

        plt.subplot(1,2,1)
        daily_summary.plot(kind="line", title="Focus Time per Day")
        plt.xlabel("Date")
        plt.ylabel("Minutes")

        plt.subplot(1,2,2)
        task_summary.plot(kind="pie", autopct='%1.1f%%', title="Time Distribution by Task")
        plt.ylabel("")

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error reading logs:", e)