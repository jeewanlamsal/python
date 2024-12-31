#WAP to ask for a sentence and count the number of words.
def count_words(sentence):
    words = sentence.split()  # Split the sentence into words based on spaces
    return len(words)         # Return the count of words

# Example usage
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The number of words in the given sentence is: {word_count}")
