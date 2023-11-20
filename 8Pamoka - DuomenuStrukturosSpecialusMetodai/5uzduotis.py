text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# letter_occurrences = {}

# for char in text:
#     if char.isalpha():
#         char = char.lower()
#         letter_occurrences[char] = letter_occurrences.get(char, 0) + 1

letter_occurrences = {char.lower(): text.lower().count(char.lower()) for char in text if char.isalpha()}

for letter, count in letter_occurrences.items():
    print(f"{letter}: {count} occurrences")



