import csv
import random
import numpy as np
import pandas as pd
import math

def randomizer(itemindex, *itemnumbers): #this is a recursive function to make sure there aren't any duplicates
        itemnumber = random.choice(itemindex) #randomly choose a number from the array of numbers
        for i in range(len(itemnumbers)):
                if itemnumber == itemnumbers[i]:
                        itemnumber = randomizer(itemindex, itemnumber)
        return itemnumber


with open('items.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    items = []
    for row in readCSV:
        item = row[0]
        items.append(item)

with open('bars.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bars = []
    for row in readCSV:
        bar = row[2]
        bars.append(bar)


possibleitemindicators = [] #array for possible number of items a place can sell
sellsitemnames = [] #array that will store the item names column in the excel file 'sells'
sellsbarnames = [] #array that will store the bar names column in the excel file 'sells'
sellsprices = [] #array that will store the prices of the corresponding item at the corresponding bar in the excel file 'sells'
for i in range(10):
    if i>=5 and i<=10: # bars can sell at least 5 items and at most 10 items
        possibleitemindicators.append(i)
itemindex = []
for i in range(len(items)):
    if i >= 1:
        itemindex.append(i)  #index to randomly choose from which item that the bar sells
for i in range(len(bars)): #will go through each bar
    irange = random.choice(possibleitemindicators) #for each specific bar, this will choose the number of items that specifc bar will sell randomly
    if i>=1:
        itemnumbers = [] #this array is going to be used when I make a function call later to choose which items to sell
        for j in range(irange): #going to go as many times as there are items in the specific bar
            if j == 0:
                itemnumber = random.choice(itemindex)
                itemnumbers.append(itemnumber)    
            sellsbarname = bars[i]  
            sellsbarnames.append(sellsbarname) #all of these items will be sold by the same bar
            itemnumber = randomizer(itemindex, itemnumbers)
            itemnumbers.append(itemnumber)    
            sellsitemname = items[itemnumber] #randomly chosen number is then used to pick item from items list
            sellsitemnames.append(sellsitemname) #stores the item name into the list
            sellsprice = round(math.log(i*itemnumber + 5) + 1, 2) #prices are unique and i basically indicates a unique bar number this basically makes the condition 2 
            sellsprices.append(sellsprice)

# here i write to a csv to create the sells tables
a2 = np.array(sellsbarnames)
b2 = np.array(sellsitemnames)
c2 = np.array(sellsprices)
df = pd.DataFrame({"bar" : a2, "item" : b2, "price" : c2})
df.to_csv("sells.csv", index=False)