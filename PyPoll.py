# the steps for retrieving data from election results written in pseudocode
# 
# add dependencies

import csv
import os

# 1. Open the data file.
# Open the election results and read the file
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# To do: perform analysis.
# print(election_data)
# Print each row in the CSV file.        

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write three counties to the file.
outfile.write("Counties in the Election\n")
outfile.write("_--------------------------------------------------------------------------------------------------------------------\n")
outfile.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()     
# Close the file.
election_data.close()

# Write down the names of all the candidates. (a complete list of candidates who received votes)
# Add a vote count for each candidate. 
# Get the total votes for each candidate. (total number of votes each candidate received)
# Get the total votes cast for the election. ( Total number of votes cast)
# (Percentage of votes each candidate won)
# (The winner of the election based on popular vote)
