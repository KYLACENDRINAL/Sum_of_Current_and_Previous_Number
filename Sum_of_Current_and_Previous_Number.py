# Print the sum of the current and previous number

# Pseudocode

print ("Printing current and previous number and their sum in a range (10)")
previous_num=0

# Create the loop from 1 to 10
for i in range (1, 11):
    sum=previous_num+i
    
# Print/display the output or the sum of the current and previous number
    print("Current Number", i, "Previous Number", previous_num, "Sum:", sum)
    previous_num=i
