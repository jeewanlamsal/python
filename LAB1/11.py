#WAP to ask for a sentence and calculate the frequency of characters in the sentences.
def calculate_frequency(sentence):
  
    frequency = {}
    for char in sentence:  # Loop through each character in the sentence
        if char in frequency:
            frequency[char] += 1  # Increment count if character already in dictionary
        else:
            frequency[char] = 1  # Initialize count for new character
    return frequency


sentence = input("Enter a sentence: ")
char_frequency = calculate_frequency(sentence)
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
