# Quiz: Question 2
# Programmer: Thuy Nguyen 1989864
# Description: This program finds the cluster of even numbers
# within a list of given values
# Due Date: October 3, 2022
# Status: Completed

# Variable for counting even clusters
counter = 0

# Variables for verifying if even and if ok to continue
even = False
okSwitch = False

print("Enter 10 integer values: ")
# Get 10 values from user
for i in range(10):
    num = int(input(""))
    
    # Validate if even and count clusters
    if num % 2 == 0:
        if even == True:
            okSwitch = True
        else:
            even = True
    else:
        if okSwitch == True:
            counter += 1
        okSwitch = False
        even = False

if okSwitch == True:
    counter += 1

# Print counter
print("Number of even clusters:", counter)