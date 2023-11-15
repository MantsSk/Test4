import random

target_number = random.randint(1, 10)

max_attempts = 3
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    if guess == target_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")
        attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct number was {target_number}. Better luck next time!")
