# Your code here
def format_word(word: str):
    word = word.lower()

    new_string = word.replace('"', "")
    new_string = new_string.replace(':', "")
    new_string = new_string.replace(';', "")
    new_string = new_string.replace(',', "")
    new_string = new_string.replace('.', "")
    new_string = new_string.replace('-', "")
    new_string = new_string.replace('+', "")
    new_string = new_string.replace('=', "")
    new_string = new_string.replace('/', "")
    new_string = new_string.replace('\\', "")
    new_string = new_string.replace('|', "")
    new_string = new_string.replace('[', "")
    new_string = new_string.replace(']', "")
    new_string = new_string.replace('{', "")
    new_string = new_string.replace('}', "")
    new_string = new_string.replace('(', "")
    new_string = new_string.replace(')', "")
    new_string = new_string.replace('*', "")
    new_string = new_string.replace('^', "")
    new_string = new_string.replace('&', "")

    return new_string


def histo(file: str):
    dict = {}
    longest_word_length = 0

    with open(file) as f:
        words = f.read()
    words = words.split()

    for word in words:
        word = format_word(word)

        if len(word) > longest_word_length:
            longest_word_length = len(word)

        if word in dict:
            dict[word] += "#"
        else:
            dict[word] = "#"

    sorted_keys = sorted(dict.keys())
    indent_for_value = longest_word_length + 8
    for key in sorted_keys:
        print(f'{key:<{indent_for_value}}{dict[key]}')

histo("robin.txt")