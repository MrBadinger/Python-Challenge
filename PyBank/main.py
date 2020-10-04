# To allow the importing and reading of .csv files
import os
import csv

# Path to collect data from the Resources folder
# ~Be extreamly careful where you are in Terminal~
# ~If you are in the wrong spot of Terminal the file can not be read~
# ~Code to grab and read CSV file is correct~
budget_csv = os.path.join("Resources", "budget_data.csv")

# Variables
pnl_total = 0
pnl_profile = 0
total_month = 0
month_change = 0

# Lists 
average_change = []


#Read in the CSV file
with open(budget_csv, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    # # Skips the header
    csv_header = next(csv_file)
    

    # # Loop through the data   # <--once it finishes this for loop we are at end of file, and if we wanted to go through the file again we would need to open another 'when open'
    for row in csv_reader:
        
        # Calculates the total number of rows in a file
        if row[0] != (None, ""):
            total_month = total_month + 1    
    
        # This sums the row to find total profit and loss
        pnl_total = pnl_total + int(row[1])
        
        # This will take the first P/L value, store it, and subtract it against the P/L value in the next row
        # The value is stored in the average change list. 
        # Then to prepare the next it will store the current P/L value to be subtracted in the next row.
        if total_month == 1:
            prev_mon_pnl = int(row[1])
        else:
            month_change = int(row[1]) - prev_mon_pnl
            average_change.append(month_change)
            prev_mon_pnl = int(row[1])
            month_change = 0




# Sums all the changes in the average change list and divides by the
# Number of items in the list to make average 
average_change_sum = (sum(average_change) / len(average_change)) 





# Completed
print("Financial Analysis")
print("----------------------------------")
# Reports backs the total number of months by totaling the number of rows
print("Total Months: " + str(total_month))
print("Total P/L: $" + "{:,}".format(pnl_total))
print("Average Monthly Change: $" + "{:,.2f}".format(average_change_sum))