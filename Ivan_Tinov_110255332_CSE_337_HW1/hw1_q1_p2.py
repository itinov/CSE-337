# Ivan Tinov, ID# 110255332, CSE 337 HW1_q1_p2
import csv
import math
from collections import defaultdict
import time


# open and read prices_sample.csv
with open('prices_sample.csv', newline='') as file:
    reader = file.read()
    fileList = reader.splitlines()
    dateDict = defaultdict(list)
    priceDict = defaultdict(list)
    # iterate over each line in file
    for i in range(len(fileList)):
        price = int(fileList[i][11:])
        priceDict["prices"].append(int(price))
        date = fileList[i][:10]
        date = time.strftime("%Y-%m-%d", time.localtime(int(date)))
        dateDict[date].append(price)

# function for calculating various percentiles
def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

# function for calculating sample variance
def variance(data, mean):
    count = 0
    sum_sq = 0
    for i in data:
        sum_sq = sum_sq + (i - mean) ** 2
        count = count + 1
    return int(sum_sq / count)

# function for calculating the mean
def mean(data):
    nsum = 0
    for i in range(len(data)):
        nsum += data[i]
    avg = nsum/len(data)
    return int(avg)
    
# finding the farthest prices to the mean
print("Date | Outlier Price Value ")

average = mean(priceDict["prices"])
meanDict = defaultdict(list)
for i in dateDict:
    meanDict[i] = abs(mean(dateDict[i]) - average)
sort = sorted(meanDict, key = meanDict.get)
farthestMean = sort[-5:]

for i in farthestMean:
    print(i + ": " + str(mean(dateDict[i])))



# print statements for percentiles and variance
print("\n25th Percentile: ", percentile(priceDict["prices"], 25))
print("50th Percentile: ", percentile(priceDict["prices"], 50))
print("75th Percentile: ", percentile(priceDict["prices"], 75))
print("Variance: ", variance(priceDict["prices"], mean(priceDict["prices"])))
