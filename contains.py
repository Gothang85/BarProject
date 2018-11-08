import csv
import random
import numpy
import pandas

def randomizer(itemindex, *itemnumbers): #this is a recursive function to make sure there aren't any duplicates
        itemnumber = random.choice(itemindex) #randomly choose a number from the array of numbers
        for i in range(len(itemnumbers)):
                if itemnumber == itemnumbers[i]:
                        itemnumber = randomizer(itemindex, itemnumber)
        return itemnumber

with open('sales.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    salesbars = []
    transactionids = []
    for row in readCSV:
        bar = row[0]
        transactionid = row[1]
        salesbars.append(bar)
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

temp_item_list = []
finalids = []
finalitems = []
quantity = []
possibleitemindicators = []
itemindex = []
for i in range(4):
    if i>=1 and i<=4: # bars can sell at least 5 items and at most 10 items
        possibleitemindicators.append(i)
for i in range(len(transactionids)):
    irange = random.choice(possibleitemindicators)
    if i>=1:
<<<<<<< HEAD
        for j in range(len(sellsbars)):
            if salesbars[i] == sellsbars[j]:
                temp_item_list.append(sellsitems[j])
        for w in range(len(temp_item_list)):
            itemindex.append(w)  #index to randomly choose from which item that the bar sells
        itemnumbers = [] #this array is going to be used when I make a function call later to choose which items to sell
        for k in range(irange): #going to go as many times as there are items in the specific bar
            if k == 0:
                itemnumber = random.choice(itemindex)
                itemnumbers.append(itemnumber)    
            finalids.append(transactionids[i])
            itemnumber = randomizer(itemindex, itemnumbers)
            itemnumbers.append(itemnumber) 
            finalitems.append(temp_item_list[itemnumber])
            quantity.append(random.randint(1,5))
        temp_item_list = []
        itemindex = []          
=======
        for j in range(m):
            if bars[i] == sellsbars[j]:
                choose = random.choice(possibleindicators)
                for k in range(choose):
                    tempid = transactionids[i]
                    finalids.append(tempid)
                    tempitem = sellsitems[j]
                    finalitems.append(tempitem)
                    quantity.append(random.randint(1,5))
>>>>>>> 6f2fc2a6d505ee476992a0e9e94ac12da83c9efa

a = numpy.array(finalids)
b = numpy.array(finalitems)
c = numpy.array(quantity)
df = pandas.DataFrame({"transactionids" : a, "items" : b, "quantity" : c})
df.to_csv("contains.csv", index=False)