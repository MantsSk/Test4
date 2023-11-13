# my_list = ["English", "Spain", "Russian"]
#
# my_list.append("Lithuanian")
#
# print(my_list)

# print(my_list[1])

# my_dictionary = {"0": 4, "1": 2, "10": 3, "4": 1}
#
# print(my_dictionary["10"])

# my_dictionary = {0: 4, 1: 2, 133: 3, 4: 1}
#
# print(my_dictionary[63])

my_dictionary = {}
# my_dictionary["name"] = "Tom"
# my_dictionary["surname"] = "Tomencio"
# lygiai tas pats
my_dictionary = {"name": "Tom", "surname": "Tomencio", "favorite_color": "Blue"}
another_dictionary = {"name": "Mantas", "codename": "Spider Man", "identity": "Evil"}

my_dictionary.update(another_dictionary)
print(my_dictionary)

# print(my_dictionary)
# print(my_dictionary["surname"])
# my_dictionary["personal_code"] = "39601231234"
# print(my_dictionary)
# my_dictionary["name"] = " Mantas"
# print(my_dictionary)

# deleted_name = del my_dictionary["name"]
# deleted_name = my_dictionary.pop("surname")
#
# print(my_dictionary)
# print(deleted_name)

#
# print(my_dictionary["personal_code"])

# for key in my_dictionary: # grazina tik key
#     print(key)
#
# for key in my_dictionary.keys(): # irgi grazina tik key
#     print(key)
#
# for item in my_dictionary.items(): # grazina ir key ir value
#     print(item)
#     print(item[0])
#     print(item[1])
#
# for value in my_dictionary.values():# grazina tik value
#     print(value)

# my_dictionary["personal_code"] = "Labas as kebabas"
#
# print(my_dictionary["personal_code"])

# print(my_dictionary)
# print(my_dictionary["favorite_color"])
#
# del my_dictionary["favorite_color"]
# print(my_dictionary)

# user_info = {
#     "name": "Albert",
#     "surname": "Einstein",
#     "occupation": {
#         "role": "Professor",
#         "workplace": "University of Berlin"
#     },
#     "languages": ["German", "Latin", "Italian", "English", "French"]
# }
#
# user_info["languages"].append("Lithuanian")

# print(user_info)

#
# for language in user_info["languages"]:
#     print(language)
#
# print(user_info["languages"][2])
#
# print("Professor: ", user_info["occupation"]["role"])
# user_info["occupation"]["role"] = "Lecturer"
# print(user_info)

# user_info["occupation"] = "Lecturer"

# print(user_info)

# print(user_info['surname'])
# user_info['surname'] = "Skara"
# print(user_info['surname'])
# print(user_info)

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)

numbers_list = [1, 2, 3, 4, 5, 5, 5, 6]
numbers_set = set(numbers_list)
print(numbers_set)

numbers_set.add(1002)
numbers_set.add(4)

print(numbers_set)

numbers_set.remove(4)
print(numbers_set)
