import csv
from datetime import datetime, timedelta

csv_file_path = r"C:\Users\MicroApt\Desktop\Python_Assign\Assignment_Timecard.csv"

def parse_datetime(datetime_str):
    try:
        # Parse the datetime string with the specified format
        return datetime.strptime(datetime_str, "%m/%d/%Y %I:%M %p")
    except ValueError:
        # Handle incorrectly formatted date/time values
        return None

def analyze_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)  # Convert the reader to a list for easier access
        
        for i in range(len(rows) - 1):
            current_end_time = parse_datetime(rows[i]['Time Out'])
            next_start_time = parse_datetime(rows[i + 1]['Time'])
            
            if current_end_time and next_start_time:
                time_difference = (next_start_time - current_end_time).seconds / 3600  # Time difference in hours
                
                # Check if time difference is greater than 1 hour and less than 10 hours
                if 1 < time_difference < 10:
                    print(f"Employee Name: {rows[i]['Employee Name']}, Position ID: {rows[i]['Position ID']}, Less than 10 hours but more than 1 hour between shifts.")
        
        # Additional checks for other conditions (7 consecutive days and more than 14 hours in a single shift) can be added here

# Call the function to analyze the CSV file
analyze_csv(csv_file_path)
