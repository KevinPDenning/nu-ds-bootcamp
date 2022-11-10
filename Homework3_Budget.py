import os
import csv

file_path = os.path.join("..", "/Users/kevindenning/Desktop/Bootcamp/NU-VIRT-DATA-PT-10-2022-U-LOLC/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")

MonthCount = 0
Total = 0
Prof_loss = []
month_list = []
monthlyChanges = []

with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        MonthCount += 1
        Total += int(row[1])
        Prof_loss.append(row[1])
        month_list.append(row[0])

avg = int(Prof_loss[0])

for i in range(1, len(Prof_loss)):
    monthlyChanges.append(int(Prof_loss[i]) - avg)
    avg = int(Prof_loss[i])
    i += 1

MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)

for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i - 1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i - 1)
    else:
        i += 1
        
MaxMonth = month_list[maxIndex]
MinMonth = month_list[minIndex]

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: ${Total}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")

outputfile = 'summary.txt'
with  open(outputfile, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-----------------------------" + "\n")
    output.write(f"Total Months: {MonthCount}\n")
    output.write(f"Total: ${Total}\n")
    output.write(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
 