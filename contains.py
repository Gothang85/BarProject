import csv
import random
import numpy
import pandas

with open('sales.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bars = []
    transactionids = []
    for row in readCSV:
        bar = row[0]
        transactionid = row[1]
        bars.append(bar)
        transactionids.append(transactionid)

with open('sells.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    sellsbars = []
    sellsitems = []
    for row in readCSV:
        sellsbar = row[0]
        sellsitem = row[1]
        sellsbars.append(sellsbar)
        sellsitems.append(sellsitem)

n = len(transactionids)
m = len(sellsbars)
possibleindicators = [1,2,3,4]
finalids = []
finalitems = []
quantity = []
for i in range(n):
    if i>=1:
        for j in range(m):
            if bars[i] == sellsbars[j]:
                choose = random.choice(possibleindicators)
                for k in range(choose):
                    tempid = transactionids[i]
                    finalids.append(tempid)
                    tempitem = sellsitems[j]
                    finalitems.append(tempitem)
                    quantity.append(random.randint(1,5))

a = numpy.array(finalids)
b = numpy.array(finalitems)
c = numpy.array(quantity)
df = pandas.DataFrame({"transactionids" : a, "items" : b, "quantity" : c})
df.to_csv("contains.csv", index=False)