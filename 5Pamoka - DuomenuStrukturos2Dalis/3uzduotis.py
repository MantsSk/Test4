# Initialize an empty dictionary to store word frequencies
word_frequency = {}

# Get input sentences from the user
input_sentences = input("Enter sentences: ")

# Split the input into sentences
sentences = input_sentences.split('.')

# Process each sentence
for sentence in sentences:
    # Split the sentence into words
    words = sentence.lower().split()

    # Count the frequency of each word
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?')

        # Update the dictionary
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

# Print the word frequency dictionary
print(word_frequency)
