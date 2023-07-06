# Budget Data Solution 
# Import csv file 

import os 
import csv 

# Set the path for file 
csvpath= os.path.join(".", "Resources", "budget_data.csv")
# print(csvpath) 

# Variables 
    lines = 0
    total_profit = 0
    total_change = 0
    max_change = 0
    max_change_date = ""
    min_change = 0
    min_change_date = ""
    for row in csvpath:
        lines = lines + 1
        month_year = row[0]
        profit = row[1]
        profit = int(profit)
        total_profit = total_profit + profit
        if lines > 1:
            change = profit - previous_profit
            total_change = total_change + change
            # print("profit, previous_profit, change", profit, previous_profit, change)
            if change > max_change:
                max_change = change
                max_change_date = month_year
            if change < min_change:
                min_change = change
                min_change_date = month_year
        previous_profit = profit
        
    print("Financial Analysis")
    print()
    print("--------------------------------------")
    print()
    print(f"Total Months: {lines} ")
    print()
    print(f"Total Profit: ${total_profit}")
    print()
    average_change = total_change/(lines - 1)
    print(f"Average Change: ${round(average_change,2)}")
    print()
    print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
    print()
    print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")



# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)





