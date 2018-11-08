import csv
import random
import numpy
import pandas

with open('bars.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bars = []
    for row in readCSV:
        bar = row[2]
        bars.append(bar)

with open('pays.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    transids = []
    for row in readCSV:
        transid = row[1]
        transids.append(transid)

m=len(transids)
x = []
y = []

for i in range(m): 
    if i>=1:
        x.append(transids[i])
        y.append(random.choice(bars))

a = numpy.array(y)
b = numpy.array(x)
df = pandas.DataFrame({"bar" : a, "transactionid" : b})
df.to_csv("sales.csv", index=False)
