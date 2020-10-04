# To allow the importing and reading of .csv files
import os
import csv

# Path to collect data from the Resources folder
# ~Be extreamly careful where you are in Terminal~
# ~If you are in the wrong spot of Terminal the file can not be read~
# ~Code to grab and read CSV file is correct~
budget_csv = os.path.join("Resources", "budget_data.csv")






#Read in the CSV file
with open(budget_csv, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Loop through the data
    for row in csv_reader:
        print(row)

