number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = number1 + number2
    print(f"The result of {number1} {operation} {number2} is: {result}")
elif operation == '-':
    result = number1 - number2
    print(f"The result of {number1} {operation} {number2} is: {result}")
elif operation == '*':
    result = number1 * number2
    print(f"The result of {number1} {operation} {number2} is: {result}")
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"The result of {number1} {operation} {number2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
