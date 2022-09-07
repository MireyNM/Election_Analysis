# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Declare a new list 
candidate_options=[]

#Declare an empty dictionary
candidate_votes={}

# 1. Initialize a total vote counter.
total_votes=0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        #2. Add the total votes count 
        total_votes=total_votes+1
         
        #Print candidate's name from each row
        candidate_name=row[2]
        

        #if the candidate name does not match any previous name     
        if candidate_name not in candidate_options:
        
         # Add it to the candidate options list:
         candidate_options.append(candidate_name)
        
         # Begin tracking that candidate's vote count
         candidate_votes[candidate_name] = 0
        
         # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

# print candidate name and percentage of votes 
#for key,value in candidate_votes.items():
 #vote_percentage=(value/total_votes)*100
 #print(f'{key}: received {vote_percentage:.1f}% of vote')
 
# Iterate through the candidate list. 
for candidate_name in candidate_votes:
 # Retrieve vote count of a candidate.    
 votes=candidate_votes[candidate_name]
 # Calculate the percentage of votes.
 vote_percentage = float(votes) / float(total_votes) * 100
 #print out each candidate's name, vote count, and percentage of
 print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
 
 # Determine if the votes is greater than the winning count.
 if (votes>winning_count) and (vote_percentage>winning_percentage):
    winning_count=votes
    winning_percentage=vote_percentage
    winning_candidate=candidate_name

#Print a wining summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Using the with statement open the file as a text file.
#with open(file_to_save,"w") as txt_file:

#write the same data to file
 #    txt_file.write("Counties in the Election\n")
  #   txt_file.write("-------------------------\n")
   #  txt_file.write("Arapahoe\nDenver \nJefferson")



# The data we need to retrieve 

# 1. The total number of votes cast 

# 2. A complete list of candidates who received votes 

# 3. The percentage of votes each candidate won

#4. The total number of votes each candidates won

#5. The winner of the election based on popular vote.



