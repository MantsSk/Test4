def unique_characters_strings(lst):
    return [s for s in lst if len(set(s)) == len(s)]


# Test the function
input_strings = ["hello", "world", "python", "unique"]
result_strings = unique_characters_strings(input_strings)
print(result_strings)
