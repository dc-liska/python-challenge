import os
import csv

csvpath = "C:/Users/Lightman/Documents/Boot Camp/Assignments/03-Python/Instructions/PyBank/Resources/budget_data.csv"
monthcount =0
cashtotal =0
prevRowValue =0
profitChange =0
runningChange =0
averageChange =0
topProfits =0
topLoss =0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        monthcount += 1
        cashtotal = cashtotal + int(row[1])
        profitChange= int(row[1]) - prevRowValue
        runningChange -= profitChange

        if profitChange >topProfits:
            topProfits =profitChange
            topProfitMonth = str(row[0])
        if profitChange <topLoss:
            topLoss =profitChange
            topLossMonth = str(row[0])
        prevRowValue = int(row[1])
        
averageChange = runningChange / (monthcount -1)

print("Financial Analysis\n-------------------------")
print("Total Months: " + str(monthcount))
print("Total: $" + str(cashtotal))
print("Average  Change: $" + str(averageChange))
print("Greatest Increase in Profits: " + topProfitMonth + " ($"+ str(topProfits)+")")
print("Greatest Decrease in Profits: " + topLossMonth + " ($"+  str(topLoss)+")")

