# Quiz: Question 2
# Programmer: Thuy Nguyen
# Description: This program asks the user to input string values
# and prints the longest and shortest values.
# Due Date: October 3, 2022
# Status: Completed

# Create list for strings
string = []

# Create variable for user to exit program
userExit = False

# Get values for string until user says stop
while userExit == False:
    value = input("Enter a string: ")
    if value == "stop" or value == "STOP" or value == "Stop":
        userExit == True
        break
    else:
        string.append(value)

# Find longest string in list
longest = max(string, key = len)

# Find shortest string in list
shortest = min(string, key = len)

# Print longest and shortest strings found
print("Longest String:", longest)
print("Shortest String:", shortest)