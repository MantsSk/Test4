# main.py

from string_module import concatenate_strings, uppercase_string
from list_module import sum_list, average_list
from number_module import square_number, cube_number

# Example usage
str_result = concatenate_strings("Hello", "World")
upper_result = uppercase_string("python")

list_result_sum = sum_list([1, 2, 3, 4, 5])
list_result_avg = average_list([1, 2, 3, 4, 5])

num_result_square = square_number(4)
num_result_cube = cube_number(3)

print("String Concatenation:", str_result)
print("Uppercase String:", upper_result)
print("Sum of List:", list_result_sum)
print("Average of List:", list_result_avg)
print("Square of Number:", num_result_square)
print("Cube of Number:", num_result_cube)