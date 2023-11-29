def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def get_list_element(my_list, index):
    try:
        value = my_list[index]
        return f"The value at index {index} is: {value}."
    except IndexError:
        return f"Error: Index {index} is out of bounds for the list."

def safe_int_conversion(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return "Error: Unable to convert to integer. Please provide a valid integer."

def dictionary_lookup(my_dict, key):
    try:
        result = my_dict[key]
        return f"The value for key '{key}' is: {result}."
    except KeyError:
        return f"Error: Key '{key}' not found in the dictionary."

def list_average(my_list):
    try:
        avg = sum(my_list) / len(my_list)
        return avg
    except ZeroDivisionError:
        return "Error: Cannot calculate average of an empty list."

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(5, 0))   # Output: Error: Division by zero is not allowed.

numbers = [1, 2, 3, 4, 5]
print(get_list_element(numbers, 2))  # Output: The value at index 2 is: 3.
print(get_list_element(numbers, 8))  # Output: Error: Index 8 is out of bounds for the list.

string_number = "123"
print(safe_int_conversion(string_number))  # Output: 123
invalid_string = "abc"
print(safe_int_conversion(invalid_string))  # Output: Error: Unable to convert to integer. Please provide a valid integer.

sample_dict = {'a': 1, 'b': 2, 'c': 3}
print(dictionary_lookup(sample_dict, 'b'))  # Output: The value for key 'b' is: 2.
print(dictionary_lookup(sample_dict, 'd'))  # Output: Error: Key 'd' not found in the dictionary.

empty_list = []
print(list_average(empty_list))  # Output: Error: Cannot calculate average of an empty list.
