import csv
from datetime import datetime, timedelta

csv_file_path = r"C:\Users\MicroApt\Desktop\Assessment_python\Assignment_Timecard.csv"
output_file_path = "output.txt"  # Specify the path for the output text file

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
        
        with open(output_file_path, 'w') as output_file:
            for i in range(len(rows) - 6):  # Check for 7 consecutive days, so iterate up to len(rows) - 7
                start_time = parse_datetime(rows[i]['Time'])
                end_time = parse_datetime(rows[i + 6]['Time Out'])
                if start_time and end_time:
                    # Check condition a (7 consecutive days)
                    if (end_time - start_time).days == 6:
                        output_file.write(f"Employee Name: {rows[i]['Employee Name']}, Position ID: {rows[i]['Position ID']}, Worked for 7 consecutive days.\n")
                    
                    # Check condition b (less than 10 hours between shifts but greater than 1 hour)
                    next_start_time = parse_datetime(rows[i + 1]['Time'])
                    if next_start_time and (next_start_time - end_time) > timedelta(hours=1) and (next_start_time - end_time) < timedelta(hours=10):
                        output_file.write(f"Employee Name: {rows[i]['Employee Name']}, Position ID: {rows[i]['Position ID']}, Less than 10 hours between shifts.\n")
                    
                    # Check condition c (more than 14 hours in a single shift)
                    if (end_time - start_time) > timedelta(hours=14):
                        output_file.write(f"Employee Name: {rows[i]['Employee Name']}, Position ID: {rows[i]['Position ID']}, Worked more than 14 hours in a single shift.\n")

# Call the function to analyze the CSV file and write output to the text file
analyze_csv(csv_file_path)
