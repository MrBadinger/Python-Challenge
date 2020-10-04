# To allow the importing and reading of .csv files
import os
import csv

# Path to collect data from the Resources folder
# ~Be extreamly careful where you are in Terminal~
# ~If you are in the wrong spot of Terminal the file can not be read~
# ~Code to grab and read CSV file is correct~

#poll_csv = os.path.join("Resources", "election_data.csv")       #<-- Live data for final results; +3.5 million rows of data
poll_csv = os.path.join("Resources", "test_election_data.csv")   #<-- Test data for code testing; 12 rows of data





#Read in the CSV file
with open(poll_csv, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Loop through the data
    for row in csv_reader:
        print(row)