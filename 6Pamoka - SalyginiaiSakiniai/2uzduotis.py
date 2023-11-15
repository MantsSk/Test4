privileged_users = ["Alice", "Bob", "Charlie", "David"]

user_name = input("Enter your name: ")

if user_name in privileged_users:
    print(f"Hello {user_name}! You are a privileged user. Special greeting for you!")
else:
    print("Welcome")
