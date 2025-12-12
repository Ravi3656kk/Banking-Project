hindi_words = {
    "madad": "help",
    "kursi": "chair",
    "hathi": "elephant"
}

word = input("Enter the Hindi word to translate into English: ").strip().lower()

# Lookup
if word in hindi_words:
    print(f"The English translation of '{word}' is '{hindi_words[word]}'.")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")
