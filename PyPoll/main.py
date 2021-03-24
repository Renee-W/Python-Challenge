#define variables
totalvote = 0
Canidate = []
#canidatecount=0
Votes = {}


#open poling data
import os
import csv
#from collections import Counter

print("Election Results")
print("----------------")

votepath=os.path.join ('Resources', 'election_data.csv')

#read CSV
with open(votepath, "r+") as csvfile:

    
    # CSV reader specifies delimiter and variable that holds contents
    vote = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    #total number of votes casts
    for row in vote:
        totalvote +=1
        

        
        #list of candidates who received votes
        Canidate = row[2]
        if Canidate not in Votes.keys():
            Votes[Canidate]=1
        else:
            x = Votes[Canidate]
            x += 1
            Votes[Canidate] = x
    print(f"Total Votes: {totalvote}")
    print("----------------")        
        #% of votes each candidate won
    for Person in Votes.keys():
        count = Votes[Person]
        percent = ((count/totalvote)*100)

        print(Person, count, round(percent,2))
        

print("----------------")
print("Winner: ")
print("----------------")