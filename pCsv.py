__author__ = 'naveen'
__date__ = '05/02/2020'

import csv
# print(dir(csv))

# ref datetime format strftime()

# link to ref ---->  https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
#link to example ---->   https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime
print(dir(datetime))
present_time = datetime.now()
print(present_time.strftime("%B %d, %Y"))


# ref csv read and write

path = "E:\Python Basic\GoogleStockMarketData.csv"
file = open(path)
for line in open(path):
    print(line)

# without csv module
lines = [line for line in file]

print(lines[1].split(',')[0])

data = lines[1].split(',')[0]
print(data)

print(lines[0])
print(len(lines))

# strip data
print(lines[0].strip())

# split data in piece
print(lines[0].strip().split(','))

# more proper arrangement of data
dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])

# using csv module
file = open(path, newline='') #open file
reader = csv.reader(file)   # read from csv module
header = next(reader)      # first line auume as header
data = [row for row in reader]  # all remaining data

print(header)
print(data[0])

data = []
data.append("something")

#store data as csv
new_path = "E:\Python Basic\GoogleStockMarketDataNew.csv"
file = open(new_path, 'w')
writer = csv.writer(file)
writer.writerow(["Name" "Age", "Gender", "Marks"])
file.close()

