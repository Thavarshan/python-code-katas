import re


class AlphabetPosition:

    alphabet = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    def find_position(self, sentence: str):
        # Convert all letters to lowercase
        sentence = sentence.lower()
        # Remove all spaces and split sentence to list of chars
        sentence = sentence.replace(" ", "")
        # Extract only letters
        characters = ''.join(re.findall("[a-zA-Z]+", sentence))
        # Make string into list of characters
        characters = list(characters)
        # Initiate an empty list to save all positions of the characters in
        positions = []
        # Iterate through each character and find its position in the alphabet.
        # once found replace the character with it's relevant position number
        for character in characters:
            positions.append(self.alphabet.get(character))
        # Convert list of integers to single string
        return ' '.join(map(str, positions))
