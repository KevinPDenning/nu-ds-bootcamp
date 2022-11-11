import os
import csv


file_path = os.path.join("..", "/Users/kevindenning/Desktop/Bootcamp/NU-VIRT-DATA-PT-10-2022-U-LOLC/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
outputfile = "election_result.txt"

vote_list = []
candidates = []
percent_vote= []
cand_count = []
totalVote = 0

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        vote_list.append(row[2])
        
totalVote = len(vote_list)

for name in vote_list:
   if name not in candidates:
        candidates.append(name)
        x = name

count = 0
candidate = vote_list[0]
lastCount = 0




print("Election Results")
print("--------------------------")
print(f"Total Votes: {totalVote}")
print("--------------------------")





for candidate in candidates:
    for vote in vote_list:
        if candidate == vote:
            count += 1
    percent = count / len(vote_list)
    percent_vote.append(percent)
    cand_count.append(count)
    
    if lastCount < count:
        Winner = candidate    
    print(f"{candidate}: {percent:.3%} ({count})")
    
    lastCount = count
    count = 0

print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")

with open(outputfile, 'w') as output:
    output.write("Election Results\n")
    output.write("--------------------------")
    output.write(f"Total Votes: {totalVote}\n")
    output.write("--------------------------")
    for candidate in candidates:
        index = candidates.index(candidate)
        output.write(f"{candidate}: {percent_vote[index]:.3%} ({cand_count[index]})\n")
    output.write("--------------------------")
    output.write(f"Winner: {Winner}\n")

