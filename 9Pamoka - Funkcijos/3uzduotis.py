def basic_calculator(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Check for division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"

    return addition, subtraction, multiplication, division

# Test the function
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
results = basic_calculator(num1, num2)
print(f"Sum: {results[0]}, Subtraction: {results[1]}, Multiplication: {results[2]}, Division: {results[3]}")
