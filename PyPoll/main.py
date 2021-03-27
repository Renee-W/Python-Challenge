#define variables
totalvote = 0
Canidate = []
#canidatecount=0
Votes = {}
w = 0
winner = ''


#open poling data
import os
import csv

file1 = open('Analysis/PollResults.txt', 'w')
print("Election Results")
print("----------------")
file1.write("Election Results \n")
file1.write("---------------- \n")


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
    file1.write(f"Total Votes: {totalvote} \n")
    file1.write("---------------- \n")
    print("----------------") 
        #% of votes each candidate won
    for Person in Votes.keys():
        count = Votes[Person]
        percent = ((count/totalvote)*100)
        
        
        file1.writelines((Person)+"   ")
        file1.writelines(str(count)+"  ")
        file1.write(str(round(percent,2))+"\n")
        print(Person, count, round(percent,2))
        
    
        if count > w:
            w = count
            winner = Person
            
    print("----------------")    
    print ("Winner: " +(winner))
    file1.write("---------------- \n")
    file1.writelines ("Winner: " +(winner))
    file1.close()