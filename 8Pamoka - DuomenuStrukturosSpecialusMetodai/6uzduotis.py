import math

user_input = input("Enter a number: ")

number = float(user_input)

if number < 0:
    print('Enter a positive number')
else:
    square_root = math.sqrt(number)
    if square_root.is_integer():
        print(f'Number {number} is a perfect square')
    else:
        print(f'Number {number} is NOT a perfect square')


