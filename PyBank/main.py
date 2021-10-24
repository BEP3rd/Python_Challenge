"""
PyBank protocode

Initilize total months before teh loop

open the budget file and read next after the title row

then intorduce the loop and add add 1 to the total months calculator

convert profit/losses to number, it starts as a string. Sum them together, have to consider to change all ot positive


For the average try to find the value at the end when its summed together both profit and loss, then divide by the number of months


Track the highest and lowest change in profits and losses by storing the value 
and as its looped through check if the new value is either the lowest value seen or highest value seen


In the end print the analysis to terminal
"""

import os
import csv
from typing import TYPE_CHECKING

budgetData = os.path.join('Resources', 'budget_data.csv')

totalMonths = 0
totalChange = 0
averageChange = 0
prevChange = 0
change = 0
difChange = 0
totalDifChange = 0
greatestInc = [0,0]
greatestDec = [0,0]

with open(budgetData) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",") # Reads the csv file to be used 
    
    csv_header = next(csv_file) # Skips the first line and stores the headers

    # For loop through the rows in the file
    for row in csv_reader:
        totalMonths = totalMonths + 1
        change = int(row[1])
        totalChange = totalChange + change
        if prevChange != 0:
            difChange = change - prevChange
            totalDifChange = totalDifChange + difChange
            if int(greatestInc[1]) < difChange:
                greatestInc = [row[0], difChange]
            elif int(greatestDec[1]) > difChange:
                greatestDec = [row[0], difChange]




        prevChange = change
      
        

averageChange = totalDifChange/(totalMonths-1)

print(f"Total Months: {totalMonths}")
print(f"Total: ${totalChange}")
print(f"Average Change: ${round(averageChange, 2)}")
print(f"Greatest Increase in Profits: {greatestInc[0]} ${greatestInc[1]}")
print(f"Greatest Decrease in Profits {greatestDec[0]} ${greatestDec[1]}")

# Specify the file to write to
filepath = '/output/results.txt'
results = open("results", 'w')

lines = [f"Total Months: {totalMonths}", f"Total: ${totalChange}",f"Average Change: ${round(averageChange, 2)}", 
    f"Greatest Increase in Profits: {greatestInc[0]} ${greatestInc[1]}",
    f"Greatest Decrease in Profits {greatestDec[0]} ${greatestDec[1]}"]

with open('readme.txt', 'w') as f:
    for line in lines:
        results.write(line)
        results.write('\n')
