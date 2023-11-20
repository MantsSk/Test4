def add_ending_to_list(lst, ending):
    return [item + ending for item in lst]


# Test the function
original_list = ["apple", "banana", "cherry"]
result_list = add_ending_to_list(original_list, "_end")
print(result_list)
