text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

words = text.split()

words_with_e = [word for word in words if 'e' in word.lower()]

# Print the result
print("Number of words containing the letter 'e':", len(words_with_e))
