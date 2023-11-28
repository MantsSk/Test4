def war_of_numbers(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)

    difference = even_sum - odd_sum

    if difference > 0:
        print("Evens win by", difference)
    elif difference < 0:
        print("Odds win by", abs(difference))
    else:
        print("It's a tie!")


# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_list2 = [1,4,4,2,5,4]
war_of_numbers(numbers_list2)
