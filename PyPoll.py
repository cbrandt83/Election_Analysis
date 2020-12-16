#1.Get the data we need to use
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
#2. Get the total number of votes cast
#3. Get a complete list of candidates who received votes
#4. Get the number of votes each candidate received
#5. Calculate the percentage of votes each candidate received
#6. Determine the winner based on who got the majority of votes



