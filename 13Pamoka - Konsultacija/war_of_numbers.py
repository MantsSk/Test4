def war_of_numbers(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return abs(even_sum - odd_sum)

# Test cases
print(war_of_numbers([2, 8, 7, 5]))  # 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 is larger than 10
# So we return 12 - 10 = 2

print(war_of_numbers([12, 90, 75]))  # 27
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))  # 168
