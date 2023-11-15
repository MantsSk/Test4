name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

if age >= 21:
    print(f"{name} {surname}, you are allowed to enter the online casino.")
else:
    print(f"{name} {surname}, sorry, you are not allowed to enter the online casino. You must be 21 or older.")
