#open budget data
import os
import csv

#define variables
total=0
change = []
calculate_change = []
months = 0
ProfLoss = 0
date_change =[]
total_change=0
average_change=0
great_increase=0
great_decrease=0
date_increase=''
date_decrease=''

#Collect data
bankpath=os.path.join ('Resources', 'budget_data.csv')

#read CSV
with open(bankpath, "r+") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budget = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
       
    for row in budget:
        #find total months and total Profit/loss

        ProfLoss = int(row[1])
        total = total + ProfLoss
        change.append(ProfLoss)
        date_change.append(row[0])
        months +=1
    
    #Calculate the changes in Profit/Loss over the entire period
    for i in range(months-1):
        calculate_change.append(change[i+1]-change[i])
        
    for i in range(len(calculate_change)):
        total_change += calculate_change[i]
    average_change=total_change/len(calculate_change)
    
    #Greatest increase in profits (date and amount)
    for i in range(len(calculate_change)):
        if calculate_change[i]>great_increase:
            great_increase = calculate_change[i]
            date_increase = date_change[i+1]
        #Greatest decrease in losses (date and amount)    
        elif calculate_change[i]<great_decrease:
            great_decrease = calculate_change[i]
            date_decrease=date_change[i+1]


#Print analysis and export a text file with the results

print("Finacial Analysis")
print("--------------------")
print("Total months: " + str(months))
print("Total: " +str(total))
print("Average Change: " +str(round(average_change,2)))
print("Greatest Increase in Profits: "+(date_increase) + " $" + (str(great_increase)))
print("Greatest Decrease in Profits: "+(date_decrease) + " $" + (str(great_decrease)))

