# Election_Analysis
## Project Overview
Tom from the Colorado Board of Elections requested assistance with this project to tabulate results from a US Congressional election in a Colorado precinct.  The tabulation of
election results are to be reported out as the total number of votes, as well as a listing of each candidate with their total number of votes received and percentage of total votes. 
The winner of the election is to be reported as well.  This project will be used to certify the results of this election and could be utilized in the future in other districts and
other elections.

Requirements of this application are: 
1. Total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. Winner of the election based on popular vote

## Resources
The data source provided from three different methods of voting were compiled into one comma separated values file: election_results.csv.
Software used to complete the task:  Python 3.7.6, Visual Studio Code 1.52.1

## Summary
The analysis of the election results show that:

Total Votes Cast: 369,711

Candidate / Percentage of total votes / total votes received
____________________________________________________________
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.2% (11,606)

-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

-------------------------

These votes represent the votes in three counties: Jefferson, Denver and Arapahoe.  Diana DeGette was by far the winner in all three counties.  This was confirmed by looking at a
pivot chart in Excel just to make sure there wasn't a small number of voters in a sparsely populated county voting for another candidate other than Diana DeGette.
[results-by-county] (https://github.com/CaroShaf/Election_Analysis/blob/main/Resources/results_by_county.png)




