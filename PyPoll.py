#1.Get the data we need to use
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #2. Get the total number of votes cast by adding incrementally to total_votes
        total_votes += 1

#print total votes
print(total_votes)

#3. Get a complete list of candidates who received votes
#4. Get the number of votes each candidate received
#5. Calculate the percentage of votes each candidate received
#6. Determine the winner based on who got the majority of votes



