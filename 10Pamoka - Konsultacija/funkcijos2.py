list_of_words = ["hello", "world", "python", "unique"]
another_list_of_words = ["hey", "heh", "wow", "youo"]


# def return_unique_words(word_list):
#     unique_strings = []
#     for word in word_list:
#         if len(word) == len(set(word)):
#             unique_strings.append(word)
#
#     return unique_strings

def return_unique_words(word_list):
    return [word for word in word_list if len(set(word)) == len(word)]

print(return_unique_words(list_of_words))
print(return_unique_words(another_list_of_words))