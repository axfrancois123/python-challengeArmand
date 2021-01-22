import os
import csv

#Set file path
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#Creating empty List
Voter_ID = []
County = []
Candidate = []

#Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    for row in csvreader:
        
        Voter_ID.append(str(row[0]))
        County.append(str(row[1]))
        Candidate.append(str(row[2]))
        Total_Votes = (len(Voter_ID))

#Establishing names as integers for comparison

    Khan = int(Candidate.count("Khan"))
    Li = int(Candidate.count("Li"))
    Correy = int(Candidate.count("Khan"))
    Tooley = int(Candidate.count("O'Tooley"))

#Getting Percentages

    Khan_Percent = (Khan/Total_Votes) * 100
    Li_Percent = (Li/Total_Votes) * 100
    Correy_Percent = (Correy/Total_Votes) * 100
    Tooley_Percent = (Tooley/Total_Votes) * 100

#If state to see who the winner is

if Khan > Correy and Khan > Li and Khan> Tooley:
    winner = "kahn"
elif Correy > Khan and Correy > Li and Correy > Tooley:
    winner = "Correy"
elif Li > Correy and Li > Khan and Li > Tooley:
    winner = "Li"
elif Tooley > Khan and Tooley > Li and Tooley > Correy:
    winner = "O'Tooley"




print("Election Results", file=open("PyPoll.txt", "Access_Mode"))
print("-----------------")
print("Total Votes: " + (str(Total_Votes), file=open("PyPoll.txt", "Access_Mode")))
print("-----------------")
print(f"Khan: {Khan_Percent}% ({Khan})", file=open("PyPoll.txt", "Access_Mode"))
print(f"Correy: {Correy_Percent}% ({Correy})", file=open("PyPoll.txt", "Access_Mode"))
print(f"Khan: {Li_Percent}% ({Li})" , file=open("PyPoll.txt", "Access_Mode"))
print(f"Khan: {Tooley_Percent}% ({Tooley})", file=open("PyPoll.txt", "Access_Mode"))
print("-----------------", file=open("PyPoll.txt", "Access_Mode"))
print(f"Winner: {winner}", file=open("PyPoll.txt", "Access_Mode"))
print("-----------------", file=open("PyPoll.txt", "Access_Mode"))

#Export Text file
file = open("PyPoll.txt","Access_Mode")

