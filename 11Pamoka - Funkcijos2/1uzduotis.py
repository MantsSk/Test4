def puzzle_pieces(list1, list2):
    if len(list1) != len(list2):
        return False  # Lists must have the same length

    sum_equal = True
    total_sum = list1[0] + list2[0]

    for i in range(1, len(list1)):
        current_sum = list1[i] + list2[i]
        sum_equal = current_sum == total_sum

    return sum_equal

# Test cases
print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))  # True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]

print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))  # True
print(puzzle_pieces([1, 2], [-1, -1]))  # False
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))  # False
