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
changes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        monthcount += 1
        cashtotal = cashtotal + int(row[1])
        if monthcount >1:
            profitChange= int(row[1]) -prevRowValue
            changes.append(profitChange)
        #runningChange -= profitChange

        


        if profitChange >topProfits:
            topProfits =profitChange
            topProfitMonth = str(row[0])
        if profitChange <topLoss:
            topLoss =profitChange
            topLossMonth = str(row[0])
        else:
            pass
        prevRowValue = int(row[1])
        

#Original averageChange calculation- flawed.        
#averageChange = runningChange / (monthcount -1)
#List usage averageChange calculation
averageChange = float(sum(changes)/len(changes))

print("Financial Analysis\n-------------------------")
print("Total Months: " + str(monthcount))
print("Total: $" + str(cashtotal))
print("Average  Change: $" + str(round(averageChange,2)))
print("Greatest Increase in Profits: " + topProfitMonth + " ($"+ str(topProfits)+")")
print("Greatest Decrease in Profits: " + topLossMonth + " ($"+  str(topLoss)+")")

#print("Financial Analysis\n------------------------\nTotal Months: " + str(monthcount)+
#   "\nTotal: $" + str(cashtotal)+"\nAverage  Change: $" + str(round(averageChange,2))+ 
#    "\nGreatest Increase in Profits: " + topProfitMonth + " ($"+ str(topProfits)+")"+ 
#    "\nGreatest Decrease in Profits: " + topLossMonth + " ($"+  str(topLoss)+")",...,)

#with open(output_path, 'w', newline='\n') as textfile:
fileHandler= open('pyBankOutput.txt','w')

fileHandler.write('Financial Analysis\n------------------------\nTotal Months: ' + str(monthcount) +
    '\nTotal: $' + str(cashtotal) +
    '\nAverage  Change: $' + str(round(averageChange,2))+
    '\nGreatest Increase in Profits: ' + topProfitMonth + ' ($'+ str(topProfits)+')' +
    '\nGreatest Decrease in Profits: ' + topLossMonth + ' ($'+  str(topLoss)+')')

fileHandler.close()

