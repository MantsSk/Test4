number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print(f"The first number ({number1}) is higher than the second number ({number2}).")
elif number1 < number2:
    print(f"The second number ({number2}) is higher than the first number ({number1}).")
else:
    print(f"The two numbers ({number1} and {number2}) are equal.")
