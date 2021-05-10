import math

# Day Three Class Notes
# Hash Tables can be useful in problems that need a quick searches with large amounts of data
# The sorting (or something else) can be done ahead of time just once instead of each time

records = [
    ('Alice', 'Engineering'),
    ('Bob', 'Sales'),
    ('Carol', 'Sales'),
    ('Sarah', 'Sales'),
    ('Pranjal', 'Sales'),
    ('Dave', 'Engineering'),
    ('Erin', 'Engineering'),
    ('Frank', 'Engineering'),
    ('Grace', 'Marketing'),
    ('Charles', 'Marketing'),
    ('Brian', 'Marketing'),
    ('Jordan', 'Marketing')
]

# Need to print all departments
# Need to print everyone in Engineering

# Proposed Dictionary
#   Keys: Departments
#   Values: Array of names

# This function is O(n)
#
def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record

        # Check if department is already in index
        if dept in index:
            # If it is, add name to list
            index[dept].append(name)
        # If not create new key with list with the name in it
        else:
            index[dept] = [name]

    return index

department_index = build_index(records)

print(department_index.keys())
print(department_index["Engineering"])  # This will be O(1) no matter what key is used (but uses more space)


# A lookup table is useful to speed up time consuming computations that must be repeated many times

# Example problem: Find inverse square root of numbers between 1 and 1000

# Proposed Dictionary
#   Keys will be numbers
#   Values will be the result of get_inverse_square

def build_sqrt_lookup_table():
    lookup_table = {}
    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table

def get_inverse_square(num):
    return 1 / math.sqrt(num)

sqrt_lookup_table = build_sqrt_lookup_table()

print(sqrt_lookup_table[3])
print(sqrt_lookup_table[234])


# Given a string, find out how many times each letter appears init

# Proposed Dictionary
#   Keys will be the letters
#   Values will be number of times it appears

def letter_count(s):
    dict = {}
    for char in s:
        if char.isspace():
            continue

        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict

print(letter_count("aaabbc"))
print(letter_count("Hello!"))
print(letter_count("The quick brown fox jumps over the lazy dogs"))


def double_letter(s):
    dict = {}
    for char in s:
        if char.isspace():
            continue

        if char not in dict:
            dict[char] = 1
        else:
            return char

print(double_letter("abcdefghijklmnopqrstuvwxyz a"))


# Dictionaries are very useful in substitution ciphers (transfer data from one thing to another)

encode_table = {
    'A': 'Z',
    'B': 'Y',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'N',
    'N': 'M',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'B',
    'Z': 'A'
}

def encode(plain_text):
    cipher = ""

    for char in plain_text:
        if char.isspace():
            cipher += ' '
        else:
            cipher += encode_table[char]
    return cipher

def decode(cipher_text):
    plain_text = ''
    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else:
            plain_text += encode_table[char]
    return plain_text

print(encode("DICTIONARIES ARE AWESOME"))
print(decode("WRXGRLMZIRVH ZIV ZDVHLNV"))

# My Code:


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # My code here



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
