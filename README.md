# Election_Analysis-
Module 3 in CU BootCamp 

## Project Overview 
In this project, we are going to assist a Colorado Board of Elections employee, Tom, to complete the election audit of a recent local congressional election. To do that we need to do the following tasks: 

1. Calculate the total number of votes cast.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
3. Determine the county with the largest number of votes (the highest turnout).
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
5. Determine the winner of the election, their vote count, and their percentage of the total votes.

### Purpose 
The aim of this work is to provide evidence to Tom's manager that there's a way to automate the process of the audit using Python instead of Excel. This will help them in the audit of other congressional districts, senatorial districts and local elections. 

## Resources 
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio 1.69.1  

## Analysis of Data 

The first major piece of our code (showed below) is to create file paths, to external files, across operating systems. To be able to do that we should import os module and csv module using ```import os``` and ```import csv```. 

- After that, we have created 2 paths. 
	- One to open the election results data file "election_results.csv" which is saved in the "Resources" folder: <br /> 
```file_to_load = os.path.join("Resources", "election_results.csv")```
	- One to save the results of our audit in a text file named "election_analysis.txt" saved in the "Analysis" folder: <br />
```file_to_save = os.path.join("analysis", "election_analysis.txt")```

- We used the ```with()``` statements to open the election results and analysis files.
 
- Inside the ```with()``` statement we have used  repetition statements and conditional statements with logical operators  to be able to find answers to our task. 

- Finally, we have used print statements ```txt_file.write()```
 to print out the candidate and county election results to the command line.

 **The final code is shown below:** 
```
# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options=[]
county_votes={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
largest_count = 0 

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]
         
        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options: 

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        county_count = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_votes_percentage = float(county_count)/float(total_votes)*100
        county_results = (
            f'{county_name}: {county_votes_percentage:.1f}% ({county_count:,})\n'
        )

         # 6d: Print the county results to the terminal.
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if county_count > largest_count:
            largest_count = county_count
            winning_county = county_name


    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n"
  )
    print(winning_county_summary)


    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

```

## Election-Audit Results
When we run the code the candidate and county election results were printed in the terminal (See Fig.1) as well as in the "election_analysis.txt” that we have already created (See Fig.2).

<p align="center">
  <img alt="Light" src="https://user-images.githubusercontent.com/109363759/189509343-7b760956-7117-4298-96fe-81f2d39bf6be.png" width="45%"> 
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="Dark" src="https://user-images.githubusercontent.com/109363759/189444167-d71611cd-0715-4138-848e-8af004511f6a.png" width="50%">
</p>

<p align="center">
 Fig. 1: Candidate and county election results printed in Terminal     
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
 Fig. 2: Candidate and county election results printed in text.file  
</p>


<br /> 

The analysis of the election shows that:

- There were "369,711" votes cast in the election.
- The Candidates were: 
    - Candidate 1: Charles Casper Stockham
    - Candidate 2: Diana DeGette
    - Candidate 3: Raymon Anthony Doane
- The county results were: 
    - Jefferson received 10.5% of the votes and "38,855" number of votes.
    - Denver received 82.8% of the votes and "306,055" number of votes.
    - Arapahoe received 6.7% of the votes and "24,801" number of votes.
- Largest County Turnout was Denver
- The candidate results were: 
    - Charles Casper Stockham received "23.0%" of the votes and "85,213" number of votes.
    - Diana DeGette received "73.8%" of the votes and "272,892" number of votes.
    - Raymon Anthony Doane received "3.1%" of the votes and "11,606" number of votes.
- The winner of the election was: 
    - Diana DeGette, who received "73.8%" of the votes and "272,892" number of votes.


## Election-Audit Summary    
The analysis of the election data with Python allows us to complete the election audit successfully. Thus, we can say that automating the process of the audit using Python should be taken into consideration. 

However, I would suggest few modifications to the code in order to be more efficient for any election file.  
 
1. **Dynamic approach:** We need to make sure that the code is as abstract as possible so it could be used with any election data file. I would suggest making it easier for the user by adding to the code the following:
- Give the user the ability to drag and drop the election file.
- Generate analysis file based on the file that the user has dragged. 

2. **Visualize the data:** Data visualization will help in understanding the results in an easier and faster way. If we have more data (more candidates and counties), it will take more than 10 minutes for us to read who won the election. While if we use a bar graph, per examples, in our output results it will take us few seconds to spot the highest bar and the name of the winner candidate. 

Please check the modified code "PyPoll_Challenge.py" in the new branch named dynamic: <br /> 
https://github.com/MireyNM/Election_Analysis-/tree/dynamic

### Challenges 
While going through the suggestions I mentioned above, I have faced the following challenges:

1-  I noticed that when dragging the file an extra **'** was added to the file name therefore I removed it by adding the following to the code. 

```
if file_to_load[0] == "'":
    file_to_load = file_to_load[1:-1]
```

2- I have tried to visualize the election results in bar charts. However, to be able to do that I should import the matplptlib module ```import matplotlib.pyplot as plt``` which gave this error ```ModuleNotFoundError: No module named 'matplotlib'```. It seems the module I need in order to draw charts doesn't exist in my version of Python. The solution should be to install pip and use it to load the module. More work and research are needed to be able to fix this issue.





 


    


