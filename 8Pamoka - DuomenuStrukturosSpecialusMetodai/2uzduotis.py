# numbers_with_9 = [number for number in range(1, 1001) if '9' in str(number)]


numbers_with_9 = []

for number in range(1, 1001):
    if '9' in str(number):
        numbers_with_9.append(number)

print("Numbers from 1 to 1000 that have '9' in them:", numbers_with_9)
