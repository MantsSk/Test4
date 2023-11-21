def add_ending_to_list(lst, ending):
    return [item + ending for item in lst]


# Test the function
original_list = ["apple", "banana", "cherry"]
result_list = add_ending_to_list(original_list, "_end")
print(result_list)

# fruit_list = ["apple", "banana", "cherry"]
# heh_list = ["heh", "kek", "rek"]
# people_list = ["Mantas", "Matas", "Tomas"]

# def add_ending_to_list(passed_list):
#     modified_passed_list = []

#     for item in passed_list:
#         item += "_ending"
#         modified_passed_list.append(item)

#     return modified_passed_list


# new_list = []
# new_list = add_ending_to_list(fruit_list)
# print(new_list)

# print(add_ending_to_list(people_list))
