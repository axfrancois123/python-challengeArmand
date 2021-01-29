import os
import csv

#Set file path
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#Creating empty List
countMonths = []
Total_PL = []
Profit_Change = []

#Open CSV
bount = -1

total = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)  

    for row in csvreader:
        countMonths.append(row[0])
        bount = bount + 1
        Total_PL.append(int(row[1]))

    for i in range(len(Total_PL)-1):
         Profit_Change.append(Total_PL[i+1]-Total_PL[i])

#Getting Max and Min from Profit/Losses

maxProfit = max(Profit_Change)
minProfit = min(Profit_Change)

#Matching Max and Min with Month
month1 = Profit_Change.index(max(Profit_Change)) + 1
month2 = Profit_Change.index(min(Profit_Change)) + 1






print("Financial Analyst")
print("---------------------")
print("Months: " + str(bount))
print(f"Total: ${sum(Total_PL)}")
print(f"Average Change: {round(sum(Profit_Change)/len(Profit_Change),2)}")
print(f"Greatest Increase in Profits: {countMonths[month1]} (${(str(maxProfit))})")
print(f"Greatest Decrease in Profits: {countMonths[month2]} (${(str(minProfit))})")

#Export Text File
output_path = 'output.txt'
# Open the output path as a file object
with open(output_path, 'w') as file:
    # Write analysis to the output file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: " + str(bount))
    file.write(f"Total: ${sum(Total_PL)}")
    file.write(f"Average Change: {round(sum(Profit_Change)/len(Profit_Change),2)}")
    file.write(f"Greatest Increase in Profits: {countMonths[month1]} (${(str(maxProfit))})"
    file.write(f"Greatest Decrease in Profits: {countMonths[month2]} (${(str(minProfit))})"


