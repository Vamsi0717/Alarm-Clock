import datetime
import time
import os

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up!")
            break
        time.sleep(60)

def main():
    alarm_time = input("Enter the alarm time in 24-hour format (HH:MM): ")
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Please use HH:MM.")
        return
    print("Alarm set for", alarm_time)
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
