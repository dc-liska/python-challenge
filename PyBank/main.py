import os
import csv

csvpath = "C:/Users/Lightman/Documents/Boot Camp/Assignments/03-Python/Instructions/PyBank/Resources/budget_data.csv"
monthcount =0
cashtotal =0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        monthcount += 1
        cashtotal = cashtotal + int(row[1])
        print(row[0])
    

print("Financial Analysis\n-------------------------")
print("Total Months: $" + str(monthcount))
print("Total: $" + str(cashtotal))
print("Average  Change: $")
