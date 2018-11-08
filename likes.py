import csv
import random
import numpy as np
import pandas as pd

drinkernames = []
itemnames = []

# here i am reading the three entitie tables in (only taking in the values i need)

with open('drinkers.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    drinkers = []
    dstates = []
    for row in readCSV:
        drinker = row[0]
        dstate = row[4]
        drinkers.append(drinker)
        dstates.append(dstate)

with open('items.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    items = []
    for row in readCSV:
        item = row[0]
        items.append(item)

n = len(drinkers)
m = len(items)-1
possibleindicators = [1,2,3,4,5,6] #amount of items a person could like
for i in range(n): #will loop through all the drinkers
    irange = random.choice(possibleindicators) #this will choose a random thing from the list possibleindicators and this will be used to be the end point for the for loop that creates what the drinkers likes
    if i >= 1: #the first row in the drinkers table is the column name table, this line makes sure we ignore that
        for j in range(irange):
            itemnumber = random.randint(1,m) #this will choose an index value of the items list that will be used to choose the item we want this drinker to like
            drinkername = drinkers[i] 
            itemname = items[itemnumber]
            drinkernames.append(drinkername)
            itemnames.append(itemname)

# here i write to a csv to create the likes tables
a = np.array(drinkernames)
b = np.array(itemnames)
df = pd.DataFrame({"drinkers" : a, "items" : b})
df.to_csv("likes.csv", index=False)