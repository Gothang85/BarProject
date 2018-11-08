import csv
import random
import numpy
import pandas

with open('drinkers.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    drinkers = []
    for row in readCSV:
        drinker = row[0]
        drinkers.append(drinker)

with open('transactionids.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    transids = []
    for row in readCSV:
        transid = row[0]
        transids.append(transid)


n = len(drinkers)
m = len(transids)-1
possibleindicators = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
drinkernames = []
x = []

for i in range(n): #will loop through all the drinkers
    irange = random.choice(possibleindicators) #this will choose a random thing from the list possibleindicators and this will be used to be the end point for the for loop that creates what the drinkers likes
    if i >= 1: #the first row in the drinkers table is the column name table, this line makes sure we ignore that
        for j in range(irange):
            drinkername = drinkers[i] 
            transaction = random.choice(transids)
            drinkernames.append(drinkername)
            x.append(transaction)
            transids.remove(transaction)

a1 = numpy.array(drinkernames)
b1 = numpy.array(x)
df = pandas.DataFrame({"drinker" : a1, "transactionid" : b1})
df.to_csv("pays.csv", index=False)