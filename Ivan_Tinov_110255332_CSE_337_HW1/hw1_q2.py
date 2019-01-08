# Ivan Tinov, ID# 110255332, CSE 337 HW1_q2
import time
from collections import defaultdict


# function for calculating the mean
def mean(data):
    nsum = 0
    for i in range(len(data)):
        nsum += data[i]
    avg = nsum/len(data)
    return int(avg)

# function for calculating weekly min, max, average values
def daily_data():
    with open('prices_sample.csv', newline='') as file:
        file_reader = file.read()
        fileList = file_reader.splitlines()
        dateDict = defaultdict(list)

        for i in range(len(fileList)):
            price = int(fileList[i][11:])
            date = fileList[i][:10]
            date = time.strftime('%Y-%m-%d', time.localtime(int(date)))
            dateDict[date].append(price)

    sunday = ''
    day = 7
    week = defaultdict(list)
    for i in sorted(dateDict):
        if (day == 7):
            day = 0
            sunday = i
        week[sunday] += dateDict[i]
        day = day + 1
       
    writer = open('daily_data.csv', 'w+')
    writer.write('Date' + ', ' + 'Max' + ', ' + 'Min' + ', ' + 'Mean\n')
    for i in week:
        minVal = min(week[i])
        maxVal = max(week[i])
        average = mean(week[i])
        output = i + ', ' + str(maxVal) + ', ' + str(minVal) + ', ' + str(int(average)) + '\n'
        writer.write(output)


daily_data()
                

        
