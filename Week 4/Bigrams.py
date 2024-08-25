def get_bigrams(string):
    # Remove spaces and split into characters
    string = string.replace(" ", "")
    bigrams = [(string[i], string[i+1]) for i in range(len(string) - 1)]
    return bigrams

# Test the function
print(get_bigrams("hello"))  # Output: [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]
