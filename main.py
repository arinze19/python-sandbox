import csv
from datetime import datetime

# Constants (configurable)

RATE = 1500 # Rate per hour in NGN
EMPLOYEE = "Kunle" # Employee name

def calculate_hours(start_time, end_time):
    start = datetime.strptime(start_time, "%Y-%m-%d %I:%M %p") # format time to start time
    end = datetime.strptime(end_time, "%Y-%m-%d %I:%M %p") # format time to start time
    duration = end - start
    hours = duration.total_seconds() / 3600  # Convert seconds to hours
    return hours

def save_to_csv(date, start_time, end_time, hours_worked, earnings):
    filename = f"{EMPLOYEE}_time_tracking.csv"
    file_exists = False
    try:
        with open(filename, "r") as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Start Time", "End Time", "Hours Worked", "Earnings (NGN)"])
        writer.writerow([date, start_time, end_time, round(hours_worked, 2), round(earnings, 2)])

def main():
    date = input("Enter the date (YYYY-MM-DD): ")
    # enable user to input time in 12-hour format?? 
    # this would be easier as most users use 12-hour format
    start_time = input("Enter the start time (HH:MM AM/PM): ")
    end_time = input("Enter the end time (HH:MM AM/PM): ")
    
    full_start_time = f"{date} {start_time}"
    full_end_time = f"{date} {end_time}"
    
    hours_worked = calculate_hours(full_start_time, full_end_time)
    rate_per_hour = RATE
    earnings = hours_worked * rate_per_hour
    
    print(f"Hours worked: {round(hours_worked, 2)} hours")
    print(f"Earnings: NGN{round(earnings, 2)}")
    
    save_to_csv(date, start_time, end_time, hours_worked, earnings)
    print("Data saved successfully!")

if __name__ == "__main__":
    main()
