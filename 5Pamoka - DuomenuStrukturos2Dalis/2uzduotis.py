nested_dict = {
    'integer': 42,
    'float': 3.14,
    'string': 'Hello, World!',
    'list': [1, 2, 3, 4],
    'set': {5, 6, 7, 8},
    'tuple': ('apple', 'banana', 'cherry'),
    'dictionary': {
        'nested_integer': 123,
        'nested_float': 2.718,
        'nested_string': 'Nested Dictionary',
        'nested_list': [9, 10, 11],
        'nested_set': {12, 13, 14},
        'nested_tuple': ('dog', 'cat', 'bird'),
        'nested_nested_dict': {
            'key1': 'value1',
            'key2': 'value2'
        }
    }
}

# Accessing values in the nested dictionary
print(nested_dict['integer'])
print(nested_dict['list'][2])
print(nested_dict['set'])
print(nested_dict['tuple'][1])
print(nested_dict['dictionary']['nested_list'][0])
print(nested_dict['dictionary']['nested_nested_dict']['key2'])
