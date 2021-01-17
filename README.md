# Election_Analysis
## Project Overview
Tom from the Colorado Board of Elections requested assistance with this project to tabulate results from a US Congressional election in a Colorado precinct.  The tabulation of
election results are to be reported out as the total number of votes, as well as a listing of each candidate with their total number of votes received and percentage of total votes. 
The winner of the election is to be reported as well.  This project will be used to certify the results of this election and could be utilized in the future in other districts and
other elections. (There is an additional project overview added at the end for an "add-on" to this project that is an extension of this project on the county level, as noted in the summary.)

Requirements of this application are: 
1. Total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. Winner of the election based on popular vote

## Resources
The data source provided from three different methods of voting were compiled into one comma separated values file: election_results.csv.
Software used to complete the task:  Python 3.7.6, Visual Studio Code 1.52.1 (additional task completed with Microsoft 365 Excel)

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
[results-by-county] (https://github.com/CaroShaf/Election_Analysis/blob/main/Resources/results_by_county.png) These votes were also tabulated through the Python code that was added after these results were examined and are detailed in the Overview and Summary below.

## Overview of Election Audit (by county)
After looking at the data by county in Excel, it seemed like Tom and the Colorado Board of Elections would benefit from integrating an analysis on the county level into the election 
analysis already provided. Ability to output the election results to a data file in text format was also added.  The addition of conditional loops and file writing statements
allowed these additional features of the project.

## Election Audit Results (by county)
From our previous analysis, we know that 369,711 votes in total were cast in this precinct in three counties for three different candidates.
  * 369,711 total votes
  
It was determined that the number of votes and percentage of votes in the counties broke down as follows:

* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

* Denver county had the largest number of votes.

From our previous analysis we know that votes were cast for the following candidates, with the associated percentages of total votes, as follows:

* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.2% (11,606)

And, again, we know that the winner was Diana DeGette with the following vote count and total percentage of votes.

* Winner: Diana DeGette
* Winning Vote Count: 272,892
* Winning Percentage: 73.8%

## Election Audit Summary
To make this analysis more robust, it would benefit from adding population figures to determine the percentage of registered voters.  It is possible that counties with smaller
populations, but with a higher percentage of registered voters, than Denver county actually may have had a higher voter turnout, but we don't have the data to determine that.  For
instance if Arapahoe county only has 24,801 residents then their voter turnout would be 100%, but only 6.7% of the total votes cast in the election.  It
might also be interesting to see if the winner of the election consistently had such popular support across counties when population is taken into account, and not just straight number of vote totals.  It is entirely possible that all of Diana DeGette's voters are in Denver county with all of Doane's and Stockham's in the other two, less populated, counties.

This project is a good foundation for future developments and distribution.


