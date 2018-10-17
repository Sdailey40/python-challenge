import os
import csv

#Define variables and lists
totalMonths = 0
totalrevenue = 0
monthly_average = []
date = []

# * The average change in revenue between months over the entire period
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Set path for file
budgetCSV = os.path.join('budget_data_1.csv')
budgetoutput = os.path.join('financial_analysis_report_1.txt')

# Read in the csv file
#  * The total number of months included in the dataset


with open(budgetCSV, newline = '') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # for testing
    #print(f"header: {header}") 
    for row in csvreader:
        totalMonths = totalMonths + 1
        
        # total Revenue column   
        totalrevenue += int(row[1])
        
        monthly_average.append(int(row[1]))
        date.append(row[0])
    # for testing
    #print(totalMonths)
    #print(totalrevenue)
    #print(monthly_average)
    #print(date)

    # call the function for average
# for testing
#print(average(monthly_average))

# The greatest increase in revenue (date and amount) over the entire period
max= 0
for increase in monthly_average:
    if increase > max:
        max= increase

# for testing
#print(max)
#print(monthly_average.index(max))

# * The greatest decrease in revenue (date and amount) over the entire period
min= 0
for decrease in monthly_average:
    if decrease < min:
        min= decrease
# for testing
#print(min)
#print(monthly_average.index(min))

# Financial Analysis report
print (" Financial Analysis")
print ("-------------------------------------------------")

print(f"Total Months: {totalMonths}" )
print(f"Total Revenue: ${int(totalrevenue)}")
print(f"Average Revenue Change: ${int(average(monthly_average))}")
print(f"Greatest increase in revenue: {date[int(monthly_average.index(max))]} ${int(max)}")
print(f"Greatest decrease in revenue: {date[int(monthly_average.index(min))]} ${int(min)}")

# Output to text tile
with open(budgetoutput, 'w', newline ='') as textwriter:
    textwriter.write("Financial Analysis\n")
    textwriter.write("-------------------------------------------------\n")
    
    textwriter.write(f"Total Months: {totalMonths}\n" )
    textwriter.write(f"Total Revenue: ${int(totalrevenue)}\n")
    textwriter.write(f"Average Revenue Change: ${int(average(monthly_average))}\n")
    textwriter.write(f"Greatest increase in revenue: {date[int(monthly_average.index(max))]} ${int(max)}\n")
    textwriter.write(f"Greatest decrease in revenue: {date[int(monthly_average.index(min))]} ${int(min)}\n")