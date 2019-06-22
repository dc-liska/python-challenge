import os
import csv


csvpath = os.path.join('C:\\Users\\Lightman\\Documents\\Boot Camp\\Assignments\\03-Python\\Resources', 'election_data.csv')
candidates = []
TotalVoteCount = 0
candidateVoteCount = 0


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        TotalVoteCount += 1
        if row[2] not in candidates:
            candidates.append(str(row[2]))
        else:
            pass
#print(candidates)
print("Election Results\n----------------------\nTotal Votes:" + str(TotalVoteCount) + "\n----------------------\n")
for name in candidates:
    print("\n"+ name +": "+ str(candidates.index(name)))

