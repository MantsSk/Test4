def can_find(bigrams, words):
    for bigram in bigrams:
        found = any(bigram in word for word in words)
        if not found:
            return False
    return True

# Test cases
print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))  # True
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))  # False
# "cu" does not exist in any of the words.
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))  # True
print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))  # False
