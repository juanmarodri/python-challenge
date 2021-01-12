# import the csv modules
import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# define empty lists to be filled with the csv data
dates = []
prof_loss = []
# open the csv file with the comma delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row
    csv_header = next(csvreader)
    
    #  iterate through the columns and append them to the emtpy lists
    for row in csvreader:
        dates.append(row[0])
        prof_loss.append(int(row[1]))
    # find the max profit and the index to match the date 
    max_prof = max(prof_loss)
    max_index = prof_loss.index(max_prof)
    max_date = dates[max_index]
    # find the max loss and the index to match the date
    min_loss = min(prof_loss)
    min_index = prof_loss.index(min_loss)
    min_date = dates[min_index]

    # sum over the entire data to get the total 
    total_prof_loss = sum(prof_loss)
    tot_month = len(dates)

    # initialize empty list to be filled with the data from the differences of the profits and losses
    diff = []
    for i in range(len(prof_loss)):
        if i > 0:
            diff.append(prof_loss[i] - prof_loss[i-1])
    # get the average of the differences of the profits and losses
    average = round(sum(diff) / len(diff))

    # print results to the terminal
    print(f'Financial Analysis\n------------------\nTotal Months: {tot_month}')
    print(f'Total: ${total_prof_loss}')
    print(f'Average  Change: ${average}')
    print(f'Greatest Increase in Profits: {max_date} (${max_prof})')
    print(f'Greatest Decrease in Profits: {min_date} (${min_loss})')

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "budget_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([tot_month, total_prof_loss, average, [max_date,max_prof], [min_date, min_loss]])