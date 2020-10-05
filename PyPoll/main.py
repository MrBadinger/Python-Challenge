# To allow the importing and reading of .csv files
import os
import csv
import shutil


# Path to collect data from the Resources folder
# ~Be extreamly careful where you are in Terminal~
# ~If you are in the wrong spot of Terminal the file can not be read~
# ~Code to grab and read CSV file is correct~

#poll_csv = os.path.join("Resources", "election_data.csv")       #<-- Live data for final results; +3.5 million rows of data
poll_csv = os.path.join("Resources", "test_election_data.csv")   #<-- Test data for code testing; 12 rows of data
#--------------------------------------------------------------------------------------------------------------------------------------

# Variables
total_votes = 0

x = 0

# List
candidates = []
votes = []

#Dictionary
election = {}

#Read in the CSV file
with open(poll_csv, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Loop through the data
    for row in csv_reader:
        
        # Calculates the total number of rows/votes in a file
        if row[0] != (None, ""):
            total_votes = total_votes + 1

        # Reviews Candidate column of csv and adds unique values to candidates list
        if row[2] not in candidates:
            candidates.append(row[2])

        # Adds vote into a list
        votes.append(row[2])
    

        # Sets the list of candidates and makes each one a key in the election dictionary
        for key in candidates:
            election[key] = 0 
        


        # if election[key] == row[2]:
        #     print(election[key])
        # for vote in votes:
            # if election[key] == vote:
            #     election[key] = x + 1


print(election)
print(votes)

for vote in votes:
    if vote == election[key]:
        election[key].append(+1)



# print(candidates)
# print(candidates[0])
print(election)
print(votes)

print("---------------------")
print("                     ")

print(election)
print(election["Khan"])
print("                     ")
print("---------------------")






# Completed
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))




















