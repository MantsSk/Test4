text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

words = text.split()

words = [word for word in words if len(word) > 5]

# Print the result
print("Number of words that have more than 5 characters:", len(words))
