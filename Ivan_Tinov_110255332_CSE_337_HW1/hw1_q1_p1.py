# Ivan Tinov, ID# 110255332, CSE 337 HW1_q1_p1
from datetime import datetime
import csv

# create a new file to store the date and time format
new_file= open('date_time_format.txt', 'w')

def dateTimeFormat(file):
    # open prices_sample.csv
    with open(file, newline='') as file:
        # read the csv file by creating a file_reader
        file_reader = csv.reader(file)
        for time in file_reader: 
            new_file.write("%s\n" % datetime.fromtimestamp(int(time[0])).strftime('%Y-%m-%d %H:%M:%S'))
            # strftime = "string format time"
    new_file.close()

dateTimeFormat('prices_sample.csv')
