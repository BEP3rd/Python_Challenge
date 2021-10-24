"""
You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate.
Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.
-----------------------------------------------------------------------------------------------------------------------------------------
Proto-Code

Run a for-loop that keeps a record of the number of lines in the list, this will be our total number of votes cast

In the loop, have it check a list for names. If a name is not in the list, add it to the list.

For each name keep a sum-total tally for them. Use this and the total votes cast to create a percentage of votes for each candidate

Determine the winner of the vote by using a max function for the candidate name list

Print the result to look like this

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------


"""
# Declare depedencies
import os
import csv
from typing import TYPE_CHECKING

# Data file path
electionData = os.path.join('Resources', 'election_data.csv')

# Declare variables to be used
votes = 0
totalVotes = 0
candidates = []
candidatesVotes = []
candidatePercent = []

# Open the file for manipulation
with open(electionData) as csv_file:
    # Reads the csv file to be used
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skips the first line and stores the headers
    csv_header = next(csv_file)

    # Loop for total and candidates
    for row in csv_reader:

        if row[2] not in candidates:       # Appends list of candidates and creates indecies for candidatesVotes
             candidates.append(row[2])
             candidatesVotes.append(0)


        for i in range(len(candidates)):        # Counts votes for each candidate
            if candidates[i] == row[2]:
                candidatesVotes[i] = candidatesVotes[i] + 1

totalVotes = sum(candidatesVotes)        # Total number of votes

for j in range(len(candidates)):        # Percentage of each candidates votes
    candidatePercent.append("{:.2%}".format(candidatesVotes[j]/totalVotes))

# Print the results to the terminal
print("Election Results")
print("-"*50)
print(f"The total number of votes is: {totalVotes}")
print("-"*50)
for k in range(len(candidates)):        # Loops through the candidates and prints the name, percent, and vote number
    print(f"{candidates[k]}: {candidatePercent[k]} ({candidatesVotes[k]})")
print("-"*50)
print(f"The winner is: {candidates[candidatesVotes.index(max(candidatesVotes))]}")        # Declares the winner
print("-"*50)

# creates the results directory if one does not already exsit
if not os.path.exists('Results'):
    os.makedirs('Results')

indentline = "-"*50        # Using this for syntax understanding and ease of implementation

# Print the results to a txt file in the results directory
results = open(os.path.join('Results', 'Results.txt'), "w")
results.write("Election Results")
results.write('\n' f"{indentline}")
results.write('\n' f"The total number of votes is: {totalVotes}")
results.write('\n' f"{indentline}")
for n in range(len(candidates)):
    results.write('\n' f"{candidates[n]}: {candidatePercent[n]} ({candidatesVotes[n]})")
results.write('\n' f"{indentline}")
results.write('\n' f"The winner is: {candidates[candidatesVotes.index(max(candidatesVotes))]}")
results.write('\n' f"{indentline}")
