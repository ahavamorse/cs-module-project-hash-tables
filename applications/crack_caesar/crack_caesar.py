# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

class CodedLetter:
    def __init__(self, letter):
        self.letter = letter
        self.num_of_appearances = 1
        self.real_value = ""

    def __lt__(self, other):
        if self.num_of_appearances < other.num_of_appearances:
            return True
        return False


def crackCaesarCipher(file: str):
    with open(file) as f:
        text = f.read()

    appearances = {}
    letters_in_order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    for char in text:
        if char in letters_in_order:
            if char in appearances:
                appearances[char].num_of_appearances += 1
            else:
                appearances[char] = CodedLetter(char)

    letters_by_frequency = []
    for coded_letter in sorted(appearances, key=appearances.get, reverse=True):
        letters_by_frequency.append(coded_letter)

    for i in range(0, 26):
        if appearances[letters_by_frequency[i]]:
            appearances[letters_by_frequency[i]].real_value = letters_in_order[i]

    for letter in appearances.values():
        text = text.replace(letter.letter, letter.real_value.lower())

    return text.upper()

print(crackCaesarCipher("ciphertext.txt"))