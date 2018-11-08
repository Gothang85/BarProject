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

with open('bars.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bars = []
    bstates = []
    for row in readCSV:
        bar = row[2]
        bstate = row[5]
        bars.append(bar)
        bstates.append(bstate)

# here is the code to generate the values for the frequents table
n2 = len(drinkers)
m2 = len(bars)
possibleindicators = [1,2]
frequentsdrinkers = []
frequentsbars = []
for i in range(n2):
    for j in range(m2):
        if dstates[i] == bstates[j]:
            choose = random.choice(possibleindicators) # randomily will decide if this is a bar the drinker will frequent
            if choose == 1:
                frequentsdrinker = drinkers[i]
                frequentsdrinkers.append(frequentsdrinker)
                frequentsbar = bars[j]
                frequentsbars.append(frequentsbar)

# here i write to a csv to create the frequents table
a1 = np.array(frequentsdrinkers)
b1 = np.array(frequentsbars)
df = pd.DataFrame({"drinkers" : a1, "bars" : b1})
df.to_csv("frequents.csv", index=False)