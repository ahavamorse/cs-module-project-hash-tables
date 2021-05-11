import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
def is_start_word(word):
    first_letter = word[0]
    return first_letter.isupper()

dict = {}
start_words = []
words = words.split()
for i in range(0, len(words)):
    word = words[i]

    if is_start_word(word):
        start_words.append(word)
    if i < len(words) - 1:
        next_word = words[i + 1]

        if word in dict:
            dict[word].append(next_word)
        else:
            dict[word] = [next_word]


# TODO: construct 5 random sentences
def is_not_stop_word(word):
    last_char = word[-1]
    if last_char == '"':
        last_char = word[-2]
    if last_char == "." or last_char == "?" or last_char == "!":
        return False
    else:
        return True


for i in range(1, 6):
    sentence_words = []
    curr_word = random.choice(start_words)
    while is_not_stop_word(curr_word):
        print(curr_word, end=" ")
        possible_words = dict[curr_word]
        curr_word = random.choice(possible_words)
    print(curr_word)
