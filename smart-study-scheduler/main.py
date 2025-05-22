from planner.scheduler import create_study_schedule
from timer.pomodoro import start_pomodoro_session
from analytics.productivity_report import show_report

def main():
    print("\n🎓 Welcome to Smart Study Scheduler 🎓")
    print("1. Create Study Plan")
    print("2. Start Focus Timer (Pomodoro)")
    print("3. View Productivity Report")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == '1':
        create_study_schedule()
    elif choice == '2':
        start_pomodoro_session()
    elif choice == '3':
        show_report()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    while True:
        main()