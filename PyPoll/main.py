#main.py for PyPoll, by David Liska
import os
import csv

csvpath = os.path.join('C:\\Users\\Lightman\\Documents\\Boot Camp\\Assignments\\03-Python\\Resources', 'election_data.csv')
candidates = []
candVotes = []
TotalVoteCount = 0
mostVotes = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        TotalVoteCount += 1
        if row[2] not in candidates:
            candidates.append(str(row[2]))
            currentIndex = candidates.index(row[2])
            candVotes.append(1)
        else:
            currentIndex = candidates.index(row[2])
            candVotes[currentIndex] += 1

#****Terminal output****
print("\nElection Results\n----------------------\nTotal Votes:" + str(TotalVoteCount) + "\n----------------------\n")

for name in candidates:
    currentIndex = candidates.index(name)
    percentOfVotes = round((candVotes[currentIndex] / TotalVoteCount) * 100,4)
    print(candidates[currentIndex] +": " + str(percentOfVotes) +"% (" + str(candVotes[int(currentIndex)]) +")")
    if candVotes[currentIndex] > mostVotes:
        mostVotes = candVotes[currentIndex]
        winner = name
    else:
        pass

print("----------------------\nWinner: " + winner + "\n----------------------")

#****Text file output****
fileHandler= open('pyPollOutput.txt','w')
fileHandler.write('\nElection Results\n----------------------\nTotal Votes:' + str(TotalVoteCount) + '\n----------------------\n')
for name in candidates:
    currentIndex = candidates.index(name)
    percentOfVotes = round((candVotes[currentIndex] / TotalVoteCount) * 100,4)
    fileHandler.write(candidates[currentIndex] +': '  + str(percentOfVotes) +'% (' + str(candVotes[int(currentIndex)]) +')\n')
fileHandler.write('\n----------------------\nWinner: ' + winner + '\n----------------------')

fileHandler.close()
