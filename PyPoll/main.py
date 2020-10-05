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

        # Sets the list of candidates and makes each one a key in the election dictionary
        # Sets the value of the key to zero
            candidates.append(row[2])
            election[row[2]] = 0

        # After the dictionary is set up in previous IF
        # this line is outside of the IF and since the dict(key) is made from the vote column
        # The counter will always equal the dictionary + 1 more before moving to the next line in the csv
        election[row[2]] = election[row[2]] +1


        
        # Adds vote into a list
        votes.append(row[2])

        # if election[row[2]] == row[2]:
        #     election[row[2]] = election[row[2]] + 1
        # for vote in votes:
            # if election[key] == vote:
            #     election[key] = x + 1


print(election)
print(votes)

# for vote in votes:
#     if vote == election[key]:
#         election[key].append(+1)



# print(candidates)
# print(candidates[0])
# print(election)
# print(votes)

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
print("----------------------------")
print(candidates[0] + ": " + '{:.2%}'.format((election[candidates[0]] / total_votes )) + " (" + str(election[candidates[0]]) + ")")
print(candidates[1] + ": " + '{:.2%}'.format((election[candidates[1]] / total_votes )) + " (" + str(election[candidates[1]]) + ")")
print(candidates[2] + ": " + '{:.2%}'.format((election[candidates[2]] / total_votes )) + " (" + str(election[candidates[2]]) + ")")
print(candidates[3] + ": " + '{:.2%}'.format((election[candidates[3]] / total_votes )) + " (" + str(election[candidates[3]]) + ")")
















