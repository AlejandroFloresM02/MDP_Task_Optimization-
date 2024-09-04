import csv
from datetime import datetime


def read_times(path):
    times = []
    time_format = "%H:%M:%S"
    
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) >= 4:
                start_time = datetime.strptime(row[2], time_format)
                end_time = datetime.strptime(row[3], time_format)
                times.append((start_time,end_time))
    return times

def calculate_time(times):
    total_seconds = 0 
    
    for start_time, end_time in times:
        time_diff = (end_time - start_time).total_seconds()
        total_seconds += time_diff
        
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return int(minutes), int(seconds)

def write_total_time(minutes, seconds):
    total_time = minutes*60 + seconds
    with open("total_time.csv", "a") as file:
        file.write(f"{total_time}\n")
        
if __name__ == "__main__":
    total_reports = 5
    for i in range(1,total_reports+1):
        report_num = i # from 1 - n
        action_set = 1 #form 1 - n
        path  = f'report_set{action_set}_{report_num}.csv'
        times = read_times(path)
        minutes, seconds = calculate_time(times)
        write_total_time(minutes, seconds)
        
    
    
