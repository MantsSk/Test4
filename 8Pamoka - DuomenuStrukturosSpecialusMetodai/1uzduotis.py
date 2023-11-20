# divisible_by_6 = [number for number in range(1, 1001) if number % 6 == 0]

divisible_by_6 = []

for number in range(1, 1001):
    if number % 6 == 0:
        divisible_by_6.append(number)

print("Numbers from 1 to 1000 divisible by 6:", divisible_by_6)
