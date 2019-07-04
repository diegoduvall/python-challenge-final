# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:36:59 2019

@author: Diego Martinez
"""

import csv
import os

filename = "budget_data.csv"
fullpath = os.path.join(filename)

input_file = csv.DictReader(open(fullpath))
idk = csv.DictReader(open(fullpath))

## avarege changes
old = 0
new = 0
difference = 0
list = []
## Greatest increst profits
greatestchange = None
salesperiod = None
## Greatest decreast profits
leastchange = None
salesperiod_m = None

for row in input_file:
   new = int(row["Profit/Losses"])
   sales = int(row["Profit/Losses"])
   if new != old:
      difference = new-old
      old=new
      list.append(difference)
   if greatestchange == None or greatestchange < sales:
           greatestchange = sales
           salesperiod = row["Date"]
   if leastchange == None or leastchange > sales:
                   leastchange = sales
                   salesperiod_m = row["Date"]

##number of months
months = len(list)

## ventas totales            
total = sum(int(row["Profit/Losses"]) for row in idk)


## funcion promedio
def averagelist(list):
    sum=0.0
    for i in range(0,len(list)):
        sum=sum+list[i]
 
    return sum/len(list)

print ("Total Months: " + str(months))
print ("Total: " + str(total))       
print ("Avarege Change:" +  " $" +   str(averagelist(list)))
print ("Gratest Increase in Profit: " + str(salesperiod) + " $" + str(greatestchange))
print ("Gratest Descrease in Profit:" + str(salesperiod_m) + " $" + str(leastchange))

