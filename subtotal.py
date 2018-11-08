import csv
import random
import numpy
import pandas

with open('sales.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    salesbars = []
    salesids = []
    for row in readCSV:
        salesbar = row[0]
        salesid = row[1]
        salesbars.append(salesbar)
        salesids.append(salesid)

with open('contains.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    containsids = []
    containsitems = []
    containsquantitys = []
    for row in readCSV:
        containsid = row[0]
        containsitem = row[1]
        containsquantity = row[2]
        containsids.append(containsid)
        containsitems.append(containsitem) 
        containsquantitys.append(containsquantity)   

with open('sells.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    sellsbars = []
    sellsitems = []
    sellsprices = []
    for row in readCSV:
        sellsbar = row[0]
        sellsitem = row[1]
        sellsprice = row[2]
        sellsbars.append(sellsbar)
        sellsitems.append(sellsitem)
        sellsprices.append(sellsprice)

subtotal = []
tax = []
tip = []
tip_percent = [.15,.18,.20]
total =[]
subtot = 0
for i in range(len(salesids)):
    if i>=1:
        for j in range(len(containsids)):
            if salesids[i] == containsids[j]:
                tempitem = containsitems[j]
                tempbar = salesbars[i]
                tempquantity = int(containsquantitys[j])
                for k in range(len(sellsbars)):
                    if k >= 1:
                        if tempbar == sellsbars[k] and tempitem == sellsitems[k]:
                            tempprice = float(sellsprices[k])
                            subtot = subtot + tempprice*tempquantity
        subtotal.append(subtot)
        tax.append(round(subtot*.07,2))
        tip.append(round(subtot*float(random.choice(tip_percent)),2))
        total.append(round(subtot+float(tax[i-1])+float(tip[i-1]),2))
        subtot = 0
del salesids[0]
print(len(subtotal))
print(len(tax))
print(len(tip))
print(len(total))

a = numpy.array(salesids)
b = numpy.array(subtotal)
c = numpy.array(tax)
d = numpy.array(tip)
e = numpy.array(total)
df = pandas.DataFrame({"transactionid" : a, "subtotal" : b, "tax" : c, "tip" : d, "total" : e})
df.to_csv("subtotal.csv", index=False)
