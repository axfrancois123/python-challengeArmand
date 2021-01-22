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






print("Financial Analyst", file=open("PyBank.txt", "Access_Mode"))
print("---------------------", file=open("PyBank.txt", "Access_Mode"))
print("Months: " + str(bount), file=open("PyBank.txt", "Access_Mode"))
print(f"Total: ${sum(Total_PL)}", file=open("PyBank.txt", "Access_Mode"))
print(f"Average Change: {round(sum(Profit_Change)/len(Profit_Change),2)}", file=open("PyBank.txt", "Access_Mode"))
print(f"Greatest Increase in Profits: {countMonths[month1]} (${(str(maxProfit))})", file=open("PyBank.txt", "Access_Mode"))
print(f"Greatest Decrease in Profits: {countMonths[month2]} (${(str(minProfit))})", file=open("PyBank.txt", "Access_Mode"))

#Export Text File
file = open("PyBank.txt","Access_Mode")