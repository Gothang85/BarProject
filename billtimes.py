import csv
import numpy
import pandas
import time
import random
from datetime import datetime




with open('bars.csv') as csvfile: #I read bars.csv to get all the opening and closing times
    readCSV = csv.reader(csvfile, delimiter=',')
    bars = []
    barotimes = []
    barctimes = []
    for row in readCSV:
        bar = row[2]
        bars.append(bar)
        barotime = row[6]
        barctime = row[7]
        barotimes.append(barotime)
        barctimes.append(barctime)
csvfile.close()  

with open('sales.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    salesbars = []
    salestransids = []
    for row in readCSV:
        salesbar = row[0]
        salestransid = row[1]
        salesbars.append(salesbar)
        salestransids.append(salestransid)
csvfile.close()   
del salesbars[0]
del salestransids[0]
del bars[0]
del barotimes[0]
del barctimes[0]

billstimes = []
billstransids = []
for i in range(len(salestransids)):
    billtransid = salestransids[i]
    billstransids.append(billtransid)
    hr = random.randint(14,23)
    hr = str(hr)
    minute = random.randint(0,59)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    billstime = hr + ":" + minute
    billstimes.append(billstime)

a1 = numpy.array(billstransids)
b1 = numpy.array(billstimes)
df = pandas.DataFrame({"transactionids" : a1, "times" : b1})
df.to_csv("billtimes.csv", index=False)