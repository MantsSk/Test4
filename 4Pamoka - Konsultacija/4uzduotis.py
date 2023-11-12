# Step 1: Get user input as a space-separated string of numbers
user_input = input("Enter a list of numbers separated by spaces: ")

# Step 2: Split the input into individual numbers and create a list
numbers = user_input.split()

# Step 3: Initialize a variable to store the sum
total_sum = 0

# Step 4: Use a loop to iterate through the list and calculate the sum
for num in numbers:
    # Convert the string to an integer and add it to the sum
    total_sum += int(num)

# Step 5: Print the total sum
print("The sum of the numbers is:", total_sum)
