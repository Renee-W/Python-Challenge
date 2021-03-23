#open budget data
import os
import csv

print("Finacial Analysis")
print("--------------------")
csvpath=os.path.join ('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget = csv.reader(csvfile, delimiter=',')
    
    
    #total number of months
    #lines= len(list(budget))
    #print("Total months: " + str((lines)-1))

      
    #total amount of Profit/Loss over the entire period
    
    sum=0
    for row in budget:
        sum += int(row[1])
        
        
            

        
        

#Calculate the changes in Profit/Loss over the entire period

#Greatest increase in profits (date and amount)

#Greatest decrease in losses (date and amount)

#Print analysis and export a text file with the results
