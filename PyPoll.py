# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:27:53 2019

@author: Diego Martinez
"""
import os
import csv
mainpath = "D:/"
filename = "election_data.csv"
fullpath = os.path.join("election_data.csv")

votes = csv.DictReader(open(fullpath))

list = []
for row in votes:
   candidate = str(row["Candidate"])
   list.append(candidate)
      
Khan =  list.count("Khan")
Correy = list.count("Correy")
Li = list.count("Li")
OTooley = list.count("O'Tooley")

Total = Khan + Correy + Li + OTooley

P_Khan = (Khan/Total)*100
P_Correy = (Correy/Total)*100
P_Li = (Li/Total)*100
P_OTooley = (OTooley/Total)*100

Winnerone = [[Khan,"Khan"],[Correy,"Correy"],[Li,"Li"],[OTooley,"O´Tooley"]]
WinnerFinal = [max(Winnerone)]


print("Total_Votes: " + str(Total))

print("Khan: " + str(P_Khan) + "% " + "(" + str(Khan) + ")") 
print("Correy: " + str(P_Correy) + "% " + "(" + str(Correy) + ")")
print("Li: " + str(P_Li) + "% " + "(" + str(Li) + ")")
print("O´Tooley: " + str(P_OTooley) + "% " + "(" + str(OTooley) + ")")

print ("Winner: " + str(WinnerFinal[0][1]))