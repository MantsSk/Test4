# Ask the user to input three integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Find the largest entered value using the max() function
largest_number = max(num1, num2, num3)
smallest_number = min(num1, num2, num3)

# Print the result
print("The largest entered number is:", largest_number)
print("The smallest entered number is:", smallest_number)
