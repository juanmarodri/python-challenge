# import the csv modules
import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# set an empty list to be filled with the csv reader data
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row
    csv_header = next(csvreader)
    # append the contents to the empty list
    for row in csvreader:
       candidates.append(row[2])

    # Initialize the counters for each candidate
    Khan = 0
    Correy = 0 
    Li = 0
    OTooley = 0
    # loop through the data and count the votes for each of the candidates
    for i in range(len(candidates)):
        if candidates[i] == 'Khan':
            Khan = Khan + 1
        elif candidates[i] == 'Correy':
            Correy = Correy + 1
        elif candidates[i] == 'Li':
            Li = Li + 1
        elif candidates[i] == "O'Tooley":
            OTooley = OTooley + 1
    # Sum all the counts to get the total 
    Total = Khan + Correy + Li + OTooley
    # get the percent of each candidate
    Khan_perc = round((Khan / Total)*100)
    Correy_perc = round((Correy / Total)*100)
    Li_perc = round((Li / Total)*100)
    OTooley_perc = round((OTooley / Total)*100)

    # Print the results to the terminal
    print(f'Election Results\n----------------------')
    print(f'Total Votes: {Total}\n----------------------')
    print(f'Khan: {Khan_perc}% ({Khan})')
    print(f'Correy: {Correy_perc}% ({Correy})')
    print(f'Li: {Li_perc}% ({Li})')
    print(f"O'Tooley: {OTooley_perc}% ({OTooley})\n----------------------")
    print(f'Winner: Khan\n----------------------')

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "election_analysis.csv")

# Open the file using "write" mode. 
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes', 'Khan', 'Correy', 'Li', "O'Tooley", 'Winner'])

    # Write the second row
    csvwriter.writerow([Total, [Khan_perc, Khan], [Correy_perc, Correy], [Li_perc, Li], [OTooley_perc, OTooley], 'Khan'])