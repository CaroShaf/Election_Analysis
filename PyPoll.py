# the steps for retrieving data from election results written in pseudocode
# 
# add dependencies

import csv
import os

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)    
    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
 
  #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

        #  To do: print out the winning candidate, vote count and percentage to
        #   terminal.

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")     

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
   


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
