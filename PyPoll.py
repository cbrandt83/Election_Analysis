#1.Get the data we need to use
#import csv and os modules
import csv
import os
#assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Open and read the file
with open(file_to_load) as election_data:
    print(election_data)
#2. Get the total number of votes cast
#3. Get a complete list of candidates who received votes
#4. Get the number of votes each candidate received
#5. Calculate the percentage of votes each candidate received
#6. Determine the winner based on who got the majority of votes



