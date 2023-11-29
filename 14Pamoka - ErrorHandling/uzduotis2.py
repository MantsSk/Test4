def calculate_square():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        result = number ** 2
    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid integer.")
    else:
        print(f"The square of {number} is: {result}")
    finally:
        print("Thank you for using the square calculator!")

    calculate_square()
