# Prompt user for input
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

# Create a dictionary with user information
user_info = {
    'Name': name,
    'Surname': surname,
    'Age': age
}

# Print the dictionary
print("User Information:")
for key, value in user_info.items():
    print(f"{key}: {value}")
